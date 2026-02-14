#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 09:32:49 2026

@author: fattabby
"""
import os
import pandas as pd
subject="terror"
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
database=pd.read_csv("database_terror.csv",index_col=0)
database_external=pd.read_csv("database_external_terror.csv",index_col=0)
database_external["ques_all"]=database_external["questions"]+database_external["options"]

find=database["questions_left"].str.find(".")
#因為pandas的操作比較麻煩，所以先一般的list去做處理
questions_for_query=[]
for i in range(database.shape[0]):
    a=find.iloc[i]
    questions_for_query.append(database.loc[i,"questions_left"][a+1:])   
    
database["key"]=pd.Series((i for i in questions_for_query))

#database["key"]=database["source"].astype(str).str[0:3]+"0"+database["source"].astype(str).str[5]+subject+database["index"].astype(str)
#answers=output_merge
merged_df=database.set_index("key").join(database_external.set_index("ques_all"), how="left", lsuffix='_left', rsuffix='_right')
merged_df=merged_df.reset_index(drop=True)

merged_df.to_csv("database_joined.csv")