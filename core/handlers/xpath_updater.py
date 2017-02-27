#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from core.handlers import *
from core.handlers.check_fucntionality import exist_check


input_limiter = 2

def exist_check_by_short_name(url: str, short_name: str, xpath: str) -> bool:
    """ Verifies if element with given name is in db

    :param plain_url: plain url as in db (without project mask)
    :param short_name: String with short element name
    :return: True if element with given name is present on page and False if not

    Doctest:
    >>> exist_check_by_short_name(url="http://10.116.93.209:9080/SVFE2/", short_name="Пользователь", xpath=".//*[@id='LoginForm:submit']")
    True
    >>> exist_check_by_short_name(url="http://10.116.93.209:9080/SVFE2/", short_name="Испепелитель", xpath=".//*[@id='LoginForm:submit']")
    False
    """
    plain_url = last(re.split(Constants.URL_SPLIT, url))
    name_list = [last(m) for v in [v for k, v in read_data()[Constants.PROJECT].items()
                                   if first([e.value for e in Constants.PROJECT if e.value in url])
                                   and k==plain_url] for m, n in v.items() if n == xpath]
    return True if short_name in name_list else False


def exist_check_by_xpath(url: str, xpath: str) -> bool:
    """ Verifies that element with given xpath exist in db

    Doctest:
    >>> exist_check_by_xpath(url="http://10.116.93.209:9080/SVFE2/", xpath=".//*[@id='LoginForm:submit']")
    ".//*[@id='LoginForm:submit']"
    >>> exist_check_by_xpath(url="http://10.116.93.209:9080/SVFE2/", xpath=".//*[@id='LoginForm:submit_FALSE']")
    False
    >>> exist_check_by_xpath(url="http://10.116.93.209:9080/SVFE2/pages/devhistorylog/devHistoryLog.jsf", xpath=".//*[@id='UserForm:statusList']")
    ".//*[@id='UserForm:statusList']"
    """
    plain_url = last(re.split(Constants.URL_SPLIT, url))
    for v in [n for v in [v for k, v in read_data()[Constants.PROJECT].items()
                          if first([e.value for e in Constants.PROJECT if e.value in url]) and k==plain_url]
                            for m, n in v.items()]:
        if v == xpath: return v
    return False


def get_project_stand(url: str,):
    """

    :param url:
    :return:

    Doctest:
    >>> get_project_stand(url="http://10.116.93.209:9080/SVFE2/")
    ".//*[@id='LoginForm:submit']"
    """
    return first([re.match(k, url) for k in [e.value for e in Constants.PROJECT if e.value in url]]).group(0)


# Service step; check element presence on page
# @check_for_valid_ret
# @catch_exceptions
def check_elem_presence(context, url, plain_url, xpath):
    context.browser = Driver()
    user_data = {'url': url}
    Common.login(context.browser, 'админ', user_data)
    Check.check_page(context.browser, "/SVFE2/pages/blank.jsf", user_data)
    Common.go_to_page(context.browser, plain_url, user_data)
    Check.check_page(context.browser, plain_url, user_data)
    Check.check_element(context.browser, xpath)
    Common.finish_work(context.browser)
    return True


def check_data(url: str, name: str, path: str, ):
    """ Checks if given url and element name/xpath exist in db

    Doctest
    >>> check_data(url="http://10.116.93.209:9080/SVFE2/", name='Masterpiece', path=".//*[@id='LoginForm:submit']")
    (True, 'Страница http://10.116.93.209:9080/SVFE2/ есть в базе.', "Элемент .//*[@id='LoginForm:submit']  есть в базе.")
    """

    status = False
    if not name or not path: return status, 'Имя или локатор отсутствуют.', ''
    short_name, plain_url = get_short_name(name), last(re.split(Constants.URL_SPLIT, url))
    if not re.match(r"http[s]*://[\da-z.-]+:[\d]{4}/", url): return status, 'Неверный адрес страницы.', ''
    if len(short_name)<input_limiter:  return status, 'Неверное имя {name}. Придумай подлиннее.'.format(name=name), ''
    if len(path)<input_limiter: return status, 'Придумай локатор подлиннее.', ''

    elem_exist = exist_check_by_xpath(url, path)
    name_exist = exist_check_by_short_name(url, short_name, path)

    # Create test context to be able to run service test with element check
    context, context.config, context.config.userdata = MyDict(), MyDict(), MyDict()
    context.config.userdata.update({"url": get_project_stand(url)})

    # Then make sure the element is on page
    try:
        if not check_elem_presence(context, get_project_stand(url), plain_url, path):
            return status, 'Не нахожу элемент "{path}" на странице "{url}".'.format(path=path, url=url), ''
    except TimeoutException:
        return status, 'Проверить элемент не получается, либо сервер SmartVista не отвечает.', ''

    # Read data from db
    site_data = read_data()
    if not site_data: return status, 'Не могу прочесть базу данных.', ''

    status = True
    page = first([value for key, value in site_data.items() if plain_url in list(value.keys())])

    name_notion = "с именем {name}".format(name=short_name) if name_exist else ""
    page_message = "Страница {page} есть в базе.".format(page=url) if page else 'Страницы {page} нет в базе.'.format(page=url)
    element_message = "Элемент {xpath} {name_notion} есть в базе.".format(xpath=path, name_notion=name_notion) \
        if elem_exist else 'Элемента {xpath} нет в базе.'.format(xpath=path)

    return status, page_message, element_message


def save_data(url: str, name: str, path: str, ) -> tuple:
    """ Saves given data to db

    # IMPORTANT #################################################################################################
    There is no extra check of the element existence on the page for save case as it should already been done in
    check case. Save only after check and do it wisely.
    #############################################################################################################

    Doctest:
    >>> save_data(url='http://10.116.93.209:9080/SVFE2/', name='Enter', path=".//*[@id='LoginForm:submit']")
    (True, 'Страница добавлена в базу.', '')
    >>> save_data(url='http://10.116.93.209:9080/SVFE2/', name='кнопка Ввод', path=".//*[@id='ВводForm:submit']")
    (True, 'Страница добавлена в базу.', '')
    """

    status = False
    short_name = get_short_name(name)
    plain_url = last(re.split(Constants.URL_SPLIT, url))

    site_data = read_data()
    if len(plain_url)<input_limiter: return status, 'Укажи правильный адрес.', ''
    if len(short_name)<input_limiter: return status, 'Неверное имя {name}. Придумай подлиннее.'.format(name=name), ''
    if len(path)<input_limiter: return status, 'Придумай локатор подлиннее.', ''

    if not site_data: return status, 'Не могу прочесть базу данных.', ''

    elem_exist = exist_check_by_xpath(url, path)
    name_exist = exist_check_by_short_name(url, short_name, path)
    if elem_exist and name_exist: return status, 'Локатор {xpath} уже есть в базе под именем {name}.'\
        .format(xpath=path, name=short_name), ''
    if elem_exist: return status, 'Локатор {xpath} уже есть в базе.'.format(xpath=path), ''

    status = True
    temp_site_data = deepcopy(site_data)
    page = first([value for key, value in temp_site_data[Constants.PROJECT].items() if plain_url == key])
    page_message = "Страница обновлена в базе." if page else 'Страница добавлена в базу.'
    element_message = "Элемент обновлён в базе." if elem_exist else 'Элемент добавлен в базу.'
    element_func = get_func_pack(get_func_by_tip(name) if exist_check(name) else False)

    if not page: temp_site_data[Constants.PROJECT][plain_url] = {(element_func, short_name): path}
    else: temp_site_data[Constants.PROJECT][plain_url][(element_func, short_name)] = path

    write_data({**site_data, **temp_site_data})
    return status, page_message, element_message


if __name__ == '__main__':
    import doctest
    doctest.testmod()
