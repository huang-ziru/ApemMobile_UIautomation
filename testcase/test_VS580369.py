# coding = utf-8
import configparser
import time, pytest
from framework.basefunc import MainPage
from selenium.webdriver.common.keys import Keys

def test_fullscreen(browser):
    try:
        MainPage(browser).is_login_successed()
    except:
        print('Fail:', browser.current_url)
    else:
        browser.find_element_by_css_selector("mat-icon[svgicon='fullscreen']").click()
        time.sleep(5)
        #get the windows size
        size = browser.get_window_size()
        # get the resolution of the machine that set in the config.ini
        config = configparser.ConfigParser()
        path = r'../framework/config.ini'
        config.read(path)
        width = config.getint('Screen_size', 'width')
        height = config.getint('Screen_size', 'height')
        #assert the size
        assert size["width"] == width
        assert size["height"] == height
if __name__ == '__main__':
    pytest.main(["-s", "test_VS580369.py"])