# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 10:46:37 2021

@author: Роман
"""

import json
#import time
import pickle
import requests
#from pprint import pprint
from bs4 import BeautifulSoup as bs


def save_pickle(o, path):
    with open(path, 'wb') as f:
        pickle.dump(o, f)


def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)


def get(url, headers, params):
    r = requests.get(url, headers=headers, params=params)
    return r

page_num=0

#while soup.find('a',attrs={"data-qa":"pager-next"})!=None:
    
url = "https://hh.ru/search/vacancy"
params = {
    "text": 'php developer',
    "area": '115',
    "page": page_num
}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/89.0.4389.90 Safari/537.36 OPR/75.0.3969.149"
}
proxies = {
    # 'http': 'http://3.88.169.225:80',
    # 'https': 'https://165.227.223.19:3128',
}
r = get(url, headers, params)

path = "hh.rsp"
save_pickle(r, path)
print()
r = load_pickle(path)
soup = bs(r.text, "html.parser")



last_page=soup.find('a',attrs={"data-qa":"pager-next"})


items = soup.find_all(attrs={"class": "vacancy-serp-item"})

items_info=[]  

for item in items:
    info = {}
    a = item.find("a", attrs={"class": "bloko-link"})
    salary=item.find(attrs={'class':'vacancy-serp-item__sidebar'}).text
    
    max_salary=0
    if (salary.find('от')!=-1):
        min_salary=salary[3:]
    elif (salary.find('до')!=-1):
        max_salary=salary[3:]
    else:
        min_salary=salary[0:salary.find('–')]
        max_salary=salary[salary.find('–')+1:]
        
    info['страница']=page_num
    info['вакансия']=a.text
    info['ссылка']=a["href"]
    info['мин. зарплата']=min_salary
    info['макс. зарплата']=max_salary
    
    #print(f'{a["href"]}, min. sal:{min_salary}, max. sal: {max_salary}')
    items_info.append(info)
        
    
    
with open("vacancies.json", "w",encoding='utf8') as f_obj:
    json.dump(items_info, f_obj,ensure_ascii=False)
    
    

