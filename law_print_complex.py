#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 14:06:08 2025
基本用途：遇到多條法律時drop duplicate以免重複聽浪費時間
@author: fattabby
"""
import os
import pandas as pd
#set workdir
if os.name=="posix":
    print("you are using Linux or Mac")
    folder_path = "/home/{}/Nextcloud/futures_archive/".format(os.getlogin())
else:
    print("you are using Windows")
    folder_path = 'C:/Users/{}/Nextcloud/futures_archive'.format(os.getlogin())
try:
    os.chdir(folder_path)
except Exception:
    os.makedirs(folder_path, exist_ok=True)
    os.chdir(folder_path)

#law_filter="證券商管理規則"# ,"證券交易法"
lawfile=pd.read_excel("laws_futures.ods",sheet_name=1)
lawfile=lawfile.drop_duplicates(subset=["query"])
#lawfile=lawfile.sort_values("lawuid")
#lawfile=pd.read_csv("lawssource.csv")
#lawfile=lawfile[lawfile['Counts']>2]
#lawfile=lawfile[(lawfile["Level"].str.contains("證券交易所"))]
#lawfile=lawfile[(lawfile["Level"].str.contains("證券商管理規則") | lawfile["Level"].str.contains("證券交易法"))]
#lawfile=lawfile[lawfile['appear_times']>2]
#lawfile=lawfile[lawfile["Level"].str.contains(law_filter)]
#lawfile=lawfile[lawfile["concat"].str.contains(law_filter)]
#lawfile["article"]=lawfile["article"].str[len(law_filter):]

#lawfile.to_csv("投顧法規匯總.csv")
#%%
import contextlib

#https://www.delftstack.com/zh-tw/howto/python/python-output-to-file/
lawfile["chapter"]=lawfile["chapter"].astype("Int64")
lawfile=lawfile.sort_values("appear_times",ascending=False)
file_path = "lawprint_shrink.txt"
with open(file_path, "w") as o:
    with contextlib.redirect_stdout(o):
        #for i,j,k in zip(lawfile["query"],lawfile["appear_times"],lawfile["resp"]):
        for h,i,j,k in zip(lawfile["chapter"],lawfile["quesno"],lawfile["query"],lawfile["resp"]):
        #for i,j,k in zip(lawfile["法別"],lawfile["title"],lawfile["text"]):
            #print("第",h,"-",i,"題。")
            print(j,"條。")
            #print(i,"條。")
            #print("出現概率：",int(j),"次。")
            print(k)
            #print(k.replace("                                                                            ", " "))
            print("")
            #print("=============")
    #print(lawfile["Counts"])
    #print(lawfile["Text"])
    
#%%
import contextlib

#https://www.delftstack.com/zh-tw/howto/python/python-output-to-file/
lawfile2=pd.DataFrame([])
for i in lawfile["chapter"].unique():  
    #data=lawfile[lawfile['chapter']==int(i)]
    data=lawfile[lawfile['chapter']==i]
    data=data.drop_duplicates(subset=["query"])
    lawfile2=pd.concat([lawfile2,data])
    
    
#lawfile2=lawfile2.reset_index(drop=True)

file_path = "lawprint_scanmode.txt"
with open(file_path, "w") as o:
    with contextlib.redirect_stdout(o):
        for i in lawfile2.index:
            print("第",lawfile2["chapter"][i],"-",lawfile2["quesno"][i],"題。")
            print(lawfile2["query"][i],"條。")
            #print(lawfile2["resp"][i])#.replace(" ",""))
            print(lawfile2["resp"][i].replace(" ",""))
