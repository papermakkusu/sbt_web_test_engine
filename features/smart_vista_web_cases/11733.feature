# language: ru

Функция: search
    Сценарий: Справочник получателей сообщений_добавление получателя

        Допустим текущий проект "Smart Vista"
        Допустим текущий пользователь "Администратор"
        Тогда пользователь (находится) на "странице /SVFE2/pages/blank.jsf"
        Когда пользователь (кликает) по "ссылке Fraud"
        Когда пользователь (кликает) по "ссылке Справочники"
        Когда пользователь (кликает) по "ссылке Получатели сообщений"
        Тогда пользователь (находится) на "странице SVFE2/pages/fraud/messagesRecipient.jsf"
        Когда пользователь (кликает) по "кнопке Добавить"
        Тогда на странице (присутствует) "форма Наименование"
        Когда пользователь (заполняет) "форму Наименование" значением "Test11733"
        Тогда на странице (присутствует) "форма Подразделение"
        Когда пользователь (заполняет) "форму Подразделение" значением "Test11733"
        Тогда на странице (присутствует) "форма Эл. почта"
        Когда пользователь (заполняет) "форму Эл. почта" значением "Test11733@mail.ru"
        Тогда на странице (присутствует) "кнопка Сохранить"
        Когда пользователь (кликает) "кнопке Сохранить"
        Тогда на странице (видна) "таблица UserForm"
        Тогда "таблица UserForm" (содержит) значение "Test11733" в столбце "Наименование"
        Тогда пользователь (завершает) работу