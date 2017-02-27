# language: ru

Функция: search
    Сценарий: Поиск по слову

        Допустим текущий проект "Smart Vista"
        Допустим текущий пользователь "Администратор"
        Тогда пользователь (находится) на "странице /SVFE2/pages/blank.jsf"
        Когда пользователь (кликает) по "ссылке Фронт-офис"
        Когда пользователь (кликает) по "ссылке Эквайринг"
        Когда пользователь (наводит) курсор на "ссылку Мерчанты"
        Когда пользователь (кликает) по "ссылке VIP-транзакции"
        Когда пользователь (наводит) курсор на "ссылку Проведение VIP-транзакции"
        Когда пользователь (кликает) по "ссылке История VIP-транзакций"
        Тогда пользователь (находится) на "странице /SVFE2/pages/acquirer/vipTransactions/vipTransactionHistory.jsf"
        Тогда на странице (присутствует) "форма Карта"
        Тогда на странице (присутствует) "форма Мерчант"
        Тогда на странице (присутствует) "кнопка Найти"
        Когда пользователь (заполняет) "форму Карта" значением "5479270010023885"
        Когда пользователь (заполняет) "форму Мерчант" значением "920000000001"
        Когда пользователь (кликает) по "кнопке Найти"
        Тогда на странице (видна) "таблица UserForm"
        Тогда "таблица UserForm" (содержит) значение "5479270010023885" в столбце "Карта"
        Тогда пользователь (завершает) работу