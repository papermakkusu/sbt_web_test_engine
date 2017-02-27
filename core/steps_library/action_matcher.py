#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from core.steps_library import *


common_verbal_expressions = {
    FuncRef.TO_PAGE             : Common.go_to_page,
    FuncRef.CLICK               : Common.click_element,
    FuncRef.EXIST               : Check.check_element,
    FuncRef.ON_PAGE             : Check.check_page,
    FuncRef.CLEAR               : Common.clear_value,
    FuncRef.CLOSE               : Common.finish_work,
    FuncRef.FILL                : Fill.fill_form,
    FuncRef.LOOK                : Common.read_element,
    FuncRef.CONTAIN             : Check.element_contents_check,
    FuncRef.WAIT                : Common.wait,
    FuncRef.LOGIN               : Common.login,
    FuncRef.HOVER               : Common.move_to_element,
    FuncRef.CHOOSE              : Common.choose_from_dd_list,
    FuncRef.ACTIVE              : Common.check_active,
    FuncRef.ENTER_DATE          : Fill.fill_date
}
