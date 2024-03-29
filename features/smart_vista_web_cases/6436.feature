# language: ru

Функция: search
    Сценарий: Поиск строки

        Допустим текущий проект "Smart Vista"
        Допустим текущий пользователь "Администратор"
        Тогда пользователь (находится) на "странице http://10.116.93.209:9080/SVFE2/pages/blank.jsf"
	    Когда пользователь (кликает) по "ссылке Фронт-офис"
	    Когда пользователь (кликает) по "ссылке Транзакции"
        Тогда пользователь (находится) на "странице http://10.116.93.209:9080/SVFE2/pages/translog/translog.jsf" 
        Тогда на странице (присутствует) "кнопка Дополнительные параметры"
        Тогда на странице (присутствует) "кнопка Найти"
        Когда пользователь (кликает) "кнопку Дополнительные параметры"
		Тогда на странице (присутствует) "дропдаун Нода"
        Когда пользователь (выбирает) "дропдаун Нода" значением "SWITCH"
        Когда пользователь (кликает) "кнопку Найти"
        Тогда на странице (видна) "таблица UserForm"
        Тогда "таблица UserForm" (содержит) значение “SWITCH” в столбце “Нода” в “ПЕРВОЙ” строке
		Тогда "таблица UserForm" (содержит) значение “SWITCH” в столбце “Нода” в “ПОСЛЕДНЕЙ” строке
		Тогда пользователь (завершает) работу