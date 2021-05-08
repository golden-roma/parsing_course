# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from pymongo import MongoClient
from pprint import pprint
import json

client = MongoClient('localhost', 27017)

db = client['my_db']

collection = db['vacancies']

with open('vacancies.json','r',encoding='utf8') as f_obj:
    doc_list = json.load(f_obj)

#print(len(strings))



#collection.delete_many({})

def upsert_data(doc_list):
    try:
        for doc in doc_list:
            collection.update_one(doc, { '$set': doc }, upsert=True)
    except ValueError:
        return 0
    else:
        return 1
    
upsert_data(doc_list)

'''collection.insert_one(
   { 'item': "canvas", 
     'qty': 100, 
     'tags': ["cotton"], 
     'size': { 'h': 28, 'w': 35.5, 'uom': "cm" } }
)

collection.insert_many([
   { 'item': "journal", 'qty': 25, 'tags': ["blank", "red"], 'size': { 'h': 14, 'w': 21, 'uom': "cm" } },
   { 'item': "mat", 'qty': 85, 'tags': ["gray"], 'size': { 'h': 27.9, 'w': 35.5, 'uom': "cm" } },
   { 'item': "mousepad", 'qty': 25, 'tags': ["gel", "blue"], 'size': { 'h': 19, 'w': 22.85, 'uom': "cm" } }
])'''

'''collection.delete_many({
    
    'item': { '$in': ['canvas','journal','mat','mousepad'] }
})

collection.update_many(
    
    { 'item': { '$in': ['journal','mousepad'] } }, 
    { '$set': { 'qty': 30 } }

)'''

def get_min_salary(min_sal): 
   
    res = collection.find({
        'мин зарплата':  { '$gt': min_sal }
    })
    
    return res

def get_salary_between(min_sal,max_sal):
    
    res = collection.find({
         '$and':[{ 'мин зарплата': { '$gt': min_sal } }, 
                 { 'макс зарплата': { '$lt': max_sal } }, 
                 { 'макс зарплата': { '$gt': min_sal } }
        ]
    })
    
    return res
    
    


min_sal = int(input('Введите мин зарплату: '))
max_sal = int(input('Введите макс зарплату: '))

salary_res = get_salary_between(min_sal,max_sal)

min_salary_res = get_min_salary(min_sal)

print()

print('Работа функции get_min_salary...')
for doc in min_salary_res:
    pprint(doc)

print()

print('Работа функции get_salary_between...')
for d in salary_res:
    pprint(d)

