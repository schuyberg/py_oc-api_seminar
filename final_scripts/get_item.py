import requests, json

ocUrl = 'https://open.library.ubc.ca/'
ocApiUrl = 'https://oc-index.library.ubc.ca'

apiKey = 'ac40e6c2cb345593ed1691e0a8b601bba398e42d85f81f893c5ab709cec63c6c'

collection = 'bcbooks'
itemId = '1.0222552'

# TASK 1

# GET AN ITEM
# url to an item
itemUrl = ocApiUrl+'/collections/'+collection+'/items/'+itemId+'?apiKey='+apiKey
print('\n Get item: ' + itemUrl)

itemData = requests.get(itemUrl)
print(itemData.json())

itemJson = requests.get(itemUrl).json()
print(json.dumps(itemJson['data']['FullText'], indent=4))

print(len(itemJson['data']['FullText'][0]['value']))
