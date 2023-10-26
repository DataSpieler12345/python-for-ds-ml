#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="6">Sequence mining | hidden Markov model</font></b></h1></center>

# In[2]:


import pylab
import numpy as np
import pandas as pd

from hmmlearn.hmm import GaussianHMM

get_ipython().run_line_magic('matplotlib', 'inline')


# ## Read the data 

# In[3]:


df = pd.read_csv("./data/speed.csv")
df


# In[4]:


x = df.drop(["corr"], axis = 1) #deleta the column corr
x["prev"] = pd.factorize(x["prev"])[0] #convert to numeric 


# In[6]:


x


# ## Create HMM Model

# In[7]:


model1 = GaussianHMM(n_components =2, n_iter=10000, random_state=1).fit(x)
model1.monitor_


# ## Make Prediction

# In[9]:


states = model1.predict(x)
pd.Series(states).value_counts()


# ## Mean reaction time 

# In[10]:


model1.means_[:, 0]


# ## Plot

# In[11]:


fig = pylab.figure(figsize=(20, 1))
ax = fig.add_subplot(111)
ax.grid(True)
ax.set_xlabel("Record number")
ax.set_ylabel("State")
ax.plot(states)

