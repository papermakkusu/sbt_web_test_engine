# language: ru

Функция: search
    Сценарий: Проверка работы дропдаунов

        Допустим текущий проект "Smart Vista"
        Допустим текущий пользователь "Администратор"
        Тогда пользователь (находится) на "странице /SVFE2/pages/blank.jsf"
        Когда пользователь (кликает) по "ссылке Фронт-офис"
        Когда пользователь (кликает) по "ссылке Эквайринг"
        Когда пользователь (наводит) курсор на "ссылку Мерчанты"
        Когда пользователь (кликает) по "ссылке Счета терминалов"
        Тогда пользователь (находится) на "странице /SVFE2/pages/acquirer/terminalaccount/terminalAccount.jsf"
        Тогда на странице (присутствует) "дропдаун Валюта"
        Когда пользователь (выбирает) в "дропдауне Валюта" значение "643 (RUB)"
        Тогда пользователь (завершает) работу