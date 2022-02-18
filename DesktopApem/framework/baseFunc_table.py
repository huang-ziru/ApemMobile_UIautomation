# coding = utf-8
from framework.basefunc import BasePage
import time
from selenium.webdriver.common.keys import Keys
class func_for_table(BasePage): # columns filter function
    #click select all checkbox
    def test_selectAll(self, element):
        target = element.find_element_by_tag_name("mat-icon")
        self.driver.execute_script("arguments[0].click();", target)
        select_all = self.driver.find_element_by_xpath("//*[@id='filcheck']/section[1]/mat-checkbox//input")
        if select_all.get_attribute('aria-checked') == 'false':
            self.driver.execute_script("arguments[0].click();", select_all)
        time.sleep(2)
        mat_list = self.driver.find_elements_by_xpath("//*[@id='filcheck']/div/div/mat-list-option")
        mat_text = []
        for mat in mat_list:
            mat_text.append(mat.find_element_by_xpath("div/div[2]").get_attribute('textContent').strip())
        time.sleep(2)
        back = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]")
        self.driver.execute_script("arguments[0].click();", back)
        return mat_text

    #clear all select
    def test_selectclear(self, element):
        mat_list = []
        target = element.find_element_by_tag_name("mat-icon")
        self.driver.execute_script("arguments[0].click();", target)
        select_all = self.driver.find_element_by_xpath("//*[@id='filcheck']/section[1]/mat-checkbox//input")
        if select_all.get_attribute('aria-checked') == 'true':
            self.driver.execute_script("arguments[0].click();", select_all)
        time.sleep(2)
        for mat in self.driver.find_elements_by_xpath("//*[@id='filcheck']/div/div/mat-list-option"):
            if mat.get_attribute('aria-selected') == 'true':
                mat_list.append(mat)
        return mat_list

    # select one data
    def test_selectone(self, element):
        target = element.find_element_by_tag_name("mat-icon")
        # MainPage(self.driver).size()
        self.driver.execute_script("arguments[0].click();", target)
        select_list = self.driver.find_elements_by_xpath("//div[@class='ng-star-inserted']/mat-list-option")
        select_all = self.driver.find_element_by_xpath("//*[@id='filcheck']/section[1]/mat-checkbox")
        if select_all.find_element_by_tag_name("input").get_attribute('aria-checked') == 'true':
            select_all.click()
        time.sleep(2)
        return select_list
    #the search in columns filter
    def test_filtersearch(self, element, keywords):
        target = element.find_element_by_tag_name("mat-icon")
        self.driver.execute_script("arguments[0].click();", target)
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='filterSearch']").click()
        self.driver.find_element_by_xpath("//*[@id='filterSearch']").send_keys(keywords)
        #defect
        self.driver.find_element_by_xpath("//*[@id='filterSearch']").send_keys(Keys.CONTROL)
        mat_list = self.driver.find_elements_by_xpath("//*[@id='filcheck']/div/div/mat-list-option")
        visual_list = []
        search_list = []
        hide_list = []
        no_search_list = []
        for mat_option in mat_list:
            # search with data
            if mat_option.value_of_css_property('display') == 'block':
                search_list.append(mat_option.find_element_by_css_selector(".mat-list-text").get_attribute('textContent').strip())
                visual_list.append(mat_option)
            else:
            #do not contains keywords
                text = mat_option.find_element_by_css_selector(".mat-list-text").get_attribute('innerText').strip()
                no_search_list.append(text)
                hide_list.append(mat_option)
        mat_dict = {"search_list": search_list, "visual_list": visual_list, "no_search_list": no_search_list, "hide_list": hide_list}
        return mat_dict
    # clear the input data in number filters
    def clear_input(self, ele, inputpath1, inputpath2):
        target = ele.find_element_by_tag_name("mat-icon")
        self.driver.execute_script("arguments[0].click();", target)
        self.driver.find_element_by_xpath(inputpath1)
        target1 = self.driver.find_element_by_xpath(inputpath1)
        self.driver.execute_script("arguments[0].click();", target1)
        # Press<Ctrl+a>,then press <Delete>
        self.driver.find_element_by_xpath(inputpath1).send_keys(Keys.CONTROL, "a")
        time.sleep(1)
        self.driver.find_element_by_xpath(inputpath1).send_keys(Keys.DELETE)
        time.sleep(1)
        target2 = self.driver.find_element_by_xpath(inputpath2)
        self.driver.execute_script("arguments[0].click();", target2)
        self.driver.find_element_by_xpath(inputpath2).send_keys(Keys.CONTROL, "a")
        time.sleep(1)
        self.driver.find_element_by_xpath(inputpath2).send_keys(Keys.DELETE)
        time.sleep(1)
        target = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]")
        self.driver.execute_script("arguments[0].click();", target)