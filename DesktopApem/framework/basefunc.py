# coding = utf-8
import datetime
import re
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    #assert if login successfully
    def is_login_successed(self):
        if "process-order" in self.driver.current_url:
            return True
        else:
            print("login failed!The url is '%s'"%self.driver.current_url)
            return False
        # the existence of an element is judged by its length
    def is_element_showed(self, css):
        lenth = self.driver.find_elements_by_css_selector(css_selector=css)
        if len(lenth) == 0:
            return False
        else:
            return True
    #logout click
    def logout(self):
        self.driver.find_element_by_xpath("/html/body/app-root/app-header/mat-toolbar/div/div[5]/mat-icon").click()
        time.sleep(5)
        logout_button = self.driver.find_element_by_xpath('//*[@id="logoutpanel"]/button[2]')
        logout_button.click()