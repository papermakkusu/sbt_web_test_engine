#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

import os
from sys import path as sys_path
from os.path import abspath, dirname, join
sys_path.append(dirname(abspath(__file__)))
sys_path.append(abspath(join(dirname(__file__), "../../")))
sys_path.append(abspath(join(dirname(__file__), "../")))
os.environ['DJANGO_SETTINGS_MODULE'] = 'front_end.settings'
from django.template.context_processors import csrf
from django.shortcuts import render
from django.db import models
from django.utils import timezone
from django.conf.urls import url
from django import forms
from django.contrib import admin
from django.test import TestCase
from django.forms.formsets import formset_factory
from core.handlers import tip_list, get_db_urls, check_data, save_data, get_db_contents
from core.script_runner.run_tests import run_scripts, get_scripts_list, get_stands_list

from .models import Post
from .forms import UrlForm, NameForm, XpathForm, ChooseForm, DbContentsForm, TestsContentsForm, StandsContentsForm, \
    TextEditorWidget, HashField
from .views import go_page, view_page, run_page, get_client_ip
from .templates import *