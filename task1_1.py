# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 20:16:24 2021

@author: Роман
"""




import requests
import os
import json
#from pprint import pprint

#token='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'
token = os.getenv('GITHUB_TOKEN', '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')
username = 'golden-roma'

query_url = 'https://api.github.com/user/repos'

headers = {'Authorization': f'token {token}'}
res = requests.get(query_url, headers=headers).text

with open('github_result.json','w') as f_obj:
    f_obj.writelines(res)


def get_repos_list(json_file):
    
    repos_list=[]
    
    for repo in json.loads(json_file):
        repos_list.append(repo['name'])
        
    return repos_list

    
#print(type(res))
#print()
print(get_repos_list(res))


'''
gh_session = requests.Session()
gh_session.auth = (username, token)

# get the list of repos belonging to me
repos = json.loads(gh_session.get(query_url).text)

# print the repo names
for repo in repos:
    print(repo['name'])
'''