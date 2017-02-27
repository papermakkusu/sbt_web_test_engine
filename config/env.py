#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from config import *


class User(Enum):
    ADMIN = {'LOGIN': 'admin',
             'PASSWORD': 'admin',
             }


class Environment(Enum):
    WINDOWS = {'DELIMITER': ', ',
               'TAB_MIN': 0,
               'WAIT_TIME': 10,
               'URL_SPLIT': re.compile(r'http://[\w.-]*:[\d]*'),
               }


class SVNodes(Enum):
    STAND_1 = 'http://10.116.93.209:9080'
    STAND_2 = 'http://sbt-oafs-578:7001'
    STAND_3 = 'http://10.68.194.117:9081'
    STAND_4 = 'http://10.116.93.209:9081'