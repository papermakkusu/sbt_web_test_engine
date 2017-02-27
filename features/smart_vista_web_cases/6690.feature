# language: ru

Функция: search
    Сценарий: Добавление группы

        Допустим текущий проект "Smart Vista"
        Допустим текущий пользователь "Администратор"
        Тогда пользователь (находится) на "странице /SVFE2/pages/blank.jsf"
		Когда пользователь (кликает) по "ссылке Fraud"
		Когда пользователь (наводит) по "ссылке Fraud-Эквайринг"
		Когда пользователь (наводит) по "ссылке Fraud-Эквайринг-Правила"
		Когда пользователь (наводит) по "ссылке Fraud-Эквайринг-Лимиты"
		Когда пользователь (наводит) по "ссылке Fraud-Эквайринг-Типы лимитов"
		Когда пользователь (кликает) по "ссылке Группы Параметров Транзакции"
		Тогда пользователь (находится) на "странице /SVFE2/pages/finadmin/limits/administration/tranParamGroupList.jsf"
		Тогда на странице (присутствует) "форма Идентификатор:"
		Когда пользователь (заполняет) "форму Идентификатор:" значением "6686"
		Когда пользователь (кликает) по "кнопке Найти"
		Тогда "таблица  UserForm" содержит значение "6686" в столбце "Идентификатор" в "ПЕРВОЙ" строке
		Тогда пользователь (завершает) работу