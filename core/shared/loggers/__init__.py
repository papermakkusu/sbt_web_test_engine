#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

import logging
import logging.handlers
import os
import sys
from os.path import join
from queue import Queue
from datetime import date, datetime
from logging import getLogger
from colorama import init as init_colors, Fore, Back, Style

from .logger import construct_logger, destruct_logger