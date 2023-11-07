#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="5">Learning how to use string accessors</font></b></h1></center>

# In[1]:


import pandas as pd


# In[2]:


operational_kpis = pd.Series(["employee satisfaction rating", "employee churn rate"])
operational_kpis


# In[3]:


#Indexing error
operational_kpis.lstrip('employee')


# In[4]:


operational_kpis[0].lstrip('employee')


# In[5]:


operational_kpis[1].lstrip('employee')


# In[6]:


pd.Series([operational_kpis[0].lstrip('employee'), operational_kpis[1].lstrip('employee')])


# In[11]:


print(operational_kpis.str)


# In[12]:


operational_kpis.str[1]


# In[13]:


operational_kpis[1]


# In[14]:


operational_kpis.str.lstrip('employee')


# #### another series

# In[15]:


test_series = pd.Series(['Text_data', 34])
test_series


# In[16]:


test_series.str.lstrip('Text_')


# In[17]:


test_series = pd.Series(['Text_data', '34'])


# In[18]:


test_series.str.lstrip('Text_')


# #### another series

# In[19]:


house_prices = pd.Series(['$400,000', '$500,000', '$600,000'])
house_prices


# In[20]:


house_prices.str.contains("$")

