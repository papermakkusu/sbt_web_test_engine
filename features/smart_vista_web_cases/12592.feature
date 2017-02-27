# language: ru

Функция: search
    Сценарий: Добавление в стоп лист по картам

        Допустим текущий проект "Smart Vista"
        Допустим текущий пользователь "Администратор"
        Тогда пользователь (находится) на "странице /SVFE2/pages/blank.jsf"
		Когда пользователь (кликает) по "ссылке Fraud"
		Когда пользователь (кликает) по "ссылке Fraud-Белые списки"
		Когда пользователь (кликает) по "кнопке Добавить"
		Тогда на странице (присутствует) "дропдаун Тип сущности"
		Когда пользователь (выбирает) в "дропдауне Тип сущности" значение "БИН карты"
		Тогда на странице (присутствует) "форма Идентификатор сущности*"
		Когда пользователь (заполняет) "форму Идентификатор сущности*" значением "546938"
		Тогда на странице (присутствует) "дропдаун Тип фрода"
		Когда пользователь (выбирает) в "дропдауне Тип фрода" значение "Эмитент"
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
		Тогда на странице (присутствует) "форма Комментарий"
		Когда пользователь (заполняет) "форму Комментарий" значением "Test"
		Тогда на странице (присутствует) "кнопка Сохранить"
		Когда пользователь (кликает) по "кнопке Добавить"
		Тогда на странице (присутствует) "дропдаун Тип сущности"
		Когда пользователь (выбирает) в "дропдауне Тип сущности" значение "БИН карты"
		Тогда на странице (присутствует) "форма Идентификатор сущности"
		Когда пользователь (заполняет) "форму Идентификатор сущности" значением "546938"
		Тогда на странице (присутствует) "дропдаун Тип фрода"
		Когда пользователь (выбирает) в "дропдауне Тип фрода" значение "Эквайер"
		Тогда на странице (присутствует) "дропдаун Причина"
		Когда пользователь (выбирает) в "дропдауне Причина" значение "Credit"
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
		Тогда на странице (присутствует) "форма Комментарий"
		Когда пользователь (заполняет) "форму Комментарий" значением "Test"
		Тогда на странице (присутствует) "кнопка Сохранить"
		Когда пользователь (кликает) "кнопке Сохранить"
		Тогда пользователь (завершает) работу
		
		
	    