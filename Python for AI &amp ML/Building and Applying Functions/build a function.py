#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="6">Build a Function</font></b></h1></center>

# ##### creating a function

# In[6]:


def hello_there(name):
    print("hello there, "+ name + ". nice to meet you!")


# In[7]:


#test the function


# In[8]:


hello_there("Franz")


# In[10]:


# creating another function

def squared_value(number):
    x = number**2
    return x


# In[11]:


# testing the function 
squared_value(5)


# In[12]:


squared_value(-5)


# In[14]:


squared_value(-0.25)

