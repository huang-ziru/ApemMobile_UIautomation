# coding = utf-8
import configparser
import time
from logging import Logger

import pytest
from selenium import webdriver
from selenium.webdriver.support.color import Color

from framework.basefunc import MainPage
class Testtitle_bar():
    def test_DarkMode(self, browser):
        browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='settings']").click()
        switch = browser.find_element_by_xpath("//div[@class='show-navigation'][4]/div/div[2]/mat-slide-toggle")
        if switch.find_element_by_tag_name('input').get_attribute('aria-checked') == 'false':
            MainPage(browser).eleclick(switch)
        time.sleep(5)
        backcolor = browser.find_element_by_xpath("//body").value_of_css_property('background-color')
        assert Color.from_string(backcolor) == Color.from_string('#2a2a2a')
        textcolor = browser.find_element_by_xpath("//body").value_of_css_property('color')
        assert Color.from_string(textcolor) == Color.from_string('#fff')
        browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='settings']").click()
        switch = browser.find_element_by_xpath("//div[@class='show-navigation'][4]/div/div[2]/mat-slide-toggle")
        if switch.find_element_by_tag_name('input').get_attribute('aria-checked') == 'true':
            MainPage(browser).eleclick(switch)
        time.sleep(5)

    def test_diffuser(self):
        config = configparser.ConfigParser()
        path = r'..\framework\config.ini'
        config.read(path)
        browser_name = config.get('Browser', 'browser')
        if browser_name == 'Chrome':
            self.driver = webdriver.Chrome(r'..\framework\chromedriver.exe')
            self.driver.maximize_window()
        elif browser_name == 'Edge':
            self.driver = webdriver.Edge(r'..\framework\msedgedriver.exe')
            self.driver.maximize_window()
        else:
            Logger.error('Do not support the Browser')
        servername = config.get('login', 'servername')
        url = "http://qaone:Aspen111@" + servername + "/ApemMobile/#/login"
        self.driver.get(url)
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys("corp\\qaone")
        self.driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys("Aspen111")
        self.driver.find_element_by_id('signInBtn').click()
        backcolor = self.driver.find_element_by_xpath("//body").value_of_css_property('background-color')
        try:
            assert Color.from_string(backcolor) != Color.from_string('#2a2a2a')
            assert "theme-light" in self.driver.find_element_by_xpath("//body").get_attribute("class")
        finally:
            self.driver.quit()
    def test_offDarkMode(self, browser):
        browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='settings']").click()
        switch = browser.find_element_by_xpath("//div[@class='show-navigation'][4]/div/div[2]/mat-slide-toggle")
        if switch.find_element_by_tag_name('input').get_attribute('aria-checked') == 'true':
            MainPage(browser).eleclick(switch)
        time.sleep(5)
        assert "theme-light" in browser.find_element_by_xpath("//body").get_attribute("class")




if __name__ == '__main__':
    pytest.main(["-s", "test_VS591819.py"])

