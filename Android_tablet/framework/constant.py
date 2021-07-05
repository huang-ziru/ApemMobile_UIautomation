# coding = utf-8
import configparser
import time
from logging import Logger

from framework.columsfunc import Func
from framework.basefunc import BasePage
'''Data processing '''
class prepare(BasePage):
    #process columns data before the testcase about columns
    def login_after(self):
        # cancle the default status filter
        Func(self.driver).clear_Status()
        # show all columns
        box = ['checkProcess Area', 'checkRep.', 'checkArticle', 'checkPO ', 'checkPO Step', 'checkEnd Date',
               'checkProcess Type', 'checkOrigin', 'checkUser Status', 'checkBatch Area', 'checkCR Modified',
               'checkRUDO (edit planned)', 'checkRUDO (edit active)', 'checkVer.', 'checkFrom', 'checkSite']
        assert 'Order / Batch Code' not in box
        self.driver.find_element_by_xpath("//*[@id='selectmenu']").click()
        for id in box:
            path = "//*[@id=\'" + id + "\']/div/mat-pseudo-checkbox"
            # print(path)
            target = self.driver.find_element_by_id(id)
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(1)
            self.driver.find_element_by_xpath(path).click()
            time.sleep(1)
        back = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]")
        self.driver.execute_script("arguments[0].click();", back)
        time.sleep(5)

