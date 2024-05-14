```python
# import libreries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")
```


```python
df = pd.DataFrame(dict(time=np.arange(500),value=np.random.randn(500).cumsum()))
g=sns.relplot(x="time",y="value",kind="line",data=df)
g.fig.autofmt_xdate()
plt.show()
```


    
![png](output_1_0.png)
    



```python
df = pd.DataFrame(np.random.randn(500,2).cumsum(axis=0),columns=["x","y"])
sns.relplot(x="x",y="y",sort=False,kind="line",data=df)
plt.show()
```


    
![png](output_2_0.png)
    


## fmri dataset


```python
fmri = sns.load_dataset("fmri")
sns.relplot(x="timepoint", y="signal",kind="line",data=fmri)
plt.show()
```


    
![png](output_4_0.png)
    



```python
sns.relplot(x="timepoint",y="signal",ci=None,kind="line",data=fmri)
plt.show()
```


    
![png](output_5_0.png)
    



```python
sns.relplot(x="timepoint",y="signal",kind="line",ci="sd",data=fmri)
plt.show()
```


    
![png](output_6_0.png)
    



```python
sns.relplot(x="timepoint",y="signal",estimator=None,kind="line",data=fmri)
plt.show()
```


    
![png](output_7_0.png)
    



```python
sns.relplot(x="timepoint",y="signal",hue="event",kind="line",data=fmri)
plt.show()
```


    
![png](output_8_0.png)
    



```python
sns.relplot(x="timepoint",y="signal",hue="region",style="event",kind="line", data=fmri)
plt.show()

```


    
![png](output_9_0.png)
    



```python
sns.relplot(x="timepoint",y="signal",hue="region",style="event",dashes=False,markers=True, kind="line", data=fmri)
plt.show()
```


    
![png](output_10_0.png)
    



```python
sns.relplot(x="timepoint",y="signal",hue="event",style="event", kind="line", data=fmri)
plt.show()
```


    
![png](output_11_0.png)
    



```python
sns.relplot(x="timepoint",y="signal",hue="region",units="subject", estimator=None, kind="line", data=fmri.query("event == 'stim'"))
plt.show()
```


    
![png](output_12_0.png)
    


### dots dataset


```python
dots = sns.load_dataset("dots").query("align == 'dots'")
sns.relplot(x="time",y="firing_rate",hue="coherence",style="choice",kind="line",data=dots)
plt.show()
```


    
![png](output_14_0.png)
    



```python
palette = sns.cubehelix_palette(light = .8,n_colors=6)
sns.relplot(x="time",y="firing_rate",hue="coherence",style="choice",palette=palette,kind="line",data=dots)
plt.show()
```


    
![png](output_15_0.png)
    



```python
from matplotlib.colors import LogNorm
```


```python
palette = sns.cubehelix_palette(light=.7, n_colors=6)
sns.relplot(x="time", y="firing_rate", hue="coherence", style="choice", hue_norm=LogNorm(), kind="line", data=dots)
plt.show()
```


    
![png](output_17_0.png)
    



```python
sns.relplot(x="time", y="firing_rate",size="coherence", style="choice",kind="line", data=dots)
plt.show()
```


    
![png](output_18_0.png)
    



```python
df = pd.DataFrame(dict(time=pd.date_range("2019-1-1", periods=500), value=np.random.randn(500).cumsum()))

g = sns.relplot(x="time", y="value", kind="line", data=df)
g.fig.autofmt_xdate()
plt.show()
```


    
![png](output_19_0.png)
    



```python

```
