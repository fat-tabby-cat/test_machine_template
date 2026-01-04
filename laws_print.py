#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 14:06:08 2025

@author: fattabby
"""
import os
import pandas as pd
#set workdir
pathname = '/home/fattabby/Nextcloud/trusts_test'
try:
    os.chdir(pathname)
except Exception:
    os.makedirs(pathname, exist_ok=True)
    os.chdir(pathname)

#law_filter="證券商管理規則"# ,"證券交易法"
lawfile=pd.read_csv("信託業法.csv")
#lawfile=pd.read_csv("lawssource.csv")
#lawfile=lawfile[lawfile['Counts']>2]
#lawfile=lawfile[(lawfile["Level"].str.contains("證券交易所"))]
#lawfile=lawfile[(lawfile["Level"].str.contains("證券商管理規則") | lawfile["Level"].str.contains("證券交易法"))]
#lawfile=lawfile[lawfile['Counts']>=2]
#lawfile=lawfile[lawfile["Level"].str.contains(law_filter)]
#lawfile=lawfile[lawfile["concat"].str.contains(law_filter)]
#lawfile["article"]=lawfile["article"].str[len(law_filter):]



import contextlib

#https://www.delftstack.com/zh-tw/howto/python/python-output-to-file/

file_path = "信託業法_shrink.txt"
with open(file_path, "w") as o:
    with contextlib.redirect_stdout(o):
        for i,k in zip(lawfile["title"],lawfile["article"]):
        #for i,j,k in zip(lawfile["法別"],lawfile["title"],lawfile["text"]):
            print(i)            
            print(k)
            #print("")
            #print("=============")
    #print(lawfile["Counts"])
    #print(lawfile["Text"])
    
    
