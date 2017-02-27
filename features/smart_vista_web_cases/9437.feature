# language: ru

Функция: search
    Сценарий: Поиск строки

        Допустим текущий проект "Smart Vista"
        Допустим текущий пользователь "Администратор"
        Тогда пользователь (находится) на "странице http://10.116.93.209:9080/SVFE2/pages/blank.jsf"
	    Когда пользователь (кликает) по "ссылке Фронт-офис"
	    Когда пользователь (кликает) по "ссылке Транзакции"
        Тогда пользователь (находится) на "странице http://10.116.93.209:9080/SVFE2/pages/translog/translog.jsf" 
        Тогда на странице (присутствует) "форма Номер карты"
        Тогда на странице (присутствует) "форма Срок действия карты"
		Тогда на странице (присутствует) "форма Дата с"
		Тогда на странице (присутствует) "форма Дата до"
		Тогда на странице (присутствует) "форма Время с"
		Тогда на странице (присутствует) "форма Время до"
		Тогда на странице (видна) "таблица UserForm"
        Тогда "таблица UserForm" (содержит) строку “№ карты, Ср. действ., Дата, Время, Ид. терм., Тип транз., Сумма, Реал. сумма, Валюта, Код ответа, Номер тр., Reversal, RRN, Код авт., Нода, Токен”
		Тогда пользователь (завершает) работу