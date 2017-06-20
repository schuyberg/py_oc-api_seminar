import requests, json

ocUrl = 'https://open.library.ubc.ca/'
ocApiUrl = 'https://oc-index.library.ubc.ca'

apiKey = 'ac40e6c2cb345593ed1691e0a8b601bba398e42d85f81f893c5ab709cec63c6c'

collection = 'bcbooks'


# GET LIST OF ITEMS
#
# url to a list of items in a collection
itemListUrl = ocApiUrl+'/collections/'+collection+'/items?apiKey='+apiKey
print('\n Get items list: ' + itemListUrl)


itemListJson = requests.get(itemListUrl).json()
print(json.dumps(itemListJson, indent=4))

# how many items are there?
items = itemListJson["data"]
print(len(items))


# print the titles of the first 10 books

for i in items[:10]:
    # print(item['_id'])
    itemUrl = ocApiUrl+'/collections/'+collection+'/items/'+i['_id']+'?apiKey='+apiKey
    item = requests.get(itemUrl).json()
    # print(json.dumps(item, indent=4))
    print(item['data']['Title'][0]['value'])


# save the metadata from the first 10 items as json

metadata = []

for i in items[:10]:
    # print(item['_id'])
    itemUrl = ocApiUrl+'/collections/'+collection+'/items/'+i['_id']+'?apiKey='+apiKey
    item = requests.get(itemUrl).json()
    # print(json.dumps(item, indent=4))
    # print()
    metadata.append(item['data'])

# write metadata to file

with open('metadata.json', 'w') as output:
    json.dump(metadata, output)