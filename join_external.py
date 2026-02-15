#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 09:32:49 2026

@author: fattabby
"""
import os
import pandas as pd
import numpy as np

subject_choice=input("請輸入欲處理科目：")
if subject_choice ==str(1):
    subject="terror"
    print("本次處理防制洗錢與資恐")
elif subject_choice ==str(2):
    subject="bank_internal_control"
    print("本次處理銀行內部控制")


if os.name=="posix":
    print("you are using Linux or Mac")
    pathname = '/home/{}/Nextcloud/{}/external'.format(os.getlogin(),subject)
else:
    print("you are using Windows")
    pathname = '/home/{}/Nextcloud/{}/external'.format(os.getlogin(),subject)
try:
    os.chdir(pathname)
except Exception:
    os.makedirs(pathname, exist_ok=True)
    os.chdir(pathname)
database=pd.read_csv("/home/{}/Nextcloud/{}/database_{}.csv".format(os.getlogin(),subject,subject),index_col=0)
database_external=pd.read_csv("database_external_{}.csv".format(subject),index_col=0)
database_external["ques_all"]=database_external["questions"]+database_external["options"]
#before
#descs1=database[database["help"].isnull()==False]
print("之前**{}**已有解析的題目數為：\n".format(subject), database[database["help"].isna()==False].shape[0])

find=database["questions_left"].str.find(".")
#因為pandas的操作比較麻煩，所以先一般的list去做處理
questions_for_query=[]
for i in range(database.shape[0]):
    symbol_location=find.iloc[i]
    questions_for_query.append(database.loc[i,"questions_left"][symbol_location+1:])   
    
database["key"]=pd.Series((i for i in questions_for_query))

#database["key"]=database["source"].astype(str).str[0:3]+"0"+database["source"].astype(str).str[5]+subject+database["index"].astype(str)
#answers=output_merge
merged_df=database.set_index("key").join(database_external.set_index("ques_all"), how="left", lsuffix='_left', rsuffix='_right')
merged_df=merged_df.reset_index(drop=True)

merged_df["help2"]=np.where(merged_df["help"].isnull(), merged_df["desc"], merged_df["help"])
merged_df["help"]=merged_df["help2"]
merged_df=merged_df[['index_left', 'questions_left', 'source_left', 'questions_right','answers','help']]

   
merged_df.to_csv("/home/{}/Nextcloud/{}/database_{}.csv".format(os.getlogin(),subject,subject))
#檢核測試用
#descs2=merged_df[merged_df["help"].isnull()==False]
print("後來**{}**有解析的題目數為：\n".format(subject), merged_df[merged_df["help"].isna()==False].shape[0])
