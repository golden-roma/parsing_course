# -*- coding: utf-8 -*-
"""
Created on Sun May  2 11:04:09 2021

@author: Роман
"""


from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['my_db']

collection = db['posts']

driver = webdriver.Chrome(executable_path='C:\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("https://vk.com/tokyofashion")

#assert "Python" in driver.title

driver.execute_script("window.scrollTo(0, 400)") 

time.sleep(3)

elem = driver.find_element_by_class_name('ui_tab_search')
elem.click()

search_elem = driver.find_element_by_id("wall_search")
search_elem.send_keys("фотография")
search_elem.send_keys(Keys.RETURN)


time.sleep(3)

driver.execute_script("window.scrollTo(0, 1000)")


post_elems = driver.find_elements_by_xpath("//div[@class='_post_content']") 

#post_date = post_elems.find_elements_by_class_name('rel_date')
#post_text = post_elems.find_elements_by_class_name('wall_post_text')

#print(len(post_elems))



for post_elem in post_elems:
    
    post_info = {}    
    
    post_date = post_elem.find_element_by_class_name('rel_date')
    post_text = post_elem.find_element_by_class_name('wall_post_text')   
    post_likes = post_elem.find_element_by_class_name('like_button_count')
    
    #print(post_elem.text)
    if(post_date!=None or post_date.strip().trim()==''):
        #print(f'Дата: {post_date.text}')
        #print(f'Текст: {post_text.text}')
        #print(f'Кол-во лайков: {post_likes.text}')
        #print()
        post_info['дата'] = post_date.text
        post_info['текст'] = post_text.text
        post_info['кол-во лайков']=post_likes.text
        collection.update_one(post_info, { '$set': post_info }, upsert=True)
    
#assert "No results found." not in driver.page_source

time.sleep(5)

driver.quit()
    




