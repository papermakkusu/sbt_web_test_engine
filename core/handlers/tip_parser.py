#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from core.handlers import *


tip_list = [
    'кнопка',
    'чекбокс',
    'дропдаун',
    'элемент',
    'форма',
    'заголовок',
    'изображение',
    'ссылка',
    'список',
    'поле',
    'радио',
    'вкладка',
    'таблица',
    'скрипт',
    ]


def match_tip(tip: str, exp: str) -> bool:
    """ Matches step variable tip with stored var type

    :param tip: step variable tip
    :param exp: stored var type
    :return: True if there was full match found and False if there was not

    Doctest:
    >>> match_tip('кнопка_2', 'кноп')
    True
    >>> match_tip('стрелка_4', 'кноп')
    False
    """

    return has_elem(re.findall(re.compile("^{reg}[\w+]*".format(reg=exp), re.U), tip))


def get_tip(exp: str) -> str:
    """ Returns meaning word from given expression

    Doctest:
    >>> get_tip('переходит дорогу')
    'переходит'
    """

    expr = first(exp.split(' ')) if 'клик' not in exp else exp
    return first([re.match(re.compile(i), r'{exp}'.format(exp=expr)).group() for i in
                  [first(list(val.value.keys())) for val in FuncRef]
                  if re.match(re.compile(i), r'{exp}'.format(exp=expr)) is not None])

def get_nick_name(full_name: str) -> str:
    """ Returns nick name for a given full_name excluding the first word which is a tip to functionality

    :param full_name: full web element name with "func tip" + "nick name"
    :return: string with web element nick name

    Doctest:
    >>> get_nick_name('кнопка Сам солнечный свет')
    'Сам солнечный свет'
    >>> get_nick_name('/SVFE2/pages/acquirer/vipTransactions/vipTransactionHistory.jsf')
    '/SVFE2/pages/acquirer/vipTransactions/vipTransactionHistory.jsf'
    """

    return last(split_name(full_name))


def name_is_page(name: str) -> str:
    """ Checks if tip refers to web page

    :param name: web element name with func tip
    :return: True if refers to page and False if not

    Doctest:
    >>> name_is_page('страница Какая-то не такая')
    True
    """

    if 'страниц' in first(split_name(name)):
        return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()