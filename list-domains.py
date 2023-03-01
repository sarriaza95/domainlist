from pip._vendor import requests
import json
import csv
from operator import itemgetter
import pandas as pd

headers = {
    'Authorization': 'whm root:9VDQH22VRU23AMHM8A8F5I2UVVFBLO69',
}

params = {
    'api.version': '1',
    'api.columns.a': 'user',
    'api.columns.b': 'domain',
    'api.columns.enable': '',
}

response = requests.get('https://io.topfloormarketing.net:2087/json-api/listaccts', params=params, headers=headers)
print(response)
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f)
response_dict = response.json()
for i in response_dict:
    print("key: ", i, "val: ", response_dict[i])

with open('data.json') as json_file:
    data = json.load(json_file)
    print ("type", type(data['data']))
    
    print("\nPeople1:", data['metadata'])
    print("\nPeople2:", data['data']['acct'])


    df = pd.DataFrame(data=data['data']['acct'])
    df.to_excel("students.xlsx", index=False)
print("Dictionary converted into excel...")