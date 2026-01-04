#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 12:31:37 2025

@author: fattabby
#https://stackoverflow.com/questions/9234560/find-all-csv-files-in-a-directory-using-python
#

"""
mode=str(input("請輸入載入模式（1為檢討本次考試，2為檢討歷屆考試）："))

import os
import glob
import pandas as pd

if os.name=="posix":
    print("you are using Linux or Mac")
    if mode=="1":
        print("檢討本次考試")
        pathname = '/home/{}/Nextcloud/trusts_test'.format(os.getlogin())
    elif mode=="2":    
        print("檢討歷屆考試")
        pathname = '/home/{}/Nextcloud/trusts_test/archive'.format(os.getlogin())
else:
    print("you are using Windows")
    if mode=="1":
        print("檢討本次考試")
        pathname = 'C:/Users/{}/Nextcloud/trusts_test'.format(os.getlogin())
    elif mode=="2":    
        print("檢討歷屆考試")
        pathname = 'C:/Users/{}/Nextcloud/trusts_test/archive'.format(os.getlogin())
try:
    os.chdir(pathname)
except Exception:
    os.makedirs(pathname, exist_ok=True)
    os.chdir(pathname)
    
filename="考試結果"
extension = 'csv'
os.chdir(pathname)
result = glob.glob('*.{}'.format(extension))
#print(result)


id_file='考試結果*'
concat_files=glob.glob(id_file)
df = pd.concat([pd.read_csv(f) for f in  concat_files])
#df = pd.concat(map(pd.read_csv, concat_files), ignore_index=True)
df=df.sort_values("pid")
#print(df)
df.to_csv("TestResult_Concat.csv",index=False)

#path = '/home/fattabby/Nextcloud/gaoye_laws'
filename="答錯題目"
extension = 'csv'
#os.chdir(path)
result = glob.glob('*.{}'.format(extension))
#print(result)


id_file='答錯題目*'
concat_files=glob.glob(id_file)
df = pd.concat([pd.read_csv(f) for f in  concat_files])
#df = pd.concat(map(pd.read_csv, concat_files), ignore_index=True)
df=df.sort_values("pid")
#print(df)
df.to_csv("TestResult_Incorrects.csv",index=False)

#
import contextlib
database=pd.read_csv("TestResult_Incorrects.csv",index_col=0)
database["desnull"]=database["help"].isnull()
#database["handle1"]=database["questions"].str.split('(', expand=False)
database=database.drop_duplicates(subset=["pid"])
database=database.reset_index(drop=True)
#subject="marked"
file_path = "incorrects.txt"
with open(file_path, "w",encoding="utf-8") as o:
    with contextlib.redirect_stdout(o):
        for i in database.index:
            print("來源：",database["source"][i])#[28:])
            print(database["questions"][i])#.replace("\n", ""))
            print("答案：",database["actual_answer"][i])#.replace("\n", ""))            
            #print("答案：",database["actual_answer"][i].replace("\n", ""))            
            if database["desnull"][i]==False:
                print("解析：",database["help"][i].replace(" ", ""))                    
            print("")
            