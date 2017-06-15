import requests
import json

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

itemJson = requests.get(itemUrl).json()
print(json.dumps(itemJson, indent=4))



#GET LIST OF ITEMS
# url to a list of items in a collection
itemListUrl = ocApiUrl+'/collections/'+collection+'/items?apiKey='+apiKey
print('\n Get items list: ' + itemListUrl)


itemListJson = requests.get(itemListUrl).json()
print(json.dumps(itemListJson, indent=4))

# task 2: How many items are in this collection?
print(len(itemListJson["data"]))