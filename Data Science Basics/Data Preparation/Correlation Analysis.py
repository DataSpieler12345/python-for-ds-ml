#!/usr/bin/env python
# coding: utf-8

# ## Correlation Analysis 

# In[5]:


import pandas as pd
import numpy as np


# In[2]:


#Create a dictionary
data = {'name':['jack', 'mason','tanya','jim','amelia'],
       'tenure': [42,52,36,24,73],
       'employees': [4,24,31,2,3 ],
       'inventory': [25,94,57,62,70]}

df = pd.DataFrame(data, columns = ['name','tenure','employees','inventory'])
df


# In[10]:


df = pd.DataFrame(data, columns=['name', 'tenure', 'employees', 'inventory'])

# Select only numeric columns
numeric_columns = df.select_dtypes(include=np.number).columns

# Calculate correlation matrix
correlation_matrix = df[numeric_columns].corr()

print(correlation_matrix)


# In[13]:


# Select only numeric columns
numeric_columns = df.select_dtypes(include=np.number).columns


# In[14]:


# Exclude non-numeric columns
numeric_df = df[numeric_columns]


# In[15]:


# Calculate correlation using Pearson method
pearson_corr = numeric_df.corr(method='pearson')
print("Pearson Correlation:")
print(pearson_corr)
print()


# In[16]:


# Calculate correlation using Kendall method
kendall_corr = numeric_df.corr(method='kendall')
print("Kendall Correlation:")
print(kendall_corr)
print()


# In[17]:


# Calculate correlation using Spearman method
spearman_corr = numeric_df.corr(method='spearman')
print("Spearman Correlation:")
print(spearman_corr)


# In[ ]:




