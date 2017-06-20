
import json, math, re, string, nltk

# load the metadata we saved
with open('./metadata.json') as json_data:
    metadata = json.load(json_data)

# print the metadata
print(json.dumps(metadata, indent=4))

#
fullTexts = []
for item in metadata:
    fullTexts.append(item['FullText'][0]['value'])

# get total length of full texts
print(len(''.join(fullTexts)))


# let's get started with NLTK analysis

nltk.download('punkt') # word tokenizer
nltk.download('stopwords') # stop words
from nltk import word_tokenize


# Tokenize the text (get individual 'words')

# allTokens = []
# for fullText in fullTexts:
#     tokenizedText = word_tokenize(fullText)
#     allTokens += tokenizedText
#
# #print
# print(allTokens)

# clean the text before tokenizing to get better results

allTokens = []
for fullText in fullTexts:
    # Lower case full text
    cleanFullText = fullText.lower()
    # Remove everything but words
    pattern = re.compile('[\W_]+') # (using regular expressions, remove non-word characters)
    cleanFullText = pattern.sub(' ', cleanFullText)
    tokenizedText = word_tokenize(cleanFullText)
    allTokens += tokenizedText

# print
print(allTokens)

# total words
print('all words ' + str(len(allTokens)))

# total unique words
print('all unique ' + str(len(set(allTokens))))


# Remove stopwords
stopwords = nltk.corpus.stopwords.words('English')

print(stopwords)

nostopwords =  [word for word in allTokens if word not in stopwords]

# NLTK.Text
text = nltk.Text(nostopwords)

# Collocations (words that frequently appear together)
colos = text.collocations()
print(colos)

# count
print(text.count('inlet'))

# words in similar contexts
print(text.similar('ship'))


text.dispersion_plot(['north', 'south', 'east', 'west'])


text.dispersion_plot(['ship', 'dock', 'boat', 'canoe', 'steamboat'])


# Frequency distributions!

from nltk import FreqDist
fdist = FreqDist(text)

print(fdist.hapaxes()) # words that occur only once

print(fdist.most_common(50))

fdist.plot(30)