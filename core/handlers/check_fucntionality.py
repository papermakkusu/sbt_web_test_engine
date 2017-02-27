#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from core.handlers import *


def func_check(verb_expr: str, value: str) -> bool:
    """ Verifies that functionality of verbal expression and connected value match

    Doctest:
    >>> func_check('кликает неистово', 'кнопку красную')
    True
    >>> func_check('кликает неистово', 'поле пустое')
    False
    >>> func_check('лежит в снегу', 'разбитая шестёрка')
    False
    """

    return compare_masks(bit_pack(verb_expr), bit_pack(value))


@check_if_val_ret
def exist_check(expr: str) -> bool:
    """ Verifies that given expression refer to existing db record

    >>> exist_check('алёшкины сказки')
    False
    >>> exist_check('изображен из сказок Пушкина')
    True
    """

    return get_func_by_tip(expr)


if __name__ == '__main__':
    import doctest
    doctest.testmod()



