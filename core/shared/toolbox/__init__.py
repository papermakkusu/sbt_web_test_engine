#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from lxml.html import fromstring as form_tree
from urllib.request import urlopen as get_page

from .switcher import Switch, case
from .dicts import MyDict
from .enums import MetaEnum, new_enum, get_regular
from .mappers import map_funcs
from .tweak_list import has_elem, calc_max, first, last, first_or_empty
from .word_constructor import compose_table_xpath, choose_table_label, split_name