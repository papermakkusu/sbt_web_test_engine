# language: ru

Функция: search
    Сценарий: SVWI_Fraud.Эквайринг.лимиты.лимиты.сброс фильтра

        Допустим текущий проект "Smart Vista"
        Допустим текущий пользователь "Администратор"
        Тогда пользователь (находится) на "странице /SVFE2/pages/blank.jsf"
		Когда пользователь (кликает) по "ссылке Fraud"
		Когда пользователь (наводит) по "ссылке Fraud-Эквайринг"
		Когда пользователь (наводит) по "ссылке Fraud-Эквайринг-Правила"
		Когда пользователь (наводит) по "ссылке Fraud-Эквайринг-Лимиты"
		Когда пользователь (наводит) по "ссылке Fraud-Эквайринг-Типы лимитов"
		Когда пользователь (кликает) по "ссылке Fraud-Эквайринг-Лимиты-Лимиты"
		Тогда пользователь (находится) на "странице /SVFE2/pages/finadmin/limits/administration/limitList.jsf"
		Тогда на странице (присутствует) "форма Идентификатор:"
		Когда пользователь (заполняет) "форму Идентификатор:" значением "11"
		Когда пользователь (кликает) по "кнопке Найти"
		Тогда "таблица UserForm" содержит значение "11" в столбце "Идентификатор" в "ПЕРВОЙ" строке
		Когда пользователь (кликает) по "кнопке Сбросить"
		Тогда "таблица UserForm" содержит значение "1" в столбце "Идентификатор" в "ПЕРВОЙ" строке
		Тогда пользователь (завершает) работу