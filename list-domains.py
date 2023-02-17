from pip._vendor import requests
import json

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
response_dict = json.loads(response.text)
for i in response_dict:
    print("key: ", i, "val: ", response_dict[i])

# create a blank Workbook object
workbook = Workbook()
# access default empty worksheet
worksheet = workbook.getWorksheets().get(0)

# set JsonLayoutOptions for formatting
layoutOptions = JsonLayoutOptions()
layoutOptions.setArrayAsTable(True)

# import JSON data to default worksheet starting at cell A1
JsonUtility.importData(response_dict, worksheet.getCells(), 0, 0, layoutOptions)

# save resultant file in JSON-TO-XLS format
workbook.save("output.xls", SaveFormat.AUTO)