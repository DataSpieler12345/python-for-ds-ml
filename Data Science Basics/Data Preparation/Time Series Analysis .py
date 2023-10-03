#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()


# ### data

# In[35]:


df = pd.read_csv('data/data.csv', skiprows=1)
df.head()


# In[36]:


df.info()


# ### Wrangle Your Data

# In[37]:


df.columns = ['month', 'diet', 'gym', 'finance']
df.head()


# #### turn the 'month' column into a DateTime data type and make it the index of the DataFrame.
# 
# 

# In[38]:


df.month = pd.to_datetime(df.month)
df.set_index('month', inplace=True)
df.head()


# #### Exploratory Data Analysis (EDA)

# In[39]:


#specifi
df.plot(figsize=(20,10), linewidth=5, fontsize=20)
plt.xlabel('Year', fontsize=20);


# ## Trends and Seasonality in Time Series Data

# In[40]:


#taking a rolling average diat column
diet = df[['diet']]
diet.rolling(12).mean().plot(figsize=(20,10), linewidth=5, fontsize=20)
plt.xlabel('Year', fontsize=20);


# In[41]:


#taking a rolling average gym  column
gym = df[['gym']]
gym.rolling(12).mean().plot(figsize=(20,10), linewidth=5, fontsize=20)
plt.xlabel('Year', fontsize=20);


# In[42]:


# plotting the trends of 'gym' and 'diet' on a single figure
df_rm = pd.concat([diet.rolling(12).mean(), gym.rolling(12).mean()], axis=1)
df_rm.plot(figsize=(20,10), linewidth=5, fontsize=20)
plt.xlabel('Year', fontsize=20);

