import time
import pytest
from framework.basefunc import MainPage
class Testnavigate():
    def test_order(self, browser):
        assert 'Process Order' in MainPage(browser).navigate("//nav/a[1]/mat-icon")

    def test_tracking(self, browser):
        assert 'Tracking' == MainPage(browser).navigate("//mat-icon[@data-mat-icon-name='process_order']/../following-sibling::a[1]/mat-icon")

    def test_setting(self, browser):
        assert 'Settings' == MainPage(browser).navigate("//mat-icon[@data-mat-icon-name='process_order']/../following-sibling::a[2]/mat-icon")



if __name__ == '__main__':
    pytest.main(["-s", "test_VS580450.py"])

