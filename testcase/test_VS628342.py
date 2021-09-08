# coding = utf-8
import configparser
import time
from framework.basefunc import MainPage
import pytest
def dialog_text(browser,state):
    config = configparser.ConfigParser()
    path = r'..\framework\config.ini'
    # open the config.ini and get the data
    config.read(path)
    password = config.get('login', 'password')
    browser.find_element_by_xpath("//textarea").send_keys('ghsgdgdh')
    browser.find_element_by_xpath("//*[@id='dialog']/div/div[1]/form/mat-form-field[3]/div/div[1]/div[1]/input").send_keys(password)
    button = "//span[contains(text(),\'"+state+"\')]/.."
    browser.find_element_by_xpath(button).click()
    time.sleep(10)
    return browser.current_url
def test_Toolbar(browser):
    time.sleep(4)
    order_ele = browser.find_element_by_xpath("//div[contains(text(),'START')]/../..")
    order_ele.find_elements_by_tag_name("td")[-1].click()
    time.sleep(5)
    phase_ele = browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='phase_state_executing']")
    phase_name = phase_ele.find_element_by_xpath("./../../../../../td[2]/div[1]/div").text
    MainPage(browser).eleclick(phase_ele)
    time.sleep(5)
    # Check the initial position is in the top center
    toolbar = browser.find_element_by_xpath("//*[@id='toolbar']/div")
    rect = toolbar.rect
    win_size = browser.get_window_size()
    toolbar_w = rect['x']+rect['width']/2
    assert abs(win_size['width']/2 - toolbar_w) <= 20
    # collapse the toolbar
    browser.find_element_by_xpath("//*[@id='toolbar']/div/button[3]").click()
    time.sleep(2)
    assert browser.find_element_by_xpath("//*[@id='toolbar']/div/button[1]").value_of_css_property('display') == 'none'
    assert browser.find_element_by_xpath("//*[@id='toolbar']/div/button[2]").value_of_css_property('display') == 'none'
    time.sleep(2)
    # expand the toolbar
    browser.find_element_by_xpath("//*[@id='toolbar']/div/button[3]").click()
    time.sleep(2)
    assert browser.find_element_by_xpath("//*[@id='toolbar']/div/button[1]").value_of_css_property('display') == 'block'
    assert browser.find_element_by_xpath("//*[@id='toolbar']/div/button[2]").value_of_css_property('display') == 'block'
    # Check the comments icon can work as expected
    browser.find_element_by_xpath("//*[@id='toolbar']/div/button[2]").click()
    time.sleep(1)
    assert MainPage(browser).is_element_showed("div#dialog") is True
    assert 'execution' in dialog_text(browser, ' Cancel ')
    browser.find_element_by_xpath("//*[@id='toolbar']/div/button[2]").click()
    time.sleep(1)
    assert 'execution' in dialog_text(browser, ' OK ')
    # Check the "Interrupt" icon can work as expected
    browser.find_element_by_xpath("//*[@id='toolbar']/div/button[1]").click()
    time.sleep(2)
    # a confirmation dialog will pops up
    assert MainPage(browser).is_element_showed("div#dialog") is True
    assert 'execution' in dialog_text(browser, ' Cancel ')
    # Can go back to tracking page, the phase state is interrupt.
    browser.find_element_by_xpath("//*[@id='toolbar']/div/button[1]").click()
    time.sleep(2)
    assert "tracking" in dialog_text(browser, ' OK ')
    phase_path = "//div[@class='phase-name-text' and text()=\'"+phase_name+"\']/../../../td[3]"
    phase_ele = browser.find_element_by_xpath(phase_path)
    phase_state = phase_ele.get_attribute('textContent')
    assert 'Interrupted' == phase_state

if __name__ == '__main__':
    pytest.main(["-s", "test_VS628342.py"])