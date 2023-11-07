#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="5">Working with the .format() Method</font></b></h1></center>

# In[1]:


time_horizon = 1, 3, 12
time_horizon


# In[3]:


product = ['Product A', 'Product B']
product


# In[6]:


'Expected sales for a period of {} month(s) for {}:'.format(12, 'Product B')


# In[7]:


'Expected sales for a period of {} month(s) for {}:'.format(time_horizon, product)


# In[8]:


'Expected sales for a period of {} month(s) for {}:'.format(time_horizon[2], product)


# In[9]:


'Expected sales for a period of {} month(s) for {}:'.format(time_horizon[2], product[1])


# In[10]:


'Expected sales for a period of {} month(s) for {}:'.format(time_horizon[2], product[0])


# In[11]:


'Expected sales for a period of {0} month(s) for {1}:'.format(time_horizon[2], product[1])


# In[13]:


'Expected sales for a period of {1} month(s) for {0}:'.format(time_horizon[2], product[1])


# In[16]:


'Expected sales for a period of {t_hor} month(s) for {prod}:'.format(t_hor = 12, prod = 'Product B')


# In[17]:


'Expected sales for a period of {t_hor} month(s) for {prod}:'.format(t_hor = 12, prod = ['Product A', 'Product B'])


# In[20]:


'Expected sales for a period of {t_hor} month(s) for {prod[1]}:'.format(t_hor = 12, prod = ['Product A', 'Product B'])


# In[21]:


'Expected sales for a period of {t_hor} month(s) for {prod[0]}:'.format(t_hor = 12, prod = ['Product A', 'Product B'])


# In[22]:


'Expected sales for a period of {t_hor[2]} month(s) for {prod[1]}:'.format(t_hor = time_horizon, prod = product)


# In[23]:


'Expected sales for a period of {t_hor[2]} month(s) for {prod[0]}:'.format(t_hor = time_horizon, prod = product)


# In[24]:


'Expected sales for a period of {t_hor[2]} month(s) for {prod[1]}: ${sales}'.format(t_hor = time_horizon, prod = product, sales = 10000)


# In[25]:


'Expected sales for a period of {0} month(s) for {prod[1]}: ${sales}'.format(12, prod = product, sales = 10000)

