# language: ru

Функция: search
    Сценарий: Добавление в стоп лист по картам

        Допустим текущий проект "Smart Vista"
        Допустим текущий пользователь "Администратор"
        Тогда пользователь (находится) на "странице /SVFE2/pages/blank.jsf"
		Когда пользователь (кликает) по "ссылке Fraud"
		Когда пользователь (наводит) по "ссылке Стоп листы"
		Когда пользователь (наводит) по "кнопке Стоп лист по терминалам"
	    Когда пользователь (кликает) по "кнопке Стоп лист по картам"
		Когда пользователь (кликает) по "ссылке Fraud"
		Когда пользователь (наводит) по "ссылке Стоп листы"
		Когда пользователь (наводит) по "кнопке Стоп лист по терминалам"
	    Когда пользователь (кликает) по "кнопке Стоп лист по картам"
		Тогда пользователь (находится) на "странице /SVFE2/pages/fraud/exclusion/black/card/cardBlackList.jsf"
	    Когда пользователь (кликает) по "кнопке Добавить"
		Тогда на странице (присутствует) "дропдаун Тип сущности"
		Когда пользователь (выбирает) в "дропдауне Тип сущности" значение "БИН карты"
		Тогда на странице (присутствует) "форма Идентификатор сущности"
		Когда пользователь (заполняет) "форму Идентификатор сущности" значением "547927"
		Тогда на странице (присутствует) "дропдаун Тип фрода"
		Когда пользователь (выбирает) в "дропдауне Тип фрода" значение "Эмитент"
		Тогда на странице (присутствует) "дропдаун Страна банка эмитента"
		Когда пользователь (выбирает) в "дропдауне Страна банка эмитента" значение "ALB"
		Тогда на странице (присутствует) "дропдаун Причина"
		Когда пользователь (выбирает) в "дропдауне Причина" значение "Fraud"
		Тогда на странице (присутствует) "кнопка Дата начала"
		Когда пользователь (кликает) "кнопке Дата начала"
		Тогда на странице (присутствует) "кнопка Предыдущий месяц"
		Когда пользователь (кликает) "кнопке Предыдущий месяц"
		Тогда на странице (присутствует) "кнопка Значение даты"
		Когда пользователь (кликает) "кнопке Значение даты"
		Тогда на странице (присутствует) "кнопка Дата окончания"
		Когда пользователь (кликает) "кнопке Дата окончания"
		Тогда на странице (присутствует) "кнопка Предыдущий месяц"
		Когда пользователь (кликает) "кнопке Предыдущий месяц"
		Тогда на странице (присутствует) "кнопка Значение даты 2"
		Когда пользователь (кликает) "кнопке Значение даты 2"
		Тогда на странице (присутствует) "дропдаун Код отказа"
		Когда пользователь (выбирает) в "дропдауне Код отказа" значение "827"
		Тогда на странице (присутствует) "форма Комментарий"
		Когда пользователь (заполняет) "форму Комментарий" значением "Test"
		Тогда на странице (присутствует) "кнопка Сохранить"
		Когда пользователь (кликает) "кнопке Сохранить"
		Тогда пользователь (завершает) работу
		
		
	    