# coding = utf-8
import configparser
import time
from logging import Logger

from selenium import webdriver
from framework.basefunc import BasePage
'''Data processing '''
class prepare(BasePage):
    #process columns data before the testcase about columns
    def login_after(self):
        # cancle the default status filter
        target = self.driver.find_element_by_xpath("//app-filter-box[@id='filterLOGIC_STATUS']/mat-icon")
        self.driver.execute_script("arguments[0].click();", target)
        time.sleep(2)
        self.driver.find_element_by_id("mat-checkbox-1").click()
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]").click()
        time.sleep(2)
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
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]").click()
        time.sleep(5)

