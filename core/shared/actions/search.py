#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Helps to perform search for text and other web elements attributes
"""

__author__ = 'MGVasilev'


class Search(object):
    """
    Contains widely used verbal expressions
    """

    @staticmethod
    def find_element(browser, xpath):
        """Switch to named page

        :param browser: browser driver
        :param xpath: universal web element locator
        :return:
        """
        return browser.find_element(xpath)