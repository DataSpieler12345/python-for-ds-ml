#!/usr/bin/env python
# coding: utf-8

# # Matplotlib

# In[20]:


import matplotlib.pyplot as plt
import numpy as np 

import warnings
warnings.filterwarnings("ignore")


# #### Generate dummie data

# In[4]:


#We now obtain the ndarray obnject of angles between 0 and 2pi
import math 
x = np.arange(0, math.pi*2, 0.05)


# In[5]:


x


# In[8]:


#y axis are obtained by the following statement 
y = np.sin(x)


# In[9]:


#The values from two arrays are plotted using the plot() function
plt.plot(x,y)


# In[10]:


x = np.arange(0, math.pi*2, 0.05)
y= np.sin(x)
plt.plot(x,y)
plt.xlabel("angle")
plt.ylabel("sine")
plt.title('sine wave')

plt.show()


# ## Barplot

# In[11]:


# X - axis values
x = [5,2,9,4,7]

# Y - axis values 
y = [10,5,8,4,2]

#funct8ion to plot the bar 
plt.bar(x,y)

#function to show the plot 
plt.show()


# ## Histogram

# In[12]:


# Y - axis values 
y = [10,5,8,4,2]

#function to plot histogram
plt.hist(y)

#function to show the plot 
plt.show()


# ## Scatter plot

# In[14]:


# X - axis values
x = [5,2,9,4,7]

# Y - axis values 
y = [10,5,8,4,2]

#function to plot the bar
plt.scatter(x,y)

#function to show the plot 
plt.show()


# # Seaborn

# In[15]:


import seaborn as sns 


# In[17]:


#load the tips dataset 
tips = sns.load_dataset("tips")
tips


# In[18]:


#Create a violinplot
sns.violinplot(x = "total_bill", data=tips)
#show the plot 
plt.show()


# In[21]:


#Load the iris dataset
iris = sns.load_dataset("iris")

#Construct iris plot
sns.swarmplot(x="species", y="petal_length", data=iris)

#show the plot
plt.show()


# In[22]:


# Define a color palette for each species
palette = {"setosa": "red", "versicolor": "blue", "virginica": "green"}

# Construct the swarm plot with the color palette
sns.swarmplot(x="species", y="petal_length", data=iris, palette=palette)

# Show the plot
plt.show()


# ## Factorplot | Catplot

# In[24]:


# Load the titanic dataset
titanic = sns.load_dataset("titanic")

# Set up a factorplot
g = sns.catplot(x="class", y="survived", hue="sex", data=titanic, kind="bar", palette="muted", legend=True)

# Show the plot
plt.show()


# ## Visualizing the distribution of a dataset 

# In[25]:


import pandas as pd
from scipy import stats


# ### Plotting univariate distributions 

# In[26]:


#raw random samples from a normal (Gaussian) distribution
x = np.random.normal(size=100)
sns.distplot(x)


# ### Kernel density estimation 

# In[27]:


sns.distplot(x, hist=False, rug=True)


# ### Plotting bivariate distributions 

# In[29]:


mean, cov = [0, 1], [(1, .5), (.5, 1)]
# Draw random samples from a multivariate normal distribution
data = np.random.multivariate_normal(mean, cov, 200)
# Make a DataFrame for data
df = pd.DataFrame(data, columns=["x", "y"])

# Print the DataFrame
print(df)


# #### Scatterplots

# In[30]:


#seaborn is to just use the jointplot() function for plotting scatterplots
sns.jointplot(x="x", y="y", data=df)


# ### Visualizing pairwise relationships in a dataset

# In[31]:


#To plot multiple pairwise bivariate distributions in a dataset, you can use the pairplot() function 

iris = sns.load_dataset("iris")
sns.pairplot(iris)


# In[ ]:




