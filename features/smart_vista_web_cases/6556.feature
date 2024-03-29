﻿#language:ru

Функция: search
    Сценарий: Эмиссия. Алерты. Сброс фильтров

        Допустим текущий проект "Smart Vista"
        Допустим текущий пользователь "Администратор"
	    Тогда пользователь (находится) на "странице /SVFE2/pages/blank.jsf"
	    Когда пользователь (кликает) по "ссылке Fraud"
	    Когда пользователь (наводит) курсор на "ссылку Эмиссия"
	    Когда пользователь (наводит) курсор на "ссылку Правила"
		Когда пользователь (кликает) по "ссылке Алерт"
		Тогда пользователь (находится) на "странице /SVFE2/pages/fraud/alerts.jsf"
		Когда пользователь (указывает) в "форме Тип алерта" значение "2"
		Когда пользователь (кликает) по "кнопке Найти"
		Тогда "таблица UserForm" (содержит) значение "2" в столбце "Тип алерта"
		Когда пользователь (кликает) по "ссылке Сбросить"
		Тогда "таблица UserForm" (содержит) значение "1" в столбце "Тип алерта"
		Тогда пользователь (завершает) работу