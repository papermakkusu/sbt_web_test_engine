#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from except_raisers import check_for_timeout_except

""" Module wraps basic selenium functions with vital custom improvements
"""


from core.shared.custom_selenium import *

__author__ = 'MGVasilev'


class Driver(object):
    """
    Basic webdriver class

    """

    def __init__(self, log_name: str, user_ip: str="localhost", driver="PhantomJS", project: str=Constants.PROJECT, ):
        """
        All configs values should be stored to configuration file
        """

        if driver == "IE":
            self.driver = webdriver.Ie("IEDriverServer")
        else:
            self.driver = webdriver.PhantomJS("PhantomJS")
        self.project = project
        self.wait_time = Constants.WAIT_TIME            # seconds to wait for element to appear on page
        self.html_tab_min = Constants.TAB_MIN           # minimum lines in html_pages table
        self.tab_delim = Constants.DELIMITER
        self.logger = construct_logger(test_name=log_name, alias=user_ip)
        self.attr = MyDict()
        self.attr.element = None
        self.attr.html_tab = None
        self.attr.html_tab_max = None
        self.attr.html_tab_label = None
        self.attr.html_tab_xpath = None

        self.logger.write("Start test {name} by user {ip}".format(name=log_name, ip=user_ip))

    def go_to(self, http_address):
        """ Navigate to certain page
        """
        self.driver.get(http_address)

    @check_for_elem_presence
    def find_element(self, xpath):
        """ Find HTML element by xpath on page. Throws exception if element was not found.
        """
        try:
            return WebDriverWait(self.driver, self.wait_time).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException as err:
            self.logger.error("Web element {elem} was not loaded in time.".format(elem=xpath))
            Common.finish_work(self.driver)


    def send_key(self, xpath, key):
        """ Send key to existing element. Submitting is possible but not currently user due to the button-oriented
        submission in application
        """
        self.find_element(xpath).send_keys(key)
        # self.attr.element.submit()

    def check_active(self, xpath: str):
        """ Check if element is active on page
        """
        return self.find_element(xpath).is_enabled()

    def choose_from_dd_list(self, xpath: str, value: str):
        """ Choose element from dd list by given value
        """
        for option in self.find_element(xpath).find_elements_by_tag_name('option'):
            if option.text in value:
                option.click()

    def verify_element(self, xpath):
        """ Verify the element is on the page
        """
        return True if self.find_element(xpath) else False

    def click(self, xpath):
        """ Click selected element
        """
        ActionChains(self.driver).click(self.find_element(xpath)).perform()

    def close(self):
        """ Closes browser session
        """
        for attr in self.attr.keys(): self.attr[attr] = None
        self.driver.close()

    def move_to_element(self, xpath):
        """ Switch cursor to given element
        """
        ActionChains(self.driver).move_to_element(self.find_element(xpath)).perform()

    def tick_checkbox(self, xpath):
        self.find_element(xpath).click()

    def check_page(self, url, i=0):
        """ Check user is on given page
        """
        while i < self.wait_time and self.driver.current_url != url:
            sleep(i)
            i += 0.5

    def delete_value(self, locator):
        """ Remove values from form
        """
        self.find_element(locator).clear()

    def parse_html_table(self, xpath, label):
        """ Parses html table located by given xpath and writes it to "self.attr.parsed_table" field of the Driver
        """

        # Read the table HEADER tag contents
        header = first([row.text.split("\n") for row in
                        self.driver.find_elements_by_xpath(".//*[@id='{label}:header']".format(label=label))])
        # Get the table BODY link
        temp = first([row for row in self.driver.find_elements_by_xpath(".//*[@id='{label}:tb']".format(label=label))])
        # Read the table BODY tag contents
        body = [a.find_elements_by_tag_name("td") for a in temp.find_elements_by_tag_name("tr")][1:]
        if not body:
            raise ElementNotFoundError("There is no required table.")

        # Compose complete dictionary out of read data
        table_template, _ = {}, 0
        while _ < len(header):
            temp_dict, iter = {}, 0
            for m in body:
                temp_dict.update({iter: m[_].text})
                iter += 1
            table_template.update({header[_]: temp_dict})
            _ += 1
        # Write generated dictionary to corresponding Driver class field
        self.attr.html_tab = table_template
        self.attr.html_tab_label = label
        self.attr.html_tab_xpath = xpath

    def find_value_in_column_and_line(self, column_name: str, value: str, position=None) -> str:
        """ Finds first value in column with given name and matches it with element value from signature

        :parameter column_name: Column name we search the value within
        :parameter value: Data we'd like to match in given column.
        :return: Value of the first cell in given column

        Doctest:
        >>> browser = Driver()
        >>> sal = {0: '$162,700', 1: '$1,200,000', 2: '$2,400,000'}
        >>> age = {0: '33', 1: '44', 2: '55'}
        >>> dat = {0: '2008/11/28', 1: '2006/12/13', 2: '2009/07/21'}
        >>> pos = {0: 'Accountant', 1: 'Manager', 2: 'Developer'}
        >>> off = {0: 'Tokyo', 1: 'Moscow', 2: 'Sidney'}
        >>> nam = {0: 'Airi Satou', 1: 'John Smith', 2: 'Simon Phoenix'}
        >>> browser.attr.html_tab = {'Sal': sal, 'Age': age, 'Date': dat, 'Pos': pos, 'Office': off, 'Name': nam}
        >>> browser.find_value_in_column_and_line('Sal', '$162,700', '1')
        '$162,700'
        >>> browser.find_value_in_column_and_line('Sal', '$1,200,000', '1')

        """

        if not position:
            return
        return first([first([val for key, val in v.items() if val == value and key == (int(position) - 1)]) for k, v in
                      self.attr.html_tab.items() if k == column_name ])

    def find_value_in_column(self, column_name: str, value: str, position=None) -> str:
        """ Check that table column with given name contains the given value

        :parameter column_name: Column name we search the value within
        :parameter value: Data we'd like to match in given column.
        :return: True if value found and False if not

        Doctest:
        >>> browser = Driver()
        >>> sal = {0: '$162,700', 1: '$1,200,000', 2: '$2,400,000'}
        >>> age = {0: '33', 1: '44', 2: '55'}
        >>> dat = {0: '2008/11/28', 1: '2006/12/13', 2: '2009/07/21'}
        >>> pos = {0: 'Accountant', 1: 'Manager', 2: 'Developer'}
        >>> off = {0: 'Tokyo', 1: 'Moscow', 2: 'Sidney'}
        >>> nam = {0: 'Airi Satou', 1: 'John Smith', 2: 'Simon Phoenix'}
        >>> browser.attr.html_tab = {'Sal': sal, 'Age': age, 'Date': dat, 'Pos': pos, 'Office': off, 'Name': nam}
        >>> browser.find_value_in_column('Sal', '$2,400,000')
        '$2,400,000'
        >>> browser.find_value_in_column('Date', '2006/12/13')
        '2006/12/13'
        >>> browser.find_value_in_column('Date', '55')

        """
        if position:
            return
        return first([first([val for key, val in v.items() if val == value]) for k, v in
                      self.attr.html_tab.items() if k == column_name ])

    def find_table_line(self, match_string: str) -> bool:
        """ Matches given line with all lines from table iteratively

        :parameter match_string: A data line we'd like to match. Expects string of format 'arg_1, arg2, arg3, ...'
        :return: True or False depending on  matching was a success or not

        Doctest:
        >>> browser = Driver()
        >>> sal = {0: '$162,700',}
        >>> age = {0: '33',}
        >>> dat = {0: '2008/11/28',}
        >>> pos = {0: 'Accountant',}
        >>> off = {0: 'Tokyo',}
        >>> nam = {0: 'Airi Satou',}
        >>> browser.attr.html_tab = {'Sal': sal, 'Age': age, 'Date': dat, 'Pos': pos, 'Office': off, 'Name': nam}
        >>> browser.attr.html_tab_max, line = 1, '33, Accountant, Airi Satou, 2008/11/28, Tokyo, $162,700'
        >>> browser.find_table_line(line)
        True
        >>> line = '03, Accountant, Airi Satou, 2008/11/28, Tokyo, $162,700'
        >>> browser.find_table_line(line)
        False
        """

        temp_di = []
        for line in range(self.html_tab_min, self.attr.html_tab_max):
            temp_di.append([self.attr.html_tab[k][line] for k, v in self.attr.html_tab.items()])
        return has_elem([True for line in temp_di if set(line) == set(match_string.split(self.tab_delim))])

    def click_table_line(self, position=None, *args, **kwargs) -> bool:
        """ Clicks specified table line

        :param position: Table line number which user wants to click
        :return: True if success
        """

        # Find table on page
        table = first([row for row in self.driver.find_elements_by_xpath(".//*[@id='{label}:tb']".format(label=self.attr.html_tab_label))])
        # Find table line by number and click it
        [a for a in table.find_elements_by_tag_name("tr")][1:][int(position)-1].click()
        return True

    def click_table_cell(self, value=None, *args, **kwargs) -> bool:
        """ Clicks specified table cell

        :param position: Table line number which user wants to click
        :return: True if success
        """

        # Find table on page
        table = first([row for row in self.driver.find_elements_by_xpath(".//*[@id='{label}:tb']".format(label=self.attr.html_tab_label))])
        # Find table line by number and click it
        elem = first([a for a in table.find_elements_by_tag_name("td") if a.text == value])
        if not elem:
            return False
        elem.click()
        return True

    @check_elements_on_page
    def parse_calendar(self, xpath: str, date_t: str):
        """ Method provides several ways to communicate with JS calendars interface
        > "29.7.2016 13:54" Means we would set date _and_ time
        > "25.9.2055" Means we would set date only
        > " " Means we would erase date info.
        """

        months = MONTHS

        @check_for_value_error
        def parse_date(date_t):
            """ Parse date into formatted fields of date_obj
            """
            if date_t == " ":
                return
            elif len(date_t.split(' ')) > 1:
                return dt.strptime(date_t, '%d.%m.%Y %H:%M')
            else:
                return dt.strptime(date_t, '%d.%m.%Y')

        date_obj = parse_date(date_t)
        calendar_link = self.find_element(xpath)
        # Click link to open main calendar window
        calendar_link.click()
        id = first(list(re.findall(re.compile("[a-zA-Z:_]+[\d]+"), xpath)))
        # Find main window
        day_editor = self.find_element(".//*[@id='{id}']".format(id=id))
        # In case we need to clear date_time from the form
        if not date_obj:
            day_editor.find_element_by_xpath(".//*[@id='{id}Footer']/table/tbody/tr/td[2]/div".format(id=id,)).click()
            return
        # Open the main window header with date picker window
        day_editor.find_element_by_xpath(".//*[@id='{id}Header']/table/tbody/tr/td[3]/div".format(id=id)).click()
        # Obtain link to the date editor window
        date_editor = day_editor.find_element_by_xpath("..//*[@id='{id}{un}']".format(id=id, un="DateEditorLayout"))
        # Find required month in calendar
        date_editor.find_element_by_xpath(".//*[contains(@id, '{id}DateEditorLayoutM') and contains(text(), '{var}')]"
                                          .format(id=id, var=months[date_obj.month])).click()

        @check_for_timeout_except
        def pick_year():
            """ Find calendar year
            """
            # Find all required buttons for year navigation
            less = date_editor.find_element_by_xpath(".//*[text()='{text}']".format(text="<"))
            more = date_editor.find_element_by_xpath(".//*[text()='{text}']".format(text=">"))

            def search_year():
                """ Search required year on the tab
                """
                date_editor.find_element_by_xpath(".//*[contains(@id, 'DateEditorLayoutY') and text()={year}]"
                                                   .format(year=date_obj.year)).click()

            el = int(date_editor.find_element_by_xpath(".//*[contains(@id, 'DateEditorLayoutY4')]").text)
            mini, maxi = el-4, el+5
            if mini <= date_obj.year <= maxi or date_obj.year == maxi: search_year()
            else:
                dif = (date_obj.year - maxi)/10
                if dif >= 0:
                    for i in range(int(ceil(fabs(dif)))): more.click()
                else:
                    for i in range(int(floor(fabs(dif)))): less.click()
                search_year()

        pick_year()

        # Click "OK" after year is picked
        date_editor.find_element_by_xpath(".//*[contains(@id, '{id}{un}')]".format(id=id, un="DateEditorButtonOk")).click()

        @check_for_timeout_except
        def pick_date():
            """ Find required day on calendar
            """
            dates = day_editor.find_elements_by_xpath(".//*[contains(@id, 'DayCell') and text()='{var}']"
                                                      .format(var=date_obj.day))
            if date_obj.day > 15 and len(dates) > 1: dates[1].click()
            else: dates[0].click()

        pick_date()

        # Indicate time if required
        if date_obj.hour and date_obj.minute:

            def pick_time(limiter, value):
                """ Clear current and set given time
                """
                time = time_editor.find_element_by_xpath(".//*[@id='{id}Time{lim}']".format(id=id, lim=limiter))
                time.clear()
                time.send_keys(value)

            # Click the clock link to open clock editor
            calendar_link.click()
            day_editor.find_element_by_xpath(".//*[@id='{id}Footer']/table/tbody/tr/td[3]/div".format(id=id)).click()
            time_editor = day_editor.find_element_by_xpath("..//*[@id='{id}{un}']".format(id=id, un="TimeEditorLayout"))
            pick_time('Hours', date_obj.hour)
            pick_time('Minutes', date_obj.minute)
            # Click "OK" button
            time_editor.find_element_by_xpath(".//*[@id='{id}TimeEditorButtonOk']".format(id=id)).click()

    @check_for_text_value
    def check_text(self, xpath: str, text: str):
        """ Received text and compares it with a text field containing the name of the form
        :parameter xpath: xpath element
        :parameter text: name field
        :return: True if name field coincides with name on the form

        Doctest:

        >>> browser = Driver(driver='IE')
        >>> browser.go_to("http://sbt-oafs-578:7001/SVFE2/")
        >>> browser.click(".//*[@id='LoginForm:Login']")
        >>> browser.send_key(".//*[@id='LoginForm:Login']", 'admin')
        >>> browser.click(".//*[@id='LoginForm:Password']")
        >>> browser.delete_value(".//*[@id='LoginForm:Password']")
        >>> browser.send_key(".//*[@id='LoginForm:Password']", 'admin')
        >>> browser.click(".//*[@id='LoginForm:submit']")
        >>> browser.check_page("http://sbt-oafs-578:7001/SVFE2/pages/blank.jsf")
        >>> browser.go_to("http://sbt-oafs-578:7001/SVFE2/pages/acquirer/terminalaccount/terminalAccount.jsf")
        >>> browser.check_page("http://sbt-oafs-578:7001/SVFE2/pages/acquirer/terminalaccount/terminalAccount.jsf")
        >>> browser.check_text(".//*[@id='UserForm:j_id534']", "Сбросить")
        True
        """

        elem = self.find_element(xpath)
        name_form = elem.text
        return True if name_form == text else False

    @check_for_text_value
    def check_text_button(self, xpath: str, text: str):
        """
        Doctest:

        >>> browser = Driver(driver='IE')
        >>> browser.go_to("http://sbt-oafs-578:7001/SVFE2/")
        >>> browser.click(".//*[@id='LoginForm:Login']")
        >>> browser.send_key(".//*[@id='LoginForm:Login']", 'admin')
        >>> browser.click(".//*[@id='LoginForm:Password']")
        >>> browser.delete_value(".//*[@id='LoginForm:Password']")
        >>> browser.send_key(".//*[@id='LoginForm:Password']", 'admin')
        >>> browser.click(".//*[@id='LoginForm:submit']")
        >>> browser.check_page("http://sbt-oafs-578:7001/SVFE2/pages/blank.jsf")
        >>> browser.go_to("http://sbt-oafs-578:7001/SVFE2/pages/report/reportJobList.jsf")
        >>> browser.check_page("http://sbt-oafs-578:7001/SVFE2/pages/report/reportJobList.jsf")
        >>> browser.check_text_button(".//*[@id='filterForm:j_id524']", 'Найти')
        True
        """
        but_text = self.find_element(xpath).get_attribute("value")
        return True if but_text == text else False

    @check_for_text_value
    def check_text_link(self, xpath: str, text: str):
        """
        Doctest:

        >>> browser = Driver(driver='IE')
        >>> browser.go_to("http://sbt-oafs-578:7001/SVFE2/")
        >>> browser.click(".//*[@id='LoginForm:Login']")
        >>> browser.send_key(".//*[@id='LoginForm:Login']", 'admin')
        >>> browser.click(".//*[@id='LoginForm:Password']")
        >>> browser.delete_value(".//*[@id='LoginForm:Password']")
        >>> browser.send_key(".//*[@id='LoginForm:Password']", 'admin')
        >>> browser.click(".//*[@id='LoginForm:submit']")
        >>> browser.check_page("http://sbt-oafs-578:7001/SVFE2/pages/blank.jsf")
        >>> browser.go_to("http://sbt-oafs-578:7001/SVFE2/pages/posting/jobList.jsf")
        >>> browser.check_page("http://sbt-oafs-578:7001/SVFE2/pages/posting/jobList.jsf")
        >>> browser.check_text(".//*[@id='filterForm:j_id537']", "Сбросить")
        True
        """
        link_text = self.find_element(xpath).text
        return True if link_text == text else False

    @check_for_text_value
    def check_text_dropdown(self, xpath: str, text: str):
        """
        :parameter xpath: xpath element
        :parameter text:
        :return: True if name field coincides with name on the form

        Doctest:

        >>> browser = Driver(driver='IE')
        >>> browser.go_to("http://sbt-oafs-578:7001/SVFE2/")
        >>> browser.click(".//*[@id='LoginForm:Login']")
        >>> browser.send_key(".//*[@id='LoginForm:Login']", 'admin')
        >>> browser.click(".//*[@id='LoginForm:Password']")
        >>> browser.delete_value(".//*[@id='LoginForm:Password']")
        >>> browser.send_key(".//*[@id='LoginForm:Password']", 'admin')
        >>> browser.click(".//*[@id='LoginForm:submit']")
        >>> browser.check_page("http://sbt-oafs-578:7001/SVFE2/pages/blank.jsf")
        >>> browser.go_to("http://sbt-oafs-578:7001/SVFE2/pages/acquirer/terminalaccount/terminalAccount.jsf")
        >>> browser.check_page("http://sbt-oafs-578:7001/SVFE2/pages/acquirer/terminalaccount/terminalAccount.jsf")
        >>> browser.check_text_dropdown(".//*[@id='UserForm:feNodeFilter']/tbody/tr/td[2]/select", 'ATM POS SWITCH')
        True
        """
        text_drop = self.find_element(xpath).text
        return True if text_drop == text else False

    @check_for_text_value
    def check_text_field(self, xpath: str, text: str):
        """
        :parameter xpath: xpath element
        :parameter text:
        :return: True if name field coincides with name on the form

        Doctest:

        >>> browser = Driver(driver='IE')
        >>> browser.go_to("http://sbt-oafs-578:7001/SVFE2/")
        >>> browser.click(".//*[@id='LoginForm:Login']")
        >>> browser.send_key(".//*[@id='LoginForm:Login']", 'admin')
        >>> browser.click(".//*[@id='LoginForm:Password']")
        >>> browser.delete_value(".//*[@id='LoginForm:Password']")
        >>> browser.send_key(".//*[@id='LoginForm:Password']", 'admin')
        >>> browser.click(".//*[@id='LoginForm:submit']")
        >>> browser.check_page("http://sbt-oafs-578:7001/SVFE2/pages/blank.jsf")
        >>> browser.go_to("http://sbt-oafs-578:7001/SVFE2/pages/acquirer/terminalaccount/terminalAccount.jsf")
        >>> browser.check_page("http://sbt-oafs-578:7001/SVFE2/pages/acquirer/terminalaccount/terminalAccount.jsf")
        >>> input_value = '12e34w567.89'
        >>> browser.send_key(".//*[@id='UserForm:merchantInput']", input_value)
        >>> fil = browser.find_element(".//*[@id='UserForm:merchantInput']").get_attribute("value")
        >>> browser.check_text_field(".//*[@id='UserForm:merchantInput']", '12e34w567.89')
        True
        """
        field_text = self.find_element(xpath).get_attribute("value")
        return True if field_text == text else False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
