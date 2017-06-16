**Instructor**: Schuyler Lindberg (UBC Library)

**Title**: Introduction to Harvesting API Data in Python from UBC Library's Open Collections

**Duration**: 3 hours

**Level**: beginner

**Prerequisites**: While this course is designed to be accessible to novice programmers, a basic
familiarity with Python is recommended. If you are new to Python, please take the time to review
[the free introductory lessons](https://www.codecademy.com/learn/python). A basic familiarity with Python
syntax, lists, and loops will allow you to get the most out of the course.

**Course plan**: This course is intended to cover the fundamentals for programmatically accessing and
harvesting data from open web APIs. It will provide an introduction to the key concepts required to
gather data from UBC Library's Open Collections API using Python. You will learn how to structure and
send basic GET and POST requests, and to receive and parse JSON responses.

- What is an API? A Brief Overview
- Getting Started with the Open Collections API
- Getting item data
  - A single request: Get the full text from an item
    - Make a Basic GET Request
  - Understanding JSON
  - Combining requests: Get the full text from multiple items
  - Parsing the Data
    - Term frequency with NLTK
	- Visualize results
- The Search API
  - Returning search results with a POST request
  - Using aggregates to construct advanced search queries
  - Visualize your results
- Other APIs and ‘Where To Go From Here’

**Setup requirements**: You will need a laptop with up-to-date versions of Python and Jupyter
installed. Instructions for installation can be found [here](https://jupyter.org/install.html). Please
ensure these are installed and working on your laptop in advance of the workshop.




-----

General Notes
Use Etherpad: https://oasis.sandstorm.io/grain/7BaGk5DpxNGrc5rzYj4tur/
Get a whole bunch of sticky notes (for I'm finished markers)


## Part 1: What is an API?

can anyone tell me?
    - what does it stand for?
    - what does it _mean_?
    
In a very basic sense an API is "A way for computers to ask for data over the internet."
    
Why use an API?

(API vs. Web Scraping?)
    
    
We're going to be dealing with HTTP APIs..


### Intro to UBC's Open Collections
- Brief demo of the website
- What kind of data might we get from this API?
- API Pages: Documentation
    - We welcome feedback!
- While we're here, **register for an API key!**
    


    
    
## Part 2:
Start building a script!
       
### Dependencies:
- Requests "HTTP for humans" -- http://docs.python-requests.org/en/master/
- json
    
You may need to install these if you don't have them:
    
    
    pip install requests json
    
Put them at the top of your script:

    import requests
    import json
    
    
### Set up the variables we'll need

    
    apiKey = 'ac40e6c2cb345593ed1691e0a8b601bba398e42d85f81f893c5ab709cec63c6c'
    ocUrl = 'https://open.library.ubc.ca/'
    ocApiUrl = 'https://oc-index.library.ubc.ca'
    collection = 'bcbooks'
    itemId = '1.0222552'

    
### TASK 1: GET AN ITEM
    
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
    
    
