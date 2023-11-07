#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="5">Exploring Python String Methods</font></b></h1></center>

# In[1]:


s = 'Price per unit'
s


# In[11]:


s1 = s.replace('Price', 'Cost')
s1


# In[12]:


s1.startswith('Cost')


# In[13]:


s1.startswith('cost')


# In[14]:


s1.startswith('Price')


# In[15]:


s1.endswith('nit')


# In[16]:


s1.endswith('nits')


# In[17]:


s1


# In[18]:


s1.split()


# In[19]:


len(s1.split())


# In[20]:


s1.split(' ')


# In[23]:


s1.split(" ")


# In[25]:


#valueError = empty separator
s1.split('')


# In[27]:


s1.split('per')


# In[28]:


s1.split(' ', maxsplit = 0)


# In[34]:


s1.split(' ', 0)


# In[35]:


s1.split(' ', 1)


# In[36]:


s1.split(' ', 2)


# In[37]:


s1.split(' ', 3)


# In[29]:


s2 = 'Mr., John, Wilson'


# In[30]:


s2.split(',')


# In[31]:


s2.split(',')[0]


# In[32]:


s2.split(',')[1]


# In[33]:


s2.split(',')[2]


# #### another string methods

# In[38]:


s3 = 'Mrs. Amy Moore'


# In[39]:


s3.upper()


# In[40]:


s3.lower()


# In[41]:


s3.capitalize()


# In[42]:


s3.title()


# In[43]:


s3 == s3.title()


# In[44]:


'Cost per unit'.title()


# ### another example

# In[45]:


s4 = '  quarterly earnings report   '


# In[46]:


s4.strip()


# In[47]:


s4.strip(' ')


# In[48]:


s4.strip(' r')


# In[49]:


s4.strip(' qt')


# In[50]:


s4.strip('qt')


# In[51]:


s4.lstrip()


# In[53]:


s4.rstrip()


# In[54]:


s4.strip(' quarterly')


# In[55]:


s4.lstrip('  quarterly')


# In[60]:


s5 = s4.strip()
s5


# In[62]:


s5.lstrip('quarterly')


# In[63]:


s5.rstrip('report')


# In[64]:


s6 = ' %&!quarterly earnings report *'


# In[65]:


s6.strip(' !@#$%^&*()')

