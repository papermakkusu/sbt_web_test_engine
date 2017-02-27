#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from core.shared.constants import *


class Constants(object):
    # USER SPECIFIC
    LOGIN       = USR.value['LOGIN']
    PASSWORD    = USR.value['PASSWORD']

    # ENV SPECIFIC
    DELIMITER       = ENV.value['DELIMITER']
    TAB_MIN         = ENV.value['TAB_MIN']
    WAIT_TIME       = ENV.value['WAIT_TIME']
    URL_SPLIT       = ENV.value['URL_SPLIT']
    PROJECT         = PROJ
