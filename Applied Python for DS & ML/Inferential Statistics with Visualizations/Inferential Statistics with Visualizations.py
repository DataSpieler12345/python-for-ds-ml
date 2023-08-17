#!/usr/bin/env python
# coding: utf-8

# ### Inferential Statistics with Visualizations

# In[64]:


#common imports 
import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
import scipy.stats as stats
get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings("ignore")

#set color style
sns.set(color_codes = True)


# #### Load the data sets

# In[65]:


df_titanic = sns.load_dataset("titanic")
df_iris = sns.load_dataset("iris")
df_tips = sns.load_dataset("tips")


# ### Titanic dataset
# 
# * Ideal for data visualization 

# #### seaborn catplot documentation
# #### link : https://seaborn.pydata.org/generated/seaborn.catplot.html

# In[3]:


df_titanic.info()


# In[5]:


df_titanic.head(10)


# #### Bar Charts

# In[9]:


#seaborn catplot
sns.catplot(x = "sex", data = df_titanic, kind = "count")
plt.show()


# In[11]:


#seaborn catplot
sns.catplot(x = "pclass", data = df_titanic, kind = "count")
plt.show()


# In[12]:


sns.catplot(x = "pclass", data = df_titanic, kind = "count", hue = "sex")
plt.show()


# In[13]:


sns.catplot(x = "pclass", data = df_titanic, kind = "count", col = "sex")
plt.show()


# In[18]:


sns.catplot(x="pclass", data=df_titanic, kind="count", col="sex", hue="embarked")
plt.show()


# #### Box Plots

# In[33]:


df_titanic.head()


# In[34]:


sns.boxplot(x = df_titanic["age"])
plt.show()


# In[35]:


sns.boxplot(y = df_titanic["age"])
plt.show()


# In[36]:


sns.boxplot(x =df_titanic["age"], y = df_titanic["sex"])
plt.show()


# ### Iris dataset
# 
# * for scatterplot

# In[4]:


df_iris.info()


# In[19]:


df_iris.head(5)


# #### seaborn distplot documentation
# #### link : https://seaborn.pydata.org/generated/seaborn.distplot.html

# #### Histogram

# In[20]:


df_iris["species"].value_counts()


# In[22]:


sns.distplot(df_iris["sepal_length"], hist = True, kde = True)
plt.show()


# In[23]:


sns.distplot(df_iris["sepal_length"], hist = True, kde = True, bins = 20)
plt.show()


# In[24]:


sns.distplot(df_iris["sepal_length"], hist = True, kde = True, rug = True)
plt.show()


# In[25]:


sns.distplot(df_iris["sepal_length"], hist = True, kde = True, bins = 20)
sns.distplot(df_iris["sepal_width"], hist = True, kde = True, bins = 20)
plt.show()


# In[32]:


sns.distplot(df_iris["sepal_length"], hist = False, kde = True, bins = 20, color = "blue", label = "Sepal Length")
sns.distplot(df_iris["sepal_width"], hist = False, kde = True, bins = 20, color = "red", label = "Sepal Width")
plt.legend()
plt.xlabel("Measure in CM")
plt.ylabel("Frequency")
plt.title("Sepal Characteristics", size = 15)
plt.show()


# In[31]:


sns.distplot(df_iris["sepal_length"], hist = True, kde = False, bins = 20, color = "blue", label = "Sepal Length")
sns.distplot(df_iris["sepal_width"], hist = True, kde = False, bins = 20, color = "red", label = "Sepal Width")
plt.legend()
plt.xlabel("Measure in CM")
plt.ylabel("Frequency")
plt.title("Sepal Characteristics", size = 15)
plt.show()


# #### Box Plots

# In[38]:


df_iris["species"].value_counts()


# In[40]:


sns.boxplot(x = df_iris["species"], y = df_iris["sepal_width"])
plt.show()


# In[41]:


#from numpy import random
from numpy import random


# In[47]:


#Normal distribution
normal_data = random.normal(loc = 100, scale = 10, size = 1000)


# In[48]:


normal_data


# In[49]:


sns.boxplot(x = normal_data)


# #### Scatter Plots

# In[50]:


df_iris.info()


# In[51]:


sns.regplot(x = "sepal_length", y = "sepal_width", data = df_iris)
plt.show()


# In[53]:


#correlation
numeric_columns = df_iris.select_dtypes(include=['float64'])
correlation_matrix = numeric_columns.corr()
print(correlation_matrix)


# In[59]:


sns.regplot(x = "petal_length", y = "petal_width", data = df_iris)
plt.show()


# In[61]:


sns.regplot(x = "petal_length", y = "petal_width", data = df_iris,
           scatter_kws = {"color":"black"}, line_kws = {"color":"red"})
plt.show()


# In[62]:


sns.regplot(x = "petal_length", y = "petal_width", data = df_iris, fit_reg = False,
           scatter_kws = {"color":"black"}, line_kws = {"color":"red"})
plt.show()


# In[63]:


sns.regplot(x = "petal_length", y = "petal_width", data = df_iris, ci = 90,
           scatter_kws = {"color":"black"}, line_kws = {"color":"red"})
plt.show()


# ### Advanced Visualizations

# #### seaborn lmplot documentation
# #### link : https://seaborn.pydata.org/generated/seaborn.lmplot.html

# In[66]:


df_tips.info()


# In[67]:


df_tips


# In[69]:


num_columns = df_tips.select_dtypes(include=['float64', 'int64'])
corr_matrix = num_columns.corr()
print(corr_matrix)


# In[72]:


sns.lmplot(x = "total_bill", y = "tip", data = df_tips)
plt.show()


# In[74]:


# difference?
sns.regplot(x = "total_bill", y = "tip", data = df_tips)
plt.show()


# In[75]:


sns.lmplot(x = "total_bill", y = "tip", data = df_tips, hue = "sex")
plt.show()


# In[76]:


sns.lmplot(x = "total_bill", y = "tip", data = df_tips, hue = "sex",
          markers = ["x","o"])
plt.show()


# In[77]:


sns.lmplot(x = "total_bill", y = "tip", data = df_tips, hue = "sex",
          markers = ["x","o"], palette = ["red","black"])
plt.show()


# In[79]:


df_tips["time"].value_counts()


# In[78]:


sns.lmplot(x = "total_bill", y = "tip", data = df_tips, hue = "time",
          markers = ["x","o"], palette = ["red","black"])
plt.show()


# In[80]:


df_tips["day"].value_counts()


# In[82]:


sns.lmplot(x = "total_bill", y = "tip", data = df_tips, hue = "day")
plt.show()


# In[83]:


sns.lmplot(x = "total_bill", y = "tip", data = df_tips, hue = "sex",
          markers = ["*","o"], palette = ["red","black"])
plt.show()


# In[86]:


sns.lmplot(x = "total_bill", y = "tip", data = df_tips, hue = "sex", col = "smoker",
          markers = ["*","o"], palette = ["red","black"])
plt.show()


# In[87]:


sns.lmplot(x = "total_bill", y = "tip", data = df_tips, hue = "sex", col = "smoker", row = "time",
          markers = ["*","o"], palette = ["red","black"])
plt.show()


# #### seaborn Jointplot documentation
# #### link : https://seaborn.pydata.org/generated/seaborn.jointplot.html

# In[88]:


sns.jointplot(x = "total_bill", y = "tip", data = df_tips, kind = "reg")
plt.show()


# In[89]:


sns.jointplot(x = "total_bill", y = "tip", data = df_tips, kind = "kde")
plt.show()


# In[90]:


num_columns = df_tips.select_dtypes(include=['float64', 'int64'])
corr_matrix = num_columns.corr()
print(corr_matrix)


# In[92]:


sns.jointplot(x="total_bill", y="tip", data=df_tips, kind="reg")
plt.annotate("Pearsonr = {:.2f}".format(stats.pearsonr(df_tips["total_bill"], df_tips["tip"])[0]),
             xy=(0.5, 0.9), xycoords='axes fraction', fontsize=12)
plt.show()

