# language: ru

Функция: search
    Сценарий: SVWI.Настройки.Характеристики пользователя.Проверка формы.

        Допустим текущий проект "Smart Vista"
        Допустим текущий пользователь "Администратор"
        Тогда пользователь (находится) на "странице /SVFE2/pages/blank.jsf"
	    Когда пользователь (кликает) по "ссылке Настройки"
	    Когда пользователь (кликает) по "ссылке Характеристики пользователя"
        Тогда пользователь (находится) на "странице /SVFE2/pages/admpages/users/personaldata.jsf"
        Тогда на странице (присутствует) "кнопка Изменить"
        Тогда на странице (присутствует) "форма Имя пользователя"
        Тогда на странице (присутствует) "форма Новый пароль"
        Тогда на странице (присутствует) "форма Подтвердите новый пароль"
    Тогда "форма Имя пользователя" (содержит) текст "admin"


Тогда пользователь (завершает) работу
