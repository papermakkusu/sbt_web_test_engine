#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Helps Check various web elements attributes or compare them with user input
"""

from core.shared.actions import Switch, case, map_funcs, ElementNotFoundError, WebElementDecompositionException, \
    FuncRef, get_regular, compose_table_xpath, choose_table_label, URL_REPR, first, split_name

__author__ = 'MGVasilev'


class Check(object):
    """ Contains checks and related actions
    """
    def __init__(self):
        pass

    @staticmethod
    def check_page(browser, page_url: str, user_data: dict):
        """ Check if current page url corresponds to referred value
        """

        return browser.check_page(user_data[URL_REPR] + page_url)

    @staticmethod
    def check_element(browser, locator: str, argument: str, *args):
        """ Check if DOM element is present on page
        """

        while Switch(argument):
            if case(get_regular(FuncRef.TABLE)):
                return browser.verify_element(compose_table_xpath(locator))
            return browser.verify_element(locator)


    @staticmethod
    def element_contents_check(browser, value: str, argument: str=None, column_name: str=None, position: str=None,
                               xpath: str=None, trans_type: str=None, not_mod: bool=False) -> bool or object:
        """ Check current (parsed web element saved to Driver) content on containing given value
        :param browser: Current Driver() instance
        :param argument: full web element name
        :param value: user input value
        :param column_name: table column name
        :param position: indicates if we are looking for top ("ПЕРВОЙ") or bottom ("ПОСЛЕДНЕЙ") line
        :param xpath: universal element locator at page
        :return: bool or ElementNotFoundError

        Doctest:
        >>> from core.shared.custom_selenium.web_driver import Driver
        >>> browser = Driver(driver="IE")
        >>> browser.go_to("http://sbt-oafs-578:7001/SVFE2/")
        >>> browser.click(".//*[@id='LoginForm:Login']")
        >>> browser.send_key(".//*[@id='LoginForm:Login']", 'admin')
        >>> browser.click(".//*[@id='LoginForm:Password']")
        >>> browser.click(".//*[@id='LoginForm:submit']")
        >>> browser.check_page("http://sbt-oafs-578:7001/SVFE2/pages/blank.jsf")
        >>> browser.go_to("http://sbt-oafs-578:7001/SVFE2/pages/acquirer/terminal/terminal.jsf")
        >>> browser.check_page("http://sbt-oafs-578:7001/SVFE2/pages/acquirer/terminal/terminal.jsf")
        >>> browser.check_text_button(".//*[@id='UserForm:j_id533']", "Найти")
        True
        """

        while Switch(first(split_name(argument))):
            if case(get_regular(FuncRef.TABLE)):
                browser.parse_html_table(compose_table_xpath(xpath), choose_table_label(xpath))
                if column_name is None:
                    return browser.find_table_line(value)
                else:
                    res = map_funcs((browser.find_value_in_column_and_line, browser.find_value_in_column),
                                    column_name, value, position)
                    if not res and not_mod is False:
                        raise WebElementDecompositionException(
                            "Could not find requested info in table: {table}".format(table=value))
                    return True
            elif case(get_regular(FuncRef.FORM)):
                return browser.check_text_in_element(xpath, value)
            elif case(get_regular(FuncRef.FIELD)):
                return browser.check_text(xpath, value)
            elif case(get_regular(FuncRef.ELEMENT)):
                pass
            elif case(get_regular(FuncRef.HEADING)):
                return browser.check_text(xpath, value)
            elif case(get_regular(FuncRef.LINK)):
                return browser.check_text_link(xpath, value)
            elif case(get_regular(FuncRef.BUTTON)):
                return browser.check_text_button(xpath, value)
            elif case(get_regular(FuncRef.DROP_DOWN)):
                return browser.check_text_dropdown(xpath, value)

            raise NotImplementedError("Cannot check contents of {element}.".format(element=argument))
