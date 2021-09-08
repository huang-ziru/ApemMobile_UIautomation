# coding = utf-8
import time, pytest
def test_bing(browser):

    time.sleep(2)
    order_ele = browser.find_element_by_xpath("//div[contains(text(),'FOR_BING')]/../..")
    order_ele.find_elements_by_tag_name("td")[-1].click()
    time.sleep(2)
    browser.find_element_by_xpath("//mat-icon[@data-mat-icon-name='phase_state_enabled']").click()
    time.sleep(3)
    assert 'https://www.bing.com/' == browser.find_element_by_xpath("//*[@id='screen']/app-aebrs-web-content/div/iframe").get_attribute("src")

if __name__ == '__main__':
    pytest.main(["-s", "test_VS626781.py"])






