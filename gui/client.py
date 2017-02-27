import sys
sys.path.insert(0, './client_data')
from front_end import wsgi


app = wsgi.application
