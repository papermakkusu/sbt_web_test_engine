#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Helps navigating through SmartVista web pages
"""

__author__ = 'MGVasilev'


class Navigate(object):
    """ Contains checks and related actions
    """

    @staticmethod
    def follow_link(browser, xpath):
        """ Fill textbox with given text

        :param browser: default browser driver
        :param xpath: universal web element locator
        :return: None
        """
        browser.click(xpath)


    @staticmethod
    def go_to_page(browser, url):
        """ Navigate to specified page

        :param browser: default browser driver
        :param url: web page url
        :return: None
        """
        browser.go_to(url)
