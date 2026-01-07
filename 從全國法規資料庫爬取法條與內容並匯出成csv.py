#%%
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
import pandas as pd
database=pd.DataFrame([],columns=["actname","title","article"]) 
 
#%%
#程式會自動抓法條標題，這樣就無須手動打
url = input('請輸入全國法規資料庫網址：')

web = requests.get(url)
soup = BeautifulSoup(web.text, "html.parser")
filename=soup.find('table').find('a').text


#urls=urls[0:6] 
#start_time=time.time()
#print(start_time)
def crawl_questions(url):
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "html.parser")
    #soup.select('p:contains("第 ")') 
    titles = soup.find_all('div', class_='col-no')      # 取得 class 為 title 的 div 內容
    #print(titles)
    #print(titles.text)
    articles=soup.find_all('div', class_='law-article')    
    
    #titles_output = []
    lawbase=pd.DataFrame([],columns=["actname","title","blank1","blank2","blank3","blank4","blank5","article"])
    #articles_output = []
    for i,j in zip(titles,articles):
        exports=pd.DataFrame([])
        exports["actname"]=[filename]
        exports["title"]=[i.text.replace(" ", "")]
        exports["article"]=j.text.strip()
        lawbase=pd.concat([lawbase,exports])
        #titles_output.append(i.text)
        #articles_output.append(j.text) 
    return lawbase
        
lawbase=crawl_questions(url)
database=pd.concat([lawbase,database])
#database.to_csv("{}.csv".format(filename))
#%%if you want to save to 
database.to_csv("{}.csv".format(filename),index=False)
