
"""Import Packages"""
import requests
import os
import sys
import time
import pandas as pd

"""log start time of crontab  """
now = time.time()
timestart = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))
print('This program started running at: ', timestart)

"""get current working directory """
cwd = os.getcwd()

""" Request Dataset and convert to dataframe"""
aws_data_exchange_test = requests.get('https://d1ewbp317vsrbd.cloudfront.net/56dae237-43a3-4d85-aee7-8785391f31c4.json') 

aws_data_exchange_test = pd.DataFrame(aws_data_exchange_test)
 
"""save dataframe to a local csv file"""
aws_data_exchange_test.to_csv('data/aws_data_exchange_test.csv', index=None)

"""save current time as a string"""
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

"""create a new file in the current working directory"""
with open(cwd + '/home/AngelPagan/crontab/testFile_' + nowStr + '.txt', 'w') as f:
    f.write(str(aws_data_exchange_test))

"""log crontab time end"""
now = time.time()
endTime = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))
print('This program started running at: ', endTime)