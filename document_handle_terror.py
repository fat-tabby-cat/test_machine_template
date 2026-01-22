#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 18:24:16 2025

@author: fattabby
"""
import os
import pandas as pd
import numpy as np
#import re
mode=str(input("請輸入載入模式（1為檢討本次考試，2為檢討歷屆考試）："))

if os.name=="posix":
    print("you are using Linux or Mac")
    pathname = '/home/{}/Nextcloud/terror'.format(os.getlogin())
else:
    print("you are using Windows")
    pathname = 'C:/Users/{}/Nextcloud/terror'.format(os.getlogin())
try:
    os.chdir(pathname)
except Exception:
    os.makedirs(pathname, exist_ok=True)
    os.chdir(pathname)
    
database=pd.read_csv("database_terror.csv",index_col=0)
#database["handle1"]=database["questions_left"].str.split('(', expand=False)
#database["handle1"]=database["questions_left"].str.replace({"(A)":"|A","(B)":"|B","(C)":"|C","(D)":"|D"})
database["handle1"]=database["questions_left"].str.replace("(A)","|A.")
database["handle1"]=database["handle1"].str.replace("(B)", "|B.")
database["handle1"]=database["handle1"].str.replace("(C)", "|C.")
database["handle1"]=database["handle1"].str.replace("(D)", "|D.")
database["handle1"]=database["handle1"].str.split("|", expand=False)#, regex=True)
database["correct_text"]="test"
database["correct_text_test1"]="helloworld"
database["correct_text_test2"]="helloworld"
database["correct_text_test3"]="helloworld"
database["correct_text_test4"]="helloworld"
database["desnull"]=database["help"].isnull()
#database=database[(database["desnull"]==False)]
#為避免舊檔案的index影響後續題項的擷取作業故重設index
database["index"]=database.index
database=database.reset_index(drop=True)
def conditions(x):
    if   x == "A":   return database["handle1"][i][1]
    elif x == "B":   return database["handle1"][i][2]
    elif x == "C":   return database["handle1"][i][3]
    elif x == "D":   return ''.join([str(s) for s in database["handle1"][i][4:]])        
func         = np.vectorize(conditions)
answer_crossref={"A":1,"B":2,"C":3,"D":4}
for i in range(database.shape[0]):
    #question=database["questions"][i]
    conditions  = [ database["answers"][i]=="A", database["answers"][i]=="B", database["answers"][i]=="C",database["answers"][i]=="D" ]
    choices     = [ database["handle1"][i][1], database["handle1"][i][2], database["handle1"][i][3],database["handle1"][i][4] ]
    #print("now i is ", i)
    #print("answer is " ,database["answers"][i])
    #print("added ",database["answers"].apply(conditions,axis=1))
    #database["correct_text"][i]=np.select(conditions, choices), default=np.nan)
    database["correct_text"][i] = func(database["answers"][i])
    database["correct_text_test1"][i]= database["handle1"][i][1][:1]=="A"
    database["correct_text_test2"][i]= database["handle1"][i][2][:1]=="B"
    database["correct_text_test3"][i]= database["handle1"][i][3][:1]=="C"
    database["correct_text_test4"][i]=''.join([str(s) for s in database["handle1"][i][4:]])[:1]=="D"
    #database["correct_text_test4"][i]= database["handle1"][i][4:]#[:1]=="D"

#%%for recording use

import contextlib
database=database.sort_values(by=['source','index'],ascending=[False,True])
#https://www.delftstack.com/zh-tw/howto/python/python-output-to-file/

file_path = "terror_print_short.txt"
with open(file_path, "w") as o:
    with contextlib.redirect_stdout(o):
        for i in database.index:            
            print(database["handle1"][i][0])
            for j in str(database["answers"][i]):
                print("答案：",func(j))
            if database["desnull"][i]==False:
                print("解析：",database["help"][i])
            print("")
            #print("=============")
    #print(lawfile["Counts"])
    #print(lawfile["Text"])

file_path = "terror_print_long.txt"
with open(file_path, "w") as o:
    with contextlib.redirect_stdout(o):
        for i in database.index:
            res = ' '.join([str(s) for s in database["handle1"][i]])
            print(res)            
            for j in str(database["answers"][i]):
                print("答案：",func(j))
            #print("答案：",database["correct_text"][i]) #original code
            if database["desnull"][i]==False:
                print("解析：",database["help"][i])
            print("")
    
#%%    
#mode=str(input("請輸入載入模式（1為檢討本次考試，2為檢討歷屆考試）："))
if os.name=="posix":
    print("you are using Linux or Mac")
    if mode=="1":
        print("檢討本次考試")
        pathname = '/home/{}/Nextcloud/terror'.format(os.getlogin())
    elif mode=="2":    
        print("檢討歷屆考試")
        pathname = '/home/{}/Nextcloud/terror/archive'.format(os.getlogin())
else:
    print("you are using Windows")
    if mode=="1":
        print("檢討本次考試")
        pathname = 'C:/Users/{}/Nextcloud/terror'.format(os.getlogin())
    elif mode=="2":    
        print("檢討歷屆考試")
        pathname = 'C:/Users/{}/Nextcloud/terror/archive'.format(os.getlogin())
try:
    os.chdir(pathname)
except Exception:
    os.makedirs(pathname, exist_ok=True)
    os.chdir(pathname)

testincorrect=pd.read_csv("TestResult_Incorrects.csv")
testincorrect=testincorrect.drop_duplicates(subset=["pid"])
#testincorrect=testincorrect[(testincorrect["source"].str.contains("法規"))]
#testincorrect=testincorrect[(testincorrect["source"].str.contains("實務"))]
#%%

file_path = "terror_print_incorrects.txt"
with open(file_path, "w") as o:
    with contextlib.redirect_stdout(o):
        for i in testincorrect.pid:
            #print(i)
            print(database["handle1"][i][0])
            for j in str(database["answers"][i]):
                print("答案：",func(j))
            #print("答案：",database["correct_text"][i])
            if database["desnull"][i]==False:
                print("解析：",database["help"][i])
            print("")
