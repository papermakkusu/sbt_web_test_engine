#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" CUSTOM SELENIUM MODULE INITIAL IMPORTS
"""

__author__ = 'MGVasilev'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from core.shared.constants import *
from core.shared.wrappers import *
from datetime import datetime as dt
from math import fabs, ceil, floor

from .web_driver import Driver