# language: ru
 
Функция: search
    Сценарий: Fraud - Эквайринг- Карты прецендентов
	 
		Допустим текущий проект "Smart Vista"
		Допустим текущий пользователь "Администратор"
		Тогда пользователь (находится) на "странице /SVFE2/pages/blank.jsf"
		Когда пользователь (кликает) по "ссылке Fraud"
	    Когда пользователь (кликает) по "ссылке Эквайринг" 
		Когда пользователь (кликает) по "ссылке Карты прецендентов"   # Проверить X-path = .//*[@id='headerMenuForm:j_id93:anchor'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/blank.jsf ; ссылка Карты прецендентов
		Тогда пользователь (находится) на "странице /SVFE2/pages/fraud/precedentList_acq_card.jsf"
		Когда пользователь (кликает) по "кнопке КалендарьС"   # Проверить X-path = .//*[@id='UserForm:j_id314PopupButton'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/fraud/precedentList_acq_card.jsf ; кнопка КалендарьС
		Тогда на странице (видна) "таблица UserFormDateFrom"  # Проверить X-path = .//*[@id='UserForm:j_id314'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/fraud/precedentList_acq_card.jsf ; таблица UserFormDateFrom
		Когда пользователь (кликает) по "элементу МесяцНазад" # Проверить X-path = .//*[@id='UserForm:j_id314Header']/table/tbody/tr/td[2]/div ; на странице http://sbt-oafs-578:7001/SVFE2/pages/fraud/precedentList_acq_card.jsf ; элемент МесяцНазад
		Когда пользователь (кликает) по "элементу ВыборДатыС" # Проверить X-path = .//*[@id='UserForm:j_id314DayCell4'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/fraud/precedentList_acq_card.jsf ; элемент ВыборДатыС
		Когда пользователь (кликает) по "кнопке КалендарьПо"  # Проверить X-path = .//*[@id='UserForm:j_id317PopupButton'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/fraud/precedentList_acq_card.jsf ; кнопка КалендарьПо
		Тогда на странице (видна) "таблица UserFormDateTo"    # Проверить X-path = .//*[@id='UserForm:j_id317'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/fraud/precedentList_acq_card.jsf ; таблица UserFormDateTo
		Когда пользователь (кликает) по "элемент ВыборДатыПо" # Проверить X-path = .//*[@id='UserForm:j_id317DayCell34'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/fraud/precedentList_acq_card.jsf ; элемент ВыборДатыПо
		Когда пользователь (кликает) по "кнопке Найти" 		  # Проверить X-path = .//*[@id='UserForm:j_id339'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/fraud/precedentList_acq_card.jsf ; кнопка Найти
		Тогда на странице (видна) "таблица UserFormTiD"       # Проверить X-path = .//*[@id='UserForm:tiD'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/fraud/precedentList_acq_card.jsf ; таблица UserFormTiD
		Тогда на странице (присутствует) "элемент Строка"     # Проверить X-path = .//*[@id='UserForm:tiD:n:0'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/fraud/precedentList_acq_card.jsf ; элемент Строка
		Когда пользователь (кликает) по "ссылке Сбросить"     # Проверить X-path = .//*[@id='UserForm:commandGrid']/tbody/tr/td[1]/table/tbody/tr/td[2]/a ; на странице http://sbt-oafs-578:7001/SVFE2/pages/fraud/precedentList_acq.jsf ; ссылка Сбросить
		Тогда на странице (присутствует) "форма ПустаяФорма"  # Проверить X-path = .//*[@id='UserForm:j_id317InputDate'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/fraud/precedentList_acq_card.jsf ; форма ПустаяФорма 
		Тогда на странице (присутствует) "элемент ПустаяСтрока" # Проверить X-path = .//*[@id='UserForm:tiD:noDataRow']/td ; на странице http://sbt-oafs-578:7001/SVFE2/pages/fraud/precedentList_acq_card.jsf ; элемент ПустаяСтрока
		Тогда пользователь (завершает) работу