#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:13:25 2024

@author: fattabby
"""
import time
import pandas as pd
import numpy as np
import os
import sys

#讀取題庫位置
if os.name=="posix":
    print("you are using Linux or Mac")
    pathname = '/home/{}/Nextcloud/trusts_test/'.format(os.getlogin())
else:
    print("you are using Windows")
    pathname = 'C:/Users/{}/Nextcloud/trusts_test/'.format(os.getlogin())
try:
    os.chdir(pathname)
except Exception:
    os.makedirs(pathname, exist_ok=True)
    os.chdir(pathname)

database=pd.read_csv("database_trusts.csv",index_col=0)
#若限定要哪一年內或哪幾科試題，可以用這個去抓
#database=database[(database["source"].str.contains("2024年") | database["source"].str.contains("2025年")| database["source"].str.contains("2023年"))]
#database=database[(database["source"].str.contains("2025年"))]
#subject="投顧"
option=eval(input("請輸入考試科目代號"))
if option==1:
    subject="信託實務"
elif option==2:
    subject="信託法規"
#elif option==3:
#    subject="財務分析"
database=database[(database["source"].str.contains(subject))]
database=database.reset_index(drop=False)
if option==1:
    n_questions=80
    #n_questions=5
elif option==2:
    n_questions=50
else:
    print("option not exist")
    sys.exit(99)

#n_questions=5 #for test use
x1 = np.random.choice(int(database.index[-1]),n_questions,replace=False)
#從6549題中隨機出50題 #幾題是由size去控制
#x1 = np.random.randint(low=0, high=int(database.count()[0]), size=(5,))
print("考試開始")
start_time=time.time()
testinput=pd.DataFrame([],columns=["pid","questions","actual_answer","input_answer"])
#testinput=pd.DataFrame([],columns=["pid","questions","actual_answer","input_answer"])

for i in x1:
    ongoing_test=pd.DataFrame([],index=["pid","questions","source","actual_answer","input_answer","help"]).transpose()
    ongoing_test_pid=database["level_0"][i]
    ongoing_test_questions=database["questions_left"][i]
    ongoing_test_actual_answer=database["answers"][i]
    ongoing_test_input_answer=str.upper(input(database["questions_left"].iloc[i]))
    ongoing_test_input_source=database["source"][i]
    ongoing_test_help=database["help"][i]
    ongoing_test=pd.DataFrame([ongoing_test_pid,
                            ongoing_test_questions,
                            ongoing_test_input_source,
                            ongoing_test_actual_answer,
                            ongoing_test_input_answer,
                            ongoing_test_help],
                           index=["pid","questions","source","actual_answer","input_answer","help"]).transpose()
    testinput=pd.concat([testinput,ongoing_test])

start_time2=time.time()    
print("考試結束")    
print("本次考試費時：", start_time2-start_time, "秒")
testinput["correctcheck"]=(testinput["input_answer"]==testinput["actual_answer"])
#計分機制與倒扣（如果有；最後兩個參數分別為答對得幾分，答錯倒扣幾分）
testinput['score'] = np.where(testinput['input_answer']==testinput["actual_answer"], (100/n_questions), -(100/n_questions))
#if testinput["correctcheck"] is True:
#    testinput["score"]=2.5
#else:
#    testinput["score"]=-1

total_score=testinput["score"].sum()

print("本次考試總得分為：", total_score)
t = time.time()
t1 = time.localtime(t)
testinput=testinput.sort_values("pid")
testinput.to_csv("考試結果_{}_{}.csv".format(subject,str(t1.tm_year)+str(t1.tm_mon)+str(t1.tm_mday)+"_"+str(t1.tm_hour)+str(t1.tm_min)),encoding="utf-8")
testinput_incorrect=testinput[(testinput["correctcheck"]==False)]
testinput_incorrect.to_csv("答錯題目_{}_{}.csv".format(subject,str(t1.tm_year)+str(t1.tm_mon)+str(t1.tm_mday)+"_"+str(t1.tm_hour)+str(t1.tm_min)),encoding="utf-8")
