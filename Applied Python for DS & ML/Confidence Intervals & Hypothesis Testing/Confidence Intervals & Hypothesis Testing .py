#!/usr/bin/env python
# coding: utf-8

# ### Seaborn Sample Data & Fitting

# In[1]:


#common imports to bring into your notebook
import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib 
import matplotlib.pyplot as plt 
import scipy.stats as st 
from fitter import Fitter
get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings("ignore")

#set color style
sns.set(color_codes=True)


# #### Link datasets: https://github.com/mwaskom/seaborn-data

# In[2]:


#list of all read ins for sns datasets

# anscombe
anscombe_df = sns.load_dataset("anscombe")

# attention
attention_df = sns.load_dataset("attention")

# brain_networks
brain_networks_df = sns.load_dataset("brain_networks")

# car_crashes
car_crashes_df = sns.load_dataset("car_crashes")

# diamonds
diamonds_df = sns.load_dataset("diamonds")

# dots
dots_df = sns.load_dataset("dots")

# exercise
exercise_df = sns.load_dataset("exercise")

# flights
flights_df = sns.load_dataset("flights")

# fmri
fmri_df = sns.load_dataset("fmri")

# geyser
geyser_df = sns.load_dataset("geyser")

# iris
iris_df = sns.load_dataset("iris")

# planets
planets_df = sns.load_dataset("planets")

# tips
tips_df = sns.load_dataset("tips")

# titanic
titanic_df = sns.load_dataset("titanic")


# ### tips dataset

# In[10]:


tips_df.head()


# In[14]:


#jointplot
sns.jointplot(x = "total_bill", y = "tip", data = tips_df, kind = "reg")
plt.show()


# In[13]:


jp = sns.jointplot(x="total_bill", y="tip", data=tips_df, kind="reg")
jp.ax_joint.annotate("Pearsonr = {:.2f}".format(st.pearsonr(tips_df["total_bill"], tips_df["tip"])[0]),
                     xy=(0.5, 0.9), xycoords='axes fraction', fontsize=12)
plt.show()


# In[15]:


data1 = tips_df["total_bill"]
data2 = tips_df["tip"]


# In[16]:


f1 = Fitter(data1)
f2= Fitter(data2)


# In[17]:


f1.fit()


# In[18]:


f2.fit()


# In[19]:


f1.summary()


# In[20]:


f2.summary()


# ### Assuming Normality

# In[22]:


#begin to standardize bill and tip data, to compare them on a singular, standard, scale
mean_bill = tips_df["total_bill"].mean()
stdev_bill = tips_df["total_bill"].std(ddof = 1)

mean_tip = tips_df["tip"].mean()
stdev_tip = tips_df["tip"].std(ddof = 1)


# In[23]:


tips_df.head()


# In[24]:


tips_df["Stand_bill"] = (tips_df["total_bill"] - mean_bill / stdev_bill)


# In[25]:


tips_df["Stand_tip"] = (tips_df["tip"] - mean_tip / stdev_tip)


# In[26]:


tips_df


# ### Normal Data: Probability Plots with Means

# In[27]:


st.probplot(tips_df["total_bill"], dist = "norm", fit = True, rvalue = True, plot = plt)
plt.show()


# In[28]:


st.probplot(tips_df["Stand_bill"], dist = "norm", fit = True, rvalue = True, plot = plt)
plt.show()


# In[29]:


st.probplot(tips_df["Stand_tip"], dist = "norm", fit = True, rvalue = True, plot = plt)
plt.show()


# In[30]:


tips_df.describe()


# In[36]:


fig = plt.figure(figsize=(10,10))

ax1 = plt.subplot(221)
res = st.probplot(tips_df["Stand_bill"], dist = "norm", fit = True, rvalue = True, plot = plt)
ax1.set_title("Bill")

ax2 = plt.subplot(222)
res = st.probplot(tips_df["Stand_tip"], dist = "norm", fit = True, rvalue = True, plot = plt)
ax1.set_title("Tip")

plt.suptitle("Probability Plots", y=1.01, fontsize = 20)
plt.tight_layout()
plt.show()


# ### Normal Data: Categorical Confidence Intervals

# #### diamonds data set 

# In[37]:


diamonds_df.info()


# In[ ]:


#!pip install statsmodels


# In[38]:


diamonds_df["cut"].value_counts()


# In[45]:


import statsmodels.api as sm
from statsmodels.stats.proportion import proportion_confint, proportions_ztest


# In[46]:


21551/53940


# In[48]:


0.3995365220615499 - 0.39540305804708686


# ##### proportion_confint

# In[47]:


proportion_confint(count = 21551, nobs = 53940, alpha = 0.05)


# #### We are 95% confident that the true value of the population proportion of diamonds that are "ideal" in their cut is between 39,54% and 40,37%

# ##### proportion_ztest

# In[51]:


#always consider alpha of 0.05
#claim from expert is thtat at least 41% of diamonds are ideal cut.
#alternative : "two-sided", "smaller", "larger"

#H0: = 0.40
#Ha: not  , <     ,>
proportions_ztest(count = 21551, nobs = 53940, value = 0.40, alternative = "smaller")

#output is going to be; value of the test statistic...second is the p-value


# In[52]:


#always consider alpha of 0.05
#claim from expert is thtat at least 41% of diamonds are ideal cut.
#alternative : "two-sided", "smaller", "larger"

#H0: = 0.40
#Ha: not  , <     ,>
proportions_ztest(count = 21551, nobs = 53940, value = 0.42, alternative = "smaller")

#output is going to be; value of the test statistic...second is the p-value


# ##### Since the Pvalue of 0.00000__146 is less than 0.05, we reject the null hypothesis. Thus, we have sufficient evidence to say that the true proportion of diamonds that are "ideal" cut is less than 42% 

# In[54]:


diamonds_df["cut"].value_counts()


# In[57]:


def two_proportions_confint(success_a, size_a, success_b, size_b, significance):
    
    prop_a = success_a / size_a
    prop_b = success_b / size_b
    var = prop_a * (1- prop_a) / size_a + prop_b * (1 - prop_b) / size_b
    se = np.sqrt(var)
    
    # z score also called a critical value
    confidence = 1 -significance
    z = st.norm(loc = 0, scale = 1).ppf(confidence + significance / 2)
    
    #standard formula for the to calculate a confidence interval
    #point-estimate (p hat) + & - z * the standard-error
    prop_diff = prop_b - prop_a
    confint = prop_diff + np.array([-1, 1]) * z * se
    return prop_diff, confint


# In[61]:


#lets test it with premium
prop_diff, confint = two_proportions_confint(13791, 53940, 12082, 53940, 0.05)
print("Est.Diff.:", prop_diff)
print("Conf. Int.:", confint)


# ###### Prop A was a Premium, Prop B was Very Good

# PropB - PropA = 0
# 
# ***We look if 0 is in the interval...if it is... can not say they are different
# 
# ***(- -) that  means PropA is larger
# 
# ***(+ +) that means PropBV is larger

# In[71]:


def two_proportions_ztest(success_a, size_a, success_b, size_b):
    
    prop_a = success_a / size_a
    prop_b = success_b / size_b
    prop_pooled = (success_a + success_b) / (size_a + size_b)
    var = prop_pooled * (1 - prop_pooled) * (1 /size_a + 1/ size_b)
    zscore = np.abs(prop_b - prop_a) / np.sqrt(var)
    one_side = 1 - st.norm(loc = 0, scale = 1).cdf(zscore)
    pvalue = one_side * 2
    return zscore, pvalue     


# In[72]:


zscore, pvalue = two_proportions_ztest(13791, 53940, 12082, 53940)
print("Zscore:", zscore)
print("Pvaluie:", pvalue)


# ### ANOVA 

# In[6]:


import pingouin as pg


# In[10]:


df = pg.read_dataset("anova")


# In[9]:


df.head()


# In[11]:


df["Hair color"].value_counts()


# In[12]:


#drop subject column
df = df.drop(columns = "Subject", axis = 1)


# In[14]:


df.head(10)


# ##### little of cleaning, specific for statsmodels
# 
# ##### lower case, and replace a "space" with a "_" in our headers
# 

# In[15]:


df.columns = [x.lower().replace(" ", "_") for x in df.columns]


# In[16]:


df.head(5)


# ##### check out statsmodels version of ANOVA

# In[18]:


import statsmodels.formula.api as smf
import statsmodels.api as sm

ols_model = smf.ols("pain_threshold ~ hair_color", data=df).fit()

anova1 = sm.stats.anova_lm(ols_model)

anova1


# In[21]:


anova2 = pg.anova(dv='pain_threshold', between='hair_color', data =df, detailed=True)

anova2


# In[22]:


anova3 = pg.welch_anova(dv='pain_threshold', between='hair_color', data =df)

anova3


# ##### pairwise_turkey

# In[25]:


import researchpy as rp
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Ajustar el modelo ANOVA
model = ols('pain_threshold ~ hair_color', data=df).fit()
anova_table = rp.summary_cont(model)

# Realizar la prueba post hoc de Tukey
posthoc = pairwise_tukeyhsd(df['pain_threshold'], df['hair_color'])

# Imprimir los resultados
print(anova_table)
print(posthoc)


# ### Non-Normal Data & Bootstrap

# In[30]:


import bootstrapped.bootstrap as bs
import bootstrapped.stats_functions as bs_stats
import bootstrapped.compare_functions as bs_compare

import numpy.random as npr


# In[31]:


mean = 1000
stdev = 50

pop = np.random.normal(loc = mean, scale = stdev, size = 100000)


# In[32]:


sns.distplot(pop, bins = 50, hist = True, kde = True)
plt.title("Population Distribution")
plt.show()


# ##### take 10000, samples from the larger population
# 

# In[33]:


samps = pop[:10000]


# ##### time to use bootstrap for mean and stdev

# In[35]:


BS_mean = bs.bootstrap(samps, stat_func=bs_stats.mean)

BS_stdev = bs.bootstrap(samps, stat_func=bs_stats.std)


# In[36]:


print("Bootstrapped mean should be: {}".format(mean))
print('\t' + str(BS_mean))
print(" ")
print("Bootstrapped stdev should be: {}".format(stdev))
print('\t' + str(BS_stdev))


# In[42]:


samp_amount = [10, 30, 50, 100, 500, 1000]
#samp_amount = [10, 30, 50, 100, 500, 1000, 2500, 5000, 10000, 25000]
bootstrap_res = []

tdist_res = []

# for loop to handle our execution and iterations
for i in samp_amount:
    samps = np.random.choice(pop, i, replace=True)
    bsres = bs.bootstrap(samps, stat_func=bs_stats.mean, alpha = 0.05)
    
    tres = st.t.interval(0.95, len(samps)-1, loc = np.mean(samps), scale = st.sem(samps))
    
    bootstrap_res.append((bsres.lower_bound, bsres.upper_bound))
    tdist_res.append(tres)


# In[43]:


plt.subplots(figsize=(7,7))

plt.plot(samp_amount, [x[1] for x in bootstrap_res], color = "yellow")
plt.plot(samp_amount, [x[1] for x in tdist_res], linestyle="--", color = "green")

plt.plot(samp_amount, [x[0] for x in bootstrap_res], color = "yellow", label = "BootStrap")
plt.plot(samp_amount, [x[0] for x in tdist_res], linestyle="--", color = "green", label = "T-Dist")

plt.axhline(pop.mean(), color = "black", label = "Actual Mean")
plt.legend(loc = "best")
plt.title("BootStrap vs T-Distribution")
plt.show()

