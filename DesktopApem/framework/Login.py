# coding = utf-8
import configparser
import time
import re
from logging import Logger
from selenium import webdriver
from framework.basefunc import BasePage
'''Data processing '''
class prepare(BasePage):
    #process columns data before the testcase about columns
    def login_after(self):
        # cancle the default status filter
        target = self.driver.find_element_by_xpath("//app-filter-box[@id='filterLOGIC_STATUS']/mat-icon")
        self.driver.execute_script("arguments[0].click();", target)
        time.sleep(2)
        self.driver.find_element_by_id("mat-checkbox-1").click()
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]").click()
        time.sleep(2)
        # show all columns
        box = ['checkProcess Area', 'checkRep.', 'checkArticle', 'checkPO ', 'checkPO Step', 'checkEnd Date',
               'checkProcess Type', 'checkOrigin', 'checkUser Status', 'checkBatch Area', 'checkCR Modified',
               'checkRUDO (edit planned)', 'checkRUDO (edit active)', 'checkVer.', 'checkFrom', 'checkSite']
        assert 'Order / Batch Code' not in box
        self.driver.find_element_by_xpath("//*[@id='selectmenu']").click()
        for id in box:
            path = "//*[@id=\'" + id + "\']/div/mat-pseudo-checkbox"
            # print(path)
            target = self.driver.find_element_by_id(id)
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            self.driver.find_element_by_xpath(path).click()
            time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]").click()
        time.sleep(5)
def login():
    global driver
    config = configparser.ConfigParser()
    path = r'..\framework\config.ini'
    # open the config.ini and get the data
    config.read(path)
    browser_name = config.get('Browser', 'browser')
    if browser_name == 'Chrome':
            driver = webdriver.Chrome(r'..\framework\chromedriver.exe')
            driver.maximize_window()
    elif browser_name == 'Edge':
        driver = webdriver.Edge(r'..\framework\msedgedriver.exe')
        driver.maximize_window()
    else:
        Logger.error('Do not support the Browser')
    servername = config.get('login', 'servername')
    username = config.get('login', 'username')
    loginname =re.split(r'\\', username)[1]
    password = config.get('login', 'password')
    login_alter = loginname + ":" + password + "@"
    url = "http://" + login_alter + servername + "/ApemMobile/#/login"
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys(password)
    time.sleep(6)
    driver.find_element_by_id('signInBtn').click()
    time.sleep(10)
    return driver

