**Instructor**: Schuyler Lindberg (UBC Library)

**Title**: Introduction to Harvesting API Data in Python from UBC Library's Open Collections

**Duration**: 3 hours

**Level**: beginner

**Prerequisites**: While this course is designed to be accessible to novice programmers, a basic
familiarity with Python is recommended. If you are new to Python, please take the time to review
[the free introductory lessons](https://www.codecademy.com/learn/python). A basic familiarity with Python
syntax, lists, and loops will allow you to get the most out of the course.

**Course plan**: This course is intended to cover the fundamentals for pragmatically accessing and
harvesting data from open web APIs. It will provide an introduction to the key concepts required to
gather data from UBC Library's Open Collections API using Python. You will learn how to structure and
send basic GET and POST requests, and to receive and parse JSON responses.

- What is an API? A Brief Overview
    - Getting Started with the Open Collections API
    - Understanding JSON
- GETting item metadata
    - Get the metadata from one item (basic GET request)
    - Combining requests: Get metadata from multiple items
    - Analyzing Text with the Natural Language Toolkit
- The Search API: POSTing a search request
    - Keyword Search
    - Filtered Search
    - Aggregate Search Queries (Faceting)
    - Visualize your results (time permitting)
- Other APIs and ‘Where To Go From Here’

**Setup requirements**: 

Please note that the setup requirements for this course have changed. We will no longer be using Jupyter notebooks.

You will need a laptop with Python 3.5+ installed and a text editor you are comfortable using. 
Demonstrations will be given using PyCharm CE and this application is highly recommended to best follow along. It can be downloaded for free at https://www.jetbrains.com/pycharm/download/

We will be using the following Python libraries, it will save time to have them installed in advance:
 - requests
 - NLTK (Natural Language Toolkit)
 - matplotlib

Please arrive early if you require assistance getting set up.

-----

## General Notes ("Before We Begin") (5-10m)

I'll be doing my demonstrations using Pycharm CE. I encourage you to follow along in a text editor of your choice.

I'll be using Etherpad to share and paste code as we go through the course:
    
    https://goo.gl/wWuNDG
    
    https://oasis.sandstorm.io/shared/8Mb_7jQKR5gigdNk02wGoZ_wk3TEgIyKwKdZbFSKbBG
    
    
I'll be passing out sticky notes that you can use to show me when you're ready to move on with each task. 


## Part 1: What is an API? (15-20m)

can anyone tell me?
    - what does it stand for?
    - what does it _mean_?
    
In a very basic sense an API is "A way for computers to ask for data over the internet."
    
Why use an API?

(API vs. Web Scraping?)
    
    
We're going to be dealing with HTTP APIs..
We'll be dealing with 2 types of queries:
    GET and POST (more on that later)


### Intro to UBC's Open Collections
- Brief demo of the website
- What kind of data might we get from this API?
- API Pages: Documentation
    - We welcome feedback!
- While we're here, **register for an API key!**


### Most web APIs "speak JSON"

Try pasting the following in a browser window (2 min):

       https://oc-index.library.ubc.ca/collections/bcbooks/items/1.0222552


Look at JSON structure:
- key / value pairs
- nested data
- objects vs arrays


Opening in the browser like this works, but to manipulate the data, we'll need to make the call using a script instead.

    
    
## Part 2: GETting Item Data


### Getting Set Up (10m):

0. Create a new Python script. I'll call mine 'get_item.py'

1. Dependencies

- Requests "HTTP for humans" -- http://docs.python-requests.org/en/master/
- json
    
You may need to install these if you don't have them:
    
    
    pip install requests json
    
Put them at the top of your script:

    import requests
    import json
    
    
2. Initial Variables

    
    apiKey = 'ac40e6c2cb345593ed1691e0a8b601bba398e42d85f81f893c5ab709cec63c6c'
    ocUrl = 'https://open.library.ubc.ca/'
    ocApiUrl = 'https://oc-index.library.ubc.ca'
    collection = 'bcbooks'
    itemId = '1.0222552'

    
### TASK 1: GET AN ITEM (30m)

For this section we'll be using 'GET' queries. 

'GET' queries get the data from a specific HTTP endpoint.
Many 'GET' requests can be run directly in the browser.


1. Build the URL you'll need for your API call:


    # url to an item
    itemUrl = ocApiUrl+'/collections/'+collection+'/items/'+itemId+'?apiKey='+apiKey
    print('\n Get item: ' + itemUrl)
    
    
2. Use **requests.get()** to get the data 

    
    itemData = requests.get(itemUrl)
    print(itemData)
    
show response as text

     print(itemData.text)

show response as json

     print(itemData.json())
    
3. Print the data using **json.dumps()** to format it legibly


    itemJson = requests.get(itemUrl).json()
    print(json.dumps(itemJson, indent=4))


4. Work with the person next to you to find the length of the full text of this item (10min).

hint1:
python has a built-in length function for Strings:
    
    len('words')
    
hint2:
look at the printed data output ...
itemJson['data]['FullText'] is an array!
   
solution:

    length = len(itemJson['data']['FullText'][0]['value'])
    print(length)
    
    469897




### TASK 2: GET MULTIPLE ITEMS FROM A COLLECTION (30)

1. Create a new script for this task, and set up the variables again:
    
    
    import requests, json

    itemListUrl = ocApiUrl+'/collections/'+collection+'/items?apiKey='+apiKey
    print('\n Get items list: ' + itemListUrl)


    itemListJson = requests.get(itemListUrl).json()
    print(json.dumps(itemListJson, indent=4))

2. How many items are in this collection (5m)?


    items = itemListJson["data"]
    print(len(items))
    
    
3. Print the titles of the first 10 books (15m).

To get the titles of the first 10 items, we need to loop through the list of items in the collection, then use a new GET request to get the data for each one.


    for i in items[:10]:
        # print(item['_id'])
        itemUrl = ocApiUrl+'/collections/'+collection+'/items/'+i['_id']+'?apiKey='+apiKey
        item = requests.get(itemUrl).json()
        # print(json.dumps(item, indent=4))
        print(item['data']['Title'][0]['value'])


4. Save the full metadata of the first 10 items in a JSON file.


    metadata = []
    
    for i in items[:10]:
        # print(item['_id'])
        itemUrl = ocApiUrl+'/collections/'+collection+'/items/'+i['_id']+'?apiKey='+apiKey
        item = requests.get(itemUrl).json()
        # print(json.dumps(item, indent=4))
        # print()
        metadata.append(item['data'])
    
    with open('metadata.json', 'w') as output:
        json.dump(metadata, output)



### TASK 3: BASIC TEXT ANALYSIS WITH NLTK (30m-40m)

For this we'll be scratching the surface of the Python 'Natural Langauage Toolkit (NLTK'

If you don't have it already, you'll need to install NLTK, matplotlib, and numPy:

    pip install nltk, matplotlib, numpy
    

1. Create a new script for this one called 'analyze_text.py' and import dependencies:


    import json, re, string, nltk


3. Load our saved metadata.json file


    # load the metadata we saved
    with open('./metadata.json') as json_data:
        metadata = json.load(json_data)
    
    # print the metadata
    print(json.dumps(metadata, indent=4))


4. Extract just the FullText field to a new List.


    fullTexts = []
    for i in metadata:
        fullTexts.append(i['FullText'][0]['value'])


5. What is the total length of full text? (5m)


    print(len(''.join(fullTexts)))
    

6. Add NLTK tokenizer and stopwords


    nltk.download('punkt') # word tokenizer
    nltk.download('stopwords') # stop words
    from nltk import word_tokenize
    
    
7. Tokenize the text 

Tokenizing the text with give us a list of all the words (space-seperated strings) in the text.
    
    
    allTokens = []
    for fullText in fullTexts:
        tokenizedText = word_tokenize(fullText)
        allTokens.append(tokenizedText)
    
    print(allTokens)

... this looks pretty messy, and we're going to get some weird results


8. Clean, and THEN tokenize the text


    allTokens = []
    for fullText in fullTexts:
        # Lower case full text
        cleanFullText = fullText.lower()
        # Remove everything but words
        pattern = re.compile('[\W_]+')
        cleanFullText = pattern.sub(' ', cleanFullText)
    
        tokenizedText = word_tokenize(cleanFullText)
        allTokens.append(tokenizedText)
    
    #print
    print(allTokens)
    


9. NLTK.Text

Remove Stopwords

    stopwords = nltk.corpus.stopwords.words('English')
    print(stopwords)
    nostopwords =  [word for word in allTokens if word not in stopwords]

Make NLTK text object

    text = nltk.Text(nostopwords)
     
Collocations (words that frequently appear together)

    colos = text.collocations()
    print(colos)
    
Count

    print(text.count('inlet'))
    
Words found in similar contexts

    print(text.similar('inlet'))
    
Dispersion plot

    text.dispersion_plot(['north', 'south', 'east', 'west'])

    
10. Make a dispersion plot of words that are appear in a similar context to 'ship'.

    text.dispersion_plot(['ship', 'dock', 'boat', 'canoe', 'steamboat'])


This doesn't tell us that much now, because we're looking at the text of all the books,
but if we sorted them by date first..

      sortedItemsData = sorted(metadata, key=lambda x: x['DateIssued'][0]['value'])
        
etc. etc. (probably won't have time)


11. Frequency Distributions


    from nltk import FreqDist
    fdist = FreqDist(text)
    
    fdist.hapaxes() # words that occur only once
    
    print(fdist.most_common(50)) # most common
    
    fdist.max() # most frequent word
    
    fdist.plot(30) # create graph
    
    


## Break! (15m)


## PART 3: SEARCH QUERIES

Search queries in Open Collections are made by sending a JSON object _to_ the server using an HTTP Post request.
This means we'll be building and submitting a JSON object to the server (instead of a string), and then getting a different on in return.

For this section, I've prepared some example json objects to use that can be found in the request_objects directory of the git repository.


### TASK 1: Keyword Search (20m)

1. Set up a new python script with requests and json

    import requests, json

2. Use Open Collections Query Builder to set up query parameters:

Copy your apiKey variable from our previous scripts.

Check out https://open.library.ubc.ca/research for the other elements we'll need

Copy the Search URL to a new variable 'searchUrl'

    searchUrl ='https://oc-index.library.ubc.ca/search?api_key='

Enter a search term and the JSON is generated for you:
    
    
    {
      "from": 0,
      "size": 10,
      "body": {
        "sort": {
          "_score": {
            "order": "desc"
          }
        },
        "fields": [
          "creator",
          "description",
          "subject",
          "title"
        ],
        "query": {
          "query_string": {
            "query": "frogs"
          }
        }
      },
      "index": "oc",
      "type": "object"
    }
    

We could copy this directly into our code, but a good script is reusable, so we're going to save it as JSON and then load it into our script so that we can use the same code for different JSON query objects.
    
Create a new file called 'search-request.json', and copy the code there.

3. Import 'search-request.json' into your Python script:

Just like we did when loading our metadata.json file to analyze:

    with open('./search-request.json') as json_data:
        queryObject = json.load(json_data)
        

3. Use 'requests' to create a POST query to search using the query object


    search = requests.post(searchUrl + apiKey, json=queryObject)

    print(json.dumps(search.json(), indent=4))
    
    
4. How many hits are there for the search term "gold rush"? What is the max score*?

hint: Modify 'query_string' -> 'query' to change your search terms.

*max score is the relevancy rating assigned by ElasticSearch

5. How would you to return the next 10 results? Additional metadata fields? Try it. (10m)


    {
      "from": 10,
      "size": 10,
      "body": {
        "sort": {
          "_score": {
            "order": "desc"
          }
        },
        "fields": [
          "creator",
          "description",
          "subject",
          "title"
        ],
        "query": {
          "query_string": {
            "query": "gold rush"
          }
        }
      },
      "index": "oc",
      "type": "object"
    }


### TASK 2: Filtered Search (skip if low on time)

#### a) Filter by collection (index)

Filtering by a collection is accomplished by changing the 'index' in Open Collections.

1. Open up the 'collection-search.json' file. Can anyone tell me what collection this is searching?


     {
      "from": 0,
      "size": 10,
      "body": {
        "sort": {
          "_score": {
            "order": "desc"
          }
        },
        "fields": [
          "creator",
          "description",
          "subject",
          "title"
        ],
        "query": {
          "query_string": {
            "query": "gold rush"
          }
        }
      },
      "index": "bcbooks",
      "type": "object"
    }


2. Update your search script to point to 'filtered-search.json.' Try changing the JSON file to search a different collection.

There is a list of collection names and the corresponding index names at https://open.library.ubc.ca/docs

You can include multiple (comma seprated) indices in a query!


3. How many results do you see for 'gold rush' in the 'Newspapers - Cascade Record' Collection?



#### b) Filter by metadata (filter_query)


We can use a 'filtered' query to limit our query to specific metadata matches.

See: https://www.elastic.co/guide/en/elasticsearch/reference/2.3/query-dsl-filtered-query.html


1. Open up the filtered-search.json file. Can you spot what metadata is being filtered here?

    
    {
      "from": 0,
      "size": 10,
      "body": {
        "sort": {
          "_score": {
            "order": "desc"
          }
        },
        "fields": [
          "creator",
          "description",
          "subject",
          "title"
        ],
        "query": {
            "filtered": {
                "query": {
                    "query_string": {
                        "default_operator": "AND",
                        "query": "gold"
                    }
                },
                "filter": {
                  "bool": {
                    "must": [
                      {
                        "terms": {
                          "genre.raw": [
                            "Report"
                          ],
                          "execution": "and"
                        }
                      },
                      {
                        "range": {
                          "ubc.date.sort": {
                            "gte": -755828599190,
                            "lte": 396718367610
                          }
                        }
                      }
                    ]
                  }
                }
            }
        }
      },
      "index": "oc",
      "type": "object"
    }
    
    
2. Update your search script to point to 'filtered-search.json' and check the results. 

3. Can you modify this query to limit to items with the subject 'Rowing'? How many are there?

    

### TASK 3: Aggregate Queries

Elasticsearch has another interesting type of query that I'd like to introduce you to. "Aggregate Queries"

Instead of search results, aggregate queries that return specific sets of metadata for given query parameters. 
They can be used to build features like facets or visualizations, and can be nested to provide data on a specific subset of results.

For these examples, I'm going to limit my queries to the MacMillan Bloedel Limited fonds collection.

I'll be using some prepared query strings from my github account at https://github.com/schuyberg/pixelating_queries/


#### a) Subject query (term)

1. Open aggregate-creator.json. Discuss with your neighbor: What differences do you notice? What do you expect this to return?


2. Point your search script at aggregate-creator.json and see if the results match your expectations.

#### b) Date query (date_range)

1. Open aggregate-date.json. Discuss with your neighbor: What differences do you notice? What do you expect this to return?

2. Point your search script at aggregate-creator.json and see if the results match your expectations.


#### c) Nested query

This is where it gets cool..

1. Open aggregate-date-subj-creator.json and see if you can guess what the data structure it returns will look like.

.. anyone want to hazard a guess?

2. Point your search script at aggregate-date-subj-creator.json and see if the results match your expectations.

Notice that for each year, you have a set of corresponding subject and creator terms. These are the matches for items on that year. This is perfect for creating visualizations..


#### d) Visualizations (?)

Check out oc-viz for an an example of a visualization using aggregation queries and matplotlib.

Can you modify this to show data from just one subject?

(can you fix my x-axis label positoning?)

