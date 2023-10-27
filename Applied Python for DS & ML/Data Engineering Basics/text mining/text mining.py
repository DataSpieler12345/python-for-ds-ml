#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="6">Text Mining</font></b></h1></center>

# ### Imports

# In[6]:


import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import wordcloud

import warnings

# Ignore warnings
warnings.filterwarnings("ignore")


# ### Location of the data 

# In[4]:


book = r'./data/jane-austen-pride-prejudice.txt'


# ### Donwload stopwords list from nltk 

# In[ ]:


nltk.download('stopwords')


# ### Read the file and store as string 

# In[9]:


with open(book, 'r') as f:
    text = f.read()
text


# ### Convert string to tokens / words

# In[10]:


words = word_tokenize(text)
words


# ### Remove stop words

# cast to set for fast loop. Added custom words

# In[11]:


stop_words = set(stopwords.words('english')+["would","could"])
clean_words = [w for w in words if not w in stop_words]
clean_words


# In[13]:


frequency_distribution = nltk.FreqDist(w.lower() for w in clean_words)


# In[14]:


words_freq = dict([(x, y) for x, y in frequency_distribution.items() if len(x) > 3])
words_freq


# In[20]:


from wordcloud import WordCloud

# Your code here
wcloud = WordCloud().generate_from_frequencies(words_freq)


# In[21]:


plt.figure(figsize=[12,12])
plt.imshow(wcloud, interpolation="bilinear")

plt.axis("off")
plt.show()

