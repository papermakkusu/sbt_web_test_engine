# language: ru

Функция: search
    Сценарий: SVWI. Fraud. Аудит расследований.

        Допустим текущий проект "Smart Vista"
        Допустим текущий пользователь "Администратор"
        Тогда пользователь (находится) на "странице /SVFE2/pages/blank.jsf"
	    Когда пользователь (кликает) по "ссылке Fraud"
	    Когда пользователь (кликает) по "ссылке Аудит расследований"
        Тогда пользователь (находится) на "странице /SVFE2/pages/investigation/investigationAudit.jsf"
        Тогда на странице (присутствует) "дропдаун Аналитик"
        Тогда на странице (присутствует) "дропдаун Расследования"
        Тогда на странице (присутствует) "кнопка Найти"
        Тогда на странице (присутствует) "ссылка Сбросить"
        Когда пользователь (выбирает) в "дропдауне Аналитик" значение "Main admin account1"
        Когда пользователь (выбирает) в "дропдауне Расследования" значение "Эквайринг"
        Когда пользователь (кликает) по "кнопке Найти"	
	    Тогда на странице (видна) "таблица UserForm"
		Когда пользователь (кликает) по "кнопке Сбросить"		
Тогда "дропдаун Аналитик" (содержит) текст ""
Тогда "дропдаун Аналитик" (содержит) текст ""
Тогда пользователь (завершает) работу
