#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Collection of the most common web operations
"""

from core.shared.actions import sleep, Switch, case, compose_table_xpath, get_regular, FuncRef, ADMIN_NAME, \
    choose_table_label, URL_REPR

__author__ = 'MGVasilev'


class Common(object):
    """
    Contains widely used verbal expressions
    """

    def __init__(self):
        pass

    @staticmethod
    def check_active(browser, locator: str, *args):
        """

        :param browser: default browser driver
        :param locator: universal wb element locator
        :return: str
        """
        return browser.check_active(locator)

    @staticmethod
    def wait(sec):
        """
        Switch to named page
        """

        return sleep(sec)

    @staticmethod
    def go_to_page(browser, page_url: str, user_data: dict):
        """
        Switch to named page
        """

        return browser.go_to(user_data[URL_REPR] + page_url)

    @staticmethod
    def click_element(browser, xpath: str, position: str=None, trans_type: str="", value: str=None, *args, **kwargs):
        """
        Click named button
        """

        while Switch(trans_type):
            if case(get_regular(FuncRef.TABLE_CELL)):
                browser.parse_html_table(compose_table_xpath(xpath), choose_table_label(xpath))
                return browser.click_table_cell(value=value)
            elif case(get_regular(FuncRef.TABLE_LINE)):
                browser.parse_html_table(compose_table_xpath(xpath), choose_table_label(xpath))
                return browser.click_table_line(position=position)
            else:
                return browser.click(xpath)

    @staticmethod
    def clear_value(browser, locator: str, *args):
        """
        Click named button
        """

        return browser.clear_value(locator)

    @staticmethod
    def finish_work(browser, *args):
        """
        Click named button
        """

        return browser.close()

    @staticmethod
    def move_to_element(browser, locator: str, *args):
        """
        Click named button
        """

        return browser.move_to_element(locator)

    @staticmethod
    def login(browser, role: str, user_data: dict):
        """ Login into SV with admin privileges

        :param browser: basic browser driver
        :param role: privileges  level. Currently only administrator supported
        :param user_data: additional console user input
        :return: None
        """

        if ADMIN_NAME in role.lower():
            browser.go_to(user_data['url']+'/SVFE2/')
            browser.find_element(".//*[@id='LoginForm:Login']")
            browser.click(".//*[@id='LoginForm:Login']")
            browser.send_key(".//*[@id='LoginForm:Login']", 'admin')
            browser.find_element(".//*[@id='LoginForm:Password']")
            browser.click(".//*[@id='LoginForm:Password']")
            browser.delete_value(".//*[@id='LoginForm:Password']")
            browser.send_key(".//*[@id='LoginForm:Password']", 'admin')
            browser.find_element(".//*[@id='LoginForm:submit']")
            browser.click(".//*[@id='LoginForm:submit']")

    @staticmethod
    def read_element(browser, locator: str, argument: str) -> object or None:
        """ Read element contents by given locator nd save to current Driver instance field

        :param browser: basic browser driver
        :param locator: unique path to web element on page
        :param argument: web element type
        :return: parsed web element or None
        """

        while Switch(argument):
            if case(get_regular(FuncRef.TABLE)):
                pass
            elif case(get_regular(FuncRef.FORM)):
                pass
            elif case(get_regular(FuncRef.ELEMENT)):
                pass
            elif case(get_regular(FuncRef.HEADER)):
                pass
            else:
                raise NotImplementedError("Web driver can't read {element}.".format(element=locator))

    @staticmethod
    def choose_from_dd_list(browser, locator: str, user_data: str) -> object:
        """ Choose a member from dd list

        :param browser: basic browser driver
        :param locator: unique path to web element on page
        :param user_data: additional console user input
        :return: link to web element
        """

        return browser.choose_from_dd_list(locator, user_data)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
