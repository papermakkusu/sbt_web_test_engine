# language: ru

Функция: search
    Сценарий: Поиск строки

        Допустим текущий проект "Smart Vista"
        Допустим текущий пользователь "Администратор"
        Тогда пользователь (находится) на "странице http://10.116.93.209:9080/SVFE2/pages/blank.jsf"
	    Когда пользователь (кликает) по "ссылке Фронт-офис"
	    Когда пользователь (кликает) по "ссылке Управление устройствами"
	    Когда пользователь (наводит) курсор на "ссылку Управление банкоматами"
	    Когда пользователь (кликает) по "ссылке История статусов банкоматов"
        Тогда пользователь (находится) на "странице http://sbt-oafs-578:7001/SVFE2/pages/devhistorylog/devHistoryLog.jsf"
        Тогда на странице (присутствует) "дропдаун Нода"
        Тогда на странице (присутствует) "дропдаун Статус"
		Тогда на странице (присутствует) "форма PID"
        Тогда на странице (присутствует) "кнопка Дата с"
		Тогда на странице (присутствует) "кнопка До"
		Тогда на странице (присутствует) "кнопка Найти"
		Тогда на странице (присутствует) "кнопка Сбросить"		
		Когда пользователь (заполняет) "форму PID" значение "990025"
        Когда пользователь (нажимает) "кнопку Найти"
		Тогда на странице (видна) "таблица UserForm"
        Тогда "таблица UserForm" (содержит) значение “990025” в столбце “PID”
		Тогда пользователь (завершает) работу