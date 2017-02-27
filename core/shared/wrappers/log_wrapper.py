#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from core.shared.wrappers import *


# TODO Experiment more with logwrap capabilities
def log_it(foo):
    @wraps(foo)
    def wrapper(name, url, user_ip):
        log = construct_logger(name, user_ip)
        a = foo(name, url, log, user_ip)
        destruct_logger(log)
        return a
    return wrapper
