#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'


class ElementsNotMatchError(BaseException):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super(ElementsNotMatchError, self).__init__(message)


class ElementNotFoundError(BaseException):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super(ElementNotFoundError, self).__init__(message)


class WrongSyntaxError(BaseException):
    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super(WrongSyntaxError, self).__init__(message)


class TestFailedException(BaseException):
    def __init__(self, message ):
        # Call the base class constructor with the parameters it needs
        super(TestFailedException, self).__init__(message)


class ConditionFailedException(BaseException):
    def __init__(self, message ):
        # Call the base class constructor with the parameters it needs
        super(ConditionFailedException, self).__init__(message)


class WaitTimeoutException(BaseException):
    def __init__(self, message ):
        # Call the base class constructor with the parameters it needs
        super(WaitTimeoutException, self).__init__(message)


class WebElementTextCheckException(BaseException):
    def __init__(self, message ):
        # Call the base class constructor with the parameters it needs
        super(WebElementTextCheckException, self).__init__(message)


class WebElementDecompositionException(BaseException):
    def __init__(self, message ):
        # Call the base class constructor with the parameters it needs
        super(WebElementDecompositionException, self).__init__(message)

