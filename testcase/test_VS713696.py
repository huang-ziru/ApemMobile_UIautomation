# # coding = utf-8
# import random
# import time, pytest
# import re
# from framework.basefunc import MainPage
# from framework.columsfunc import Func
# def test_workflows(browser):
#     # Check the default columns show correctly: Order/Batch Code | Quantity | Unites | Date | Status | Workcenter.
#     assert "Order / Batch Code" == browser.find_element_by_xpath("//*[@id='headerOrder / Batch Code']").get_attribute('textContent')
#     assert "Quantity" == browser.find_element_by_xpath("//*[@id='headerQuantity']").get_attribute('textContent')
#     assert "Units" == browser.find_element_by_xpath("//*[@id='headerUnits']").get_attribute('textContent')
#     assert "Date" == browser.find_element_by_xpath("//*[@id='headerDate']").get_attribute('textContent')
#     assert "Status" == browser.find_element_by_xpath("//*[@id='headerStatus']").get_attribute('textContent')
#     assert "Workcenter" == browser.find_element_by_xpath("//*[@id='headerWorkcenter']").get_attribute('textContent')
#     # Check "search" function can work as expected.
#     browser.find_element_by_id("ordersearch").send_keys('order')
#     time.sleep(2)
#     browser.get_screenshot_as_file(r"..\\report\\result_picture\\search.png")
#     table_list = []
#     table_tr_list = browser.find_elements_by_xpath("//div[@class='full show-navigation']/div[2]/table/tbody/tr")
#     # match 'er' and case insensitive
#     pattern = re.compile(r'order', re.I)
#     count1 = 0
#     for tr in table_tr_list:
#         table_td_list = tr.find_elements_by_tag_name("td")[1::]
#         for td in table_td_list:
#             row_list = []
#             row_list.append(td.text)
#             table_list.append(row_list)
#             # Verify bold matches
#             strong_list = td.find_elements_by_tag_name("strong")
#             for st in strong_list:
#                 count1 = count1 + 1
#                 result1 = re.sub(pattern, '', st.text)
#                 assert len(result1) == 0
#     # Verify that there are matches in the non BOLD data
#     count2 = 0
#     for i in range(len(table_list)):
#         for j in range(len(table_list[i])):
#             it = re.finditer(pattern, table_list[i][j])
#             for ww in it:
#                 count2 = count2 + 1
#     assert count1 == count2
#     time.sleep(5)
#     # Check "Visible Column" on the top of right can work  as expected.
#     visiblecols = ['checkProcess Area', 'checkRep.', 'checkArticle', 'checkPO ', 'checkPO Step', 'checkEnd Date','checkProcess Type', 'checkOrigin', 'checkUser Status', 'checkBatch Area', 'checkCR Modified','checkRUDO (edit planned)', 'checkRUDO (edit active)', 'checkVer.', 'checkFrom', 'checkSite']
#     Func(browser).visiblecols(visiblecols)
#     for id in visiblecols:
#         headerid = "header" + id[5::]
#         # Scroll to the location where the specified element appears
#         target2 = browser.find_element_by_id(headerid)
#         browser.execute_script("arguments[0].scrollIntoView();", target2)
#         browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + id + ".png")
#         assert id[5::].rstrip() == browser.find_element_by_id(headerid).text.rstrip()
#     # Check the phase list of an order can show.
#     time.sleep(2)
#     order_ele = browser.find_element_by_xpath("//div[contains(text(),'FROM_RPL')]/../..")
#     order_ele.find_elements_by_tag_name("td")[-1].click()
#     time.sleep(2)
#     phase_list = ['PHASE55', 'PHASE58', 'PHASE61', 'PHASE64', 'PHASE67', 'PHASE70', 'PHASE73']
#     for phase in browser.find_elements_by_xpath("//div[@class='phase-name-text']"):
#         phaseName = phase.get_attribute('textContent')
#         assert phaseName in phase_list
#     # Check the default columns show correctly: No. | Phase | Status |Status icon.
#     default_head = browser.find_elements_by_xpath("//*[@id='tracking-content']/app-tracking-list/div/div[2]/table/thead/tr/th")
#     assert len(default_head) == 4
#     for i in range(len(default_head)):
#         head_name = default_head[i].find_element_by_xpath("div/div/div").get_attribute('textContent')
#         assert head_name in ("No.", "Phase", "Status", "")
#     # Check "Visible Column" on the top of right can work  as expected.
#     browser.find_element_by_css_selector("mat-icon[data-mat-icon-name='visible_column']").click()
#     all_list_option = browser.find_elements_by_xpath("//*[@id='colselectpanel']/mat-list-option")
#     hide_list_option = browser.find_elements_by_css_selector("mat-list-option[class ~= 'hide']")
#     for hide_option in hide_list_option:
#         all_list_option.remove(hide_option)
#     columns_list = []
#     for list_option in all_list_option:
#         option_text = list_option.find_element_by_css_selector("div.mat-list-text").get_attribute('textContent')
#         columns_list.append("check" + option_text.strip())
#     # Check default columns are not allowed to hide and are not in this list
#         assert option_text not in ("No.", "Phase", "Status", "")
#     # The related columns will show/hide in the order table
#     time.sleep(2)
#     back = browser.find_element_by_xpath("/html/body/div[2]/div[1]")
#     MainPage(browser).eleclick(back)
#     Func(browser).visiblecols(columns_list)
#     for id in columns_list:
#         headerid = "header" + id[5::]
#         # Scroll to the location where the specified element appears
#         target2 = browser.find_element_by_id(headerid)
#         browser.execute_script("arguments[0].scrollIntoView();", target2)
#         browser.get_screenshot_as_file(r"..\\report\\result_picture\\" + id + ".png")
#         assert id[5::] == browser.find_element_by_id(headerid).get_attribute('textContent')
#     # Click bread crumb to switch order and phase list
#     time.sleep(3)
#     browser.find_element_by_xpath("//input[@aria-label='OrderName']").click()
#     time.sleep(3)
#     select_list = browser.find_elements_by_css_selector("span.mat-option-text")
#     select_datalist = []
#     for select in select_list:
#         select_data = select.get_attribute('textContent')
#         select_datalist.append(select_data.replace(" ", ""))
#     # Click the order in the dropdown list to change the chosen order
#     num = random.choice(range(len(select_datalist)))
#     MainPage(browser).eleclick(select_list[num])
#     browser.find_element_by_xpath("//*[@id='tracking-content']/app-tracking-list/div/div[2]").click()
#     name = browser.find_element_by_xpath("//input[@aria-label='OrderName']").get_attribute('value')
#     assert name == select_datalist[num]
#     # User can input value, click "OK" to save the values.
#     phase_ele = browser.find_element_by_xpath("//button[@aria-label='Toggle PHASE57']")
#     MainPage(browser).eleclick(phase_ele)
#     param_input1 = browser.find_element_by_xpath("//span[contains(text(),'TEMP')]/../mat-form-field/div/div/div/input")
#     before_change = param_input1.get_attribute("value")
#     param_input1.clear()
#     param_input1.send_keys('111')
#     time.sleep(2)
#     # click 'OK' and Uncheck the check box,then click 'ok'
#     browser.find_element_by_xpath("//span[text()=' OK ']/..").click()
#     assert MainPage(browser).is_element_showed("#audit-dialog") is True
#     browser.find_element_by_xpath("//*[@id='audit-dialog']/div/div[2]/mat-form-field/div/div/div/textarea").send_keys('for test')
#     browser.find_element_by_xpath("//span[text()='OK']/..").click()
#     time.sleep(2)
#     phase_ele = browser.find_element_by_xpath("//button[@aria-label='Toggle PHASE57']")
#     MainPage(browser).eleclick(phase_ele)
#     param_input2 = browser.find_element_by_xpath("//span[contains(text(),'TEMP')]/../mat-form-field/div/div/div/input")
#     after_change = param_input2.get_attribute("value")
#     assert after_change != before_change
#     assert after_change == '111'
#     # CLick one value of the left page, check the details in the right page.
#     paramEle = browser.find_element_by_xpath("//div[@class='ng-star-inserted']/div/span").text
#     paramtitle = re.split(':', paramEle)[0]
#     browser.find_elements_by_xpath("//div[@class='ng-star-inserted']/div/span")[0].click()
#     time.sleep(2)
#     phase_title = browser.find_element_by_xpath("//mat-card-title/div").text
#     phaser_descrip = browser.find_element_by_xpath("//mat-card-subtitle[@class='mat-card-subtitle']/p").text
#     assert phase_title == paramtitle
#     assert phaser_descrip == 'Temperature'
#     # click another parameter,the detail card updates
#     browser.find_elements_by_xpath("//div[@class='ng-star-inserted']/div/span")[1].click()
#     time.sleep(2)
#     phase_title2 = browser.find_element_by_xpath("//mat-card-title/div").text
#     phaser_descrip2 = browser.find_element_by_xpath("//mat-card-subtitle[@class='mat-card-subtitle']/p").text
#     assert phase_title2 == 'VOL'
#     assert phaser_descrip2 == 'Volume'
#
#
#
# if __name__ == '__main__':
#     pytest.main(["-s", "test_VS713696.py"])