#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="6">Groceries Association Rule 
#     (Apriori-Algorithm)</font></b></h1></center>

# ![](basket.png)

# ## Imports

# In[58]:


import pandas as pd
import numpy as np
import plotly.express as px
from mlxtend.preprocessing import TransactionEncoder
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud


import warnings
warnings.filterwarnings("ignore")


# ## Load the data

# In[3]:


data = pd.read_csv("./data/Groceries_dataset.csv")
data


# In[4]:


data.shape


# The dataset has **38765 rows** of the purchase orders of people from the grocery stores. These orders can be analysed and association rules can be generated using **Market Basket Analysis** by algorithms like **Apriori Algorithm**.

# In[5]:


data.head()


# ## group the data 

# In[6]:


data.groupby(['Date'])['itemDescription'].agg(['count']).plot(figsize=(12,5), grid=True, title="Total Number of Items Sold by Date").set(xlabel="Date", ylabel="Total Number of Items Sold")


# ## Set date as index

# In[7]:


d=data.set_index(['Date'])


# In[8]:


d


# In[11]:


d.index=pd.to_datetime(d.index)


# In[14]:


total_items = len(d)
total_days = len(np.unique(d.index.date))
total_months = len(np.unique(d.index.month))
average_items = total_items / total_days
unique_items = d.itemDescription.unique().size

print("There are {} unique items sold ".format(unique_items))
print("Total {} items sold in {} days throughout {} months".format(total_items, total_days, total_months))
print("With an average of {} items sold daily".format(average_items))


# In[15]:


d.resample("D")['itemDescription'].count().plot(figsize=(12,5), grid=True, title="Total Number of Items Sold by Date").set(xlabel="Date", ylabel="Total Number of Items Sold")


# In[16]:


d.resample("M")['itemDescription'].count().plot(figsize=(12,5), grid=True, title="Total Number by Items Sold by Month").set(xlabel="Date", ylabel="Total Number of Items Sold")


# In[17]:


d["Hour"] = d.index.hour
d["Weekday"] = d.index.weekday + 1

d.head(10)


# In[18]:


data['itemDescription'].value_counts()


# In[19]:


data['Date'].nunique()


# In[22]:


def bar_plot(df,col):

    fig = px.bar(df,
        x = df[col].value_counts().keys(), 
        y = df[col].value_counts().values,
        color= df[col].value_counts().keys()
    )
    fig.update_layout(
    xaxis_title= col,
    yaxis_title="Count",
    legend_title=col,
    font_family="Courier New",
    font_color="blue",
    title_font_family="Times New Roman",
    title_font_color="red",
    legend_title_font_color="green"
)
    
    fig.show()


# In[24]:


bar_plot(data,'itemDescription')


# In[25]:


df=data.groupby(['Member_number','Date'])['itemDescription'].apply(sum)


# In[26]:


df


# In[41]:


array = df.values
array


# In[42]:


pd.set_option('display.max_colwidth', None)


# In[43]:


transactions = [a[1]['itemDescription'].tolist() for a in list(data.groupby(['Member_number','Date']))]


# In[37]:


transactions


# In[45]:


te = TransactionEncoder()


# In[46]:


array = te.fit(transactions).transform(transactions)


# In[47]:


te.columns_


# In[48]:


array


# In[49]:


transactions = pd.DataFrame(array, columns=te.columns_)
pf = transactions.describe()


# In[50]:


pf


# In[51]:


pf.iloc[0]-pf.iloc[3]


# In[52]:


f = pf.iloc[0]-pf.iloc[3]
a = f.tolist()
b = list(f.index)
item = pd.DataFrame([[a[r],b[r]]for r in range(len(a))], columns=['Count','Item'])
item = item.sort_values(['Count'], ascending=False).head(50)


# In[53]:


c_transactions = transactions.copy()
c_transactions.replace(False, '', inplace=True)
c_transactions.replace(True, 1, inplace=True)

c_transactions.rename(columns=lambda x: x.title(), inplace=True)
transactions.rename(columns=lambda x: x.title(), inplace=True)


# In[54]:


c_transactions.head()
# transactions.head()


# In[55]:


transactions.to_csv('groceries_heeral.csv', index=False)
c_transactions.to_csv('groceries_heeral_2.csv', index=False)


# In[56]:


item


# In[59]:


plt.rcParams['figure.figsize'] = (15, 15)
wordcloud = WordCloud(background_color = 'white', width = 1200,  height = 1200, max_words = 121).generate(str(item['Item']))
plt.imshow(wordcloud)
plt.axis('off')
plt.title('Items',fontsize = 20)
plt.show()

