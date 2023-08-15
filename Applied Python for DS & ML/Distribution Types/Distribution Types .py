#!/usr/bin/env python
# coding: utf-8

# In[9]:


#libraries 
import pandas as pd
import numpy as np
from numpy import random
import seaborn as sns 
import matplotlib.pyplot as plt 
import warnings
warnings.filterwarnings("ignore")

get_ipython().run_line_magic('matplotlib', 'inline')


# ### Uniform Distribution

# In[33]:


#create a list of random uniform data 
#uniform(lower bound, upper bound, size = ( rows, columns))
uniform_data = random.uniform(1, 6, size = (5,5))


# In[34]:


#type data
type(uniform_data)


# In[35]:


uniform_data


# In[36]:


#distplot
sns.distplot(uniform_data, hist = True, kde = False )
plt.show()


# In[37]:


#distplot
sns.distplot(uniform_data, hist = True, kde = True )
plt.show()


# In[39]:


#distplot with random direct
sns.distplot(random.uniform(10, 100, size = 1000), hist = True, kde = True )
plt.show()


# ### Binomial Distribution

# In[41]:


#create a list of random data from the binomial distribution 
#binomial (n = {number of trial}, p = {probability of succes}, size = N {number of scenarios executed})
binomial_data = random.binomial(n = 10, p = 0.25, size = 20)


# In[42]:


binomial_data


# In[43]:


#distplot
sns.distplot(binomial_data, hist=True, kde=True)
plt.show()


# In[44]:


#expecte value....
10*0.25


# In[45]:


#distplot with random direct
sns.distplot(random.binomial(n=100, p = 0.25, size = 1000), hist=True, kde=True)
plt.show()


# In[46]:


#distplot with random direct
sns.distplot(random.binomial(n=100, p = 0.25, size = 1000), hist=True, kde=False)
plt.show()


# In[47]:


#10 trail
sns.distplot(random.binomial(n=10, p = 0.25, size = 1000), hist=True, kde=True)
plt.show()


# In[48]:


#10 trail
sns.distplot(random.binomial(n=10, p = 0.25, size = 1000), hist=True, kde=False)
plt.show()


# In[49]:


#50 trail
sns.distplot(random.binomial(n=50, p = 0.8, size = 1000), hist=False, kde=True)
plt.show()


# In[50]:


#50 trail
sns.distplot(random.binomial(n=50, p = 0.8, size = 1000), hist=True, kde=True)
plt.show()


# ### Poisson distribution

# In[51]:


#creating a list of random data from the Poisson distribution
#poisson(lamba = {n}, size = {N})
poisson_data = random.poisson(lam = 5, size = 10)


# In[52]:


poisson_data


# In[53]:


#distplot
sns.distplot(poisson_data, hist=True, kde=True)
plt.show()


# In[58]:


#displot with random direct
sns.distplot(random.poisson(lam = 20, size = 5), hist=True, kde=True)
plt.show()


# In[60]:


#50 lam | size = 1000
sns.distplot(random.poisson(lam = 50, size = 1000), hist=True, kde=True)
plt.show()


# ### Normal Distribution

# In[61]:


url = "https://www.basketball-reference.com/leagues/NBA_2020.html"

df = pd.read_html(url, header =0)


# In[63]:


temp_df = df[3]
df_west = temp_df[~temp_df["W"].str.contains("Divsion")]
df_west1 = df_west.copy()
df_west1[['W', 'L', 'W/L%', 'GB', 'PS/G', 'PA/G', 'SRS']] = df_west1[['W', 'L', 'W/L%', 'GB', 'PS/G', 'PA/G', 'SRS']].apply(pd.to_numeric, errors = "coerce")


# In[66]:


df_west1


# In[64]:


#describe
df_west1.describe()


# In[75]:


numeric_fields = ['W', 'L', 'W/L%', 'GB', 'PS/G', 'PA/G', 'SRS']
numeric_df = df_west1[numeric_fields]


# In[76]:


#correlation
correlation = numeric_df.corr()


# In[77]:


print(correlation)


# In[79]:


df_west1.head()


# In[82]:


df_west1.iloc[:,0]


# In[83]:


df_west1.iloc[:,1]


# In[84]:


#iloc df.iloc[ : , ]
all_data = df_west1.iloc[:, 1:]


# In[85]:


#distplot
sns.distplot(all_data, hist=True, kde=True)
plt.show()


# In[86]:


df_west1.columns


# In[88]:


# call df_west1 W column
sns.distplot(df_west1["W"], hist=True, kde=True)
plt.show()


# ### Fitting Distributions - Advanced

# In[ ]:


#documentation of Scypy continuous distributions 
#https://docs.scipy.org/doc/scipy/reference/stats.html


# In[89]:


#getting some new data to look at from Seaborn
df_exercise = sns.load_dataset("exercise")


# In[90]:


df_exercise.head(10)


# In[91]:


#info
df_exercise.info()


# In[94]:


#!pip install fitter
#link : https://fitter.readthedocs.io/en/latest/


# In[97]:


#import fitter 
from fitter import Fitter 


# In[98]:


data = df_exercise["pulse"]


# In[99]:


f = Fitter(data)


# In[100]:


f.fit()


# In[101]:


f.summary()


# In[ ]:




