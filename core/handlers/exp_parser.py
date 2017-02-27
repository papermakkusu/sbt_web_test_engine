#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from core.handlers import *


@check_verbal_compatibility
def get_short_name(full_name: str, ) -> str:
    """

    :param full_name:
    :return:

    Doctest:
    >>> get_short_name('ссылка Fraud')
    'Fraud'
    """

    return last(full_name.split(" ", 1))


@check_verbal_compatibility
def get_func_by_tip(verb_exp: str, ) -> tuple or bool:
    """ Parses given expression and returns a first value for given tip to the expression

    Doctest:
    >>> get_func_by_tip('переходит дорогу')
    (<FuncMask.IS_PAGE: 40>, <FuncMask.HAS_TITLE: 7>)
    # >>> check_for_exceptions(ElementNotFoundError, get_func_by_tip, 'лезет на стену')
    # False
    >>> get_func_by_tip('поле пустое')
    (<FuncMask.IS_FIELD: 24>, <FuncMask.WRITABLE: 2>)
    >>> get_func_by_tip('избушка на курьих ножках')
    False
    >>> get_func_by_tip('изображение из сказок Пушкина')
    (<FuncMask.IS_IMAGE: 27>,)
    >>> get_func_by_tip('алёшкины сказки')
    False
    >>> get_func_by_tip('кликает по ячейке')

    """


    temp_item, tip, func_list = [], get_tip(verb_exp), iter([val.value.items() for val in FuncRef])
    for item in range(len(FuncRef)):
        temp_item += [v for k, v in next(func_list) if match_tip(tip, k)]
    return first(temp_item)


@check_verbal_compatibility
def get_func_pack(functionality: tuple) -> Enum or None:
    """

    Doctest:
    >>> get_func_pack((FuncMask.IS_BUTTON, FuncMask.CLICKABLE, ) )
    <FuncRef.BUTTON: {'кноп': (<FuncMask.IS_BUTTON: 20>, <FuncMask.CLICKABLE: 0>)}>
    >>> get_func_pack((FuncMask.IS_BUTTON, FuncMask.IS_IMAGE, ) )

    """
    return first([item for item in FuncRef if functionality in list(item.value.values())])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
