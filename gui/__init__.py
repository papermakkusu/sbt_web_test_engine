#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from sys import path as sys_path
from os.path import abspath, dirname, join

sys_path.append(abspath(join(dirname(__file__), "../toolbox")))

from server import *
from client import *