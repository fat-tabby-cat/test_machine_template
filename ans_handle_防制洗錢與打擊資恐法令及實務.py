#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 16:58:14 2025

@author: fattabby
本解答處理程式適用於防制洗錢與打擊資恐法令及實務（適合自動化處理）的已公佈解答
請尊重著作權，僅於合法範圍內使用
"""
import pandas as pd
import os
import glob
host="sfi"
if os.name=="posix":
    print("you are using Linux or Mac")
    folder_path = "/home/{}/Nextcloud/terror/ans/type_{}".format(os.getlogin(),host)
else:
    print("you are using Windows")
    folder_path = 'C:/Users/{}/Nextcloud/terror/ans/type_{}'.format(os.getlogin(),host)
try:
    os.chdir(folder_path)
except Exception:
    os.makedirs(folder_path, exist_ok=True)
    os.chdir(folder_path)
'''
因主考單位每季會輪換，各單位釋出的解答格式不同，故要分別做轉換
Type: SFI（證基會）
(先略過2列)
（1-80題）防制洗錢與打擊資恐法令及實務
'''
file_names = os.listdir(folder_path)    
extension = 'txt'
#os.chdir(pathname)
file_names = glob.glob('*.{}'.format(extension))
file_names=sorted(file_names)
subject="防制洗錢與打擊資恐法令及實務"

col_quesno=[0,2,4,6,8]
col_answer=[1,3,5,7,9]
output=pd.DataFrame([])    
for i in file_names:
    workspace=pd.DataFrame([],columns=["source","questions","answers"])    
    data = pd.read_csv(i, sep=" ", header=None,skiprows=2,nrows=16)    
    for j,k in zip(col_quesno,col_answer):
        #answer=pd.Series(data.iloc[0:10,k])
        #answer.index=data.iloc[0:10,j]
        #workspace=workspace._append(answer)
        #workspace2=pd.DataFrame([workspace]).transpose()
        source=pd.Series([i[0:5]+subject]*data.shape[0])
        workspace["source"]=source
        workspace["questions"]=data.iloc[0:16,j]
        #workspace["key"]=source+data.iloc[0:10,j]
        workspace["answers"]=data.iloc[0:16,k]
        output=pd.concat([output,workspace])
    workspace=pd.DataFrame([],columns=["source","questions","answers"])    
output_merge=pd.DataFrame([],columns=["source","questions","answers"])    

output["source"]=output["source"].astype(str) +output["questions"].astype(str) 
output_merge=pd.concat([output_merge,output])
output.to_csv(os.path.abspath(os.path.join(folder_path, os.pardir))+"/answer_{}.csv".format(host))      

#%%
'''
TYPE: TABF（台灣金融研訓院）
(先略過4列)
（1-80題）防制洗錢與打擊資恐法令及實務
'''
host="tabf"
if os.name=="posix":
    print("you are using Linux or Mac")
    folder_path = "/home/{}/Nextcloud/terror/ans/type_{}".format(os.getlogin(),host)
else:
    print("you are using Windows")
    folder_path = 'C:/Users/{}/Nextcloud/terror/ans/type_{}'.format(os.getlogin(),host)
try:
    os.chdir(folder_path)
except Exception:
    os.makedirs(folder_path, exist_ok=True)
    os.chdir(folder_path)
    
file_names = os.listdir(folder_path)    
extension = 'txt'
#os.chdir(pathname)
file_names = glob.glob('*.{}'.format(extension))
file_names=sorted(file_names)


col_quesno=[0]
col_answer=[1]
#output=pd.DataFrame([])    
for i in file_names:
    #for 信託法規 all
    workspace=pd.DataFrame([],columns=["source","questions","answers"])    
    data = pd.read_csv(i, sep=' ', header=None,skiprows=4,nrows=80,engine='python',names=["quesno","ans1"])    
    #data=data.dropna(axis='columns')
    output=pd.DataFrame([])    
    for j,k in zip(col_quesno,col_answer):        
        source=pd.Series([i[0:5]+subject]*data.shape[0])
        workspace["source"]=source
        workspace["questions"]=data["quesno"]        
        workspace["answers"]=data["ans1"]
        output=pd.concat([output,workspace])

output["source"]=output["source"].astype(str) +output["questions"].astype(str) 
output_merge=pd.concat([output_merge,output])
output.to_csv(os.path.abspath(os.path.join(folder_path, os.pardir))+"/answer_{}.csv".format(host))      
#%%
'''
Type: TII（保發中心）
(先略過2列)
（1-80題）防制洗錢與打擊資恐法令及實務
'''
host="tii"
if os.name=="posix":
    print("you are using Linux or Mac")
    folder_path = "/home/{}/Nextcloud/terror/ans/type_{}".format(os.getlogin(),host)
else:
    print("you are using Windows")
    folder_path = 'C:/Users/{}/Nextcloud/terror/ans/type_{}'.format(os.getlogin(),host)
try:
    os.chdir(folder_path)
except Exception:
    os.makedirs(folder_path, exist_ok=True)
    os.chdir(folder_path)

file_names = os.listdir(folder_path)    
extension = 'txt'
#os.chdir(pathname)
file_names = glob.glob('*.{}'.format(extension))
file_names=sorted(file_names)
subject="防制洗錢與打擊資恐法令及實務"

col_quesno=[0,2,4,6,8,10,12,14]
col_answer=[1,3,5,7,9,11,13,15]
output=pd.DataFrame([])    
for i in file_names:
    workspace=pd.DataFrame([],columns=["source","questions","answers"])
    data = pd.read_csv(i, sep=" ", header=None,skiprows=2,nrows=16)
    data=data.drop(columns=0)
    data=data.transpose()
    for j,k in zip(col_quesno,col_answer):        
        workspace["questions"]=data.iloc[0:11,j].astype(str)
        workspace["answers"]=data.iloc[0:11,k].astype(str)
        workspace["source"]=i[0:5]+subject
        output=pd.concat([output,workspace])
    workspace=pd.DataFrame([],columns=["source","questions","answers"])    

output["source"]=output["source"].astype(str)+output["questions"].astype(str) 
output_merge=pd.concat([output_merge,output])
output.to_csv(os.path.abspath(os.path.join(folder_path, os.pardir))+"/answer_{}.csv".format(host))      
#%%
'''
Type: IAFI（犯防中心）
(先略過2列)
（1-80題）防制洗錢與打擊資恐法令及實務
'''
host="iafi"
if os.name=="posix":
    print("you are using Linux or Mac")
    folder_path = "/home/{}/Nextcloud/terror/ans/type_{}".format(os.getlogin(),host)
else:
    print("you are using Windows")
    folder_path = 'C:/Users/{}/Nextcloud/terror/ans/type_{}'.format(os.getlogin(),host)
try:
    os.chdir(folder_path)
except Exception:
    os.makedirs(folder_path, exist_ok=True)
    os.chdir(folder_path)

file_names = os.listdir(folder_path)    
extension = 'txt'
#os.chdir(pathname)
file_names = glob.glob('*.{}'.format(extension))
file_names=sorted(file_names)
subject="防制洗錢與打擊資恐法令及實務"

def texthandle(input_file):
    with open(input_file) as file:        
        whole=[]  
        for line in file:
            if "【" in line:
                whole.append(line)                             
        df=pd.DataFrame(whole)
        df.to_csv(input_file[0:5]+"_processed"+".csv", index=False)
             
for i in file_names:
    texthandle(i)
'''
因為檔案狀況不適合全自動化處理，故部份操作會改在LibreOffice Calc上進行後轉存
'''
#%%for iafi import only
output_merge=pd.DataFrame([],columns=["source","questions","answers"])    
file_names = os.listdir(folder_path)    
extension = 'csv'
#os.chdir(pathname)
file_names = glob.glob('*.{}'.format(extension))
file_names=sorted(file_names)
for i in file_names:
    output=pd.read_csv(i)
    output_merge=pd.concat([output_merge,output])

#%%combine answers to database
'''
從犯防中心來的檔案處理後必須人工校對，故另存新檔後用LibreOffice編輯回原題庫檔案
'''
database=pd.read_csv("/home/fattabby/Nextcloud/terror/database_terror.csv",index_col=0)
'''
#database請自建，相關參數如下：
Index(['index', 'questions_left', 'source', 'questions_right', 'answers',
       'help'],
      dtype='object')
其中下面使用的串接key格式：民國年度+第幾次測驗+科目（"防制洗錢與打擊資恐法令及實務"）+題號
如：11404防制洗錢與打擊資恐法令及實務78

'''
#將步驟以code標準化
if host != "iafi":
    #print("jack in the box")
    database["index"]=database["index"]+1 #因python的index起始值為0，故要+1才能做題目編號的整併    
else:
    print("skip [index+=1] procedure")
#取source的若干個字母+index
#database["key"]=database["source"].astype(str).str[0:3]+"0"+database["source"].astype(str).str[5]+database["source"].astype(str).str[12:16]+database["index"].astype(str)
database["key"]=database["source"].astype(str).str[0:3]+"0"+database["source"].astype(str).str[5]+subject+database["index"].astype(str)
answers=output_merge
merged_df=database.set_index("key").join(answers.set_index("source"), how="left", lsuffix='_left', rsuffix='_right')
merged_df=merged_df.reset_index(drop=True)
if host != "iafi":
    merged_df.to_csv("database_terror.csv")
else:
    merged_df.to_csv("database_terror_iafi.csv")
