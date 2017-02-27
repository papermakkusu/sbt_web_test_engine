#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from core.steps_library import *


@check_for_none_return
def parse_arg(browser, name: str) -> str:
    """ Looks for xpath in db that corresponds to given web element name
    Inside method: read_data() gives dictionary from DB with all projects and all pages inside every project

    :param name: web element name in db
    :return: String if found or error ElementNotFoundError if it was not

    Doctest:
    >>> class driver(): current_url="http://10.116.93.209:9080/SVFE2/pages/blank.jsf"
    >>> drv = driver()
    >>> class browser(): driver = drv
    >>> bro = browser()
    >>> parse_arg(bro, 'страницу /SVFE2/pages/blank.jsf')
    '/SVFE2/pages/blank.jsf'
    >>> parse_arg(bro, 'страницу /SVFE2/pages/blank_1.html')

    >>> parse_arg(bro, 'вкладки Эквайринг')
    ".//*[@id='headerMenuForm:j_id24:anchor']"
    >>> parse_arg(bro, 'заголовок Заголовок')
    ".//*[@id='statusBar']/table/tbody/tr/td[1]/div"
    """

    nick_name, plain_url = get_nick_name(name), last(re.split(Constants.URL_SPLIT, browser.driver.current_url))
    if name_is_page(name):
        return first([key for key, value in read_data()[Constants.PROJECT].items() if nick_name == key])
    return first([value for key, value in read_data()[Constants.PROJECT][plain_url].items() if nick_name == last(key)])


@check_for_none_return
def parse_exp(expression: str, value: str=None):
    """ Parses expressions and finds fitting function to handle it

    :param expression: user verbal expression
    :param value: web element name
    :return: Fitting function or ElementNotFoundError

    Doctest:
    >>> parse_exp("кликает", "кнопке Поиск")
    <function Common.click_element at 0x0269ADB0>
    >>> parse_exp("кликает", "картинке Поиск")
    core.custom_exceptions.exceptions.ElementNotFoundError: Element ('картинке Поиск',) was not found in db
    """

    assert func_check(expression, value) if value is not None else True
    exp = first([key for key in common_verbal_expressions.keys()
                 if re.match(re.compile(first(list(key.value.keys()))), expression) is not None])
    return common_verbal_expressions[exp] if exp else False


if __name__ == "__main__":
    import doctest
    doctest.testmod()

