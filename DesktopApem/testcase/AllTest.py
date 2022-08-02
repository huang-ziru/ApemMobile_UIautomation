import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("DesktopApem\\")+len("DesktopApem\\")]
sys.path.extend([rootPath, rootPath])
from xml.dom.minidom import parse
from xml.dom.minidom import Document
from framework.conf import conf_xml
#from framework.conf import modifyConf
conf_xml()
#modifyConf()
# Process the current script running address
path1 = os.path.dirname(os.path.abspath(__file__))
command = "pytest " + path1 + " --junit-xml=../report/report1.xml"
os.system(command)
import xml.dom.minidom
import re
DOMTree = xml.dom.minidom.parse("..\\report\\report1.xml")
collection = DOMTree.documentElement
testsuite = collection.getElementsByTagName("testsuite")
if testsuite[0].getAttribute("failures") != '0':
    command = "pytest --lf " + path1 + " --junit-xml=../report/report2.xml"
    os.system(command)

#Create a document object
doc = Document()
#Create a root node
root = doc.createElement('testsuites')
#Join root node to tree
doc.appendChild(root)
#Create secondary node
testsuite = doc.createElement('testsuite')
testresult = doc.createElement('testresult')
# Using minidom parser to open XML document
filename = path1 + '\..\\report\\report2.xml'
DOMTree = xml.dom.minidom.parse("..\\report\\report1.xml")
collection = DOMTree.documentElement
CaseNames_fail = []
case_list=[{'caseID': '580300', 'caseName': 'UC558888_APEM mobile - Login successfully with valid user name and password _ for desktop'}, {'caseID': '580320', 'caseName': 'UC558888_APEM - Login APEM mobile using invalid user name or password _ For desktop'}, {'caseID': '580352', 'caseName': 'UC558888_APEM mobile - Can not login if user has no access'}, {'caseID': '580358', 'caseName': 'UC558383_APEM mobile - "User info", "help", "license", "switch layout", "full screen" will show on the title bar_ for desktop'}, {'caseID': '580360', 'caseName': 'UC558383_APEM mobile - “User info” icon can work on the title bar for desktop'}, {'caseID': '580362', 'caseName': 'UC558383_APEM mobile - "Help" icon can work on the title bar_ For desktop'}, {'caseID': '580364', 'caseName': 'UC558383_APEM mobile - "Error/warning" icon can work on the title bar _ for desktop'}, {'caseID': '580365', 'caseName': 'UC558383_APEM mobile - "Switch layout" icon can work on the title bar _ For desktop'}, {'caseID': '580369', 'caseName': 'UC558383_APEM mobile - "Full screen" icon can work on the title bar _ For desktop'}, {'caseID': '580450', 'caseName': 'UC558383_APEM mobile - The navigation bar work for desktop.'}, {'caseID': '580454', 'caseName': 'UC558383_APEM mobile - loading order list for desktop'}, {'caseID': '580455', 'caseName': 'UC558383_APEM mobile - Order table function : Filter function for desktop'}, {'caseID': '580519', 'caseName': 'UC558383_APEM mobile - Sort function for order table_ Desktop'}, {'caseID': '580550', 'caseName': 'UC558383_APEM mobile - Order table shows visible columns_ Desktop'}, {'caseID': '580580', 'caseName': 'UC558383_APEM mobile - Scroll function for APEM mobile_desktop'}, {'caseID': '580588', 'caseName': 'UC558383 - APEM mobile - Search function_ Desktop'}, {'caseID': '585400', 'caseName': 'UC558383_APEM mobile - Order/batch column filter function for desktop'}, {'caseID': '591770', 'caseName': 'UC558386_ APEM mobile - "Audit reason" testing on "Setting" page'}, {'caseID': '591819', 'caseName': 'UC558386_APEM mobile -  "Dark Mode" button function on "Settings" page'}, {'caseID': '591822', 'caseName': 'UC558385_APEM mobile - Go to Order tracking page '}, {'caseID': '591825', 'caseName': 'UC558385_APEM mobile - Check the default view of Order tracking page'}, {'caseID': '591827', 'caseName': 'UC558386_APEM mobile - "Consolidated interface" button function on "Settings" page'}, {'caseID': '591862', 'caseName': 'UC558385_APEM mobile - Visible columns on Order tracking page'}, {'caseID': '591865', 'caseName': 'UC558385_APEM mobile - Sort function on Order tracking page'}, {'caseID': '591875', 'caseName': 'UC558385_APEM mobile - Filter function on Order tracking page'}, {'caseID': '591876', 'caseName': 'UC558385_APEM mobile - Scroll function on Order tracking page'}, {'caseID': '591893', 'caseName': 'UC558385_APEM mobile - Change the order on the order tracking page'}, {'caseID': '626781', 'caseName': 'UC558390_Check the Bing can show in APEM mobile execution page'}, {'caseID': '626810', 'caseName': 'UC604824_APEM mobile - Check the state icon under the table of the order tracking page'}, {'caseID': '627824', 'caseName': 'UC558394_Can go to parameter page in "Process order"/"Tracking"/ PFC graphic page'}, {'caseID': '627837', 'caseName': 'UC558394_Check the bread crumb shows correctly'}, {'caseID': '627866', 'caseName': 'UC558394_Check the parameter page shows correctly on dark/ light mode'}, {'caseID': '627898', 'caseName': 'UC558394_Check the tree structure can work as expected'}, {'caseID': '627904', 'caseName': 'UC558394_Check the parameter details show as expected'}, {'caseID': '627922', 'caseName': 'UC558394_Audit for parameter value change'}, {'caseID': '628336', 'caseName': 'UC558903_APEM mobile-Check the breadcrumb can show and work as expected on execution page'}, {'caseID': '628342', 'caseName': 'UC558903_APEM mobile-Check the Toolbar can show and work on execution page'}, {'caseID': '629854', 'caseName': 'UC558903_Execute a basic phase OK/Cancel on APEM mobile'}, {'caseID': '629858', 'caseName': 'UC558903_ Leave the execution page directly via click order name for APEM mobile'}, {'caseID': '629860', 'caseName': 'UC558903_Leave the execution page via close the browser/tab on APEM mobile'}]
failed_caseid = []
passed_caseid = []
if os.path.exists(filename) is True:
    DOMTree2 = xml.dom.minidom.parse(filename)
    collection2 = DOMTree2.documentElement
    testsuites = collection2.getElementsByTagName("testsuite")
    testcases = collection2.getElementsByTagName("testcase")
    for testcase in testcases:
        classname = testcase.getAttribute("classname")
        # casename1 = testcase.getAttribute("name")
        case_id = classname.split('.')[0]
        failure = testcase.getElementsByTagName('failure')
        if failure != []:
            message = failure[0].getAttribute('message')
            casepoint = doc.createElement('testcase')
            casepoint.setAttribute('result', 'failed')
            if case_id not in failed_caseid:
                # print(case_id)
                failed_caseid.append(case_id)
                casepoint.setAttribute('case_id', case_id)
                for caseDict in case_list:
                    if caseDict['caseID'] == re.sub(r'\D', "", case_id):
                        casename = caseDict['caseName']
                        # print(casename)
                        casepoint.setAttribute('case_name', casename)
                        casepoint.setAttribute('message', message)
                        vsts_id = 'VSTS' + re.sub(r'\D', "", case_id)
                        casepoint.setAttribute('VSTS_id', vsts_id)
                        testresult.appendChild(casepoint)
                        if casename not in CaseNames_fail:
                            CaseNames_fail.append(casename)
else:
    testsuites = collection.getElementsByTagName("testsuite")
testcases = collection.getElementsByTagName("testcase")
for testcase in testcases:
    classname = testcase.getAttribute("classname")
    case_id = classname.split('.')[0]
    if (case_id not in failed_caseid) and (case_id not in passed_caseid):
        passed_caseid.append(case_id)
        for caseDict in case_list:
            if caseDict['caseID'] == re.sub(r'\D', "", case_id):
                casename = caseDict['caseName']
                if casename not in CaseNames_fail:
                    casepoint = doc.createElement('testcase')
                    casepoint.setAttribute('result', 'passed')
                    casepoint.setAttribute('case_id', case_id)
                    casepoint.setAttribute('case_name', casename)
                    vsts_id = 'VSTS' + re.sub(r'\D', "", case_id)
                    casepoint.setAttribute('VSTS_id', vsts_id)
                    testresult.appendChild(casepoint)
                    testsuite.appendChild(testresult)
                    root.appendChild(testsuite)
testsuites = collection.getElementsByTagName("testsuite")
# total_test = testsuites[0].getAttribute("tests")
error = testsuites[0].getAttribute("errors")
skipped = testsuites[0].getAttribute("skipped")
time = testsuites[0].getAttribute("time")
num_passed = len(passed_caseid)
num_failed = len(failed_caseid)
total_test = num_passed + num_failed
testsuite.setAttribute('errors', error)
testsuite.setAttribute('failed', str(num_failed))
testsuite.setAttribute('skipped', skipped)
testsuite.setAttribute('passed', str(num_passed))
testsuite.setAttribute('total', str(total_test))
testsuite.setAttribute('time', time)

#存成xml文件
fp = open('..\\report\\test.xml','w',encoding='utf-8')
doc.writexml(fp, indent='', addindent='\t', newl='\n', encoding='utf-8')
fp.close()

