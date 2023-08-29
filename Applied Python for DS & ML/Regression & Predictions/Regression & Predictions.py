#!/usr/bin/env python
# coding: utf-8

# ### Loading & Exploring Diamonds Data

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LassoCV
from sklearn.linear_model import ElasticNetCV
from sklearn.ensemble import RandomForestRegressor 

    
import statsmodels.api as sm

import pingouin as pg 

import warnings
warnings.filterwarnings("ignore")


# #### diamonds dataset

# In[2]:


df_diamonds = sns.load_dataset("diamonds")


# In[3]:


df_diamonds.head()


# carat: The weight of the diamond, equivalent to 200mg (should be a good indicator)
# 
# cut: Quality of the cut
# 
# color: Color of the diamond from J to D (worst to best)
# 
# clarity: How clear the diamond is: I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best)
# 
# depth: Total depth percentage (relative to x and y). Will likely be collinear
# 
# table: Width of top of diamond relative to widest point(43-95)
# 
# price: In US dollars ($)
# 
# x,y,z: Dimnesions of the diamond

# In[4]:


df_diamonds.info()


# In[5]:


#missing values?
df_diamonds.isnull().sum()


# In[6]:


df_diamonds.describe()


# In[7]:


print(df_diamonds.dtypes)


# In[8]:


#unique values of the most common at the top
df_diamonds.describe(include=["category"])


# In[9]:


#set color design
sns.set(color_codes=True)
colors = sns.color_palette("bright")


# ### https://seaborn.pydata.org/tutorial/color_palettes.html

# In[10]:


df_diamonds.describe()


# #### data viz

# In[11]:


fig, axes = plt.subplots(2, 4, figsize = (15,8))

sns.distplot(df_diamonds["carat"], color = colors[0], ax = axes[0,0])
sns.distplot(df_diamonds["depth"], color = colors[1], ax = axes[0,1])
sns.distplot(df_diamonds["table"], color = colors[2], ax = axes[0,2])
sns.distplot(df_diamonds["price"], color = colors[3], ax = axes[0,3])
sns.distplot(df_diamonds["x"], color = colors[4], ax = axes[1,0])
sns.distplot(df_diamonds["y"], color = colors[5], ax = axes[1,1])
sns.distplot(df_diamonds["z"], color = colors[6], ax = axes[1,2])

plt.suptitle("Distribution of Quantitative Variables", y = 1.01, size = 18)
plt.tight_layout()
plt.show()


# In[12]:


fig, axes = plt.subplots(2, 4, figsize = (15,8))

sns.boxplot(y=df_diamonds["carat"], color = colors[0], ax = axes[0,0])
sns.boxplot(y=df_diamonds["depth"], color = colors[1], ax = axes[0,1])
sns.boxplot(y=df_diamonds["table"], color = colors[2], ax = axes[0,2])
sns.boxplot(y=df_diamonds["price"], color = colors[3], ax = axes[0,3])
sns.boxplot(y=df_diamonds["x"], color = colors[4], ax = axes[1,0])
sns.boxplot(y=df_diamonds["y"], color = colors[5], ax = axes[1,1])
sns.boxplot(y=df_diamonds["z"], color = colors[6], ax = axes[1,2])

plt.suptitle("Distribution of Quantitative Variables", y = 1.01, size = 18)
plt.tight_layout()
plt.show()


# ### Categorical Coding & Data Splitting

# In[13]:


weird_zeros = df_diamonds[(df_diamonds["x"] == 0) | (df_diamonds["y"] == 0) | (df_diamonds["z"] == 0)]


# In[14]:


all_zeros = df_diamonds[(df_diamonds["x"] == 0) & (df_diamonds["y"] == 0) & (df_diamonds["z"] == 0)]


# In[15]:


all_zeros


# In[16]:


weird_zeros.shape


# In[17]:


weird_zeros


# In[18]:


#copy the original data frame
df_diamondsX = df_diamonds.copy()


# In[19]:


#opposite with the data + drop null values
df_diamondsX = df_diamondsX[~df_diamondsX.isin(weird_zeros)].dropna(how= "all")


# In[20]:


#total count = 53940
#-weird_zeros = 20
#53920
df_diamondsX.shape


# In[21]:


fig, axes = plt.subplots(1, 3, figsize=(10, 6))

sns.countplot(x="cut", data=df_diamonds, ax=axes[0])
sns.countplot(x="color", data=df_diamonds, ax=axes[1])
sns.countplot(x="clarity", data=df_diamonds, ax=axes[2])

#quick look at the categorical variable
for ax in fig.axes:
    ax.tick_params(labelrotation=90)
    
plt.suptitle("Categorical Variables", y= 1.01, size = 18)
plt.tight_layout()
plt.show()


# #### One-Hot-Encoding

# In[22]:


new_cols = pd.get_dummies(df_diamondsX["cut"])
new_cols


# In[23]:


#redefine the dataframe
df_diamondsX = df_diamondsX.drop(["color","clarity","cut"], axis = 1)


# In[24]:


df_diamondsX


# In[25]:


#put all together
df = pd.concat([df_diamondsX, new_cols], axis = 1)


# In[26]:


df


# In[27]:


df.info()


# #### Splitting the data

# In[28]:


train_df, test_df = train_test_split(df, test_size = 0.3, random_state = 32)


# In[29]:


Y_test = test_df["price"]

X_test = test_df.drop(columns = ["price"], axis = 1)

Y_train = train_df["price"]

X_train = train_df.drop(columns = ["price"], axis = 1)


# #### our evaluation function 

# In[30]:


def error_metrics(y_true, y_pred):
    mean_abs = "Mean Absolute Error: {}".format(mean_absolute_error(y_true, y_pred))
    mean_squared = "Mean Square Error: {}".format(mean_squared_error(y_true, y_pred))
    r2 = "r2 score: {}".format(r2_score(y_true, y_pred))
    return mean_abs, mean_squared, r2


# #### Linear Regression

# In[31]:


linear_regression = LinearRegression()


# #### fit it

# In[32]:


linear_regression.fit(X_train, Y_train) 


# In[33]:


#intercept
print(linear_regression.intercept_)


# In[34]:


#coeficient
print(linear_regression.coef_)


# #### Building Predictions

# In[35]:


Y_pred_linear = linear_regression.predict(X_test)


# In[36]:


Y_pred_linear


# In[37]:


linear_comparison = pd.DataFrame({"Actual":Y_test, "Predicted":Y_pred_linear})


# In[38]:


linear_comparison


# #### accuracy

# In[39]:


error_metrics(Y_test, Y_pred_linear)


# #### another method

# In[40]:


linear_comparison["Diff"] = np.abs(linear_comparison["Actual"] - linear_comparison["Predicted"])


# In[41]:


linear_comparison.head(5)


# In[42]:


#check how the dataframe works
linear_comparison["Dist100"] = ["Yes" if x <= 100.00 else "No" for x in linear_comparison["Diff"]]

linear_comparison["Dist500"] = ["Yes" if x <= 500.00 else "No" for x in linear_comparison["Diff"]]


# In[43]:


linear_comparison.head(5)


# In[44]:


#count Dist100
linear_comparison["Dist100"].value_counts()


# In[45]:


#pretty low at 13,5% accuracy
2194/(13982+2194)


# In[46]:


#count Dist500
linear_comparison["Dist500"].value_counts()


# In[47]:


#a little over 50%....thats not a very good advertising pitch here
8549/(8549+7627)


# #### Statsmodels Version

# In[48]:


# Verify the data types of the columns in Y_train and X_train
print(Y_train.dtypes)
print(X_train.dtypes)

# Convert columns to numeric type if required
Y_train = Y_train.astype(float)
X_train = X_train.astype(float)

# Continue with the original code
model_linear = sm.OLS(Y_train, X_train)
linear_stats_model = model_linear.fit()
print(linear_stats_model.summary())


# #### Linear ping

# In[49]:


linear_ping = pg.linear_regression(X_train[["x","y","z"]], Y_train)
linear_ping


# ### Polynomial Regression

# In[50]:


rng = np.random.RandomState(1)

x = 7 * rng.rand(50)
    
y = np.sin(x) + 0.3 * rng.randn(50)


# In[51]:


x = x[:, np.newaxis]
y = y[:, np.newaxis]

inds = y.ravel().argsort()
x = x.ravel()[inds].reshape(-1,1)
y = y[inds]


# In[52]:


sns.set(color_codes=True)
plt.scatter(x,y)
plt.show()


# In[53]:


#checking the model
model = sm.OLS(y,x).fit()


# #### Prediction

# In[54]:


y_pred = model.predict(x)


# In[55]:


plt.scatter(x,y)
plt.plot(x, y_pred)
plt.show()


# #### Polynomial Features

# * Link info: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html
# * Link info: https://machinelearningmastery.com/polynomial-features-transforms-for-machine-learning/

# In[56]:


poly_feat = PolynomialFeatures(degree = 5)
xp5 = poly_feat.fit_transform(x)
xp5.shape


# In[57]:


model = sm.OLS(y, xp5).fit()
y_pred = model.predict(xp5)


# In[58]:


plt.scatter(x,y)
plt.plot(x, y_pred)
plt.show()


# In[59]:


print(model.summary())


# ### Ridge Regression

# * link info : https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html

# #### data processing to keep our data set consistent
# 

# In[60]:


df_diamonds = sns.load_dataset("diamonds")
weird_zeros = df_diamonds[(df_diamonds["x"] == 0) | (df_diamonds["y"] == 0) | (df_diamonds["z"] == 0)]

df_diamondsX = df_diamonds.copy()
df_diamondsX = df_diamondsX[~df_diamondsX.isin(weird_zeros)].dropna(how= "all")

new_cols = pd.get_dummies(df_diamondsX["cut"])
df_diamondsX = df_diamondsX.drop(["color","clarity","cut"], axis = 1)

df = pd.concat([df_diamondsX, new_cols], axis = 1)


# In[61]:


train_df, test_df = train_test_split(df, test_size = 0.3, random_state = 32)

Y_test = test_df["price"]

X_test = test_df.drop(columns = ["price"], axis = 1)

Y_train = train_df["price"]

X_train = train_df.drop(columns = ["price"], axis = 1)


# In[62]:


def error_metrics(y_true, y_pred):
    mean_abs = "Mean Absolute Error: {}".format(mean_absolute_error(y_true, y_pred))
    mean_squared = "Mean Square Error: {}".format(mean_squared_error(y_true, y_pred))
    r2 = "r2 score: {}".format(r2_score(y_true, y_pred))
    return mean_abs, mean_squared, r2


# #### common alpha for ridge

# In[63]:


alphas = [.01, .1, 1, 10, 100, 1000, 10000]


# In[64]:


ridge = RidgeCV(alphas = alphas, cv = 5)
ridge_fit = ridge.fit(X_train, Y_train)


# In[65]:


yhat_ridge = ridge_fit.predict(X_test)


# In[66]:


error_metrics(Y_test, yhat_ridge)


# ### Lasso Regression

# In[67]:


#common alpha for Lasso
alphas = [.01, .1, 1, 10, 100, 1000, 10000]


# In[68]:


lasso = LassoCV(cv = 5, random_state=32, alphas=alphas)


# In[69]:


lasso_fit = lasso.fit(X_train, Y_train)


# In[70]:


yhat_lasso = lasso_fit.predict(X_test)


# In[71]:


#lasso
error_metrics(Y_test, yhat_lasso)


# In[72]:


#ridge
error_metrics(Y_test, yhat_ridge)


# In[73]:


#compare it 
lasso_ridge_comp = pd.DataFrame({"Actual":Y_test, "Pred Lasso": yhat_lasso, " Pred Ridge":yhat_ridge})


# In[74]:


# Eliminate blank spaces in column names
lasso_ridge_comp.columns = lasso_ridge_comp.columns.str.strip()


# In[75]:


print(lasso_ridge_comp.columns)


# In[76]:


lasso_ridge_comp["Diff"] = np.abs(lasso_ridge_comp["Pred Lasso"] - lasso_ridge_comp["Pred Ridge"])


# In[77]:


lasso_ridge_comp


# In[78]:


lasso_ridge_comp.describe()


# ### ElasticNet Regression

# In[79]:


#common alpha for ElasticNet Regression
alphas = [.01, .1, 1, 10, 100, 1000, 10000]


# In[80]:


elasticnet = ElasticNetCV(cv =5, random_state = 32, l1_ratio = 0.5, alphas=alphas)
elastic_fit = elasticnet.fit(X_train, Y_train)
yhat_elastic = elastic_fit.predict(X_test)


# In[81]:


error_metrics(Y_test, yhat_elastic)


# ### Random Forest Regression

# In[82]:


rf = RandomForestRegressor(n_estimators=1000, random_state=32)


# In[83]:


rf_fit = rf.fit(X_train, Y_train)


# In[84]:


yhat_rf = rf_fit.predict(X_test)


# In[85]:


#1000
error_metrics(Y_test, yhat_rf)


# ### Model Comparison Tool

# #### rename some things, makes our work more understandable and transferable

# In[86]:


features = X_train.copy()
targets = Y_train.copy()


# #### defining models we want to compare

# In[87]:


models = [
    	LinearRegression(),
    RidgeCV(),
    LassoCV(),
    #ElasticNetCV(),
    RandomForestRegressor()
]


# #### Number of cross validation, 5 is standard... lets go 10

# In[88]:


CV = 10
cv_df = pd.DataFrame(index=range(CV * len(models)))
entries = []


# #### Outer for loop to execute our cross validation on the above models 

# In[89]:


for model in models: 
    #accesing model information class
    model_name = model.__class__.__name__
    #get our parameters of model to calculate R2
    accuracies = cross_val_score(model, features, targets, scoring="r2", cv=CV)
    #inner for loop to fill in the entries
    for fold_idx, accuracy in enumerate(accuracies):
        entries.append((model_name, fold_idx, accuracy))
#finalizing the dataframe
cv_df = pd.DataFrame(entries, columns=["model_name", 'fold_idx', 'r2'])


# In[90]:


sns.set(color_codes=True)
sns.boxplot(x="model_name", y="r2", data=cv_df)
sns.stripplot(x="model_name", y="r2", data=cv_df, size = 7, jitter=True, edgecolor="gray", linewidth=2)
plt.title("Regression Models", fontsize=20)
plt.ylabel("R Squared", fontsize = 15)
plt.xlabel("")
plt.xticks(fontsize = 12, rotation=90)
plt.yticks(fontsize = 12, rotation=0)
plt.show()


# In[91]:


sns.set(color_codes=True)
sns.boxplot(x="model_name", y="r2", data=cv_df)
sns.stripplot(x="model_name", y="r2", data=cv_df, size = 7, jitter=True, edgecolor="gray", linewidth=2)
plt.title("Regression Models", fontsize=20)
plt.ylabel("R Squared", fontsize = 15)
plt.xlabel("")
plt.xticks(fontsize = 12, rotation=90)
plt.yticks(fontsize = 12, rotation=0)
plt.show()


# In[92]:


cv_df.head(5)


# In[93]:


final_comp = cv_df.groupby("model_name").r2.mean().reset_index().sort_values(by = "r2", ascending = False)
final_comp


# In[ ]:




