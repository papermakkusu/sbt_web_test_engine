#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Helps to construct correct xpath by given suffix od short name
"""

__author__ = 'MGVasilev'


def compose_table_xpath(xpath: str) -> str:
    """ Composes table xpath by given suffix

    :param xpath: table xpath suffix, most times looks like 'UserForm'
    :return: full table xpath

    Doctest:
    >>> compose_table_xpath(".//*[@id='UserForm:tiD:tu']")
    ".//*[@id='UserForm:tiD:tu']"
    >>> compose_table_xpath(".//*[@id='mainForm:tiD:tu']")
    ".//*[@id='mainForm:tiD:tu']"
    """

    return ".//*[@id='{0}:tu']".format(choose_table_label(xpath))


def choose_table_label(xpath: str) -> str:
    """ Chooses table label base on xpath suffix

    :param xpath: table xpath suffix
    :return: table label

    Doctest:
    >>> choose_table_label("MyUserForm")
    'UserForm:tiD'
    >>> choose_table_label("MyForm")
    'mainForm:tiD'
    """

    return 'UserForm:tiD' if 'UserForm' in xpath else 'mainForm:tiD'


def split_name(name: str) -> str:
    """ Helps to decompose names into two elements

    Doctest:
    >>> split_name("Куздрячит Бокрёнка")
    ['Куздрячит', 'Бокрёнка']
    """

    return name.split(" ", 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
