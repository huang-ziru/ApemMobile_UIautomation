#Batch execute all py files in the current folder
# import os
# lst = os.listdir(os.getcwd())  # Get all the file names in the current directory
# for c in lst:
#     if os.path.isfile(c) and c.endswith('.py') and c.find("AllTest")== -1:  #Determine that the file name ends with. Py, and remove the AllTest.py file
#         os.system('python {}'.format(c)) #execute python file one by one
#





#batch execute all testcase by in the current folder with one command

import os
os.system('pytest -q -s ..\\testcase --html=../report/result.html')
