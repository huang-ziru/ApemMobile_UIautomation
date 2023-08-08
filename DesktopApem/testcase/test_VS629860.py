# coding = utf-8
from framework.constant import get_caseID
import time
from framework.common import Common
import pytest
from framework.Login import login
from selenium.webdriver.common.by import By
def test_change_excute():
    browser = login()
    time.sleep(4)
    order_ele = browser.find_element(By.XPATH, "//div[contains(text(),'X_ORDER')]/../..")
    order_ele.find_elements(By.TAG_NAME, "td")[-1].click()
    time.sleep(2)
    phase_list = browser.find_elements(By.XPATH, "//div/a")
    phase_name = phase_list[1].find_element(By.XPATH, "./../../../../../td[2]/div/div").get_attribute('textContent')
    Common(browser).eleclick(phase_list[1].find_element(By.TAG_NAME, "mat-icon"))
    time.sleep(5)
    change_ele = browser.find_element(By.XPATH, "//*[@id='MAIN.Table10_2']")
    Common(browser).eleclick(change_ele)
    time.sleep(2)
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\"+get_caseID()+"test_changing.png")
    browser.find_element(By.XPATH, "//div[@role='listbox']/mat-option[1]").click()
    time.sleep(1)
    browser.find_element(By.ID, "order").click()
    time.sleep(4)
    browser.close()
    new_driver = login()
    time.sleep(2)
    order_ele = new_driver.find_element(By.XPATH, "//div[contains(text(),'X_ORDER')]/../..")
    order_ele.find_elements(By.TAG_NAME, "td")[-1].click()
    time.sleep(2)
    phase_list = new_driver.find_elements(By.XPATH, "//div/a")
    phase_path = "//div[@class='phase-name-text' and text()=\'" + phase_name + "\']/../../.."
    phase_ele = new_driver.find_element(By.XPATH, phase_path).find_element(By.CSS_SELECTOR, value="td[class ~= 'cdk-column-STATUS']")
    phase_state = phase_ele.get_attribute('textContent')
    Common(new_driver).eleclick(phase_list[1].find_element(By.TAG_NAME, "mat-icon"))
    time.sleep(5)
    new_driver.get_screenshot_as_file(r"..\\report\\result_picture\\"+get_caseID()+"test_changAfter.png")
    # the phase state is "Executing".
    assert 'Executing' == phase_state
    new_driver.close()
if __name__ == '__main__':
    pytest.main(["-s", "test_VS629860.py"])