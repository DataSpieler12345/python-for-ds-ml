#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing Neccessary Libraries
import pandas as pd


# In[2]:


# Uploading the data with file name 'train (1).csv' using pandas
dp = pd.read_csv('data/train.csv')


# In[3]:


# We make a copy of the original dataframe.
df = dp.copy()


# In[4]:


# We see a glipmse of our dataset
df.head()


# In[5]:


# Knowing more about the data types in our data set
df.info()


# #### Identifying Data Cleaning Issues
# 
# (1) There are NaN values in Age column.
# 
# (2) We need not require columns like PassengerId, Name, Cabin and Ticket.
# 
# (3) Apart form Survived Column having values '0' and '1', Creating a new Column with Class/Categorical Status of Survival is needed mentioning 'Survived' or 'Did Not Survived'.
# 
# (4) Fare value i.e. 512.32 in the data is an outlier

# In[7]:


print('Mean Fare is', df['Fare'].mean())
print('Minimum Fare is',df['Fare'].min())
print('Maximum Fare is', df['Fare'].max())


# In[8]:


# let's see that how many unique values are there in our data set.
df['Fare'].unique()


# In[9]:


df[df['Fare'] > 300]


# In[10]:


# Second Data Cleaning Issue: we need not require columns like PassengerId, Name, Cabin and Ticket Hence we remove them.
df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis = 1)


# In[11]:


df.head()


# In[12]:


# We check our first cleaning issue is resolved or not. 
#And it is resolved. Now we do not have any NaN values in our data.
df.info()


# In[13]:


#Third : Creating a Column with Class/Categorical Status of Survival instead of Numbers

df['Survival_Status'] = df['Survived'].replace({1: 'Survived', 0: 'Did Not Survived'})


# In[14]:


# Checking our Third Cleaning Issue
df.head()


# In[15]:


# Fourth: Cleaning issue where the outlier Fare 512.32 needs to be removed from data
df = df[df['Fare'] < 512]


# In[16]:


df[df['Fare'] > 300]


# In[17]:


df


# In[18]:


#Saving the Cleaned data in csv format into our PC
df.to_csv('Titanic.csv') 


# In[19]:


# We look at first five rows in our data set
df.head()


# In[20]:


# To investigate measures of centre
df.describe()


# In[43]:


df.dtypes


# In[45]:


# Select only the relevant numeric columns
num_columns = ['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']


# In[46]:


# Let us see if there is any co-linearity or correlation amongst the variables.
corr = df[num_columns].corr()
print(corr)


# In[32]:


# Let us import our neccessary libraries for our visualisation
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import warnings
warnings.filterwarnings("ignore")

get_ipython().run_line_magic('matplotlib', 'inline')


# In[23]:


# Number of Passenger travelled in each type of Class
sb.countplot(data = df, x = 'Pclass');


# In[24]:


color_palette = sb.color_palette()[0]
sb.countplot(data = df, x = 'Pclass', color= color_palette);


# In[25]:


ordered = df['Pclass'].value_counts().index


# In[26]:


sb.countplot(data = df, y = 'Pclass', color= color_palette, order = ordered);


# In[27]:


# Histogram for Quantitative Variable 'Age'
# By default the bin size is 10

plt.hist(data = df, x = 'Age');


# In[28]:


plt.hist(data = df, x = 'Age', bins = 100);


# In[29]:


plt.hist(data = df, x = 'Age', bins = 4);


# In[30]:


Bin = np.arange(0, df['Age'].max() + 3, 3)
plt.hist(data = df, x = 'Age', bins = Bin);


# In[33]:


sb.distplot(df['Age'], kde = False, hist_kws= {'alpha' : 1}, bins = Bin);


# In[34]:


df['Embarked'].unique()


# In[35]:


# Let us try to create pie chart for Embarked variable
counts = df['Embarked'].value_counts()
plt.pie(counts, labels = counts.index,startangle= 90, counterclock= False)
plt.axis('square');


# In[36]:


# Let's plot a donut
counts = df['Embarked'].value_counts()
plt.pie(counts, labels = counts.index, startangle= 90, counterclock= False, wedgeprops = {'width' : 0.3})
plt.axis('square');


# In[37]:


#Plotting bar chart using figure
fig = plt.figure()
color_palette = sb.color_palette()[0]
ordered = df['Pclass'].value_counts().index
sb.countplot(data = df, x = 'Pclass', color= color_palette, order = ordered);


# In[38]:


#Let us use axes in our plot
fig = plt.figure()
ax = fig.add_axes([.1, .1, .8, .8])
color_palette = sb.color_palette()[0]
ordered = df['Pclass'].value_counts().index
sb.countplot(data = df, x = 'Pclass', color= color_palette, order = ordered);


# In[39]:


# let us create subplots
plt.figure(figsize=[20,5])

plt.subplot(1,4,1)
color_palette = sb.color_palette()[0]
ordered = df['Pclass'].value_counts().index
sb.countplot(data = df, x = 'Pclass', color= color_palette, order = ordered);

plt.subplot(1,4,2)
color_palette = sb.color_palette()[2]
ordered = df['Pclass'].value_counts().index
sb.countplot(data = df, x = 'Pclass', color= color_palette, order = ordered);

plt.subplot(1,4,3)
color_palette = sb.color_palette()[3]
ordered = df['Pclass'].value_counts().index
sb.countplot(data = df, x = 'Pclass', color= color_palette, order = ordered);

plt.subplot(1,4,4)
color_palette = sb.color_palette()[4]
ordered = df['Pclass'].value_counts().index
sb.countplot(data = df, x = 'Pclass', color= color_palette, order = ordered);


# In[40]:


# Lets plot two plot one without transformation and another with log transformation
plt.figure(figsize = [9, 6])

data = df['Age']
# left histogram: data plotted without scaling
plt.subplot(1, 2, 1)
bin_edges = np.arange(0, data.max()+2, 2)
plt.hist(data, bins = bin_edges)
plt.xlabel('values')

# right histogram: data plotted after logarithmic transformation
plt.subplot(1, 2, 2)
log_data = np.log10(data) # direct data transform
log_bin_edges = np.arange(0.7, log_data.max()+0.1, 0.1)
plt.hist(log_data, bins = log_bin_edges)
plt.xlabel('log(values)');


# In[ ]:




