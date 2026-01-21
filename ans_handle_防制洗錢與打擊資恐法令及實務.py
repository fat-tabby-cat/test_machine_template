#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 16:58:14 2025

@author: fattabby
本解答處理程式適用於防制洗錢與打擊資恐法令及實務（適合自動化處理）的已公佈解答
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
#%%combine answers to database
#database請自建
database=pd.read_csv("/home/fattabby/Nextcloud/terror/database_terror.csv",index_col=0)
#將步驟以code標準化
database["index"]=database["index"]+1 #因python的index起始值為0，故要+1才能做題目編號的整併
#取source的若干個字母+index
#database["key"]=database["source"].astype(str).str[0:3]+"0"+database["source"].astype(str).str[5]+database["source"].astype(str).str[12:16]+database["index"].astype(str)
database["key"]=database["source"].astype(str).str[0:3]+"0"+database["source"].astype(str).str[5]+subject+database["index"].astype(str)
answers=output_merge
merged_df=database.set_index("key").join(answers.set_index("source"), how="left", lsuffix='_left', rsuffix='_right')
merged_df=merged_df.reset_index(drop=True)
merged_df.to_csv("database_terror.csv")
