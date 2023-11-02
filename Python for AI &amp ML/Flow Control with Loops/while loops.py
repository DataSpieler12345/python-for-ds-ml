#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="6">While Loops</font></b></h1></center>

# In[7]:


# sum the number 1 through N

N = int(input("Enter your N value here: "))

summation = 0
j = 1

while j <= N: 
    summation = summation + j
    j = j + 1
    
print("Our summation is equal to", summation)


# In[8]:


counter = 0

while counter < 5:
    print("Interior loop value")
    counter = counter + 1 
else:
    print("Exterior loop value")


# In[9]:


counter = 0

while counter <= 5:
    print("Interior loop value")
    counter = counter + 1 
else:
    print("Exterior loop value")


# In[ ]:




