# coding = utf-8
import time, pytest
def test_bing(browser):

    time.sleep(2)
    order_ele = browser.find_element_by_xpath("//div[contains(text(),'FOR_BING')]/../..")
    order_ele.find_elements_by_tag_name("td")[-1].click()
    time.sleep(2)
    browser.find_element_by_xpath("//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/tbody/tr/td[12]/div/div/a/mat-icon").click()
    time.sleep(3)
    browser.get_screenshot_as_file(r"..\\report\\result_picture\\GO_bing.png")
    assert 'https://www.bing.com/' == browser.find_element_by_xpath("//*[@id='screen']/app-aebrs-web-content/div/iframe").get_attribute("src")

if __name__ == '__main__':
    pytest.main(["-s", "test_VS626781.py"])






