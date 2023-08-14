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

# In[6]:


print('Mean Fare is', df['Fare'].mean())
print('Minimum Fare is',df['Fare'].min())
print('Maximum Fare is', df['Fare'].max())


# In[7]:


# let's see that how many unique values are there in our data set.
df['Fare'].unique()


# In[8]:


df[df['Fare'] > 300]


# In[9]:


# Second Data Cleaning Issue: we need not require columns like PassengerId, Name, Cabin and Ticket Hence we remove them.
df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis = 1)


# In[10]:


df.head()


# In[11]:


# We check our first cleaning issue is resolved or not. 
#And it is resolved. Now we do not have any NaN values in our data.
df.info()


# In[12]:


#Third : Creating a Column with Class/Categorical Status of Survival instead of Numbers

df['Survival_Status'] = df['Survived'].replace({1: 'Survived', 0: 'Did Not Survived'})


# In[13]:


# Checking our Third Cleaning Issue
df.head()


# In[14]:


# Fourth: Cleaning issue where the outlier Fare 512.32 needs to be removed from data
df = df[df['Fare'] < 512]


# In[15]:


df[df['Fare'] > 300]


# In[16]:


df


# In[17]:


#Saving the Cleaned data in csv format into our PC
df.to_csv('data/Titanic.csv') 


# In[18]:


# We look at first five rows in our data set
df.head()


# In[19]:


# To investigate measures of centre
df.describe()


# In[20]:


df.dtypes


# In[21]:


# Select only the relevant numeric columns
num_columns = ['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']


# In[22]:


# Let us see if there is any co-linearity or correlation amongst the variables.
corr = df[num_columns].corr()
print(corr)


# In[23]:


# Let us import our neccessary libraries for our visualisation
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import warnings
warnings.filterwarnings("ignore")

get_ipython().run_line_magic('matplotlib', 'inline')


# In[24]:


# Number of Passenger travelled in each type of Class
sb.countplot(data = df, x = 'Pclass');


# In[25]:


color_palette = sb.color_palette()[0]
sb.countplot(data = df, x = 'Pclass', color= color_palette);


# In[26]:


ordered = df['Pclass'].value_counts().index


# In[27]:


sb.countplot(data = df, y = 'Pclass', color= color_palette, order = ordered);


# In[28]:


# Histogram for Quantitative Variable 'Age'
# By default the bin size is 10

plt.hist(data = df, x = 'Age');


# In[29]:


plt.hist(data = df, x = 'Age', bins = 100);


# In[30]:


plt.hist(data = df, x = 'Age', bins = 4);


# In[31]:


Bin = np.arange(0, df['Age'].max() + 3, 3)
plt.hist(data = df, x = 'Age', bins = Bin);


# In[32]:


sb.distplot(df['Age'], kde = False, hist_kws= {'alpha' : 1}, bins = Bin);


# In[33]:


df['Embarked'].unique()


# In[34]:


# Let us try to create pie chart for Embarked variable
counts = df['Embarked'].value_counts()
plt.pie(counts, labels = counts.index,startangle= 90, counterclock= False)
plt.axis('square');


# In[35]:


# Let's plot a donut
counts = df['Embarked'].value_counts()
plt.pie(counts, labels = counts.index, startangle= 90, counterclock= False, wedgeprops = {'width' : 0.3})
plt.axis('square');


# In[36]:


#Plotting bar chart using figure
fig = plt.figure()
color_palette = sb.color_palette()[0]
ordered = df['Pclass'].value_counts().index
sb.countplot(data = df, x = 'Pclass', color= color_palette, order = ordered);


# In[37]:


#Let us use axes in our plot
fig = plt.figure()
ax = fig.add_axes([.1, .1, .8, .8])
color_palette = sb.color_palette()[0]
ordered = df['Pclass'].value_counts().index
sb.countplot(data = df, x = 'Pclass', color= color_palette, order = ordered);


# In[38]:


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


# In[39]:


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


# ### Bi Variate Visualization

# In[41]:


df.head()


# In[54]:


df.dtypes


# In[42]:


# Let us plot Clutered bar plot to find relationship between two categorical variable
# Let us take two variables i.e. 'Embarked' and 'Survival_Status'

sb.countplot(data = df, x = 'Embarked', hue= 'Survival_Status');


# In[43]:


# Let us plot a scatter plot showing relationship between two Quantitative Variables
# Let's draw scatter plot between Age and Fare variables.

sb.scatterplot(data = df, x = 'Age', y = 'Fare', color = 'r');


# In[44]:


# We plot a regplot to know more about these two variables


sb.regplot(data = df, x = 'Age', y = 'Fare', color = 'g');


# In[45]:


# Let's get the correlation value between Age and Fare variable
dd = df[['Age', 'Fare']]
dd.corr()


# In[46]:


# Let's plot a violin plot with a categorical variable and a quantitative variable.
# We take categorical variable Embarked and Quantitative variable Age

color_palette = sb.color_palette()[0]
sb.violinplot(data = df, x = 'Embarked', y = 'Age', color = color_palette, inner = 'quartile');


# In[47]:


# To find the relationship between a categorical variable and a quantitative variable.
# Let us now plot a bar plot using the same variables as in violin plots.
sb.boxplot(data = df, x = 'Embarked', y = 'Age', color = color_palette);


# In[48]:


# Let us use Facet techniue in visualing relationship between 'Pclass' And 'Age'
# Here, categorical variable is 'Pclass' and quantitative variable is 'Age'
p = sb.FacetGrid(data = df, col = 'Pclass')
p.map(plt.hist, "Age");


# In[49]:


# Stacked Bar Plot between Survival Status and Pclass
# Just like Clustered Bar Plot, both the variables here are Categorical variables.
cat1_order = ['Did Not Survived', 'Survived']
cat2_order = [1, 2, 3]

baselines = np.zeros(len(cat1_order))
# for each second-variable category:
for i in range(len(cat2_order)):
     # isolate the counts of the first category,
    cat2 = cat2_order[i]
    inner_counts = df[df['Pclass'] == cat2]['Survival_Status'].value_counts()
    # then plot those counts on top of the accumulated baseline
    plt.bar(x = np.arange(len(cat1_order)), height = inner_counts[cat1_order],
            bottom = baselines)
    baselines += inner_counts[cat1_order]

plt.xticks(np.arange(len(cat1_order)), cat1_order)
plt.legend(cat2_order);


# In[55]:


df.dtypes


# In[59]:


import seaborn as sb
import matplotlib.pyplot as plt

# Calcular las medias agrupadas por 'Pclass'
group_means = df.groupby(['Pclass'])['Age'].mean().reset_index()

# Ordenar los grupos por edad promedio en orden descendente
group_order = group_means.sort_values(['Age'], ascending=False)['Pclass']

# Crear el objeto FacetGrid y asignar los parámetros
g = sb.FacetGrid(data=df, row='Pclass', row_order=group_order, height=0.9, aspect=7)

# Mapear el gráfico kdeplot a la columna 'Age' en el objeto FacetGrid
g.map(sb.kdeplot, 'Age', shade=True)

# Mostrar el gráfico
plt.show()


# In[51]:


# Let us plot swarm plot to find relationship between categorical and quantitative
# Categorical: 'Pclass' and Quantitative: 'Age'
sb.swarmplot(data = df, x = 'Pclass', y = 'Age', color = color_palette);


# In[ ]:




