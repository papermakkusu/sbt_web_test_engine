#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

import re


class Switch(object):
    """
    Simple imitation of Switch case tool in Python. Used for visual simplification

    """

    value = None

    def __new__(class_, value):
        """
        Assigns given value to class variable on class creation

        :return: Returns True if the assignment was a success
        :rtype: Boolean
        """

        class_.value = value
        return True


def case(*args):
    """
    Matches given value with class value

    :return: returns True if given argument is in .value field of Switch class
    :rtype: Boolean

    Doctest:
    >>> swi =  Switch('кнопка Найти')
    >>> case(r'^кноп[\w]*$')
    True
    >>> case(r'^чекбокс[\w]*$')
    False
    """

    return any(re.match(re.compile(arg), Switch.value) for arg in args)


if __name__ == '__main__':
    import doctest
    doctest.testmod()