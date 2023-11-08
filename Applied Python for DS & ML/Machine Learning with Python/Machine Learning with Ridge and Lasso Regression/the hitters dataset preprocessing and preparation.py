#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="5">The Hitters Dataset: Preprocessing and Preparation</font></b></h1></center>

# #### Importing the Libraries

# In[13]:


import pandas as pd
import numpy as np 
import math
import matplotlib.pyplot as plt
import seaborn as sns 
sns.set()

from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LassoCV

from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_squared_error


import warnings
warnings.filterwarnings("ignore")


# #### Load the data

# In[4]:


data = pd.read_csv('./data/Hitters.csv')
data.head()


# #### make a copy of the original DF

# In[7]:


df_hitters = data.copy()
df_hitters
#Salary target variable = predict a baseball players salary based on the rest of the features


# #### Categorical Variables

# In[8]:


print('The league types are:', df_hitters['League'].unique())
print('The division types are:', df_hitters['Division'].unique())
print('The new league options are:', df_hitters['NewLeague'].unique())


# #### Converts categorical variables into 0s and 1s

# In[9]:


df_hitters_num = pd.get_dummies(df_hitters, columns = ['League', 'Division', 'NewLeague'], drop_first=True)
df_hitters_num


# #### Checking NaN values

# In[10]:


df_hitters_num.isnull().sum()


# #### Fill NaNs with predicted values

# In[11]:


df_hitters_num_nonull = df_hitters_num.dropna()
df_hitters_num_nonull.isnull().sum()


# In[17]:


numeric_df = df_hitters.select_dtypes(include='number')


# In[18]:


# check for multicolinearity
plt.figure(figsize=(13,6))
sns.heatmap(numeric_df.corr(),
            vmin = -1,
            vmax = 1,
            cmap = "GnBu",
            annot=True)
plt.show()


# <center><h1><b><font size="5">Exploratory Data Analysis</font></b></h1></center>

# #### Plot salary from df_hitter_num_nonull

# In[14]:


sns.displot(df_hitters_num_nonull['Salary']);


# #### Check the relationship of  dependent and the independent variable in the dataset

# In[15]:


correlation = df_hitters_num_nonull.corr()
correlation['Salary'].sort_values(ascending=True)
#salaray = dependent variable 
# the others one are independent variables
# pearson correlation ( 1 stron positive correlation / -1 strong negative correlation / 0 there is no relationship)


# #### Declare the dependent and independent variables 

# In[19]:


X = df_hitters_num_nonull.drop('Salary', axis = 1)
y = df_hitters_num_nonull['Salary']


# #### Split the data into train and test sets

# In[21]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state = 365)


# In[23]:


scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# #### Perform linear regression

# In[26]:


lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)


# In[28]:


print("Linear Regression coefficients are: ", lin_reg.coef_)
print("Linear Regression y-intercept is: ", lin_reg.intercept_)


# #### create a new variable

# In[29]:


lin_reg_y_pred = lin_reg.predict(X_test)
lin_reg_y_pred


# #### Compre the predicted values with the actual ones

# In[30]:


#create a DF containing the results
lin_comp = pd.DataFrame({'Predicted': lin_reg_y_pred, 'Actual': y_test})
lin_comp


# #### Performing Linear Regression

# In[32]:


print("Linear Regression Model RMSE is: ", math.sqrt(mean_squared_error(y_test, lin_reg_y_pred)))
print("Linear Regression Model Training Score: ", lin_reg.score(X_train, y_train))
print("Linear Regression Model Testing Score: ", lin_reg.score(X_test, y_test))


# #### Performing Ridge Regression with Cross-validation

# In[34]:


cv = RepeatedKFold(n_splits=5, n_repeats=3, random_state=1)


# In[35]:


ridge = RidgeCV(alphas=np.arange(0.1, 10, 0.1), cv=cv, scoring='neg_mean_squared_error')


# In[36]:


ridge.fit(X_train, y_train)
ridge_reg_y_pred = ridge.predict(X_test)

print("Ridge tuning parameter:", (ridge.alpha_))
print("Ridge model cofficients:", (ridge.coef_))
print("Ridge model intercept:", (ridge.intercept_))


# In[43]:


print("Ridge Regression Model RMSE is: ", math.sqrt(mean_squared_error(y_test, ridge_reg_y_pred)))
print("Ridge Regression Model Training Score: ", ridge.score(X_train, y_train))
print("Ridge Regression Model Testing Score: ", ridge.score(X_test, y_test))


# #### Performing Lasso Regresion with Cross-validation
# 
# Lasso regression decreases the coefficients values in a way that the least significant of them can fall all the way to 0

# In[37]:


lasso = LassoCV(alphas=np.arange(0.1, 10, 0.1), cv=cv, tol=1) # 1 to prevents dualiuty gap and #tol = optimization tolerance tell the algorithm to stop searching once the tolerance between minimum and maximum is achieved


# In[38]:


lasso.fit(X_train, y_train)
lasso_reg_y_pred = lasso.predict(X_test)

print("Lasso tuning parameter:", (lasso.alpha_))
print("Lasso model cofficients:", (lasso.coef_))
print("Lasso model intercept:", (lasso.intercept_))


# In[47]:


print("Lasso Regression Model RMSE is: ", math.sqrt(mean_squared_error(y_test, lasso_reg_y_pred)))
print("Lasso Regression Model Training Score: ", lasso.score(X_train, y_train))
print("Lasso Regression Model Testing Score: ", lasso.score(X_test, y_test))


# <center><h1><b><font size="5">Compare the Scores</font></b></h1></center>

# In[44]:


print("Linear Regression Model Training Score: ", lin_reg.score(X_train, y_train)) #highes value
print("Linear Regression Model Testing Score: ", lin_reg.score(X_test, y_test)) #Only 35% of the data managed to fit the model properly

print("Ridge Regression Model Training Score: ", ridge.score(X_train, y_train))
print("Ridge Regression Model Testing Score: ", ridge.score(X_test, y_test))

print("Lasso Regression Model Training Score: ", lasso.score(X_train, y_train))
print("Lasso Regression Model Testing Score: ", lasso.score(X_test, y_test))


# <center><h1><b><font size="5">Compare the root mean squared error | RMSE</font></b></h1></center>

# In[46]:


print("Linear Regression Model RMSE is: ", math.sqrt(mean_squared_error(y_test, lin_reg_y_pred)))
#the average distance between predicted and actual values is shortest when applying ridge regression
print("Ridge Regression Model RMSE is: ", math.sqrt(mean_squared_error(y_test, ridge_reg_y_pred))) 

print("asso Regression Model RMSE is: ", math.sqrt(mean_squared_error(y_test, lasso_reg_y_pred)))


# #### Conclusion
#  **Ridge** and **Lasso** handle the data better than the linear regression
#  
#  In this case **Ridge Regression** is the properly algorithm
#  
#  It is essential to understand the data and what problem you are facin in order to choose the most suitable approach every time

# #### Replacing the Missing Values in the DataFrame 

# ##### Store null values in a new variable 

# In[48]:


# 59 register as a NaN values would be replaced after predictions
df_hitters_nan = df_hitters_num[df_hitters_num['Salary'].isnull()]
df_hitters_nan


# ##### Assign the dependent and independent variables 

# In[49]:


X_nan = df_hitters_nan.drop('Salary', axis=1)
y_nan = df_hitters_nan['Salary']


# In[50]:


scaler = StandardScaler()
X_nan = scaler.fit_transform(X_nan)


# In[51]:


nan_pred = ridge.predict(X_nan)
nan_pred


# #### Populate the dataframe 

# In[53]:


df_nan_full = df_hitters_nan.copy()
df_nan_full['Salary'] = nan_pred
df_nan_full

