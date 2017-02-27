# language: ru

Функция: search
    Сценарий: Поиск строки

        Допустим текущий проект "Smart Vista"
        Допустим текущий пользователь "Администратор"
        Тогда пользователь (находится) на "странице http://10.116.93.209:9080/SVFE2/pages/blank.jsf"
	    Когда пользователь (кликает) по "ссылке Фронт-офис"
	    Когда пользователь (кликает) по "ссылке Отчеты"
	    Когда пользователь (наводит) курсор на "ссылку Управление отчетами"
	    Когда пользователь (кликает) по "ссылке Контроль создания отчетов"
        Тогда пользователь (находится) на "странице http://10.116.93.209:9080/SVFE2/pages/report/reportExecutionList.jsf"
        Тогда на странице (присутствует) "дропдаун Отчет"
        Тогда на странице (присутствует) "дропдаун Задача"
		Тогда на странице (присутствует) "дропдаун Результат"
        Тогда на странице (присутствует) "кнопка Дата с"
		Тогда на странице (присутствует) "кнопка Дата по"
		Тогда на странице (присутствует) "кнопка Найти"
		Тогда на странице (присутствует) "кнопка Сбросить"
		Тогда на странице (видна) "таблица UserForm"
        Тогда "таблица UserForm" (содержит) строку “Время запуска, Время завершения, Отчет, Задача, Имя файла, Кол-во строк, Путь к файлу, Время работы, Результат”
		Тогда пользователь (завершает) работу