# coding = utf-8

from framework.basefunc import BasePage
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Func(BasePage):
    # clear columns status default filter
    def clear_Status(self):
        target = self.driver.find_element_by_xpath("//app-filter-box[@id='filterLOGIC_STATUS']/mat-icon")
        self.driver.execute_script("arguments[0].click();", target)
        time.sleep(2)
        self.driver.find_element_by_id("mat-checkbox-1").click()
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]").click()
        time.sleep(2)
    # visible columns select
    def visiblecols(self, visiblecols):
        self.driver.find_element_by_xpath("//*[@id='selectmenu']").click()
        for id in visiblecols:
            path = "//*[@id=\'" + id + "\']/div/mat-pseudo-checkbox"
            # print(path)
            target = self.driver.find_element_by_id(id)
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            self.driver.find_element_by_xpath(path).click()
            time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]").click()
        time.sleep(5)
    # mouse hover to get text
    def hover_text(self, xpath):
        mouse = self.driver.find_element_by_xpath(xpath)
        ActionChains(self.driver).move_to_element(mouse).perform()
        hover_text = self.driver.find_element_by_xpath("/html/body/div[2]").text
        return hover_text
class testfilter(BasePage): # columns filter function
    #click select all checkbox
    def test_selectAll(self, element):
        target = element.find_element_by_tag_name("mat-icon")
        self.driver.execute_script("arguments[0].click();", target)
        select_all = self.driver.find_element_by_xpath("//*[@id='filcheck']/section[1]/mat-checkbox")
        if select_all.find_element_by_tag_name("input").get_attribute('aria-checked') == 'false':
            select_all.click()
        time.sleep(2)
        mat_list = self.driver.find_elements_by_xpath("//*[@id='filcheck']/div/div/mat-list-option")
        mat_text = []
        for mat in mat_list:
            mat_text.append(mat.find_elements_by_tag_name('div')[2].text)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]").click()
        return mat_text
    #clear all select
    def test_selectclear(self, element):
        mat_list = []
        target = element.find_element_by_tag_name("mat-icon")
        self.driver.execute_script("arguments[0].click();", target)
        select_all = self.driver.find_element_by_xpath("//*[@id='filcheck']/section[1]/mat-checkbox")
        if select_all.find_element_by_tag_name("input").get_attribute('aria-checked') == 'true':
            select_all.click()
        time.sleep(2)
        for mat in self.driver.find_elements_by_xpath("//*[@id='filcheck']/div/div/mat-list-option"):
            if mat.get_attribute('aria-selected') == 'true':
                mat_list.append(mat)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]").click()
        return mat_list
    # select one data
    def test_selectone(self, element):
        target = element.find_element_by_tag_name("mat-icon")
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
        # self.driver.find_element_by_xpath("//*[@id='filterSearch']").send_keys(Keys.CONTROL)
        mat_list = self.driver.find_elements_by_xpath("//*[@id='filcheck']/div/div/mat-list-option")
        visual_list = []
        search_list = []
        hide_list = []
        no_search_list = []
        for mat_option in mat_list:
            # search with data
            if mat_option.value_of_css_property('display') == 'block':
                search_list.append(mat_option.find_element_by_css_selector(".mat-list-text").text)
                visual_list.append(mat_option)
            else:
            #do not contains keywords
                text = mat_option.find_element_by_css_selector(".mat-list-text").get_attribute('innerText')
                no_search_list.append(text)
                hide_list.append(mat_option)
        mat_dict = {"search_list": search_list, "visual_list": visual_list, "no_search_list": no_search_list, "hide_list": hide_list}
        return mat_dict



