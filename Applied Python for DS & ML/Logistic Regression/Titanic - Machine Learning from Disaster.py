#!/usr/bin/env python
# coding: utf-8

# ## Titanic - Machine Learning from Disaster
# #### Predict survival on the Titanic and get familiar with ML basic

# ### Loading the Data

# In[1]:


# The Libraries 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#set style for sns plots
sns.set()


# In[3]:


#read the train data set
train_df = pd.read_csv('train.csv')
train_df.head()


# In[4]:


#create a df with survived column
survived = train_df['Survived']
print(train_df['Survived'])


# In[5]:


#describe
print(train_df['Survived'].describe())


# In[6]:


#info of train data set
train_df.info()


# In[7]:


#describe dataset
train_df.describe()
#Age column values 714 and the others columns 891 (missing values)
# Age Mean 29.69
# Age Min 0.42 ?
# Age Max 80


# ### Preliminary Analysis of Data

# In[8]:


#Null values 
train_df.isnull()


# In[9]:


#call any method
train_df.isnull().any()


# In[10]:


# check de number with sum()
train_df.isnull().sum()
#Age = 177 null values 
#Cabin = 687 null values
#Embarked = 2 null values


# In[11]:


# calculate the % of it 
train_df.isnull().sum() / train_df.shape[0]*100 # 0 = row
# Age = 19.86% missing values 
# Cabin = 77.10 missing values
# Embarked 0.22 missing values 


# In[12]:


# store null values into a variable 
nulls = train_df.isnull().sum()
nulls


# In[13]:


# create a barplot with the variable nulls
sns.barplot(x=nulls.index,y=nulls) #nulls.index = name of columns,  nulls = the numeric values 


# In[14]:


# more readable 
g = sns.barplot(x=nulls.index,y=nulls)
g.set_xticklabels(nulls.index,rotation=45)
plt.show()


# In[15]:


#heatmap with the original df
sns.heatmap(train_df.isnull())


# ### Data Cleanup

# In[16]:


nulls = train_df.isnull().sum()
nulls
#Age = 19.86% missing 
#Cabin = 77.10 % missing 
#Embarked = 0.22


# In[17]:


#call column Age
train_df['Age']


# In[18]:


# create a histogram plot of the 'Age' column
sns.histplot(train_df['Age'], kde=True, bins=40) #distplot are no updated

# set the title and axis labels
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Count')

# display the plot
plt.show()


# In[19]:


#the mean of the df
train_df['Age'].mean()


# In[20]:


#the median
train_df['Age'].median()
#we have to take a call because this data is actually skewed on the right side, using median will be a little bit better choice


# In[21]:


#lets fill NaN values and fill it with the median value and save the change
train_df['Age'].fillna(train_df['Age'].median(), inplace=True)


# In[23]:


#missing values again in Age column?
train_df.isnull().sum() / train_df.shape[0]*100


# In[24]:


# create a histogram plot of the 'Age' column
sns.histplot(train_df['Age'], kde=True, bins=40) #distplot are no updated

# set the title and axis labels
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Count')

# display the plot
plt.show()


# In[25]:


#drop the cabin column
train_df.drop('Cabin', axis=1, inplace=True)


# In[26]:


#cabin column? dropped
train_df.isnull().sum() / train_df.shape[0]*100


# In[27]:


#Embarked column values amount
train_df.isnull().sum(),#embarked = 2 missing values 


# In[28]:


#check the values of Embarked column
train_df['Embarked'].value_counts()
#S the most comun one / fill it with S values of the same column


# In[29]:


train_df['Embarked'].fillna('S', inplace=True)


# In[30]:


#check if we still are having missing value in Embarket column
train_df.isnull().sum() # e violaaa! alles erledigt! 


# In[31]:


train_df.isnull().any()


# In[32]:


#do we need the name column?
train_df.head()


# In[33]:


#drop the unuseful columns that not affect the final result 
train_df.drop(['PassengerId','Name','Ticket'], axis=1, inplace=True) # axis 1  = columns


# In[34]:


#lets look at the df again
train_df.head()


# ### Categorical to Numerical 

# In[35]:


#unique values in the sex column
train_df['Sex']


# In[36]:


train_df['Sex'].unique()


# In[40]:


#create numerical data of it 
train_df = pd.get_dummies(train_df,columns=['Sex'], dtype=int)
#notice = we dont have any kind of inplace function. We need to pass in this DataFrame to the Original DataFrame


# In[41]:


train_df.head()
#both are unuseful. 0 actually implies sex male equals 1. so we can drop one of theses columns
#In facts, its import to drop those two columns because these two columns are dependent on each other, and this will
#introduce a problem calle MULTICOLLINEARITY
#so delete any of them


# In[42]:


#drop the unuseful columns that not affect the final result 
#delete sex_male
train_df.drop('Sex_male', axis=1, inplace=True) # axis 1  = columns


# In[43]:


#Sex_male column dropped
train_df.head()


# In[44]:


#create numerical data of Embarked
train_df = pd.get_dummies(train_df,columns=['Embarked'], dtype=int)


# In[46]:


train_df.head()
#so we have Embarked_C, Embarked_Q, Embarked_S 
#similar with sex female and male, we can actually drop one of this 3 columns.
#because, for example, if C is 0,Q = 0, it means that it was S because embarked column actually had onle one of these three and no null values.
#drop the last one = Embarked_S


# In[47]:


#drop the unuseful columns that not affect the final result 
#delete sex_male
train_df.drop('Embarked_S', axis=1, inplace=True) # axis 1  = columns


# In[48]:


train_df.head()


# In[49]:


#check again the function info
train_df.info()
#wen can actually pass this dataset directly to the Model, but we will do some visual analysis
#all data type are numeric!So, now we are ready !


# ### Visualization

# #### We will do some visual exploration of the data. So, we are going to create some plots and we will understand how our data is.

# In[51]:


train_df.head()
#just numerics data type and columns
#we do not habe null values


# #### How many people survived vers did not survive

# In[53]:


sns.countplot(x='Survived',data=train_df)


# In[55]:


#hue parameter for more analysis
#So, note that suvived 0 means died and 1 surive
sns.countplot(x='Survived',data=train_df,hue='Sex_female')


# In[56]:


#hue parameter for more analysis
#So, note that suvived 0 means died and 1 surive
#lets look at Pclass = 1 first class / 2 second class and 3 third class
sns.countplot(x='Survived',data=train_df,hue='Pclass')


# In[69]:


# create a histogram plot of the 'Age' column with survived
sns.histplot(data=train_df,x='Age', hue='Survived', kde=True, bins = 40) #distplot are no updated

# set the title and axis labels
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend(['Survived','Not Survived'])

# display the plot
plt.show()


# In[68]:


sns.kdeplot(data=train_df, x='Age', hue='Survived', bw_method='scott', fill=True, palette={0: 'blue', 1: 'orange'})

# set the title and axis labels
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend(['Survived','Not Survived'])

# display the plot
plt.show()


# ### Modeling Processing - Training the Model | Making Some Predictions

# In[70]:


#the dataFrame
train_df


# In[71]:


# assign the dataFrame to X variable with out survived column | inplace function not necessary because we are making a copy of DF
X = train_df.drop('Survived',axis=1)


# In[72]:


#set y to target variable = Survived column | the value that we want to make predictions
y = train_df['Survived']


# In[73]:


#from sklearn.model_selection | import train_test_split
from sklearn.model_selection import train_test_split


# In[74]:


#create the training and testing dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# In[75]:


#Now we are ready to create the model
from sklearn.linear_model import LogisticRegression


# In[84]:


#create the instance of logistic Regression
lr =LogisticRegression(solver='liblinear')
# solver = liblinear to avoid the warning message or use max_iter=1000


# In[85]:


#train the model by calling the fit, and it will need X and y train
lr.fit(X_train, y_train)


# ### Evaluation of Predictions

# ### So, now we are going to make some predictions

# In[86]:


y_pred = lr.predict(X_test)


# In[88]:


#lets understand the use of this evaluation 
#confusion_matrix, classification_report, accuracy_score
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score


# In[89]:


#accuracy_score is 81% for our model
accuracy_score(y_test, y_pred)


# In[90]:


#classification_report = 1 survived = 0.80      0.72      0.76       120 
# 0 not survived =  0.82      0.87      0.85       175
print(classification_report(y_test, y_pred))


# In[91]:


#confusion_matrix
#can see that 153 is TP and 87 is TN
confusion_matrix(y_test, y_pred)


# In[92]:


#tweak the parameters and fit the model
lr2 =LogisticRegression(max_iter=200)
lr2.fit(X_train,y_train)


# ##### Now we make again predictions

# In[93]:


y_pred2 = lr2.predict(X_test)


# In[94]:


#check the classification report (y_pred2) (second model)
print(classification_report(y_test, y_pred2))


# In[95]:


#lest print this again the first one (y_pred) (first model)
#check the classification report
print(classification_report(y_test, y_pred))


# In[ ]:




