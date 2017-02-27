#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Contains bit  shifts for various web elements attributes and collection of web elements types descriptions
"""

from core.shared.constants import Enum, IntEnum, unique

__author__ = 'MGVasilev'


@unique
class FuncMask(IntEnum):
    """ A collection of bit shift values for various elem attributes
    """
    # FUNC
    CLICKABLE = 0
    SUBMITTABLE = 1
    WRITABLE = 2
    HAS_ID = 3
    HAS_LINK = 4
    HAS_NAME = 5
    HAS_TEXT = 6
    HAS_TITLE = 7
    HOVERABLE = 8
    READABLE = 9

    # ELEMENTS
    IS_BUTTON = 20
    IS_CHECKBOX = 21
    IS_DROP_DOWN = 22
    IS_ELEMENT = 23
    IS_FIELD = 24
    IS_FORM = 25
    IS_HEADING = 26
    IS_IMAGE = 27
    IS_LINK = 28
    IS_LIST = 29
    IS_RADIO_BUTTON = 30
    IS_TAB = 31
    IS_TABLE = 32
    IS_JS = 33
    IS_TABLE_CELL = 34
    IS_TABLE_LINE = 35

    # PAGES
    IS_PAGE = 40


@unique
class FuncRef(Enum):
    """ Collection of elements and actions with attached attributes
    """

    # ELEMENT REFS
    BUTTON = {r'^кноп[\w]*$': (FuncMask.IS_BUTTON, FuncMask.CLICKABLE,)}
    CHECK_BOX = {r'^чекбокс[\w]*$': (FuncMask.IS_CHECKBOX, FuncMask.CLICKABLE,)}
    DROP_DOWN = {r'^дропдаун[\w]*$': (FuncMask.IS_DROP_DOWN, FuncMask.CLICKABLE,)}
    ELEMENT = {r'^элемент[\w]*$': (FuncMask.IS_ELEMENT,)}
    FORM = {r'^форм[\w]*$': (FuncMask.IS_FORM, FuncMask.SUBMITTABLE, FuncMask.WRITABLE,)}
    HEADING = {r'^заголов[\w]*$': (FuncMask.IS_HEADING, FuncMask.HAS_TITLE,)}
    IMAGE = {r'^изображен[\w]*$': (FuncMask.IS_IMAGE,)}
    LINK = {r'^ссыл[\w]*$': (FuncMask.IS_LINK, FuncMask.CLICKABLE, FuncMask.HOVERABLE,)}
    LIST = {r'^спис[\w]*$': (FuncMask.IS_LIST,)}
    FIELD = {r'^пол[\w]*$': (FuncMask.IS_FIELD, FuncMask.READABLE,)}
    RADIO_BUTTON = {r'^радио[\w]*$': (FuncMask.IS_RADIO_BUTTON, FuncMask.CLICKABLE,)}
    TAB = {r'^вклад[\w]*$': (FuncMask.IS_TAB, FuncMask.CLICKABLE,)}
    TABLE = {r'^таблиц[\w]*$': (FuncMask.IS_TABLE, FuncMask.WRITABLE,)}
    JS_LINK = {r'^скрипт[\w]*$': (FuncMask.IS_JS, FuncMask.HOVERABLE,)}
    TABLE_CELL = {r'^[\w\s ]*ячей[\w]*$': (FuncMask.IS_TABLE_CELL, FuncMask.CLICKABLE, FuncMask.READABLE)}
    TABLE_LINE = {r'^[\w\s ]*строк[\w]*$': (FuncMask.IS_TABLE_LINE, FuncMask.CLICKABLE, FuncMask.READABLE)}

    # PAGE REFS
    PAGE = {r'^страниц[\w]*$': (FuncMask.IS_PAGE,)}

    # VERBAL EXPRESSIONS
    CLICK = {r'^клик[\w]*$': (FuncMask.IS_LINK, FuncMask.IS_BUTTON, FuncMask.IS_CHECKBOX, FuncMask.IS_ELEMENT,
                              FuncMask.IS_RADIO_BUTTON, FuncMask.CLICKABLE, FuncMask.IS_TAB, FuncMask.HOVERABLE,
                              FuncMask.IS_DROP_DOWN, FuncMask.READABLE, FuncMask.IS_TABLE_LINE, FuncMask.IS_TABLE_CELL,
                              FuncMask.IS_TABLE, FuncMask.WRITABLE,)}
    TO_PAGE = {r'^переход[\w]*$': (FuncMask.IS_PAGE, FuncMask.HAS_TITLE,)}
    EXIST = {r'^присутств[\w]*$': (FuncMask.IS_BUTTON, FuncMask.IS_CHECKBOX, FuncMask.IS_DROP_DOWN,
                                   FuncMask.IS_ELEMENT, FuncMask.IS_TABLE, FuncMask.WRITABLE, FuncMask.IS_TAB,
                                   FuncMask.CLICKABLE, FuncMask.IS_LINK, FuncMask.IS_FORM, FuncMask.SUBMITTABLE,
                                   FuncMask.HOVERABLE, FuncMask.READABLE,)}
    ON_PAGE = {r'^находи[\w]*$': (FuncMask.IS_PAGE, FuncMask.HAS_TITLE,)}
    CLEAR = {r'^очища[\w]*$': (FuncMask.IS_FORM, FuncMask.IS_FIELD,)}
    CLOSE = {r'^заверш[\w]*$': ()}
    FILL = {r'^заполн[\w]*$': (FuncMask.IS_FORM, FuncMask.SUBMITTABLE, FuncMask.WRITABLE,)}
    LOOK = {r'^вид[\w]*$': (FuncMask.IS_TABLE, FuncMask.WRITABLE,)}
    CONTAIN = {r'^содерж[\w]*$': (FuncMask.IS_TABLE, FuncMask.IS_FIELD, FuncMask.WRITABLE, FuncMask.READABLE,
                                  FuncMask.IS_HEADING, FuncMask.HAS_TITLE,)}
    HOVER = {r'^навод[\w]*$': (FuncMask.IS_JS, FuncMask.HOVERABLE, FuncMask.IS_LINK, FuncMask.CLICKABLE,)}
    WAIT = {r'^жд[\w]*$': ()}
    LOGIN = {r'^вход[\w]*$': ()}
    CHOOSE = {r'^выб[\w]*$': (FuncMask.IS_DROP_DOWN, FuncMask.HAS_TEXT, FuncMask.CLICKABLE,)}
    ACTIVE = {r'^актив[\w]*$': (FuncMask.IS_BUTTON, FuncMask.CLICKABLE, FuncMask.IS_DROP_DOWN,
                                FuncMask.IS_ELEMENT, FuncMask.IS_FIELD, FuncMask.WRITABLE,
                                FuncMask.IS_CHECKBOX,)}
    ENTER_DATE = {r'^указ[\w ]*$': (FuncMask.IS_FORM, FuncMask.SUBMITTABLE, FuncMask.WRITABLE,)}
