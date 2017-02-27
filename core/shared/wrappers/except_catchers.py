#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from core.shared.wrappers import *


def catch_exceptions(func):
    @wraps(func)
    def wrapper(context, *args):
        try:
            return func(context, *args)
        except (NoSuchElementException, ElementNotFoundError,) as err:
            context.config.userdata['log'].error(err)
            Common.finish_work(context.browser)
        except (TimeoutException) as err:
            context.config.userdata['log'].error(err)
            Common.finish_work(context.browser)
        except StaleElementReferenceException as err:
            context.config.userdata['log'].error(err)
            Common.finish_work(context.browser)
        except TestFailedException as err:
            context.config.userdata['log'].warning("Test conditions were not met: ", err)
            Common.finish_work(context.browser)
        except AttributeError as err:
            context.config.userdata['log'].warning("Exception in test attributes: ", err)
            Common.finish_work(context.browser)
    return wrapper


def check_for_valid_ret(func):
    @wraps(func)
    def wrapper(*args):
        try: return func(*args)
        except: return False
    return wrapper


def ignore_element_absence(func):
    @wraps(func)
    def wrapper(*args):
        try: return func(*args)
        except NoSuchElementException: pass
    return wrapper

