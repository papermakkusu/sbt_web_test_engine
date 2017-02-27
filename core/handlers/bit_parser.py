#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from core.handlers import *


def calc_mask(features: tuple, ) -> int:
    """
    Calculates bit masks for given features

    :param features: tuple of strings with number of features for given web element
    :returns: bit mask for given features

    Doctest
    >>> calc_mask((FuncMask.CLICKABLE, FuncMask.IS_BUTTON, ))
    1048577
    >>> calc_mask((FuncMask.CLICKABLE, FuncMask.IS_LINK, ))
    268435457
    """

    return sum([1 << feature for feature in features if feature in FuncMask])


def bit_pack(ref: str) -> int:
    """ Packs elements functionality in bit masks by given element reference

    :parameter ref: Element reference 'aka' element type in plain Russian
    :returns: Bit mask with element functionality hash

    Doctest:
    >>> bit_pack('кнопка_2')
    1048577
    >>> bit_pack('поле пустое')
    16777220
    >>> bit_pack('избушка на курьих ножках')

    """

    return calc_mask(get_func_by_tip(ref))


def compare_masks(exp_mask: int, val_mask: int) -> bool:
    """ Matches 2 bit masks with encoded functionality

    :returns: True if masks match and False if they don't

    Doctest:
    >>> a = 1 << 2
    >>> a += 1 << 4
    >>> b = 1 << 4
    >>> b += 1 << 7
    >>> c = 1 << 7
    >>> c == c & b
    True
    >>> a == a & b
    False
    """

    return val_mask == val_mask & exp_mask


if __name__ == '__main__':
    import doctest
    doctest.testmod()
