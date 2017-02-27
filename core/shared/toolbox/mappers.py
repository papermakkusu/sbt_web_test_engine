#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from core.shared.toolbox.tweak_list import first


def map_funcs(func_list, *args):
    """ Maps list of functions to arguments set

    Doctest:
    >>> def foo_0(x, y): return "yappi!" if x==2 and y==3 else None
    >>> def foo_1(x, y): return "yappi!" if x==3 and y==4 else None
    >>> map_funcs((foo_0, foo_1, foo_1), 2, 3)
    'yappi!'
    >>> map_funcs((foo_0, foo_1, foo_0), 2, 3)
    'yappi!'
    >>> map_funcs((foo_1, foo_1, foo_1), 2, 3)

    """

    return first([element for element in [foo(*args) for foo in func_list if foo(*args)] if element])


if __name__ == "__main__":
    import doctest
    doctest.testmod()