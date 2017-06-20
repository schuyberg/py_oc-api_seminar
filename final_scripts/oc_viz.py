import requests, json, matplotlib, numpy
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker

apiKey = 'ac40e6c2cb345593ed1691e0a8b601bba398e42d85f81f893c5ab709cec63c6c'
searchUrl ='https://oc-index.library.ubc.ca/search?api_key='

with open('/Users/schuyler/dev/py_oc-api_seminar/request_objects/aggregate-date-subj-creator.json') as json_data:
    queryObject = json.load(json_data)


print('QUERY OBJECT')
print(json.dumps(queryObject, indent=4))

search = requests.post(searchUrl + apiKey, json=queryObject)

print('RESPONSE')
# print(json.dumps(search.json(), indent=4))

response = search.json()

date_hist = response['data']['data']['aggregations']['date_hist']['buckets']

print(json.dumps(date_hist, indent=4))

N = len(date_hist)

ind = numpy.arange(N)  # the x locations for the groups
width = 0.8       # the width of the bars

counts =  [ item['doc_count'] for item in date_hist ]
labels = [ item['key_as_string'] for item in date_hist ]


fig, ax = plt.subplots()
rects1 = ax.bar(ind, counts, width, color='r')


# add some text for labels, title and axes ticks
ax.set_ylabel('Count')
ax.set_title('Items by Date')
ax.set_xticks(ind + width)
ax.set_xticklabels(labels, fontsize=6)
fig.autofmt_xdate()

loc = plticker.MultipleLocator(base=3.0) # this locator puts ticks at regular intervals
ax.xaxis.set_major_locator(loc)


# ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))

plt.show()

