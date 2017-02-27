#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

"""
Translations for Russian / русский
             And: И, К тому же
            Then: То, Тогда
Scenario Outline: Структура сценария
             But: Но, А
        Examples: Примеры
      Background: Предыстория, Контекст
           Given: Допустим, Дано, Пусть
        Scenario: Сценарий
            When: Если, Когда
         Feature: Функция, Функционал, Свойство
"""

from behave import given, when, then, step
from behave.matchers import register_type
from core.handlers import *

from .action_matcher import common_verbal_expressions
from .action_parser import parse_arg, parse_exp