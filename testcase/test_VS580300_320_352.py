import configparser
from logging import Logger

from selenium import webdriver
import time, pytest, os
def login(name, password1, caseID):
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
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(name)
    driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys(password1)
    driver.find_element_by_id('signInBtn').click()
    time.sleep(10)
    now_url = driver.current_url
    driver.get_screenshot_as_file(r"..\\report\\result_picture\\" + caseID + ".png")
    # print('nowurl:', now_url)
    if now_url != url:
        text1 = driver.current_url
    elif now_url == url:
        text1 = driver.find_element_by_xpath('/html/body/app-root/div/app-login/div/div[1]/form/div').text
    else:
        return 'warning！'
    driver.quit()
    return text1

# login with legal username and password
def test_loginok():
    assert "process-order" in login('corp\\qapart', 'QQQaaa000','580300')

#login with username and password without domain name
def test_nodomain():
    assert "WinNTUserNoDomain" in login('hahahha', 'hdhdhhdhd', 'nodomain')
#login with invalid username and password
def test_Invalid():
    assert "Invalid username or password. Please re-enter domain\\username and password." in login('jhh\\hahahha', 'hdhdhhdhd','580320')
#login with username and password without access
def test_Denied():
    assert "You do not have permission to login." in login('corp\\huangzi', 'Hzrlove1213','580352')

def test_login_ui():
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
    sign_in = driver.find_element_by_id('signInBtn')
    driver.get_screenshot_as_file(r"..\\report\\result_picture\\noinput.png")
    time.sleep(2)
    #"Sign in" button is grey out befor input username and password
    assert sign_in.get_attribute('disabled') == 'true'
    assert sign_in.value_of_css_property('background-color') == 'rgba(0, 0, 0, 0.12)'
    #"Eye" icon is shown at the rightmost when typing the password, and user can see the typed when hold it
    driver.find_element_by_xpath('//*[@id="username"]').send_keys('hshhsh')
    driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys('hhhhhhhhyywywy')
    driver.find_element_by_xpath("/html/body/app-root/div/app-login/div/div[1]/form/mat-form-field[2]/div/div[1]/div[4]/mat-icon").click()

    assert driver.find_element_by_xpath('//*[@id="mat-input-1"]').get_attribute("type") == 'text'
    assert sign_in.value_of_css_property('background-color') == 'rgba(38, 152, 251, 1)'
    driver.get_screenshot_as_file(r"..\\report\\result_picture\\input.png")
    driver.quit()

if __name__ == '__main__':
    pytest.main(["-s", "test_VS580300_320_352.py"])