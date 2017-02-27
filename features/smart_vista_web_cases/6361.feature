# language: ru
 
Функция: search
    Сценарий: Управление очередями-Настройки очередей
	 
		Допустим текущий проект "Smart Vista"
		Допустим текущий пользователь "Администратор"
		Тогда пользователь (находится) на "странице /SVFE2/pages/blank.jsf"
		Когда пользователь (кликает) по "ссылке Фронт-офис"
		# Проверить X-path = .//*[@id='headerMenuForm:j_id55:anchor'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/blank.jsf ; ссылка  Управление очередями
		Когда пользователь (кликает) по "ссылке Управление очередями"
		Тогда пользователь (находится) на "странице /SVFE2/pages/svfe/queueManagement.jsf" # Проверить X-path = .//*[@id='mainForm:j_id398'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/svfe/queueManagement.jsf ; кнопка  Найти
		Когда пользователь (кликает) по "кнопке Настройки очередей" # Проверить X-path = .//*[@id='mainForm:j_id429'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/svfe/queueManagement.jsf ; кнопка  Настройки очередей
		Тогда на странице (видна) "таблица ManagementSettingsPanelContentDiv" # Проверить X-path = .//*[@id='queueManagementSettingsPanelContentDiv'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/svfe/queueManagement.jsf ; таблица ManagementSettingsPanelContentDiv
		Тогда на странице (видна) "таблица Настройки очередей" # Проверить X-path = .//*[@id='queueManagementSettingsPanelHeader'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/svfe/queueManagement.jsf ; таблица Настройки очередей
		Тогда на странице (виден) "<элемент отображения>"
		Примеры : элемент к отображению
			| элемент отображения |   						
			| элемент Нода |			            # Проверить X-path = .//*[@id='queueManagementSettingsPanelForm:j_id308_body']/table/tbody/tr[1]/td[1] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/svfe/queueManagement.jsf ; элемент Нода
			| элемент Контроль очередей |           # Проверить X-path = .//*[@id='queueManagementSettingsPanelForm:j_id308_body']/table/tbody/tr[2]/td[1] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/svfe/queueManagement.jsf ; элемент Контроль очередей
			| элемент Всего транзакций в очереди |  # Проверить X-path = .//*[@id='queueManagementSettingsPanelForm:j_id308_body']/table/tbody/tr[3]/td[1] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/svfe/queueManagement.jsf ; элемент Всего транзакций в очереди
			| элемент Период мониторинга, сек |     # Проверить X-path = .//*[@id='queueManagementSettingsPanelForm:j_id308_body']/table/tbody/tr[4]/td[1] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/svfe/queueManagement.jsf ; элемент Период мониторинга, сек
			| элемент Время устаревания, сек |      # Проверить X-path = .//*[@id='queueManagementSettingsPanelForm:j_id308_body']/table/tbody/tr[5]/td[1] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/svfe/queueManagement.jsf ; элемент Время устаревания, сек
			| элемент Файл отчета |  			    # Проверить X-path = .//*[@id='queueManagementSettingsPanelForm:j_id308_body']/table/tbody/tr[6]/td[1] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/svfe/queueManagement.jsf ; элемент Файл отчета
		Когда пользователь (заполняет) "форму Всего транзакций в очереди" значением "821" # Проверить X-path = .//*[@id='queueManagementSettingsPanelForm:totalQueue'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/svfe/queueManagement.jsf ; Форма Всего транзакций в очереди
		Когда пользователь (заполняет) "форму Период мониторинга, сек" значением "13"     # Проверить X-path = .//*[@id='queueManagementSettingsPanelForm:monitoringPeriod'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/svfe/queueManagement.jsf ; Форма Период мониторинга, сек
		Когда пользователь (заполняет) "форму Время устаревания, сек" значением "133" 	  # Проверить X-path = .//*[@id='queueManagementSettingsPanelForm:obsolescenceTime'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/svfe/queueManagement.jsf ; Форма Время устаревания, сек
		Когда пользователь (кликает) по "кнопке Сохранить" 								  # Проверить X-path = .//*[@id='queueManagementSettingsPanelForm:j_id327'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/svfe/queueManagement.jsf ; кнопка  Настройки очередей
		Тогда пользователь (находится) на "странице /SVFE2/pages/svfe/queueManagement.jsf"
		Когда пользователь (кликает) по "кнопке Применить настройки" 					  # Проверить X-path = .//*[@id='mainForm:j_id430'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/svfe/queueManagement.jsf ; кнопка  Применить настройки
		Тогда пользователь (ждет) "2" секунды
		Тогда пользователь (находится) на "странице /SVFE2/pages/svfe/queueManagement.jsf"
		Тогда на странице (видна) "таблица Настройки очередей" # Проверить X-path = .//*[@id='j_id433:0:j_id434'] ; на странице http://sbt-oafs-578:7001/SVFE2/pages/svfe/queueManagement.jsf ; таблица Операция успешно выполнена
		Тогда пользователь (завершает) работу