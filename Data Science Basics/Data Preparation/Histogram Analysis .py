#!/usr/bin/env python
# coding: utf-8

# # Histogram

# #### Plot a Histogram in Python using Matplotlib

# In[1]:


import matplotlib.pyplot as plt 

x = [1,1,2,3,3,5,7,8,9,10,
    10,11,11,13,13,15,16,17,18,18,
    18,19,20,21,21,23,24,24,25,25,
    25,25,26,26,26,27,27,27,27,27,
    29,30,30,31,33,34,34,34,35,36,
    36,37,37,38,38,39,40,41,41,42,
    43,44,45,45,46,47,48,48,49,50,
    51,52,53,54,55,55,56,57,58,60,
    61,63,64,65,66,68,70,71,72,74,
    75,77,81,83,84,87,89,90,90,91
    ]

plt.hist(x, bins=10)
plt.show()


# In[2]:


#style your histogram
plt.style.use('ggplot')
plt.hist(x, bins=10)
plt.show()


# #### Histogram for distribution

# In[3]:


import numpy as np 
from matplotlib import colors 
from matplotlib.ticker import PercentFormatter 

# Creating dataset 
np.random.seed(23685752) 
N_points = 10000
n_bins = 20

# Creating distribution 
x = np.random.randn(N_points) 
y = .8 ** x + np.random.randn(10000) + 25

# Creating histogram 
fig, axs = plt.subplots(1, 1, figsize =(10, 7),tight_layout = True) 

axs.hist(x, bins = n_bins) 

# Show plot 
plt.show() 


# ### Costomized Histogram

# #### The code below modifies the above histogram for a better view and accurate readings

# In[8]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# Creating dataset
np.random.seed(23685752)
N_points = 10000
n_bins = 20

# Creating distribution
x = np.random.randn(N_points)
y = 0.8 ** x + np.random.randn(10000) + 25
legend = ['distribution']

# Creating histogram
fig, axs = plt.subplots(1, 1, figsize=(10, 7), tight_layout=True)

# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    axs.spines[s].set_visible(False)

# Remove x, y ticks
axs.xaxis.set_ticks_position('none')
axs.yaxis.set_ticks_position('none')

# Add padding between axes and labels
axs.xaxis.set_tick_params(pad=5)
axs.yaxis.set_tick_params(pad=10)

# Add x, y gridlines
axs.grid(which='both', color='grey', linestyle='-.', linewidth=0.5, alpha=0.6)

# Add Text watermark
fig.text(0.9, 0.15, 'Jeeteshgavande30', fontsize=12, color='red', ha='right', va='bottom', alpha=0.7)

# Creating histogram
N, bins, patches = axs.hist(x, bins=n_bins)

# Setting color
fracs = ((N ** (1 / 5)) / N.max())
norm = colors.Normalize(fracs.min(), fracs.max())

for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

# Adding extra features
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.legend(legend)
plt.title('Customized histogram')

# Show plot
plt.show()


# In[ ]:




