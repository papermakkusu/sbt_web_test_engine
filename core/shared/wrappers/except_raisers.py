#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from core.shared.wrappers import *


def check_verbal_compatibility(func):
    @wraps(func)
    def wrapper(*args):
        temp = func(*args)
        if not temp:
            raise ElementsNotMatchError("Element {args} does not match given verbal expression".format(args=args))
        return temp
    return wrapper


def check_not_implemented(func):
    @wraps(func)
    def wrapper(*args):
        temp = func(*args)
        if not temp: raise NotImplementedError("Web driver can't read {element}.".format(element=args))
        return temp
    return wrapper


def check_for_output(func):
    @wraps(func)
    def wrapper(*args):
        temp = func(*args)
        if not temp: raise ElementNotFoundError("Element {args} was not found in db".format(args=args))
        return temp
            # Put logging expression here in future
            # raise ElementNotFoundError('Web element {element} was not found in the library'.format(element=args))
    return wrapper


def check_for_elem_presence(func):
    @wraps(func)
    def wrapper(*args):
        elem = func(*args)
        if not elem: raise NoSuchElementException('Web element {element} was not found on page'.format(element=args))
        return elem
    return wrapper


def check_if_val_ret(func):
    @wraps(func)
    def wrapper(*args):
        return True if func(*args) else False
    return wrapper


def check_for_none_return(func):
    @wraps(func)
    def wrapper(*args):
        try: return func(*args)
        except:
            raise ElementNotFoundError("Element {element} was not found in DB".format(element=args))
    return wrapper

def check_elements_on_page(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NoSuchElementException:
            raise ElementNotFoundError("Some elements {element} were not found on web page".format(element=args))
    return wrapper


def check_for_value_error(func):
    @wraps(func)
    def wrapper(*args):
        try: return func(*args)
        except:
            raise ValueError("Incorrect date format: {date}".format(date=args))
    return wrapper


def check_for_timeout_except(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TimeoutException:
            raise WaitTimeoutException("Waiting time ended: ")
    return wrapper


def check_for_text_value(func):
    @wraps(func)
    def wrapper(*args):
        if not func(*args): raise Exception("Incorrect text value")
        return func(*args)
    return wrapper


