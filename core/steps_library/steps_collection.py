#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from core.steps_library import *


def parse_optional(text):
    return text.strip()

parse_optional.pattern = r'\s?\w*\s?'
register_type(optional=parse_optional)


class Counter:
    """ Counts steps numbers
    """

    def __init__(self):
        self.count = 1

    def next(self):
        """ Increments counter by 1
        """
        self.count += 1

    def reset(self):
        """ Resets counter to 1
        """
        self.count = 1

    def result(self):
        return "RESULT: {num} steps passed".format(num=self.count)


# Apply project settings
@catch_exceptions
@given('текущий проект "{project}"')
def step_impl(context, project):
    context.counter = Counter()
    context.browser = Driver(driver='IE', log_name=context.config.userdata['name'],
                             user_ip=context.config.userdata['user_ip'])
    context.browser.logger.write("*"*100)
    context.browser.logger.write("START TEST {TEST}".format(TEST=context.config.userdata['user_ip']))
    context.browser.logger.write('Step {step}: Допустим текущий проект "{project}"'
                                 .format(step=context.counter.count, project=project))
    context.counter.next()


# Login
@catch_exceptions
@given('текущий пользователь "{user}"')
def step_impl(context, user):
    context.browser.logger.write('Step {step}: Допустим текущий пользователь "{user}"'
                                 .format(step=context.counter.count, user=user))
    Common.login(context.browser, user, context.config.userdata)
    context.counter.next()


# The internals of "value_2" should look like "val_1, val_2, val_3, ..." to be parsed correctly
@catch_exceptions
@when('пользователь ({expression}) "{value_1}" значениями "{value_2}" из списка')
def step_impl(context, expression, value_1, value_2):
    context.browser.logger.write('Step {step}: Когда пользователь ({expression}) "{value_1}" значениями "{value_2}" '
                                 'из списка'.format(step=context.counter.count, expression=expression, value_2=value_2,
                                                    value_1=value_1))
    val_holder, val_dict = [], {}
    for _ in value_2.split(','):
        val_holder.append(_.strip())
    for row in context.table:
        for key in val_holder:
            val_dict[key] = row[key]
    parse_exp(expression, value_1)(context.browser, parse_arg(value_1), val_dict)
    context.counter.next()


# Fill search box with passed value
@catch_exceptions
@when('пользователь ({expression}) "{value_1}" значением "{value_2}"')
def step_impl(context, expression, value_1, value_2):
    context.browser.logger.write('Step {step}: Когда пользователь ({expression}) "{value_1}" значением "{value_2}"'
                                 .format(step=context.counter.count, expression=expression, value_2=value_2,
                                         value_1=value_1))
    parse_exp(expression, value_1)(context.browser, parse_arg(context.browser, value_1), value_2)
    context.counter.next()


# ==== START CHECK ELEMENT PRESENCE ====

# Check element presence
@catch_exceptions
@given('на странице ({expression}) "{value}"')
def step_impl(context, expression, value):
    context.browser.logger.write('Step {step}: Допустим на странице ({expression}) "{value}"'
                                 .format(step=context.counter.count, expression=expression, value=value))
    parse_exp(expression, value)(context.browser, parse_arg(context.browser, value), value)
    context.counter.next()


# Check element presence
@catch_exceptions
@then('на странице ({expression}) "{value}"')
def step_impl(context, expression, value):
    context.browser.logger.write('Step {step}: Тогда на странице ({expression}) "{value}"'
                                 .format(step=context.counter.count, expression=expression, value=value))
    parse_exp(expression, value)(context.browser, parse_arg(context.browser, value), value)
    context.counter.next()


# Check element presence
@catch_exceptions
@when('на странице ({expression}) "{value}"')
def step_impl(context, expression, value):
    context.browser.logger.write('Step {step}: Когда на странице ({expression}) "{value}"'
                                 .format(step=context.counter.count, expression=expression, value=value))
    parse_exp(expression, value)(context.browser, parse_arg(context.browser, value), value)
    context.counter.next()

# ==== END CHECK ELEMENT PRESENCE ====


# ==== START TABLE STEPS ====
# Parse tables and find given value in table cells: table, value, column, row = value_1, value_2, value_3, value_4
@catch_exceptions
# Когда пользователь (кликает) по строке "2" "таблицы UserForm"
@when('{hu_0:optional} ({expression}) "{value_5}" "{value_4}" "{value_1}"')
def step_impl(context, expression, value_1, value_2=None, value_3=None, value_4=None, value_5=None, hu_0=None,):
    context.browser.logger.write('Step {step}: Когда {hu_0} ({expression}) "{value_5}" "{value_4}" "{value_1}"'
                                 .format(step=context.counter.count, hu_0=hu_0, expression=expression, value_5=value_5,
                                         value_4=value_4, value_1=value_1))
    not_mod = True if 'не' in hu_0 else False
    parse_exp(expression, value_1)(browser=context.browser, xpath=parse_arg(context.browser, value_1), argument=value_1,
                                   value=value_2, column_name=value_3, position=value_4, trans_type=value_5,
                                   not_mod=not_mod)
    context.counter.next()


@catch_exceptions
@when('{hu_0:optional} ({expression}) "{value_5}" {hu_1:optional} {hu_2:optional} "{value_2}" "{value_1}"')
def step_impl(context, expression, value_1, value_2=None, value_3=None, value_4=None, value_5=None, hu_0=None,
              hu_1=None, hu_2=None,):
    context.browser.logger.write('Step {step}: Когда {hu_0} ({expression}) "{value_5}" {hu_1} {hu_2} "{value_2}" '
                                 '"{value_1}"'.format(step=context.counter.count, hu_0=hu_0, expression=expression,
                                                      value_5=value_5, value_4=value_4, value_1=value_1,
                                                      value_2=value_2, hu_1=hu_1, hu_2=hu_2,))
    not_mod = True if 'не' in hu_0 else False
    parse_exp(expression, value_1)(browser=context.browser, xpath=parse_arg(context.browser, value_1), argument=value_1,
                                   value=value_2, column_name=value_3, position=value_4, trans_type=value_5,
                                   not_mod=not_mod)
    context.counter.next()


@catch_exceptions
# Тогда "таблица UserForm" (содержит) значение "516814677860" в столбце "Номер тр."
@then('"{value_1}" ({expression}) {hu_0:optional} "{value_2}" {hu_1:optional} {hu_2:optional} "{value_3"')
def step_impl(context, expression, value_1, value_2=None, value_3=None, value_4=None, value_5=None, hu_0=None,
              hu_1=None, hu_2=None,):
    context.browser.logger.write('Step {step}: Тогда "{value_1}" ({expression}) {hu_0} "{value_2}" {hu_1} {hu_2} '
                                 '"{value_3}"'.format(step=context.counter.count, hu_0=hu_0, expression=expression,
                                                      value_5=value_5, value_4=value_4, value_1=value_1,
                                                      value_2=value_2, hu_1=hu_1, hu_2=hu_2, value_3=value_3))
    not_mod = True if 'не' in hu_0 else False
    parse_exp(expression, value_1)(browser=context.browser, xpath=parse_arg(context.browser, value_1), argument=value_1,
                                   value=value_2, column_name=value_3, position=value_4, trans_type=value_5,
                                   not_mod=not_mod)
    context.counter.next()


@catch_exceptions
# Тогда "таблица UserForm" не (содержит) значение "516814677860" в столбце "Номер тр."
@then('"{value_1}" {hu_0:optional} ({expression}) {hu_1:optional} "{value_2}" {hu_2:optional} {hu_3:optional} '
      '"{value_3}"')
def step_impl(context, expression, value_1, value_2=None, value_3=None, value_4=None, value_5=None, hu_0=None,
              hu_1=None, hu_2=None, hu_3=None,):
    context.browser.logger.write('Step {step}: Тогда "{value_1}" {hu_0} ({expression}) {hu_1} "{value_2}" {hu_2} '
                                 '{hu_3} "{value_3}"'.format(step=context.counter.count, hu_0=hu_0,
                                                             expression=expression, value_5=value_5, value_4=value_4,
                                                             value_1=value_1, value_2=value_2, hu_1=hu_1, hu_2=hu_2,
                                                             hu_3=hu_3, value_3=value_3))
    not_mod = True if 'не' in hu_0 else False
    parse_exp(expression, value_1)(browser=context.browser, xpath=parse_arg(context.browser, value_1), argument=value_1,
                                   value=value_2, column_name=value_3, position=value_4, trans_type=value_5,
                                   not_mod=not_mod)
    context.counter.next()


@catch_exceptions
# Тогда "таблица UserForm" (содержит) значение "516814677860" в столбце "Номер тр." во "2" строке
@then('"{value_1}" ({expression}) {hu_0:optional} "{value_2}" {hu_1:optional} {hu_2:optional} "{value_3}" '
      '{hu_3:optional} "{value_4}" {hu_4:optional}')
def step_impl(context, expression, value_1, value_2=None, value_3=None, value_4=None, value_5=None, hu_0=None,
              hu_1=None, hu_2=None, hu_3=None, hu_4=None):
    context.browser.logger.write('Step {step}: Тогда "{value_1}" ({expression}) {hu_0} "{value_2}" {hu_1} {hu_2} '
                                 '"{value_3}" {hu_3} "{value_4}" {hu_4}'
                                 .format(step=context.counter.count, hu_0=hu_0, expression=expression, value_4=value_4,
                                         value_1=value_1, value_2=value_2, hu_1=hu_1, hu_2=hu_2, hu_3=hu_3,
                                         value_3=value_3, hu_4=hu_4))
    not_mod = True if 'не' in hu_0 else False
    parse_exp(expression, value_1)(browser=context.browser, xpath=parse_arg(context.browser, value_1), argument=value_1,
                                   value=value_2, column_name=value_3, position=value_4, trans_type=value_5,
                                   not_mod=not_mod)
    context.counter.next()


@catch_exceptions
@then('"{value_1}" ({expression}) {hu_0:optional} "{value_2}" {hu_1:optional}')
def step_impl(context, expression, value_1, value_2=None, value_3=None, value_4=None, value_5=None, hu_0=None,
              hu_1=None,):
    context.browser.logger.write('Step {step}: Тогда "{value_1}" ({expression}) {hu_0} "{value_2}" {hu_1}'
                                 .format(step=context.counter.count, hu_0=hu_0, expression=expression, value_1=value_1,
                                         value_2=value_2, hu_1=hu_1,))
    not_mod = True if 'не' in hu_0 else False
    parse_exp(expression, value_1)(browser=context.browser, xpath=parse_arg(context.browser, value_1), argument=value_1,
                                   value=value_2, column_name=value_3, position=value_4, trans_type=value_5,
                                   not_mod=not_mod)
    context.counter.next()
# ==== END TABLE STEPS ====


# ==== START ELEMENT ACTIVITY ====
# Check element activity
@catch_exceptions
@then('элемент "{value}" ({expression})')
def step_impl(context, expression, value, hu_1=None):
    context.browser.logger.write('Step {step}: Тогда элемент "{value}" ({expression})'
                                 .format(step=context.counter.count, expression=expression, value=value,))
    result = parse_exp(expression, value)(context.browser, parse_arg(context.browser, value))
    if hu_1 == 'не' and result:
        raise TestFailedException("Element {value} active and it should not.".format(value=value))
    context.counter.next()


# Check element activity
@catch_exceptions
@then('элемент "{value}" {hu_1:optional} ({expression})')
def step_impl(context, expression, value, hu_1=None):
    context.browser.logger.write('Step {step}: Тогда элемент "{value}" {hu_1} ({expression})'
                                 .format(step=context.counter.count, hu_1=hu_1, expression=expression, value=value,))
    result = parse_exp(expression, value)(context.browser, parse_arg(context.browser, value))
    if hu_1 == 'не' and result:
        raise TestFailedException("Element {value} active and it should not.".format(value=value))
    context.counter.next()

# ==== END ELEMENT ACTIVITY ====


# Finish work
@catch_exceptions
@then('пользователь ({expression}) {hu_0:optional}')
def step_impl(context, expression, hu_0=None):
    context.browser.logger.write('Step {step}: Тогда пользователь ({expression}) {hu_0}'
                                 .format(step=context.counter.count, hu_0=hu_0, expression=expression))
    parse_exp(expression)(context.browser)
    context.browser.logger.write(context.counter.result())
    context.counter.next()


# Work with calendar
# Когда пользователь (указывает) в "форме Календарь" дату "29.7.2016 13:54"
# & Choose from dd list
# Когда пользователь (выбирает) в "дропдауне Тип сущности" значение "БИН карты"
@catch_exceptions
@when('{hu_0:optional} ({expression}) {hu_1:optional} "{value_1}" {hu_2:optional} "{value_2}"')
def step_impl(context, expression, value_1=None, hu_0=None, hu_1=None, hu_2=None, value_2=None):
    context.browser.logger.write('Step {step}: Когда {hu_0} ({expression}) {hu_1} "{value_1}" {hu_2} "{value_2}"'
                                 .format(step=context.counter.count, hu_0=hu_0, expression=expression, value_1=value_1,
                                         value_2=value_2, hu_1=hu_1, hu_2=hu_2, ))
    if 'выб' in expression:
        parse_exp(expression, value_1)(context.browser, parse_arg(context.browser, value_1), value_1)
    elif 'указ' in expression:
        parse_exp(expression, value_1)(context.browser, parse_arg(context.browser, value_1), value_2)
    context.counter.next()


# Verify the page
# Тогда пользователь (находится) на "странице /SVFE2/pages/blank.jsf"
@catch_exceptions
@then('{hu_0:optional} ({expression}) {hu_2:optional} "{value_1}"')
def step_impl(context, expression, value_1=None, hu_0=None, hu_2=None):
    context.browser.logger.write('Step {step}: Тогда {hu_0} ({expression}) {hu_2} "{value_1}"'
                                 .format(step=context.counter.count, hu_0=hu_0, expression=expression, value_1=value_1,
                                         hu_2=hu_2, ))
    parse_exp(expression, value_1)(context.browser, parse_arg(context.browser, value_1), context.config.userdata)
    context.counter.next()


# Click element
# Когда пользователь (кликает) по "ссылке Фронт-офис"
@catch_exceptions
@when('{hu_0:optional} ({expression}) {hu_1:optional} "{value_1}"')
def step_impl(context, expression, value_1=None, hu_0=None, hu_1=None):
    context.browser.logger.write('Step {step}: Когда {hu_0} ({expression}) {hu_1} "{value_1}"'
                                 .format(step=context.counter.count, hu_0=hu_0, hu_1=hu_1, expression=expression,
                                         value_1=value_1))
    parse_exp(expression, value_1)(context.browser, parse_arg(context.browser, value_1), context.config.userdata)
    context.counter.next()


# Hover element with cursor
# Когда пользователь (наводит) курсор на "ссылку Проведение VIP-транзакции"
@catch_exceptions
@when('{hu_0:optional} ({expression}) {hu_1:optional} {hu_2:optional} "{value_1}"')
def step_impl(context, expression, value_1=None, hu_0=None, hu_1=None, hu_2=None):
    context.browser.logger.write('Step {step}: Когда {hu_0} ({expression}) {hu_1} {hu_2} "{value_1}"'
                                 .format(step=context.counter.count, hu_0=hu_0, hu_1=hu_1, hu_2=hu_2,
                                         expression=expression, value_1=value_1))
    parse_exp(expression, value_1)(context.browser, parse_arg(context.browser, value_1), context.config.userdata)
    context.counter.next()


# Waiting
# Тогда пользователь (ждет) "2" секунды
@catch_exceptions
@then('{hu_0:optional} ({expression}) "{value_1}" {hu_1:optional}')
def step_impl(context, expression, value_1=None, hu_0=None, hu_1=None):
    context.browser.logger.write('Step {step}: Тогда {hu_0} ({expression}) "{value_1}" {hu_1}'
                                 .format(step=context.counter.count, hu_0=hu_0, hu_1=hu_1, expression=expression,
                                         value_1=value_1))
    parse_exp(expression, value_1)(context.browser, parse_arg(context.browser, value_1), context.config.userdata)
    context.counter.next()


# Check element text
# Тогда "поле Автор" (содержит) текст "Автор"
@catch_exceptions
@then('"{value_1}" ({expression}) {hu_2:optional} "{value_2}"')
def step_impl(context, expression, value_1=None, hu_2=None, value_2=None):
    context.browser.logger.write('Step {step}: Тогда {value_1}" ({expression}) {hu_2} "{value_2}"'
                                 .format(step=context.counter.count, hu_2=hu_2, expression=expression, value_1=value_1,
                                         value_2=value_2))
    parse_exp(expression, value_1)(browser=context.browser, xpath=parse_arg(context.browser, value_1), argument=value_1,
                                   value=value_2)
    context.counter.next()


# Clear form
# Когда пользователь (очищает) "форму Пароль"
@catch_exceptions
@then('{hu_0:optional} ({expression}) "{value_1}"')
@when('{hu_0:optional} ({expression}) "{value_1}"')
def step_impl(context, expression, value_1=None, hu_0=None):
    context.browser.logger.write('Step {step}: Когда {hu_0:optional} ({expression}) "{value_1}'
                                 .format(step=context.counter.count, hu_0=hu_0, expression=expression, value_1=value_1))
    parse_exp(expression, value_1)(context.browser, parse_arg(context.browser, value_1), context.config.userdata)
    context.counter.next()


# General purpose step
@catch_exceptions
@when('{hu_0:optional} {hu_1:optional} ({expression}) "{value_1}"')
@when('{hu_0:optional} {hu_1:optional} ({expression}) {hu_2:optional} "{value_1}"')
@then('{hu_0:optional} ({expression}) {hu_1:optional}')
@then('{hu_0:optional} {hu_1:optional} ({expression}) "{value_1}"')
def step_impl(context, expression, value_1=None, hu_0=None, hu_1=None, hu_2=None):
    context.browser.logger.write('Step {step}: Когда {hu_0} {hu_1} ({expression}) {hu_2} "{value_1}"'
                                 .format(step=context.counter.count, hu_0=hu_0, hu_1=hu_1, hu_2=hu_2,
                                         expression=expression, value_1=value_1))
    parse_exp(expression, value_1)(context.browser, parse_arg(context.browser, value_1), context.config.userdata)
    context.counter.next()
