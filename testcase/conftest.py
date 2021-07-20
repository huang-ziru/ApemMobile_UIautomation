import os, sys
from logging import Logger
import configparser
import time
from selenium import webdriver
import pytest
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
@pytest.fixture()
def browser():
    '''Define global driver parameters'''
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
    password = config.get('login', 'password')
    login_alter = username[5::] + ":" + password + "@"
    url = "http://" + login_alter + servername + "/ApemMobile/#/login"
    driver.get(url)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys(password)
    driver.find_element_by_id('signInBtn').click()
    time.sleep(5)
    yield driver
    time.sleep(5)
    driver.quit()
    return driver


