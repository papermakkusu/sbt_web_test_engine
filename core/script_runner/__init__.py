#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from subprocess import Popen, PIPE
from os import path, listdir
from os.path import abspath, dirname, isfile, join
from core.shared import *

from .run_tests import get_scripts_list, get_stands_list, run_scripts