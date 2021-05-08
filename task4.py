# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 22:25:55 2021

@author: Роман
"""


from pprint import pprint
from lxml import html
import requests
import time
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['my_db']

collection = db['news']

def get_news_response(web_url):
    time.sleep(1)
    header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.218"}
    response = requests.get(web_url,params=None,headers = header)

    root = html.fromstring(response.text)

    return root

lenta_url='https://lenta.ru'

yandex_url = 'https://yandex.ru'

mail_url = 'https://mail.ru'


lenta_result = get_news_response(lenta_url).xpath("//section[contains(@class,'b-top7-for-main')]/div[@class]/div[contains(@class,'item')]/a")

yandex_result = get_news_response(yandex_url).xpath("//div[contains(@class,'mix-tabber-slide2__panel')]/ol[contains(@class,'news__list')]/li[contains(@class,'list__item')]")

mail_result = get_news_response(mail_url).xpath("//li[contains(@class,'tabs-content__item')]/div[contains(@class,'news-item')]")

for res in lenta_result:
    news_time=''
    news_name=''
    if len(res.xpath('.//text()'))==2:
        news_time = res.xpath('.//text()')[0]
        news_name = res.xpath('.//text()')[1]
    
    news_link = 'https://lenta.ru'+res.xpath('.//@href')[0]
    
    lenta_doc = {}
    
    if(news_name!=''):
        '''print(f'Источник: {lenta_url}')
        print(f'Новость: {news_name}')
        print(f'Время: {news_time}')
        print(f'Ссылка: {news_link}')'''
        
        lenta_doc['источник'] = lenta_url
        lenta_doc['новость'] = news_name
        lenta_doc['время'] = news_time
        lenta_doc['ссылка'] = news_link
        
        collection.update_one(lenta_doc, { '$set': lenta_doc }, upsert=True)
    
    #print()

for res in yandex_result:
    news_name = res.xpath(".//a[@class]/span[contains(@class,'news__item-inner')]/span[@class]/text()")[0]
    news_link = res.xpath('.//a/@href')[0]
    
    yandex_doc = {}
    
    #print(f'Источник: {yandex_url}')
    #print(f'Новость: {news_name}')
    #print(f'Ссылка: {news_link}')
    
    yandex_doc['источник'] = yandex_url
    yandex_doc['новость'] = news_name
    yandex_doc['ссылка'] = news_link
    
    collection.update_one(yandex_doc, { '$set': yandex_doc }, upsert=True)
    
    #print()



for res in mail_result:
    news_name = res.xpath(".//a[contains(@class,'news-visited')]/text()")[0]
    news_link = res.xpath(".//a[contains(@class,'news-visited')]/@href")[0]
    
    mail_doc = {}
    
    #print(f'Источник: {mail_url}')
    #print(f'Новость: {news_name}')
    #print(f'Ссылка: {news_link}')
    
    mail_doc['источник'] = mail_url
    mail_doc['новость'] = news_name
    mail_doc['ссылка'] = news_link
    
    collection.update_one(mail_doc, { '$set': mail_doc }, upsert=True)
    
    #print()
#print(len(result))

