# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 23:40:42 2021

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


url = "https://www.superjob.ru/vacancy/search/"
params = {
    "keywords": 'Разработчик PHP',
    "geo": '7'
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

path = "superjob.rsp"
save_pickle(r, path)
print()
r = load_pickle(path)
soup = bs(r.text, "html.parser")


items = soup.find_all(attrs={"class": "f-test-search-result-item"})

#print(items)

items_info=[]

for item in items:
    a = item.find("a", attrs={"class": "icMQ_"})
    

        
        
    #Вакансия: {a.text}
    print(a.text)
    #items_info.append(a)