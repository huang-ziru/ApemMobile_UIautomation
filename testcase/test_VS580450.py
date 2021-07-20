import time
import pytest
from framework.basefunc import MainPage
def test_navigate(browser):

    assert 'Process Order' in MainPage(browser).navigate("//mat-icon[@data-mat-icon-name='process_order']")
    assert 'Tracking' == MainPage(browser).navigate("//mat-icon[@data-mat-icon-name='process_order']/../following-sibling::a[1]/mat-icon")
    assert 'Settings' == MainPage(browser).navigate("//mat-icon[@data-mat-icon-name='process_order']/../following-sibling::a[2]/mat-icon")

if __name__ == '__main__':
    pytest.main(["-s", "test_VS580450.py"])

