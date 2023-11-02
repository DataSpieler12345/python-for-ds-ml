#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="6">Structure with different data types</font></b></h1></center>

# <center><h1><b><font size="4">Strings</font></b></h1></center>

# In[1]:


this = "my long string"


# In[2]:


type(this)


# In[3]:


this[0:2]


# In[4]:


new = "...ends here!"


# In[5]:


type(new)


# In[6]:


new[0:3]


# In[9]:


new_string = this + new
new_string


# In[10]:


print(new_string*2)


# ### create a function

# In[11]:


count = 0
for letter in new_string:
    if(letter == "n"):
        count +=1
        #count = count + 1
print(count, "n's found in string.")


# In[12]:


len(new_string)

