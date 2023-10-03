#!/usr/bin/env python
# coding: utf-8

# ## Using Seaborn

# In[8]:


import pandas as pd

import warnings
warnings.filterwarnings("ignore")


# In[4]:


df = pd.read_csv('data/Advertising.csv')
df.head()


# In[6]:


#remove unwanted column
adsdata = df[['TV', 'Radio','Newspaper','Sales']]
adsdata


# In[9]:


import seaborn as sns
sns.pairplot(adsdata)


# In[11]:


adsdata_features = df[['TV', 'Radio','Newspaper']]
sns.pairplot(adsdata_features)


# ### Using pandas.plotting module

# In[13]:


import pandas.plotting as pd
plot = pd.scatter_matrix(adsdata_features)

