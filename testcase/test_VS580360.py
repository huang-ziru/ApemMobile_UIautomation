# coding = utf-8
from selenium import webdriver
import time, pytest
from framework.basefunc import MainPage
import configparser
config = configparser.ConfigParser()
path = r'E:\PycharmProjects\ApemMobile\framework\config.ini'
config.read(path)
workstation = config.get('login', 'workstation')
username = config.get('login', 'username')
user_info = username + "\n(" + workstation + ")"
def test_loginuser(browser):
    browser.find_element_by_xpath("/html/body/app-root/app-header/mat-toolbar/div/div[5]/mat-icon").click()
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\loginuser.png")
    time.sleep(5)
    assert user_info == browser.find_element_by_xpath('//*[@id="logoutpanel"]/button[1]/span').text
def test_logout(browser):
    MainPage(browser).logout()
    time.sleep(3)
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\logout.png")
    assert 'logged out successfully' in browser.find_element_by_xpath("/html/body/app-root/div/app-logout/div/div/h1").text

if __name__ == '__main__':
    pytest.main(["-s", "test_VS580360.py"])
    pytest.main(["--lf", "test_VS580360.py"])
