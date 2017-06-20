import requests, json

apiKey = 'ac40e6c2cb345593ed1691e0a8b601bba398e42d85f81f893c5ab709cec63c6c'
searchUrl ='https://oc-index.library.ubc.ca/search?api_key='

with open('./request_objects/aggregate-date-subj-creator.json') as json_data:
    queryObject = json.load(json_data)


print('QUERY OBJECT')
print(json.dumps(queryObject, indent=4))

search = requests.post(searchUrl + apiKey, json=queryObject)

print('RESPONSE')
print(json.dumps(search.json(), indent=4))