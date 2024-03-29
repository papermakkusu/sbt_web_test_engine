# language: ru

Функция: search
    Сценарий: SVWI. Фронт-офис. Управление устройствами. Легальные серийные номера EPP

        Допустим текущий проект "Smart Vista"
        Допустим текущий пользователь "Администратор"
        Тогда пользователь (находится) на "странице /SVFE2/pages/blank.jsf"
	    Когда пользователь (кликает) по "ссылке Фронт-офис"
	    Когда пользователь (кликает) по "ссылке Управление устройствами"
		Когда пользователь (наводит) на "ссылку Управление банкоматами"
		Когда пользователь (кликает) по "ссылке Легальные серийные номера EPP"
        Тогда пользователь (находится) на "странице /SVFE2/pages/atmmanagement/eppList.jsf"
        Тогда на странице (присутствует) "форма Серийный номер EPP"
		Тогда на странице (присутствует) "форма PID"
		Тогда на странице (присутствует) "дропдаун Источник данных"
		Тогда на странице (присутствует) "форма Дата загрузки с"
		Тогда на странице (присутствует) "форма Дата загрузки до"
        Тогда на странице (присутствует) "кнопка Найти"
		Тогда на странице (присутствует) "кнопка Загрузить"
        Тогда на странице (присутствует) "кнопка Удалить"
        Тогда на странице (присутствует) "ссылка Сбросить"       
		Тогда на странице (видна) "таблица UserForm"
		#Добавить проверку столбцов таблицы
		Когда пользователь (кликает) по "кнопке Загрузить"
		Когда пользователь (кликает) по "кнопке Выполнить"
		Тогда на странице (присутствует) "поле Процесс запущен"
		Когда пользователь (кликает) по "ПЕРВОЙ" строке в "таблица UserForm"
		Когда пользователь (кликает) по "кнопке Удалить"
		Тогда на странице (присутствует) "поле Запись удалена"
		Тогда пользователь (завершает) работу
