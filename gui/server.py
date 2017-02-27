#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from sys import path as sys_path
from os.path import abspath, dirname, join
import datetime
from threading import Thread

sys_path.append(abspath(join(dirname(__file__), "../")))


import socket
from io import StringIO
import sys
from core.shared import *
import urllib.request as request


SERVER_ADDRESS = (HOST, PORT) = '', 8888
SIZE = 1024
UNACCEPTED_CONNECTIONS = 1


class WSGIServer(object):

    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = UNACCEPTED_CONNECTIONS

    def __init__(self, server_address):
        # Create a listening socket
        self.listen_socket = listen_socket = socket.socket(
            self.address_family,
            self.socket_type
        )
        self.threads = []
        self.size = SIZE
        # Allow to reuse the same address
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind to server
        listen_socket.bind(server_address)
        # Activate socket connection
        listen_socket.listen(self.request_queue_size)
        # Get server host name and port
        host, port = self.listen_socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port
        # Return headers set by Web framework/Web application
        self.headers_set = []

    def set_app(self, application):
        self.application = application

    def serve_forever(self):

        listen_socket = self.listen_socket
        while True:
            # New client connection
            try:
                self.listen(listen_socket)
            except (KeyboardInterrupt, SystemExit):
                for thread in self.threads:
                    thread.join()
                sys.exit()


    def listen(self, socket):
        client_connection, client_address = socket.accept()
        # TODO Look closely on thread joining here
        self.threads.append(Thread(target=self.listen_to_client, args=(client_connection, client_address)).start())


    def listen_to_client(self, client_connection, client_address):
        while True:
            try:
                request_data = client_connection.recv(self.size)
                if request_data:
                    result = self.handle_request(request_data, client_connection, client_address)
                    # Construct a response and send it back to the client
                    self.finish_response(client_connection, result)
                else:
                    # TODO Forward to server logs
                    raise Exception('Client disconnected')
            except:
                client_connection.close()
                return False

    def handle_request(self, request_data, client_connection, client_address):
        # Print formatted request data a la 'curl -v'
        # TODO Forward to server logs
        print('< {line}\n'.format(line=line) for line in request_data.splitlines())
        if request_data:
            method, path, version = self.parse_request(request_data)
            print("request_data: ", request_data)
            # Construct environment dictionary using request data
            env = self.get_environ(request_data, method, path)
            # It's time to call our application callable and get
            # back a result that will become HTTP response body
            result = self.application(env, self.start_response)
        else: result=b''
        return result

    def parse_request(self, text):
        request_line = first_or_empty(text.splitlines())
        request_line = request_line.decode().rstrip('\r\n')
        # Break down the request line into components
        (request_method,                 # GET
         path,                           # /hello
         request_version                 # HTTP/1.1
         ) = request_line.split()
        return request_method, path, request_version

    def get_environ(self, request_data, method, path):
        env = {}
        # The following code snippet does not follow PEP8 conventions
        # but it's formatted the way it is for demonstration purposes
        # to emphasize the required variables and their values
        #
        # Required WSGI variables
        env['wsgi.version']      = (1, 0)
        env['wsgi.url_scheme']   = 'http'
        env['wsgi.input']        = StringIO(request_data.decode())
        env['wsgi.errors']       = sys.stderr
        env['wsgi.multithread']  = False
        env['wsgi.multiprocess'] = False
        env['wsgi.run_once']     = False
        # Required CGI variables
        env['REQUEST_METHOD']    = method                   # GET
        env['PATH_INFO']         = path                     # /hello
        env['SERVER_NAME']       = self.server_name         # localhost
        env['SERVER_PORT']       = str(self.server_port)    # 8888

        # if method == 'POST':
        #     a = env['wsgi.input'].readlines()
        #     enc = None
        #     for _ in range(len(a)-1):
        #         if 'Content-Length' in a[_]:
        #             # enc.append(a[_])
        #             # enc.append(a[_+1])
        #             enc= a[_+2]
        #     # print("RENVIRON: ", env['wsgi.input'].readlines())
        #     print("RENVIRON_TRUE: ", enc)
        #     # print(StringIO(enc))
        #     env['wsgi.input'] = enc

        return env

    def start_response(self, status, response_headers, exc_info=None):
        # Add necessary server headers
        server_headers = [
            ('Date', datetime.datetime.now().strftime("%Y-%m-%d %H:%M")),
            ('Server', 'WSGIServer 1.0'),
        ]
        self.headers_set[:] = [status, response_headers + server_headers]
        # To adhere to WSGI specification the start_response must return
        # a 'write' callable. We simplicity's sake we'll ignore that detail
        # for now.
        return self.finish_response

    def finish_response(self, client_connection, result):
        try:
            status, response_headers = self.headers_set
            response = 'HTTP/1.1 {status}\r\n'.format(status=status)
            for header in response_headers:
                response += '{0}: {1}\r\n'.format(*header)
            response += '\r\n'
            for data in result:
                response += data.decode()
            # Print formatted response data a la 'curl -v'
            # TODO Forward to server logs
            print(''.join('> {line}\n'.format(line=line) for line in response.encode().splitlines() ))
            client_connection.sendall(response.encode())
        finally:
            client_connection.close()


def make_server(server_address, application):
    server = WSGIServer(server_address)
    server.set_app(application)
    return server


if __name__ == '__main__':
    if len(sys.argv) < 2: sys.exit('Provide a WSGI application object as module:callable')
    app_path = sys.argv[1]
    module, application = app_path.split(':')
    module = __import__(module)
    application = getattr(module, application)
    httpd = make_server(SERVER_ADDRESS, application)
    # TODO Forward to server logs
    print('WSGIServer: Serving HTTP on port {port} ...\n'.format(port=PORT))
    httpd.serve_forever()