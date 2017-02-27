#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from core.shared.constants import *

sites = {
    Constants.PROJECT: {
        '/SVFE2/pages/atmmanagement/actionTmplList.jsf': {
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='UserForm:j_id365']",
            (FuncRef.DROP_DOWN, 'Нода'): ".//*[@id='UserForm:feNodeFilter']/tbody/tr/td[2]/select"},
        '/SVFE2/pages/svdl/loaderJobList.jsf': {
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='filterForm:j_id576']"},
        '/SVFE2/pages/fraud/fraudMatrixFilling.jsf': {
            (FuncRef.BUTTON, 'Сохранить'): ".//*[@id='editPanelForm:j_id319']",
            (FuncRef.DROP_DOWN,
             'Матрица'): ".//*[@id='mainForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td[2]/select",
            (FuncRef.BUTTON, 'Экспорт'): ".//*[@id='mainForm']/table[2]/tbody/tr/td[2]/input",
            (FuncRef.DROP_DOWN, 'Матрица*'): ".//*[@id='editPanelForm:matrixId']",
            (FuncRef.BUTTON, 'Удалить'): ".//*[@id='mainForm:j_id366']",
            (FuncRef.BUTTON, 'Изменить'): ".//*[@id='mainForm:j_id365']",
            (FuncRef.TABLE, 'UserForm'): ".//*[@id='mainForm:mainGrid']/tbody/tr/td",
            (FuncRef.FORM, 'Значение2*'): ".//*[@id='editPanelForm:columnValue']",
            (FuncRef.FORM, 'Результат*'): ".//*[@id='editPanelForm:resultValue']",
            (FuncRef.FORM, 'Значение1*'): ".//*[@id='editPanelForm:rowValue']",
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='mainForm:j_id347']",
            (FuncRef.ELEMENT, 'Ячейка'): (".//*[@id='mainForm:mainTable:BG|BRA|{3}:j_id350']/div", "Полный путь"),
            (FuncRef.LINK, 'Сбросить'): ".//*[@id='mainForm:j_id349']",
            (FuncRef.BUTTON, 'Добавить'): ".//*[@id='mainForm:j_id364']"},
        '/SVFE2/pages/fraud/precedentList_acq.jsf': {
            (FuncRef.BUTTON, 'КалендарьПо'): ".//*[@id='UserForm:j_id317PopupButton']",
            (FuncRef.ELEMENT, 'ВыборДатыС'): ".//*[@id='UserForm:j_id314DayCell4']",
            (FuncRef.TABLE, 'UserFormDateFrom'): ".//*[@id='UserForm:j_id314']",
            (FuncRef.TABLE, 'UserFormDateTo'): ".//*[@id='UserForm:j_id317']",
            (FuncRef.ELEMENT, 'ВыборДатыПо'): ".//*[@id='UserForm:j_id317DayCell34']",
            (FuncRef.ELEMENT, 'МесяцНазад'): ".//*[@id='UserForm:j_id314Header']/table/tbody/tr/td[2]/div",
            (FuncRef.TABLE, 'UserFormTiD'): ".//*[@id='UserForm:tiD']",
            (FuncRef.FORM, 'ПустаяФорма'): ".//*[@id='UserForm:j_id317InputDate']",
            (FuncRef.ELEMENT, 'Строка'): ".//*[@id='UserForm:tiD:n:0']",
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='UserForm:j_id339']",
            (FuncRef.BUTTON, 'КалендарьС'): ".//*[@id='UserForm:j_id314PopupButton']",
            (FuncRef.ELEMENT, 'ПустаяСтрока'): ".//*[@id='UserForm:tiD:noDataRow']/td",
            (FuncRef.LINK, 'Сбросить'): ".//*[@id='UserForm:commandGrid']/tbody/tr/td[1]/table/tbody/tr/td[2]/a"},
        '/SVFE2/pages/fraud/rules.jsf': {
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='UserForm:j_id333']"},
        '/SVFE2/pages/audit/auditlogin.jsf': {
            (FuncRef.TABLE, 'UserForm'): ".//*[@id='main:searchForm:tID_base']"},
        '/SVFE2/pages/finadmin/limits/administration/tranParamSetList.jsf': {
            (FuncRef.BUTTON, 'Значения по умолчанию'): ".//*[@id='editForm:j_id345']",
            (FuncRef.DROP_DOWN, 'Индикатор наличия CVV2*'): ".//*[@id='editForm:cvv2piList']",
            (FuncRef.FORM, 'Мерчант'): ".//*[@id='editForm:editInputGrid']/tbody/tr[8]/td[4]/input",
            (FuncRef.BUTTON, 'Сбросить'): ".//*[@id='UserForm:j_id392']",
            (FuncRef.DROP_DOWN, 'Группа MCC*'): ".//*[@id='editForm:mccGroupList']",
            (FuncRef.DROP_DOWN,
             'Тип терминала:'): ".//*[@id='UserForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td[4]/select",
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='UserForm:j_id391']",
            (FuncRef.DROP_DOWN, 'Валюта транзакции*\t'): ".//*[@id='editForm:currencyList']",
            (FuncRef.BUTTON, 'Добавить'): ".//*[@id='UserForm:j_id415']",
            (FuncRef.BUTTON, 'Добавить набор'): ".//*[@id='editForm:j_id342']",
            (FuncRef.DROP_DOWN, 'Тип терминала'): ".//*[@id='headerMenuForm:j_id100']",
            (FuncRef.DROP_DOWN,
             'Тип транзакции:'): ".//*[@id='UserForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td[2]/select"},
        '/SVFE2/pages/callcenter/voiceAuth.jsf': {
            (FuncRef.FORM, 'Введите терминал'): ".//*[@id='UserForm:terminalInput']"},
        '//SVFE2/pages/admpages/params/appparams.jsf': {
            (FuncRef.BUTTON, 'Очистить кэш'): ".//*[@id='mainForm:j_id460']"},
        '/SVFE2/pages/callcenter/voiceReversal.jsf': {
            (FuncRef.DROP_DOWN, 'Нода'): ".//*[@id='UserForm:feNodeFilter']/tbody/tr/td[2]/select",
            (FuncRef.ELEMENT, 'Календарь'): ".//*[@id='UserForm:j_id332']",
            (FuncRef.FORM,
             'Сумма'): ".//*[@id='UserForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[6]/input",
            (FuncRef.FORM,
             'Терминал'): ".//*[@id='UserForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input",
            (FuncRef.FORM,
             'UTRNNO'): ".//*[@id='UserForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/input",
            (FuncRef.FORM,
             'Номер карты'): ".//*[@id='UserForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[4]/input",
            (FuncRef.TABLE, 'UserForm'): ".//*[@id='UserForm:reversalTransactionTable:sd']",
            (FuncRef.FORM,
             'Валюта'): ".//*[@id='UserForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[5]/input",
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='UserForm:j_id346']",
            (FuncRef.DROP_DOWN,
             'Тип транзакции'): ".//*[@id='UserForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[3]/select",
            (FuncRef.LINK, 'Сбросить'): ".//*[@id='UserForm:j_id347']",
            (FuncRef.FORM, 'Календарь'): ".//*[@id='UserForm:j_id332PopupButton']"},
        '/SVFE2/': {
            (FuncRef.FORM, 'Пользователь'): ".//*[@id='LoginForm:Login']",
            (FuncRef.BUTTON, 'Enter'): ".//*[@id='LoginForm:submit']",
            (FuncRef.FORM, 'Пароль'): ".//*[@id='LoginForm:Password']",
            (FuncRef.LINK, 'Списки рассылки'): ".//*[@id='headerMenuForm:j_id126:anchor']"},
        '/SVFE2/pages/investigation/supervisorIssView.jsf': {
            (FuncRef.FORM, 'Правила'): ".//*[@id='UserForm:filterLine1']/tbody/tr[2]/td[4]/input",
            (FuncRef.DROP_DOWN, 'Аналитик'): ".//*[@id='UserForm:filterLine1']/tbody/tr[3]/td[4]/select",
            (FuncRef.FORM, 'С_дата'): ".//*[@id='UserForm:j_id531InputDate']",
            (FuncRef.FORM, 'hpan_'): ".//*[@id='UserForm:filterLine1']/tbody/tr[1]/td[4]/input",
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='UserForm:j_id542']",
            (FuncRef.FORM, 'По_дата'): ".//*[@id='UserForm:j_id536InputDate']",
            (FuncRef.DROP_DOWN, 'Статус'): ".//*[@id='UserForm:filterLine1']/tbody/tr[1]/td[2]/select",
            (FuncRef.FORM, 'Id123'): ".//*[@id='UserForm:filterLine1']/tbody/tr[4]/td[2]/input"},
        '/SVFE2/pages/fraud/terminalStoplist.jsf': {
            (FuncRef.ELEMENT, 'Кат. мерч.'): ".//*[@id='UserForm:tiD:j_id337']",
            (FuncRef.FORM,
             'Инициатор'): ".//*[@id='UserForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[1]/td[4]/input",
            (FuncRef.BUTTON, 'по:'): ".//*[@id='UserForm:j_id311InputDate']",
            (FuncRef.ELEMENT, 'Дата окончания'): ".//*[@id='UserForm:tiD:j_id343']",
            (FuncRef.ELEMENT, 'Название ТСТ'): ".//*[@id='UserForm:tiD:j_id334']",
            (FuncRef.ELEMENT, 'Причина'): ".//*[@id='UserForm:tiD:j_id349']",
            (FuncRef.BUTTON, 'Удалить'): ".//*[@id='UserForm:j_id370']",
            (FuncRef.BUTTON, 'Дата создания с:'): ".//*[@id='UserForm:j_id308InputDate']",
            (FuncRef.BUTTON, 'Сбросить'): ".//*[@id='UserForm:j_id329']",
            (FuncRef.BUTTON, 'Изменить'): ".//*[@id='UserForm:j_id368']",
            (FuncRef.ELEMENT, 'Дата начала'): ".//*[@id='UserForm:tiD:j_id340']",
            (FuncRef.TABLE, 'UserForm'): ".//*[@id='UserForm:tiD']",
            (FuncRef.BUTTON, 'Удалить все'): ".//*[@id='UserForm:j_id371']",
            (FuncRef.FORM,
             'ID терминала'): ".//*[@id='UserForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[1]/td[2]/input",
            (FuncRef.ELEMENT, 'ID терминала'): ".//*[@id='UserForm:tiD:j_id331']",
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='UserForm:search']",
            (FuncRef.ELEMENT, 'Дата создания'): ".//*[@id='UserForm:tiD:j_id352']",
            (FuncRef.ELEMENT, 'Код отказа'): ".//*[@id='UserForm:tiD:j_id346']",
            (FuncRef.BUTTON, 'Добавить'): ".//*[@id='UserForm:j_id366']",
            (FuncRef.ELEMENT, 'Инициатор'): ".//*[@id='UserForm:tiD:j_id355']",
            (FuncRef.DROP_DOWN,
             'Причина'): ".//*[@id='UserForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td[2]/select"},
        '/SVFE2/pages/finadmin/limits/administration/limitList.jsf': {
            (FuncRef.DROP_DOWN, 'Тип лимита'): ".//*[@id='editForm:editInputGrid']/tbody/tr[3]/td[2]/select",
            (FuncRef.BUTTON, 'Сохранить'): ".//*[@id='editForm:j_id320']",
            (FuncRef.FORM,
             'Описание:'): ".//*[@id='UserForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td[4]/input",
            (FuncRef.DROP_DOWN, 'Сущность'): ".//*[@id='editForm:editInputGrid']/tbody/tr[4]/td[2]/select",
            (FuncRef.FORM, 'Идентификатор:'): ".//*[@id='UserForm:j_id334Edit']/input",
            (FuncRef.FORM,
             'Название лимита в back-office'): ".//*[@id='editForm:editInputGrid']/tbody/tr[6]/td[2]/input",
            (FuncRef.DROP_DOWN,
             'Группа транзакционных параметров'): ".//*[@id='editForm:editInputGrid']/tbody/tr[2]/td[2]/select",
            (FuncRef.BUTTON, 'Удалить'): ".//*[@id='UserForm:j_id386']",
            (FuncRef.BUTTON, 'Сбросить'): ".//*[@id='UserForm:j_id361']",
            (FuncRef.BUTTON, 'Изменить'): ".//*[@id='UserForm:j_id385']",
            (FuncRef.FORM, 'Идентификатор'): ".//*[@id='editForm:editInputGrid']/tbody/tr[1]/td[2]/input",
            (FuncRef.TABLE, 'UserForm'): ".//*[@id='UserForm:tiD']",
            (FuncRef.FIELD, 'Ячейка 11'): ".//*[@id='UserForm:tiD:1:j_id364']",
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='UserForm:j_id360']",
            (FuncRef.FORM, 'Описание'): ".//*[@id='editForm:editInputGrid']/tbody/tr[5]/td[2]/input",
            (FuncRef.DROP_DOWN,
             'Тип лимита:'): ".//*[@id='UserForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td[6]/select",
            (FuncRef.BUTTON, 'Добавить'): ".//*[@id='UserForm:j_id384']",
            (FuncRef.BUTTON, 'Добавить лимит'): ".//*[@id='editForm:j_id319']"},
        '/SVFE2/pages/fraud/precedentList_acq_card.jsf': {
            (FuncRef.BUTTON, 'Clean'): ".//*[@id='UserForm:j_id304Footer']/table/tbody/tr/td[2]/div",
            (FuncRef.TABLE, 'UserForm'): ".//*[@id='UserForm:tiD:tu']",
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='UserForm:j_id335']",
            (FuncRef.BUTTON, 'Дата по'): ".//*[@id='UserForm:j_id307PopupButton']",
            (FuncRef.BUTTON, 'Дата с'): ".//*[@id='UserForm:j_id304PopupButton']",
            (FuncRef.FORM, 'Номер карты'): ".//*[@id='UserForm:hpan']"},
        '/SVFE2/pages/report/reportExecutionList.jsf': {
            (FuncRef.TABLE, 'UserForm'): ".//*[@id='mainForm:mainTable:tu']",
            (FuncRef.DROP_DOWN,
             'Результат'): ".//*[@id='filterForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[1]/td[6]/select",
            (FuncRef.DROP_DOWN,
             'Задача'): ".//*[@id='filterForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td[2]/select",
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='filterForm:j_id337']",
            (FuncRef.DROP_DOWN, 'Отчет'): ".//*[@id='filterForm:ReportInput']",
            (FuncRef.BUTTON, 'Дата по'): ".//*[@id='filterForm:j_id323PopupButton']",
            (FuncRef.BUTTON, 'Сбросить'): ".//*[@id='filterForm:j_id348']",
            (FuncRef.BUTTON, 'Дата с'): ".//*[@id='filterForm:j_id312PopupButton']"},
        '/SVFE2/pages/posting/targetSystemList.jsf': {
            (FuncRef.BUTTON, 'Обновить'): ".//*[@id='mainForm:j_id367']",
            (FuncRef.BUTTON, 'пагинации >> >>'): ".//*[@id='mainForm:mainTable:j_id381_table']/tbody/tr/td[6]",
            (FuncRef.BUTTON, 'Удалить'): ".//*[@id='mainForm:j_id385']",
            (FuncRef.BUTTON, 'пагинации >>'): ".//*[@id='mainForm:mainTable:j_id381_table']/tbody/tr/td[5]",
            (FuncRef.TABLE, 'Целевые системы SVPosting'): ".//*[@id='mainForm:mainTable:sd']",
            (FuncRef.BUTTON, 'Редактировать'): ".//*[@id='mainForm:j_id384']",
            (FuncRef.BUTTON, 'пагинации <<'): ".//*[@id='mainForm:mainTable:j_id381_table']/tbody/tr/td[2]",
            (FuncRef.BUTTON, 'пагинации << <<'): ".//*[@id='mainForm:mainTable:j_id381_table']/tbody/tr/td[1]",
            (FuncRef.BUTTON, 'Добавить'): ".//*[@id='mainForm:mainTable:j_id369:sortDiv']"},
        '/SVFE2/pages/acquirer/terminal/terminal.jsf': {
            (FuncRef.DROP_DOWN,
             'Нужна проверка эквайера'): ".//*[@id='UserForm']/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody/tr[4]/td[2]/select",
            (FuncRef.DROP_DOWN, 'Нода'): ".//*[@id='UserForm:feNodeFilter']/tbody/tr/td[2]/select",
            (FuncRef.FORM,
             'ID терминала'): ".//*[@id='UserForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[4]/input",
            (FuncRef.TABLE, 'UserForm'): ".//*[@id='UserForm:tiD:tu']",
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='UserForm:j_id517']",
            (FuncRef.LINK, 'Терминалы\\Доп.параметры'): ".//*[@id='UserForm:j_id520']",
            (FuncRef.FORM,
             'PID'): ".//*[@id='UserForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/input"},
        '/SVFE2/pages/report/reportJobList.jsf': {
            (FuncRef.BUTTON, 'Добавить'): ".//*[@id='j_id572:j_id573']",
            (FuncRef.BUTTON, 'Изменить'): ".//*[@id='j_id572:j_id574']"},
        '/SVFE2/pages/fe/node/feNodeBalancerList.jsf': {
            (FuncRef.LINK, 'Фронт-офис'): ".//*[@id='headerMenuForm:j_id12']/div[1]/span",
            (FuncRef.BUTTON, 'Сохранить'): ".//*[@id='feNodeBalancerEditPanelForm:j_id328']",
            (FuncRef.LINK, 'Администрирование'): ".//*[@id='headerMenuForm:j_id63:anchor']",
            (FuncRef.BUTTON, 'Удалить'): ".//*[@id='j_id359:j_id362']",
            (FuncRef.TABLE, 'UserForm'): ".//*[@id='mainForm']/table/tbody/tr/td",
            (FuncRef.BUTTON, 'Обновить'): ".//*[@id='filterForm:j_id331']",
            (FuncRef.FIELD, 'Наименование'): ".//*[@id='feNodeBalancerEditPanelForm:nameInput']",
            (FuncRef.BUTTON, 'Изменить'): ".//*[@id='j_id359:j_id361']",
            (FuncRef.FORM, 'URL'): ".//*[@id='feNodeBalancerEditPanelForm:urlInput']"},
        '/SVFE2/pages/fraud/exclusion/black/card/cardBlackList.jsf': {
            (FuncRef.BUTTON, 'Сохранить'): ".//*[@id='editForm:j_id464']",
            (FuncRef.FORM, 'Комментарий'): ".//*[@id='editForm:j_id432_body']/table/tbody/tr[9]/td[2]/input",
            (FuncRef.DROP_DOWN, 'Тип фрода'): ".//*[@id='editForm:j_id432_body']/table/tbody/tr[3]/td[2]/select",
            (FuncRef.BUTTON, 'Дата окончания'): ".//*[@id='editForm:j_id456PopupButton']",
            (FuncRef.FORM, 'Идентификатор сущности'): ".//*[@id='editForm:j_id432_body']/table/tbody/tr[2]/td[2]/input",
            (FuncRef.BUTTON, 'Значение даты 2'): ".//*[@id='editForm:j_id456DayCell14']",
            (FuncRef.DROP_DOWN,
             'Страна банка эмитента'): ".//*[@id='editForm:j_id432_body']/table/tbody/tr[4]/td[2]/select",
            (FuncRef.BUTTON, 'Дата начала'): ".//*[@id='editForm:j_id454PopupButton']",
            (FuncRef.DROP_DOWN, 'Код отказа'): ".//*[@id='editForm:j_id432_body']/table/tbody/tr[8]/td[2]/select",
            (FuncRef.BUTTON, 'Предыдущий месяц'): ".//*[@id='editForm:j_id454Header']/table/tbody/tr/td[2]/div",
            (FuncRef.BUTTON, 'Добавить'): ".//*[@id='UserForm:j_id416']",
            (FuncRef.BUTTON, 'Значение даты'): ".//*[@id='editForm:j_id454DayCell7']",
            (FuncRef.DROP_DOWN, 'Причина'): ".//*[@id='editForm:j_id432_body']/table/tbody/tr[5]/td[2]/select"},
        '/SVFE2/pages/fraud/precedentList.jsf': {
            (FuncRef.LINK,
             'Дополнительные параметры'): ".//*[@id='UserForm:commandGrid']/tbody/tr/td[2]/table/tbody/tr/td/a",
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='UserForm:j_id335']",
            (FuncRef.FORM, 'Дата с'): ".//*[@id='UserForm:j_id314InputDate']",
            (FuncRef.LINK, 'Сбросить'): ".//*[@id='UserForm:commandGrid']/tbody/tr/td[1]/table/tbody/tr/td[2]/a",
            (FuncRef.FORM, 'Дата по'): ".//*[@id='UserForm:j_id317InputDate']",
            (FuncRef.FORM, 'Номер карты'): ".//*[@id='UserForm:hpan']"},
        '/SVFE2/pages/fraud/ruleGroupList.jsf': {
            (FuncRef.BUTTON, 'обновить'): ".//*[@id='UserForm:j_id306']"},
        '/SVFE2/pages/fe/node/feNodeList.jsf': {
            (FuncRef.BUTTON, 'Обновить'): ".//*[@id='filterForm:j_id418']",
            (FuncRef.TABLE, 'UserForm'): ".//*[@id='mainForm']/table/tbody/tr/td",
            (FuncRef.BUTTON, 'Добавить'): ".//*[@id='j_id458:j_id459']",
            (FuncRef.BUTTON, 'Изменить'): ".//*[@id='j_id448:j_id450']"},
        '/SVFE2/pages/fraud/alerts.jsf': {
            (FuncRef.TABLE, 'UserForm'): ".//*[@id='mainForm:mainGrid']/tbody/tr/td",
            (FuncRef.FIELD, 'Ячейка1'): ".//*[@id='mainForm:tiD:29151:j_id332']/div",
            (FuncRef.FORM, 'Тип алерта'): ".//*[@id='mainForm:alertType']",
            (FuncRef.BUTTON, 'Удалить'): ".//*[@id='mainForm:buttonDelete']",
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='mainForm:buttonSearch']",
            (FuncRef.FORM, 'Время по'): ".//*[@id='mainForm:dateToInputDate']",
            (FuncRef.FORM, 'Время с'): ".//*[@id='mainForm:dateFromInputDate']",
            (FuncRef.LINK, 'Сбросить'): ".//*[@id='mainForm:j_id331']"},
        '/SVFE2/pages/acquirer/vipTransactions/vipTransactionHistory.jsf': {
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='UserForm:j_id335']",
            (FuncRef.FORM, 'Мерчант'): ".//*[@id='UserForm:merchantInput']",
            (FuncRef.FORM,
             'Карта'): ".//*[@id='UserForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td[2]/input",
            (FuncRef.TABLE, 'UserForm'): ".//*[@id='UserForm:tiD:tu']"},
        '/SVFE2/pages/fraud/suspectTransactionReportList.jsf': {
            (FuncRef.TABLE, 'UserForm'): ".//*[@id='UserForm:grid']/tbody/tr/td",
            (FuncRef.BUTTON, 'Создать'): ".//*[@id='UserForm:j_id345']",
            (FuncRef.FIELD, 'Операции за период'): ".//*[@id='UserForm:tiD:8:j_id355']/div",
            (FuncRef.BUTTON, 'Выполнить'): ".//*[@id='modalForm:j_id311']",
            (FuncRef.FORM, 'Дата с'): ".//*[@id='modalForm:j_id306InputDate']",
            (FuncRef.FIELD, 'Состояние'): ".//*[@id='UserForm:tiD:8:j_id352']",
            (FuncRef.FORM, 'Дата по'): ".//*[@id='modalForm:j_id309InputDate']"},
        '/SVFE2/pages/admpages/params/appparams.jsf': {
            (FuncRef.ELEMENT, 'SVRM'): ".//*[@id='mainForm:j_id444:12:mainTree:0::j_id445:handle:img:collapsed']",
            (FuncRef.ELEMENT,
             'SVRM_URL'): ".//*[@id='mainForm:j_id444:12:mainTree:0:346::j_id445:text']/table/tbody/tr/td[2]/span",
            (FuncRef.ELEMENT,
             'Настройка отображения'): ".//*[@id='mainForm:j_id444:1:mainTree:0::j_id445:handle:img:collapsed']",
            (FuncRef.ELEMENT,
             'SVPosting_URL'): ".//*[@id='mainForm:j_id444:11:mainTree:0:344::j_id445:text']/table/tbody/tr/td[2]/span",
            (FuncRef.ELEMENT,
             'Максимальное количество загружаемых данных для формы транслог'): ".//*[@id='mainForm:j_id444:1:mainTree:0:313::j_id445:text']/table/tbody/tr/td[2]/span",
            (FuncRef.ELEMENT, 'Очистить кэш'): ".//*[@id='mainForm:j_id460']",
            (FuncRef.ELEMENT,
             'Язык по умолчанию_1'): ".//*[@id='mainForm:j_id444:1:mainTree:0:59::j_id445:text']/table/tbody/tr/td[3]/select",
            (FuncRef.ELEMENT,
             'Максимальный период отбора транзакций для формы транслог (час)'): ".//*[@id='mainForm:j_id444:1:mainTree:0:309::j_id445:text']/table/tbody/tr/td[2]/span",
            (FuncRef.ELEMENT, 'Параметры приложения изменены'): ".//*[@id='mainForm:j_id432:0:j_id433']",
            (FuncRef.ELEMENT, 'SVDL'): ".//*[@id='mainForm:j_id444:10:mainTree:0::j_id445:handle:img:collapsed']",
            (FuncRef.ELEMENT, 'SVPosting'): ".//*[@id='mainForm:j_id444:11:mainTree:0::j_id445:handle:img:expanded']",
            (FuncRef.ELEMENT,
             'Нижний порог TPS'): ".//*[@id='mainForm:j_id444:9:mainTree:0:339::j_id445:text']/table/tbody/tr/td[2]/span",
            (FuncRef.ELEMENT, 'Мониторинг'): ".//*[@id='mainForm:j_id444:9:mainTree:0::j_id445:handle:img:collapsed']",
            (FuncRef.BUTTON, 'Изменить'): ".//*[@id='mainForm:j_id459']",
            (FuncRef.ELEMENT,
             'Число выбираемых строк'): ".//*[@id='mainForm:j_id444:1:mainTree:0:58::j_id445:text']/table/tbody/tr/td[2]/span",
            (FuncRef.CHECK_BOX,
             'Оповещения'): ".//*[@id='mainForm:j_id444:9:mainTree:0:337::j_id445:text']/table/tbody/tr/td[1]/input",
            (FuncRef.ELEMENT,
             'Язык по умолчанию'): ".//*[@id='mainForm:j_id444:1:mainTree:0:59::j_id445:text']/table/tbody/tr/td[2]/span",
            (FuncRef.FIELD, 'Application parameters'): ".//*[@id='statusBar']/table/tbody/tr/td[1]/div",
            (FuncRef.ELEMENT,
             'Верхний порог TPS'): ".//*[@id='mainForm:j_id444:9:mainTree:0:340::j_id445:text']/table/tbody/tr/td[2]/span",
            (FuncRef.ELEMENT,
             'SVDL_URL'): ".//*[@id='mainForm:j_id444:10:mainTree:0:342::j_id445:text']/table/tbody/tr/td[2]/span"},
        '/SVFE2/pages/acquirer/terminalaccount/terminalAccount.jsf': {
            (FuncRef.DROP_DOWN,
             'Валюта'): ".//*[@id='UserForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/select"},
        '/SVFE2/pages/blank.jsf': {
            (FuncRef.LINK, 'Настройки'): ".//*[@id='headerMenuForm:j_id171']/div[1]/span",
            (FuncRef.LINK, 'Параметры'): ".//*[@id='headerMenuForm:j_id182:anchor']",
            (FuncRef.LINK, 'VIP-транзакции'): ".//*[@id='headerMenuForm:j_id28:anchor']",
            (FuncRef.LINK, 'Эмиссия'): ".//*[@id='headerMenuForm:j_id80']",
            (FuncRef.LINK, 'Аудит пользователей'): ".//*[@id='headerMenuForm:j_id170:anchor']",
            (FuncRef.LINK, 'Планировщик задач постинга'): ".//*[@id='headerMenuForm:j_id137:anchor']",
            (FuncRef.LINK, 'Управление банкоматами'): ".//*[@id='headerMenuForm:j_id32:anchor']",
            (FuncRef.LINK, 'Возможные действия'): ".//*[@id='headerMenuForm:j_id35:anchor']",
            (FuncRef.LINK, 'Транзакции'): ".//*[@id='headerMenuForm:j_id18:anchor']",
            (FuncRef.LINK, 'Настройки'): ".//*[@id='headerMenuForm:j_id171']/div[1]/span",
            (FuncRef.LINK, 'Фронт-офис'): ".//*[@id='headerMenuForm:j_id14']/div[1]/span",
            (FuncRef.LINK, 'Fraud'): ".//*[@id='headerMenuForm:j_id76']/div[1]/span",
            (FuncRef.LINK, 'Аэрофлот'): ".//*[@id='headerMenuForm:j_id54:anchor']",
            (FuncRef.LINK, 'Fraud-Эквайринг-Правила'): ".//*[@id='headerMenuForm:j_id92']",
            (FuncRef.LINK, 'Fraud-Эквайринг'): ".//*[@id='headerMenuForm:j_id91']",
            (FuncRef.LINK, 'Счета терминалов'): ".//*[@id='headerMenuForm:j_id27:anchor']",
            (FuncRef.LINK, 'Fraud-Эквайринг-Лимиты'): ".//*[@id='headerMenuForm:j_id97']",
            (FuncRef.LINK, 'Fraud-Эквайринг-Лимиты-Лимиты'): ".//*[@id='headerMenuForm:j_id99']",
            (FuncRef.HEADING, 'Имя страницы'): ".//*[@id='statusBar']/table/tbody/tr/td[1]/div",
            (FuncRef.LINK, 'Прогрузка УС'): ".//*[@id='headerMenuForm:j_id140']/div[1]/span",
            (FuncRef.LINK, 'Информация о бронировании'): ".//*[@id='headerMenuForm:j_id55:anchor']",
            (FuncRef.LINK, 'Reversal'): ".//*[@id='headerMenuForm:j_id23:anchor']",
            (FuncRef.LINK, 'Прецеденты'): ".//*[@id='headerMenuForm:j_id94:anchor']",
            (FuncRef.LINK, 'Обработка статусных сообщений'): ".//*[@id='headerMenuForm:j_id34:anchor']",
            (FuncRef.LINK, 'Эквайринг'): ".//*[@id='headerMenuForm:j_id24:anchor']",
            (FuncRef.LINK, 'Fraud-Эмиссия-Правила'): ".//*[@id='headerMenuForm:j_id81:anchor']",
            (FuncRef.LINK, 'Голосовые операции'): ".//*[@id='headerMenuForm:j_id21:anchor']",
            (FuncRef.LINK, 'Управление устройствами'): ".//*[@id='headerMenuForm:j_id31:anchor']",
            (FuncRef.LINK, 'Параметры'): ".//*[@id='headerMenuForm:j_id182:anchor']",
            (FuncRef.DROP_DOWN, 'Модули'): ".//*[@id='headerMenuForm:j_id127']/div[1]/span",
            (FuncRef.LINK, 'Администрирование-Ноды-Ноды-Балансировщики'): ".//*[@id='headerMenuForm:j_id68:anchor']",
            (FuncRef.LINK, 'Управление отчетами'): ".//*[@id='headerMenuForm:j_id52:anchor']",
            (FuncRef.LINK, 'Fraud\\Эквайринг'): ".//*[@id='headerMenuForm:j_id80:anchor']",
            (FuncRef.LINK, 'История VIP-транзакций'): ".//*[@id='headerMenuForm:j_id30:anchor']",
            (FuncRef.BUTTON, 'Стоп лист по терминалам'): ".//*[@id='headerMenuForm:j_id108:anchor']",
            (FuncRef.LINK, 'Проведение VIP-транзакции'): ".//*[@id='headerMenuForm:j_id29:anchor']",
            (FuncRef.LINK, 'Правила'): ".//*[@id='headerMenuForm:j_id93:anchor']",
            (FuncRef.LINK, 'Карты прецедентов'): ".//*[@id='headerMenuForm:j_id95']",
            (FuncRef.LINK, 'Целевые системы'): ".//*[@id='headerMenuForm:j_id134:anchor']",
            (FuncRef.LINK, 'Голосовые авторизации'): ".//*[@id='headerMenuForm:j_id22:anchor']",
            (FuncRef.LINK, 'Fraud-Эквайринг-Наборы параметров транзакций'): ".//*[@id='headerMenuForm:j_id100']",
            (FuncRef.LINK, 'Получатели сообщений'): ".//*[@id='headerMenuForm:j_id104']",
            (FuncRef.LINK, 'Списки рассылки'): ".//*[@id='headerMenuForm:j_id126:anchor']",
            (FuncRef.LINK, 'Отчеты'): ".//*[@id='headerMenuForm:j_id51:anchor']",
            (FuncRef.LINK, 'Администрирование-Ноды'): ".//*[@id='headerMenuForm:j_id66:anchor']",
            (FuncRef.LINK, 'Администрирование'): ".//*[@id='headerMenuForm:j_id65:anchor']",
            (FuncRef.LINK, 'SVPosting'): ".//*[@id='headerMenuForm:j_id133:anchor']",
            (FuncRef.LINK, 'Отчеты по нарушениям в ТСТ'): ".//*[@id='headerMenuForm:j_id116:anchor']",
            (FuncRef.LINK, 'Мерчанты'): ".//*[@id='headerMenuForm:j_id25:anchor']",
            (FuncRef.LINK, 'Группы Параметров Транзакции'): ".//*[@id='headerMenuForm:j_id101']",
            (FuncRef.LINK, 'История статусов банкоматов'): ".//*[@id='headerMenuForm:j_id33:anchor']",
            (FuncRef.LINK, 'Справочники'): ".//*[@id='headerMenuForm:j_id103']",
            (FuncRef.LINK, 'Стоп листы'): ".//*[@id='headerMenuForm:j_id107']",
            (FuncRef.LINK, 'Администрирование-Ноды-Ноды'): ".//*[@id='headerMenuForm:j_id67:anchor']",
            (FuncRef.LINK, 'Терминалы'): ".//*[@id='headerMenuForm:j_id26:anchor']",
            (FuncRef.BUTTON, 'Стоп лист по картам'): ".//*[@id='headerMenuForm:j_id109:anchor']",
            (FuncRef.LINK, 'Контроль создания отчетов'): ".//*[@id='headerMenuForm:j_id53:anchor']"},
        '/SVFE2/pages/fraud/fraudMailingLists.jsf': {
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='filterForm:j_id361']"},
        '/SVFE2/pages/devhistorylog/devHistoryLog.jsf': {
            (FuncRef.DROP_DOWN, 'Нода'): ".//*[@id='UserForm:feNodeFilter']/tbody/tr/td[2]/select",
            (FuncRef.TABLE, 'UserForm'): ".//*[@id='UserForm:tiD:tu']",
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='UserForm:j_id332']",
            (FuncRef.BUTTON, 'Дата до'): ".//*[@id='UserForm:j_id317PopupButton']",
            (FuncRef.BUTTON, 'Дата с'): ".//*[@id='UserForm:j_id314PopupButton']",
            (FuncRef.FORM, 'PID'): ".//*[@id='UserForm:pidInput']",
            (FuncRef.DROP_DOWN, 'Статус'): ".//*[@id='UserForm:statusList']"},
        '/SVFE2/pages/translog/translog.jsf': {
            (FuncRef.FORM,
             '№ транзакции'): ".//*[@id='mainFilter:mainFilterSecondRow']/tbody/tr[1]/td[1]/table/tbody/tr[1]/td[2]/input",
            (FuncRef.DROP_DOWN,
             'Нода'): ".//*[@id='mainFilter:mainFilterSecondRow']/tbody/tr[4]/td[1]/table/tbody/tr/td[2]/select",
            (FuncRef.BUTTON, 'Последние транзакции'): ".//*[@id='mainFilter:j_id378']",
            (FuncRef.FORM, 'Терминал'): ".//*[@id='mainFilter:atmid']",
            (FuncRef.FORM, 'Срок действия карты'): ".//*[@id='mainFilter:expDateFilterInput']",
            (FuncRef.FORM, 'Дата до'): ".//*[@id='mainFilter:fDateToDate']",
            (FuncRef.FORM, 'Мерчант'): ".//*[@id='mainFilter:cardaccidc']",
            (FuncRef.FORM, 'Дата с'): ".//*[@id='mainFilter:fDateFromDate']",
            (FuncRef.DROP_DOWN,
             'Reversal'): ".//*[@id='mainFilter:mainFilterSecondRow']/tbody/tr[1]/td[1]/table/tbody/tr[1]/td[4]/select",
            (FuncRef.FORM, 'Номер карты'): ".//*[@id='mainFilter:hpan']",
            (FuncRef.BUTTON, 'Дополнительные параметры'): ".//*[@id='mainFilter:j_id373']",
            (FuncRef.FORM, 'Код ответа'): ".//*[@id='mainFilter:resp']",
            (FuncRef.TABLE, 'UserForm'): ".//*[@id='mainForm:tiD:tu']",
            (FuncRef.LINK, 'Сбросить дату и время'): ".//*[@id='mainFilter:j_id381']",
            (FuncRef.BUTTON, 'Экспорт'): ".//*[@id='mainFilter:filterButtonPanel']/tbody/tr/td[3]/input",
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='mainFilter:searchButton']",
            (FuncRef.LINK, 'Сбросить'): ".//*[@id='mainFilter:j_id380']",
            (FuncRef.FORM, 'Время с'): ".//*[@id='mainFilter:fDateFromTime']",
            (FuncRef.DROP_DOWN,
             'Тип транзакции'): ".//*[@id='mainFilter:mainFilterSecondRow']/tbody/tr[1]/td[1]/table/tbody/tr[2]/td[4]/select",
            (FuncRef.FORM, 'Время до'): ".//*[@id='mainFilter:fDateToTime']"},
        '/SVFE2/pages/finadmin/limits/administration/tranParamGroupList.jsf': {
            (FuncRef.FORM, 'Добавить группу'): ".//*[@id='editForm:j_id308']",
            (FuncRef.BUTTON, 'Сохранить'): ".//*[@id='editForm:j_id309']",
            (FuncRef.FORM,
             'Описание:'): ".//*[@id='UserForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td[4]/input",
            (FuncRef.FORM, 'Идентификатор:'): ".//*[@id='UserForm:j_id323Edit']/input",
            (FuncRef.BUTTON, 'Удалить'): ".//*[@id='UserForm:j_id351']",
            (FuncRef.BUTTON, 'Сбросить'): ".//*[@id='UserForm:j_id340']",
            (FuncRef.BUTTON, 'Изменить'): ".//*[@id='UserForm:j_id350']",
            (FuncRef.FORM, 'Идентификатор'): ".//*[@id='editForm:editInputGrid']/tbody/tr[1]/td[2]/input",
            (FuncRef.TABLE, 'UserForm'): ".//*[@id='UserForm:tiD']",
            (FuncRef.FIELD, 'Ячейка 11'): ".//*[@id='UserForm:tiD:1:j_id341']",
            (FuncRef.FORM, 'Описание'): ".//*[@id='editForm:editInputGrid']/tbody/tr[2]/td[2]/input",
            (FuncRef.BUTTON, 'Добавить'): ".//*[@id='UserForm:j_id349']",
            (FuncRef.BUTTON, 'Добавить лимит'): ".//*[@id='UserForm:j_id339']"},
        '/SVFE2/pages/svfe/aeroflot/aeroflotTransactionList.jsf': {
            (FuncRef.TABLE, 'UserForm'): ".//*[@id='mainForm:mainTable:tu']",
            (FuncRef.DROP_DOWN, 'Нода'): ".//*[@id='mainFilter:feNodeFilter']/tbody/tr/td[2]/select",
            (FuncRef.FORM,
             'Номер билета'): ".//*[@id='mainFilter']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td[7]/input",
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='mainFilter:j_id324']",
            (FuncRef.FORM,
             'Код платежа'): ".//*[@id='mainFilter']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td[5]/input",
            (FuncRef.FORM,
             'Код брони'): ".//*[@id='mainFilter']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td[3]/input"},
        '/SVFE2/pages/fraud/messagesRecipient.jsf': {
            (FuncRef.TABLE, 'UserForm'): ".//*[@id='UserForm:tiD']",
            (FuncRef.BUTTON, 'Сохранить'): ".//*[@id='MessagesRecipientEditPanelForm:j_id379']",
            (FuncRef.FORM, 'Наименование'): ".//*[@id='MessagesRecipientEditPanelForm:nameInput']",
            (FuncRef.FORM, 'Эл. почта'): ".//*[@id='MessagesRecipientEditPanelForm:emailInput']",
            (FuncRef.FORM, 'Подразделение'): ".//*[@id='MessagesRecipientEditPanelForm:placeInput']",
            (FuncRef.BUTTON, 'Добавить'): ".//*[@id='UserForm:j_id356']",
            (FuncRef.LINK, 'Fraud-Эквайринг'): ".//*[@id='headerMenuForm:j_id91']"},
        '/SVFE2/pages/finadmin/limits/administration/limitTypeList.jsf': {
            (FuncRef.BUTTON, 'Сохранить'): ".//*[@id='editForm:j_id319']",
            (FuncRef.DROP_DOWN, 'Сущность'): ".//*[@id='editForm:editInputGrid']/tbody/tr[2]/td[2]/select",
            (FuncRef.CHECK_BOX, 'Цикличность'): ".//*[@id='editForm:editInputGrid']/tbody/tr[3]/td[2]/input",
            (FuncRef.FORM, 'Идентификатор:'): ".//*[@id='headerMenuForm:j_id100']",
            (FuncRef.BUTTON, 'Сбросить'): ".//*[@id='UserForm:j_id351']",
            (FuncRef.BUTTON, 'Изменить'): ".//*[@id='UserForm:j_id373']",
            (FuncRef.ELEMENT, 'Ячейка 11'): ".//*[@id='UserForm:tiD:1:j_id352']",
            (FuncRef.TABLE, 'UserForm'): ".//*[@id='UserForm:tiD']",
            (FuncRef.CHECK_BOX, 'Откат при реверсале'): ".//*[@id='editForm:editInputGrid']/tbody/tr[5]/td[2]/input",
            (FuncRef.FIELD, 'Ячейка 11'): ".//*[@id='UserForm:tiD:11:j_id352']",
            (FuncRef.CHECK_BOX, 'Значение увеличивается'): ".//*[@id='editForm:editInputGrid']/tbody/tr[4]/td[2]/input",
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='UserForm:j_id350']",
            (FuncRef.BUTTON, 'Добавить тип лимита'): ".//*[@id='editForm:j_id318']",
            (FuncRef.BUTTON, 'Добавить'): ".//*[@id='UserForm:j_id372']"},
        '/SVFE2/pages/posting/jobList.jsf': {
            (FuncRef.DROP_DOWN,
             'Нода'): ".//*[@id='filterForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td[2]/select",
            (FuncRef.BUTTON, 'пагинации >>'): ".//*[@id='mainForm:mainTable:j_id578_table']/tbody/tr/td[7]",
            (FuncRef.TABLE, 'Планировщик задач постинга'): ".//*[@id='mainForm:mainTable']",
            (FuncRef.ELEMENT,
             'Нода'): ".//*[@id='filterForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td[1]",
            (FuncRef.BUTTON, 'Удалить'): ".//*[@id='j_id598:j_id601']",
            (FuncRef.BUTTON, 'пагинации <<'): ".//*[@id='mainForm:mainTable:j_id578_table']/tbody/tr/td[2]",
            (FuncRef.BUTTON, 'Сбросить'): ".//*[@id='filterForm:j_id537']",
            (FuncRef.BUTTON, 'Изменить'): ".//*[@id='j_id598:j_id600']",
            (FuncRef.BUTTON, 'пагинации << <<'): ".//*[@id='mainForm:mainTable:j_id578_table']/tbody/tr/td[1]",
            (FuncRef.BUTTON, 'пагинации >> >>'): ".//*[@id='mainForm:mainTable:j_id578_table']/tbody/tr/td[8]",
            (FuncRef.BUTTON, 'Запустить'): ".//*[@id='j_id598:j_id602']",
            (FuncRef.ELEMENT,
             'Тип постинга'): ".//*[@id='filterForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td[3]",
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='filterForm:j_id536']",
            (FuncRef.HEADING, 'Планировщик задач постинга'): ".//*[@id='statusBar']/table/tbody/tr/td[1]/div",
            (FuncRef.DROP_DOWN,
             'Тип постинга'): ".//*[@id='filterForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td[4]/select",
            (FuncRef.BUTTON, 'Добавить'): ".//*[@id='j_id598:j_id599']"
            },
            '/SVFE2/pages/acquirer/merchant/merchant.jsf':{
            (FuncRef.BUTTON, 'Найти'): ".//*[@id='UserForm:j_id345']",
            (FuncRef.LINK, 'Сбросить'): ".//*[@id='UserForm:j_id346']",
            (FuncRef.HEADING, 'Мерчант'): ".//*[@id='UserForm']/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]",
            (FuncRef.DROP_DOWN, 'Нода'):".//*[@id='UserForm:feNodeFilter']/tbody/tr/td[2]/select"},


    }
}


