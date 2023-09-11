#!/usr/bin/env python
# coding: utf-8

# ### Data Loading & Exploration

# #### Libraries 

# In[123]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns 

get_ipython().run_line_magic('matplotlib', 'inline')

import nltk
nltk.download("all", quiet=True)


import warnings
warnings.filterwarnings("ignore")   


# #### Link data: https://www.gutenberg.org

# #### Link data: https://www.gutenberg.org/files/43/43-h/43-h.htm

# In[2]:


url = "https://www.gutenberg.org/files/43/43-h/43-h.htm"


# In[3]:


req = requests.get(url)


# In[4]:


type(req)


# In[10]:


#html is in..
html = req.text


# In[13]:


soup = BeautifulSoup(html, "html.parser")


# In[14]:


type(soup)


# In[15]:


#get the titlte
soup.title


# In[22]:


soup.title.string


# In[24]:


# Find all the <a> tags in the HTML
links = soup.find_all('a')

# Iterate over the extracted links and print their text and href attributes
for link in links:
    print("Text:", link.text)
    print("Href:", link.get('href'))


# In[25]:


text = soup.get_text()


# In[27]:


print(text)


# ### NLTK to Examine Text 

# In[28]:


tokenizer = nltk.tokenize.RegexpTokenizer("\w+")


# In[29]:


tokens = tokenizer.tokenize(text)


# In[33]:


tokens[0:16]


# In[34]:


len(tokens)


# In[36]:


### for loops
words = []


# In[38]:


for word in tokens:
    words.append(word.lower())


# In[39]:


words[0:16]


# In[40]:


sw = nltk.corpus.stopwords.words("english")


# In[41]:


type(sw)


# In[44]:


sw[:9]


# In[43]:


len(sw)


# In[45]:


words2 = []


# In[46]:


for word in words:
    if word not in sw:
        words2.append(word)


# In[47]:


words2[:7]


# In[48]:


sns.set(color_codes=True)
freqDist = nltk.FreqDist(words2)
freqDist.plot(20)


# ### For Loop Creation of 8.2

# In[49]:


def plot_words(url):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    tokenizer = nltk.tokenize.RegexpTokenizer("\w+")
    tokens = tokenizer.tokenize(text)
    words = []
    for word in tokens:
        words.append(word.lower())
    sw =  nltk.corpus.stopwords.words("english")
    words2 = []
    for word in words:
        if word not in sw:
            words2.append(word)
    freqDist = nltk.FreqDist(words2)
    freqDist.plot(20)


# In[50]:


#book: a Tale of two cities
plot_words("https://www.gutenberg.org/files/98/98-h/98-h.htm")


# In[51]:


#book: Alice in Wonderland
plot_words("https://www.gutenberg.org/files/11/11-h/11-h.htm")


# ### Movie Reviews Text Analysis & Frequency

# In[54]:


import random


# In[55]:


documents = [(list(nltk.corpus.movie_reviews.words(fileid)), category)
            	for category in nltk.corpus.movie_reviews.categories()
            	for fileid in nltk.corpus.movie_reviews.fileids(category)]


# In[56]:


random.shuffle(documents)


# In[58]:


print(documents[0])


# In[59]:


all_words = []


# In[60]:


for w in nltk.corpus.movie_reviews.words():
    all_words.append(w.lower())


# In[61]:


#freq distribution
all_words = nltk.FreqDist(all_words)


# In[63]:


all_words


# In[64]:


#most common words
print(all_words.most_common(10))


# In[65]:


# search of individual...
print(all_words["bad"])


# In[67]:


print(all_words["good"])


# ### Finding Features of Textual Data 

# In[69]:


word_feats = list(all_words.keys())[:2500]


# In[74]:


def find_feats(document):
    words = set(document)
    feats = {}
    for w in word_feats:
        feats[w] = (w in words)
        
    return feats


# In[75]:


#build the set of features
feat_set = [(find_feats(rev), category) for (rev, category) in documents]


# In[76]:


type(feat_set)


# In[79]:


len(feat_set)


# ### Naive Bayes with NLTK

# In[80]:


0.75 *2000


# In[81]:


trainer = feat_set[:1500]

tester = feat_set[1500:]


# In[82]:


#classifier 
classifier = nltk.NaiveBayesClassifier.train(trainer)


# In[83]:


#accuracy
print("Accuracy of Classifier Percentage:", (nltk.classify.accuracy(classifier, tester))*100)


# In[84]:


#most informative features
classifier.show_most_informative_features(20)


# ### Cosine Similarity Between Texts

# In[85]:


#Jekyll Hyde 
url1 = "https://www.gutenberg.org/files/43/43-h/43-h.htm"

#Treasure Island
url2 = "https://www.gutenberg.org/files/120/120-h/120-h.htm"

#Dracula
url3 = "https://www.gutenberg.org/files/345/345-h/345-h.htm"

#Two Cities
url4 = "https://www.gutenberg.org/files/98/98-h/98-h.htm"


# In[98]:


import string 

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# In[99]:


def clean_word_list(url):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    tokenizer = LemNormalize
    tokens = tokenizer(text)
    words = []
    for word in tokens:
        words.append(word)
    return words


# In[100]:


#Jekyll Hyde 
clean1 = clean_word_list(url1)

#Treasure Island
clean2 = clean_word_list(url2)

#Dracula
clean3 = clean_word_list(url3)

#Two Cities
clean4 = clean_word_list(url4)


# In[101]:


type(clean1)


# In[102]:


clean1[:10]


# In[103]:


#list to string 
def list_to_string(orig_list, seperator=' '):
    return seperator.join(orig_list)


# In[104]:


#Jekyll Hyde 
string1 = list_to_string(clean1)

#Treasure Island
string2 = list_to_string(clean2)

#Dracula
string3 = list_to_string(clean3)

#Two Cities
string4 = list_to_string(clean4)


# In[105]:


type(string1)


# In[106]:


string1[:10]


# In[112]:


#doc lib or list of strings
doc_lib = [string1, string2, string3, string4]


# #### TfidfVectorizer

# In[113]:


#feature extraction
from sklearn.feature_extraction.text import TfidfVectorizer


# In[117]:


TfidfVec = TfidfVectorizer(tokenizer = LemNormalize, stop_words="english")


# In[118]:


def   cos_similarity(textlist):
       tfidf = TfidfVec.fit_transform(textlist)
       return ( tfidf * tfidf.T).toarray()


# In[119]:


stored = cos_similarity(doc_lib)


# In[120]:


stored


# In[ ]:


#Jekyll Hyde 


#Treasure Island


#Dracula


#Two Cities


# In[121]:


names = ["Jekill","Treasure","Dracula","Two Cities"]


# In[124]:


visual = pd.DataFrame(stored, index = names, columns = names)


# In[125]:


print("Cosine Similarity Matrix")
visual

