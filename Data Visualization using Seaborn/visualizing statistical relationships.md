# Scatter Plot


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
# set background
sns.set(style="darkgrid")
```


```python
# load the dataset
tips = sns.load_dataset("tips")
tips
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>239</th>
      <td>29.03</td>
      <td>5.92</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>240</th>
      <td>27.18</td>
      <td>2.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>241</th>
      <td>22.67</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>242</th>
      <td>17.82</td>
      <td>1.75</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>243</th>
      <td>18.78</td>
      <td>3.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
<p>244 rows × 7 columns</p>
</div>




```python
# relplot
sns.relplot(x="total_bill", y="tip", data=tips);
plt.show()
```


    
![png](output_4_0.png)
    



```python
sns.relplot(x="total_bill",y="tip",hue="smoker",data=tips)
plt.show()
```


    
![png](output_5_0.png)
    



```python
sns.relplot(x="total_bill",y="tip",hue="smoker",style="time",data=tips)
plt.show()
```


    
![png](output_6_0.png)
    



```python
sns.relplot(x="total_bill",y="tip",hue="size",palette="ch:r=-5,l=.75",data=tips)
plt.show()
```


    
![png](output_7_0.png)
    



```python
sns.relplot(x="total_bill",y="tip",hue="size",data=tips)
plt.show()
```


    
![png](output_8_0.png)
    



```python
sns.relplot(x="total_bill",y="tip",size="size",sizes=(15,200),data=tips);
plt.show()
```


    
![png](output_9_0.png)
    



```python
# load again the dataset
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
```


```python
tips = sns.load_dataset("tips")
ax=sns.scatterplot(x="total_bill",y="tip",data=tips)
plt.show()
```


    
![png](output_11_0.png)
    



```python
ax = sns.scatterplot(x="total_bill",y="tip",hue="time",data=tips)
plt.show()
```


    
![png](output_12_0.png)
    



```python
# group them
ax = sns.scatterplot(x="total_bill",y="tip",hue="time",style="time",data=tips)
plt.show()
```


    
![png](output_13_0.png)
    



```python
ax = sns.scatterplot(x="total_bill",y="tip",hue="day",style="time",data=tips)
plt.show()
```


    
![png](output_14_0.png)
    



```python
ax = sns.scatterplot(x="total_bill",y="tip",size="size",data=tips)
plt.show()
```


    
![png](output_15_0.png)
    



```python
ax = sns.scatterplot(x="total_bill",y="tip",hue="size",size="size",data=tips)
plt.show()
```


    
![png](output_16_0.png)
    


###  continuos color map




```python
cmap = sns.cubehelix_palette(dark=.3, light=.8, as_cmap=True)
```


```python
ax = sns.scatterplot(x="total_bill",y="tip",hue="size",size="size", palette=cmap,data=tips)
plt.show()
```


    
![png](output_19_0.png)
    



```python
cmap = sns.cubehelix_palette(dark=.3, light=.8, as_cmap=True)
```


```python
tips = sns.load_dataset("tips") 

ax = sns.scatterplot(x="total_bill", y="tip", hue="size", size="size", palette="viridis", legend="full", data=tips)
plt.show()
```


    
![png](output_21_0.png)
    



```python
ax = sns.scatterplot(x="total_bill",y="tip",s=100,color=".2",marker="+",data=tips)
plt.show()
```


    
![png](output_22_0.png)
    


## Iris dataset


```python
iris =sns.load_dataset("iris")
```


```python
iris = sns.load_dataset("iris")  

ax = sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", style="species", data=iris)
plt.show()
```


    
![png](output_25_0.png)
    



```python
index = pd.date_range("1 1 2000",periods=100,freq="m",name="date")
data = np.random.randn(100,4).cumsum(axis=0)
wide_df = pd.DataFrame(data,index,["a","b","c","d"])
ax = sns.scatterplot(data=wide_df)
plt.show()
```


    
![png](output_26_0.png)
    

