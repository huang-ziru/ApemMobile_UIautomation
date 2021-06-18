# coding = utf-8
import time, pytest
from framework.basefunc import MainPage


def test_layout(browser):
    try:
        MainPage(browser).is_login_successed()
    except:
        print('Fail:', browser.current_url)
    else:
        browser.find_element_by_css_selector("mat-icon[data-mat-icon-name='desktop_switch']").click()
        time.sleep(5)
        browser.find_element_by_xpath("//button[@role='menuitem'][1]").click()
        time.sleep(3)
        try:
            assert "tablet_switch" == browser.find_element_by_xpath("//div[@class='icon'][2]/mat-icon").get_attribute('data-mat-icon-name')
            #navgation bar is in the bottom of page
            assert MainPage(browser).is_element_showed("div.mat-tab-link-container") is True
        except:
            print('Switch failed:', browser.find_element_by_xpath("//div[@class='icon'][2]/mat-icon").get_attribute('data-mat-icon-name'))
        else:
            browser.find_element_by_css_selector("mat-icon[data-mat-icon-name='tablet_switch']").click()
            time.sleep(3)
            browser.find_element_by_xpath("//button[@role='menuitem'][2]").click()
            time.sleep(3)
            assert "desktop_switch" == browser.find_element_by_xpath("//div[@class='icon'][2]/mat-icon").get_attribute('data-mat-icon-name')

if __name__ == '__main__':
    pytest.main(["-s", "test_VS580365.py"])


