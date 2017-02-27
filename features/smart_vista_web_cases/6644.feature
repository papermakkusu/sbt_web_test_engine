# language: ru

Функция: search
    Сценарий: Поиск по слову

        Допустим текущий проект "Smart Vista"
        Допустим текущий пользователь "Администратор"
        Тогда пользователь (находится) на "странице http://10.116.93.209:9080/SVFE2/pages/blank.jsf"
	    Когда пользователь (кликает) по "ссылке Fraud"
	    Когда пользователь (кликает) по "ссылке Fraud-Эквайринг"
	    Когда пользователь (наводит) курсор на "ссылку Правила"
	    Когда пользователь (кликает) по "ссылке Карты прецендентов"
        Тогда пользователь (находится) на "странице http://10.116.93.209:9080/SVFE2/pages/fraud/precedentList_acq_card.jsf"
        Тогда на странице (присутствует) "форма Номер карты"
        Тогда на странице (присутствует) "кнопка Найти"
		Тогда на странице (присутствует) "кнопка Дата с"
		Тогда на странице (присутствует) "кнопка Дата по"		
		Когда пользователь (кликает) на "кнопку Clean"
		Когда пользователь (заполняет) "форму Номер карты" значение "5209050042180359"
		Когда пользователь (нажимает) "кнопку Найти"		
		Тогда на странице (видна) "таблица UserForm"
        Тогда "таблица UserForm" (содержит) значение 5209050042180359 в столбце “ID”
		Тогда пользователь (завершает) работу
		