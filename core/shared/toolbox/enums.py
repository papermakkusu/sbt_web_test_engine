#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from core.shared.toolbox.tweak_list import first


class MetaEnum(object):
    """
    Provides valid enumerated container.
    """
    class __metaclass__(type):
        def __iter__(self):
            for item in self.__dict__:
                if item == self.__dict__[item]:
                    yield item


def new_enum(name, *class_members):
    """ Builds a class <name> with <class_members> having the name as value.
    """

    return type(name, (MetaEnum, ), {val: val for val in class_members})


def get_regular(enumerator) -> str:
    """ Gets regular expressions from Values in FuncRef enumerator

    :param enumerator: enum key
    :return: string with regular expression from given Enum

    Doctest:
    >>> from enum import Enum
    >>> from core.shared.constants import FuncMask
    >>> class FuncRef(Enum): BUTTON = {r'^кноп[\w]*$': (FuncMask.IS_BUTTON, FuncMask.CLICKABLE,)}
    >>> get_regular(FuncRef.BUTTON)
    '^кноп[\\\w]*$'
    """

    return first([k for k, v in enumerator.value.items()])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
