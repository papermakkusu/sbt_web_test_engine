#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from pickle import load as pickle_load, dump as pickle_dump, UnpicklingError
from copy import deepcopy
from core.shared import *

from .tip_parser import tip_list, match_tip, get_tip, get_nick_name, name_is_page
from .exp_parser import get_short_name, get_func_by_tip, get_func_pack
from .bit_parser import calc_mask, bit_pack, compare_masks
from .db_access import read_data, write_data, get_db_urls, get_db_contents
from .xpath_updater import check_data, save_data
from .check_fucntionality import func_check, exist_check