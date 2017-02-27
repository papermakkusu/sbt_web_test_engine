#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Helps fill indicated web forms with user input data
"""

__author__ = 'MGVasilev'


class Fill(object):
    """
    Contains checks and related actions
    """

    def __init__(self):
        pass


    @staticmethod
    def fill_form(browser, xpath, value):
        """
        Fill textbox with given text
        """
        # browser.find_element_by_id('gs_htif0')
        browser.find_element(xpath)
        browser.send_key(xpath, value)

    @staticmethod
    def fill_table(browser, xpath, values):
        """
        Fill table with parameters
        """
        pass

    @staticmethod
    def fill_date(browser, xpath, date):
        """ Enter date in dynamic date form
        """
        browser.parse_calendar(xpath, date)
