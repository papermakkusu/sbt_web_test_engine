#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from core.handlers import *


file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", r"shared\constants\bxpath.py"))


def file_exists(func):
    @wraps(func)
    def wrapper(*args):
        if not os.path.exists(file_path):
            # TODO print error message here
            open(file_path, 'wb').close()
        return func(*args)
    return wrapper


@file_exists
def read_data():
    with open(file_path, 'rb') as handle:
        try: return pickle_load(handle)
        except UnpicklingError: return None
        except EOFError: return {}

## DEBUG. READ FROM BACKUP DATABASE
# def read_data():
#     """
#
#     :return:
#     """
#
#     return sites


@file_exists
def write_data(data: dict) -> None:
    old_data = read_data()
    with open(file_path, 'wb') as handle:
        temp_dict = {**old_data, **data}
        pickle_dump(temp_dict, handle)
    return 'OK'


def get_db_urls():
    """ Get all project URLs to display in web form

    :return: list of strings with pages addresses for current project

    Doctest:
    >>> get_db_urls()
    ['/SVFE2/pages/acquirer/vipTransactions/vipTransactionHistory.jsf', '/SVFE2/', '/SVFE2/pages/acquirer/terminal/terminal.jsf', '/SVFE2/pages/svfe/aeroflot/aeroflotTransactionList.jsf', '/SVFE2/pages/translog/translog.jsf', '/SVFE2/pages/blank.jsf']
    """
    return [k for k, v in read_data()[Constants.PROJECT].items()]


def get_db_contents(url, type_el=None,  name_el=None, xpath_el=None):
    """ Provides db contents for a ui view in web for a given url

    :param url: url string for which we are collection data
    :return: list of tuples [('ELEM_TYPE', 'ELEM_NAME', 'ELEM_XPATH'), ]

    Doctest:
    >>> get_db_contents('/SVFE2/')
    [('форма', 'Пароль', ".//*[@id='LoginForm:Password']"), ('кнопка', 'Enter', ".//*[@id='LoginForm:submit']"),
    ('форма', 'Пользователь', ".//*[@id='LoginForm:Login']")]
    """

    url_contents = first([v for k, v in read_data()[Constants.PROJECT].items() if k == url])
    temp = []
    for k, v in url_contents.items():
        if type_el and not re.findall(re.compile(first(list(k[0].value.keys()))), type_el):
            continue
        elif name_el and not name_el.lower() in k[1].lower():
            continue
        elif xpath_el and not xpath_el in v:
            continue
        temp.append([first(list(k[0].value.keys())), k[1], v])

    return [(m, temp[x][1], temp[x][2]) for x in range(len(temp)) for m in tip_list if first(re.findall(temp[x][0], m))]


if __name__ == "__main__":
    # a = read_data()
    # print(a)
    # write_data(a)
    import doctest
    doctest.testmod()