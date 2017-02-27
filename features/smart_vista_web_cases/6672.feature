# language: ru

Функция: search
    Сценарий: Добавление в лимиты

        Допустим текущий проект "Smart Vista"
        Допустим текущий пользователь "Администратор"
        Тогда пользователь (находится) на "странице /SVFE2/pages/blank.jsf"
		Когда пользователь (кликает) по "ссылке Fraud"
		Когда пользователь (наводит) по "ссылке Fraud-Эквайринг"
		Когда пользователь (наводит) по "ссылке Fraud-Эквайринг-Правила"
		Когда пользователь (наводит) по "ссылке Fraud-Эквайринг-Лимиты"
		Когда пользователь (наводит) по "ссылке Fraud-Эквайринг-Типы лимитов"
                Когда пользователь (кликает) по "ссылке Fraud-Эквайринг-Типы лимитов"
		Тогда пользователь (находится) на "странице /SVFE2/pages/finadmin/limits/administration/limitTypeList.jsf"
		Когда пользователь (заполняет) "форму Идентификатор:" значением "11"
		Когда пользователь (кликает) по "кнопке Найти"
                Тогда на странице (присутствует) "таблица UserForm"
                Тогда "таблица  UserForm" (содержит) значение "11" в столбце "Идентификатор"
		Когда пользователь (кликает) по "кнопке Сбросить"
		Тогда "таблица  UserForm" содержит значение "1" в столбце "Идентификатор" в "ПЕРВОЙ" строке
		Тогда пользователь (завершает) работу