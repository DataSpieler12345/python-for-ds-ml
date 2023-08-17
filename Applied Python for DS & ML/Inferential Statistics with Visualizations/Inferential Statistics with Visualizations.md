### Inferential Statistics with Visualizations


```python
#common imports 
import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
import scipy.stats as stats
%matplotlib inline 

import warnings
warnings.filterwarnings("ignore")

#set color style
sns.set(color_codes = True)
```

#### Load the data sets


```python
df_titanic = sns.load_dataset("titanic")
df_iris = sns.load_dataset("iris")
df_tips = sns.load_dataset("tips")
```

### Titanic dataset

* Ideal for data visualization 

#### seaborn catplot documentation
#### link : https://seaborn.pydata.org/generated/seaborn.catplot.html


```python
df_titanic.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 891 entries, 0 to 890
    Data columns (total 15 columns):
     #   Column       Non-Null Count  Dtype   
    ---  ------       --------------  -----   
     0   survived     891 non-null    int64   
     1   pclass       891 non-null    int64   
     2   sex          891 non-null    object  
     3   age          714 non-null    float64 
     4   sibsp        891 non-null    int64   
     5   parch        891 non-null    int64   
     6   fare         891 non-null    float64 
     7   embarked     889 non-null    object  
     8   class        891 non-null    category
     9   who          891 non-null    object  
     10  adult_male   891 non-null    bool    
     11  deck         203 non-null    category
     12  embark_town  889 non-null    object  
     13  alive        891 non-null    object  
     14  alone        891 non-null    bool    
    dtypes: bool(2), category(2), float64(2), int64(4), object(5)
    memory usage: 80.7+ KB
    


```python
df_titanic.head(10)
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
      <th>survived</th>
      <th>pclass</th>
      <th>sex</th>
      <th>age</th>
      <th>sibsp</th>
      <th>parch</th>
      <th>fare</th>
      <th>embarked</th>
      <th>class</th>
      <th>who</th>
      <th>adult_male</th>
      <th>deck</th>
      <th>embark_town</th>
      <th>alive</th>
      <th>alone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>7.2500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>71.2833</td>
      <td>C</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.9250</td>
      <td>S</td>
      <td>Third</td>
      <td>woman</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>53.1000</td>
      <td>S</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>8.0500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>True</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>8.4583</td>
      <td>Q</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Queenstown</td>
      <td>no</td>
      <td>True</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0</td>
      <td>1</td>
      <td>male</td>
      <td>54.0</td>
      <td>0</td>
      <td>0</td>
      <td>51.8625</td>
      <td>S</td>
      <td>First</td>
      <td>man</td>
      <td>True</td>
      <td>E</td>
      <td>Southampton</td>
      <td>no</td>
      <td>True</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>2.0</td>
      <td>3</td>
      <td>1</td>
      <td>21.0750</td>
      <td>S</td>
      <td>Third</td>
      <td>child</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>27.0</td>
      <td>0</td>
      <td>2</td>
      <td>11.1333</td>
      <td>S</td>
      <td>Third</td>
      <td>woman</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1</td>
      <td>2</td>
      <td>female</td>
      <td>14.0</td>
      <td>1</td>
      <td>0</td>
      <td>30.0708</td>
      <td>C</td>
      <td>Second</td>
      <td>child</td>
      <td>False</td>
      <td>NaN</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



#### Bar Charts


```python
#seaborn catplot
sns.catplot(x = "sex", data = df_titanic, kind = "count")
plt.show()

```


    
![png](output_9_0.png)
    



```python
#seaborn catplot
sns.catplot(x = "pclass", data = df_titanic, kind = "count")
plt.show()
```


    
![png](output_10_0.png)
    



```python
sns.catplot(x = "pclass", data = df_titanic, kind = "count", hue = "sex")
plt.show()
```


    
![png](output_11_0.png)
    



```python
sns.catplot(x = "pclass", data = df_titanic, kind = "count", col = "sex")
plt.show()
```


    
![png](output_12_0.png)
    



```python
sns.catplot(x="pclass", data=df_titanic, kind="count", col="sex", hue="embarked")
plt.show()
```


    
![png](output_13_0.png)
    


#### Box Plots


```python
df_titanic.head()
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
      <th>survived</th>
      <th>pclass</th>
      <th>sex</th>
      <th>age</th>
      <th>sibsp</th>
      <th>parch</th>
      <th>fare</th>
      <th>embarked</th>
      <th>class</th>
      <th>who</th>
      <th>adult_male</th>
      <th>deck</th>
      <th>embark_town</th>
      <th>alive</th>
      <th>alone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>7.2500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>71.2833</td>
      <td>C</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.9250</td>
      <td>S</td>
      <td>Third</td>
      <td>woman</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>53.1000</td>
      <td>S</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>8.0500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.boxplot(x = df_titanic["age"])
plt.show()
```


    
![png](output_16_0.png)
    



```python
sns.boxplot(y = df_titanic["age"])
plt.show()
```


    
![png](output_17_0.png)
    



```python
sns.boxplot(x =df_titanic["age"], y = df_titanic["sex"])
plt.show()
```


    
![png](output_18_0.png)
    


### Iris dataset

* for scatterplot


```python
df_iris.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 150 entries, 0 to 149
    Data columns (total 5 columns):
     #   Column        Non-Null Count  Dtype  
    ---  ------        --------------  -----  
     0   sepal_length  150 non-null    float64
     1   sepal_width   150 non-null    float64
     2   petal_length  150 non-null    float64
     3   petal_width   150 non-null    float64
     4   species       150 non-null    object 
    dtypes: float64(4), object(1)
    memory usage: 6.0+ KB
    


```python
df_iris.head(5)
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
  </tbody>
</table>
</div>



#### seaborn distplot documentation
#### link : https://seaborn.pydata.org/generated/seaborn.distplot.html

#### Histogram


```python
df_iris["species"].value_counts()
```




    species
    setosa        50
    versicolor    50
    virginica     50
    Name: count, dtype: int64




```python
sns.distplot(df_iris["sepal_length"], hist = True, kde = True)
plt.show()
```


    
![png](output_25_0.png)
    



```python
sns.distplot(df_iris["sepal_length"], hist = True, kde = True, bins = 20)
plt.show()
```


    
![png](output_26_0.png)
    



```python
sns.distplot(df_iris["sepal_length"], hist = True, kde = True, rug = True)
plt.show()
```


    
![png](output_27_0.png)
    



```python
sns.distplot(df_iris["sepal_length"], hist = True, kde = True, bins = 20)
sns.distplot(df_iris["sepal_width"], hist = True, kde = True, bins = 20)
plt.show()
```


    
![png](output_28_0.png)
    



```python
sns.distplot(df_iris["sepal_length"], hist = False, kde = True, bins = 20, color = "blue", label = "Sepal Length")
sns.distplot(df_iris["sepal_width"], hist = False, kde = True, bins = 20, color = "red", label = "Sepal Width")
plt.legend()
plt.xlabel("Measure in CM")
plt.ylabel("Frequency")
plt.title("Sepal Characteristics", size = 15)
plt.show()
```


    
![png](output_29_0.png)
    



```python
sns.distplot(df_iris["sepal_length"], hist = True, kde = False, bins = 20, color = "blue", label = "Sepal Length")
sns.distplot(df_iris["sepal_width"], hist = True, kde = False, bins = 20, color = "red", label = "Sepal Width")
plt.legend()
plt.xlabel("Measure in CM")
plt.ylabel("Frequency")
plt.title("Sepal Characteristics", size = 15)
plt.show()
```


    
![png](output_30_0.png)
    


#### Box Plots


```python
df_iris["species"].value_counts()
```




    species
    setosa        50
    versicolor    50
    virginica     50
    Name: count, dtype: int64




```python
sns.boxplot(x = df_iris["species"], y = df_iris["sepal_width"])
plt.show()
```


    
![png](output_33_0.png)
    



```python
#from numpy import random
from numpy import random
```


```python
#Normal distribution
normal_data = random.normal(loc = 100, scale = 10, size = 1000)
```


```python
normal_data
```




    array([ 98.37077406, 104.94503109,  97.21005643, 110.18904235,
           105.13635598, 110.69338464, 103.22887679,  82.79960863,
           104.42219851, 107.45742021,  86.59830922, 104.31140474,
           102.13885181,  89.02734756,  94.65496627, 106.59679669,
            91.15884958, 104.57589982,  99.79183409,  99.49497018,
            93.34653337, 115.52490815,  89.89800865,  94.69479573,
           103.51537315,  98.77979063,  96.59905133, 100.81389093,
           111.25588067,  74.80853024, 108.65641303,  96.49798668,
            99.53686056, 101.38265305,  95.27932909, 106.48793828,
            94.00157225,  99.69971516,  91.54905822,  96.22992552,
           106.50435963,  90.08549599, 107.23196066, 115.76639547,
           107.22947566,  99.93386619, 100.45951598,  95.62461392,
            84.16940104, 108.19589054,  85.68311098, 108.97390871,
           102.13568787, 102.67421955,  96.79337871,  98.05502103,
            86.42260638, 104.22449908,  91.92891881,  99.56740253,
           110.27004988,  92.34119899, 103.22057891,  79.89611096,
            98.34302121, 107.24112886, 106.15719512, 106.83751424,
           105.50713319,  76.94010379, 107.22806013,  97.92371181,
           106.51539697, 110.2556517 ,  88.35933084, 112.59909666,
           102.86002044,  96.67487127, 103.50128688, 114.01433542,
            96.77448823, 105.24661451, 101.09865521,  79.71836462,
            88.1514342 , 106.11363679, 114.4500554 , 113.68451417,
           117.79474327, 102.97260923, 118.46246841, 100.50673611,
            84.86200815,  84.29396207,  95.89383964, 104.33758893,
            93.27816501, 110.34785967,  82.40530024, 108.33939905,
            79.28563612,  91.9540755 ,  79.90659282,  89.47508758,
           113.21826213,  93.80130614,  88.70957432,  78.54122207,
           100.43738754,  86.35259724,  95.99827542, 107.94103951,
           108.98399268,  85.21745072,  88.68637216,  92.51471488,
           111.90762498, 102.85599839,  92.91686632, 106.76905227,
           102.98443327,  93.34406349,  94.18514624,  90.27375949,
           116.42090775,  95.77397585,  98.5156413 ,  99.79450644,
            99.95544925,  85.54574432,  93.19000603,  94.53723018,
            87.76937295, 107.63638853, 111.22319196, 111.1300449 ,
           119.29136024, 104.42544458,  92.53278833, 106.1034176 ,
            90.82101421, 102.07346911,  96.09920244, 116.09959891,
            94.53429144, 105.74314915, 104.85258546,  92.96558785,
           113.0917424 ,  99.62293223,  95.28435232, 106.14665531,
           105.05780212, 108.78495215, 100.07642329, 106.5842899 ,
           108.88430309, 108.68810088, 109.95320198,  88.61627314,
           108.43728008,  98.09871906, 106.27469369,  97.96044592,
            94.02163809, 114.00705587,  78.03192487,  99.60906224,
           114.69069202,  94.91415926,  94.30026613,  98.11732246,
           117.61449862,  80.3600584 ,  94.3720894 , 101.95582656,
           115.66894752, 103.13601281,  95.27746337,  94.15682581,
            90.10963015,  93.06507952, 117.8346248 ,  86.49287565,
           107.82286876, 101.79868785,  95.8537022 , 105.24229721,
            95.20988829,  90.81241723, 108.70499195,  92.14040955,
            96.86512918,  98.58457951, 106.67465657, 107.46104017,
            88.54296349,  81.4242854 ,  78.50770989,  90.74296573,
            97.54852767, 103.10276373, 101.54740415,  97.02020471,
            90.5302653 , 105.56923451, 105.59198299,  98.08380262,
           100.52315001,  91.98203466,  99.0532443 , 110.20164509,
           104.99007765, 105.76768787,  95.87840606,  82.70992751,
           107.64812493, 110.70564104, 105.8788906 , 102.74233204,
           104.78861577,  85.91651863,  82.53459399, 107.99341919,
            93.94698131, 107.86999237,  91.13629882,  96.21867992,
            99.39013001,  99.77472541,  97.52479611,  88.10413979,
            96.6070876 , 112.80625567, 102.39836559,  91.87148092,
            88.78716189,  93.06885237,  90.32529148, 103.96408278,
           103.63998223,  92.34729313, 112.99743039, 113.60835538,
           104.34490603,  94.52296406, 100.93310187,  87.58134342,
           106.94643431, 108.51136781,  94.08382443,  96.48256478,
           101.50539732,  98.70237272, 107.70728722,  91.35122035,
           103.42522237,  97.80333735,  97.58428891,  92.8358175 ,
            98.4225572 , 115.19290617, 107.81829114, 101.4773508 ,
           101.0950472 , 114.41105012,  80.83572392,  98.21180652,
           106.98180202,  81.23618887, 104.12363535,  89.06672414,
           103.17147161,  80.84543258, 112.47437485, 118.81535214,
            95.99570567,  85.69802406, 102.36383505,  86.1170471 ,
           113.20020551,  93.12484485,  79.60332864,  93.66410839,
            91.67715003,  85.11164508,  88.93139445, 105.23569932,
           110.16171908, 108.49071097,  96.23098463, 103.34468898,
           125.96293893,  95.68516658, 111.01154682, 104.92732404,
            92.03914744,  97.99625066, 102.12755945,  90.62944088,
            81.44855525, 115.58554376, 101.4994125 , 118.1837513 ,
           105.64129749,  88.39084936, 102.1777025 ,  94.44965368,
            88.61664491, 105.13464158, 105.91031133,  94.56919701,
            96.05682143, 111.63834853,  95.25522116,  95.64489108,
           104.62054752, 104.86778697,  83.9939807 , 106.63060042,
            97.4428147 ,  99.67781479, 105.09613781,  92.64814929,
            82.41771113,  99.51308315,  83.77746853, 117.80392628,
           101.70416458,  97.56948312, 129.42960372, 103.39705051,
           102.19499037,  85.87778462,  83.15018269, 104.43848312,
           112.96462924,  85.04478108, 102.91315808, 103.75618304,
            93.79293897,  99.28913831,  81.9469582 ,  83.03870933,
           106.44370359,  72.74269279, 105.24260253,  84.0977929 ,
           107.5038858 ,  96.75427403, 104.11117047,  85.7763735 ,
           102.20360484,  92.4404764 , 102.3965129 , 102.30486275,
           109.89335409,  94.02160221, 101.92388612,  84.90204968,
            77.71041117, 100.13352501,  93.27188732,  92.80226383,
           109.82133996,  88.12341133, 106.40333876,  85.70792328,
           112.01196528,  87.15709255, 107.83154574,  80.33109299,
           112.95460449, 103.81182088, 109.29034625,  82.91488214,
            94.83146717, 108.88593541, 104.22826602,  96.44577388,
           102.39883372,  97.65998422, 104.61966532,  84.46702128,
           111.61175594,  97.41423551,  99.6444192 ,  95.93421748,
           111.81982551, 109.03390137, 102.50152645, 108.11524407,
            76.55392095, 105.40132048, 117.09814687, 127.20256535,
           105.74350041, 105.06021033,  94.1382769 , 104.86330197,
            90.4454952 , 111.57915912, 102.58774673, 108.29373385,
           100.09863417,  80.8364063 ,  97.91081412,  92.86304406,
            90.40363423,  95.9880094 , 107.56875477, 104.47696525,
            99.72248608, 108.8298949 ,  82.86572084,  81.4212775 ,
            99.31545475, 106.1297551 ,  75.68418081, 107.54362518,
            74.36987229, 110.22025429,  88.820395  ,  88.54301846,
           108.13953195, 115.6946127 ,  90.51397744,  98.39057155,
            99.98689696, 115.654646  ,  93.06844822,  87.24730454,
            96.05562613, 107.63671767,  98.85491204, 103.87830429,
            97.29006629,  97.33064381,  97.01464666, 101.98231854,
            99.77787036,  90.60214407,  94.3303326 , 110.70497354,
            83.86565452,  89.61419778,  96.77443871,  85.80571451,
            76.94019621,  98.42274387, 118.14893176, 114.18164469,
            81.55481018,  98.20101777,  99.94229347,  98.96323282,
           100.4505547 , 107.37149463, 108.24681987,  97.47485208,
           110.06676826, 103.61583689,  89.34194047, 114.16651019,
           104.88795201,  99.70006637,  86.90445705, 109.50188173,
           102.89179103, 101.76135835, 103.51793851,  91.72666969,
            98.40005611,  90.80651031,  82.34944155,  77.60159877,
            85.13511968, 108.302374  ,  96.35147841, 103.43347555,
           110.62590051, 108.47988224, 115.34978741, 107.24989931,
           102.94374888,  91.23801864,  85.50648349,  88.8307089 ,
            94.04748111,  82.89989086, 116.31485095, 101.23774583,
           100.07650685, 108.21337351,  90.18590138, 103.70600999,
           105.09678971,  99.60260043,  92.84193843,  91.80933965,
            94.1998601 , 117.39251999, 109.50489482, 102.89584599,
           101.73041257, 114.93460661,  86.07037383,  90.41244543,
           107.17799871,  91.07423237, 111.85800175,  94.1669246 ,
           105.30854956,  92.12363315, 110.23071139,  94.25070668,
            95.97716699,  99.12070921, 103.34773086, 100.57055683,
           100.29499754,  99.2983503 ,  72.67641508, 101.21834982,
            93.0544421 , 105.9386845 , 100.26890505, 106.82330364,
            93.6315295 ,  98.22350537,  99.63404257,  98.07259703,
            99.97089087,  96.00759138, 122.83391279, 108.39106241,
            91.26911403,  97.01020253, 112.6668403 ,  89.1018999 ,
            69.62232724,  85.76480594, 100.81947175,  95.56070897,
           115.58425159, 112.25696776,  97.91316152,  93.00158958,
           104.00255853, 126.99898561, 100.57807535, 100.18574528,
           102.84354017,  86.66447135,  94.32895359,  93.16817595,
            98.36347148,  91.11715371,  92.39365262,  92.60417068,
           105.5227129 , 105.79916274, 100.08443749,  98.06656481,
            84.64607818, 115.72629623, 103.26028616,  92.33955175,
           110.83337115,  99.81748869,  85.61785559, 116.44216152,
            86.57516619,  98.75320162,  95.9648919 ,  91.36101118,
            82.42361527,  94.16018118, 100.7357847 ,  99.98029299,
            98.24874101,  87.00717355,  81.45846771,  91.73138882,
           103.47790455, 117.53604753,  95.19110971, 109.57844174,
            95.19398503, 111.34707695,  87.12548082,  95.68313729,
           100.73276447,  90.54059786, 113.11805831,  91.81100428,
           107.49250166, 103.36981346,  79.50889765, 100.05230425,
            96.49664821, 102.56379126,  97.75656896, 103.45496944,
           106.29419266, 103.45933488,  83.68374078,  94.29334924,
           101.05097408,  98.19580002, 106.91831336, 102.740205  ,
           100.01487537,  95.98415651, 109.58053363, 106.22470792,
            95.14687299,  90.40246243, 119.78417342, 123.86974583,
            96.38126322,  99.22120429,  95.26134248, 109.35194791,
           106.42237913, 107.3520103 ,  87.3209961 ,  80.95613841,
            97.69771281,  94.14418349,  84.52613117, 103.12108557,
           108.85485334,  94.28277763,  94.47698369,  98.26403924,
            90.19698351,  98.42198805,  86.89379158,  93.08308629,
           117.56116042,  99.36595886, 104.95837414, 104.57094891,
            99.90137907, 113.61698457,  83.59075263, 105.98341802,
           101.35391022,  90.94436568, 100.10958713, 100.40519592,
            98.03666458, 110.37862935,  89.9431265 ,  91.94195679,
            93.66425983,  97.97354425,  85.87875457,  92.26665086,
           111.98825358, 105.78323899, 101.74905654,  80.523588  ,
           109.98509708, 107.83859863,  99.82059348,  95.18216088,
           100.7095769 ,  98.13921213, 107.74792503, 103.59816956,
           104.38560508,  95.49498499, 104.00603607, 108.79320121,
            85.47893594, 112.14280053, 113.69623346,  96.64161905,
           117.10495977,  84.1783013 , 111.31547971, 103.68994483,
           111.56712699,  93.5739525 , 104.77460688, 111.53387335,
            86.77808527,  89.72038264, 117.07396229,  98.36347505,
            94.86406322,  83.56145849,  98.93800971, 104.94561993,
           102.04275236, 123.50725108, 105.79655812,  85.82061757,
            97.74842872, 104.77875369,  98.62560408, 111.66779282,
            95.17817747,  94.30836905, 104.34185916,  96.98038058,
            96.94096785, 103.14381552,  99.71127451, 108.23451014,
           106.99566396, 100.4053021 , 110.67964553, 115.66112658,
            94.45507165, 108.20758945,  86.2597609 ,  81.78671006,
            85.83859305,  95.72660443, 103.98030741, 108.54877632,
           124.17015479, 104.34625142, 114.16589864, 103.05367328,
           108.66766229, 107.6681677 , 119.84421885,  89.35731665,
           116.31147779, 110.76603744,  96.94218084,  92.85985987,
            97.10570234,  96.2072822 ,  94.42710748,  93.86710825,
           111.71235397, 116.18786931, 100.01477153, 101.78546572,
            92.83495184,  91.97950066, 110.21079176, 109.20072268,
            99.29874725,  93.30977121, 112.44188602, 104.76576198,
           104.3630829 , 102.55979085, 105.00815959,  90.72269589,
            88.31454491, 109.55480881, 106.25116029,  91.44244372,
            88.58473919,  94.98903894,  97.17749394, 103.73904768,
            85.47572968,  97.82098014,  89.68258516,  90.18070217,
           104.37195499, 110.39499205,  84.52992242, 107.72590045,
            83.4788194 , 107.57303669,  99.14620118, 114.54202504,
            96.11205373,  82.82593362,  99.52169072, 100.34107427,
           110.19071988,  96.45263206,  96.8002082 ,  96.42388378,
           102.66422993, 116.63806962,  94.36315117, 105.99068522,
            91.24870435,  85.39593193,  88.96877248,  87.16183896,
            88.32877246,  94.6326122 ,  78.55735517,  90.24933955,
           104.66439094,  85.74156549,  87.50162909, 104.48560327,
           104.55453153, 112.87132697,  98.37364433,  92.79996404,
           101.90333735, 116.3934895 ,  81.21979545,  94.73512024,
           104.23863913,  90.11979931,  97.45425235,  95.4120274 ,
            83.879688  ,  78.87042423,  92.76164298,  95.16632568,
           101.92223452,  91.2723593 , 103.3473569 ,  86.45480496,
           100.15617661, 117.52246277,  95.49670416,  85.5603686 ,
           111.78604327,  97.45956709, 112.1251902 , 105.28454471,
            89.76090379, 103.68744468, 109.45327567,  96.28923962,
            93.31477667, 100.23999986,  95.83708256,  94.41339178,
           101.51351031,  98.02222451,  81.30507148, 110.44285322,
           125.1551835 ,  99.92187153, 106.71225799,  97.28012805,
            89.45365741,  91.92258384, 103.6548695 , 100.85355002,
            92.74220455,  90.81310443, 109.86798625, 107.10306718,
           102.76178465,  98.93077749, 115.12569741, 114.66695841,
           102.35906249, 114.97395402, 100.92573602,  86.9787612 ,
            99.36844559,  93.65499528,  82.21392348, 105.73323615,
           120.2927408 , 101.54041009,  99.83632097,  92.14850261,
           110.478998  , 111.342032  , 109.9288689 , 120.11720939,
            97.13869217,  93.32736852,  95.08745705, 108.68690902,
           112.19512928, 102.12052518, 126.4730607 , 107.65465442,
            99.60501273, 110.83161161,  86.46879648, 106.76673379,
           103.33682343, 104.78744275, 112.39017714, 103.28116242,
            92.98355438,  81.86511023,  84.87180979, 100.10976593,
            98.13186333,  96.18256761, 113.48124823, 112.67061792,
           113.92716627, 108.52334996, 100.32937205,  98.23661835,
            87.6662286 , 104.67420846, 100.89103364,  95.44804074,
           108.39597031,  93.23097787, 107.51426093,  96.06154021,
            88.70346248, 109.3055287 ,  94.16390789, 108.5831543 ,
           119.72306269,  82.08091157, 101.51880643, 120.53657524,
           105.96960329,  91.64443024, 117.31829407,  86.57320305,
           110.19432448,  92.77255512, 104.73472882, 123.8709143 ,
           103.85466314, 115.05248551, 111.67234961, 105.06495547,
           114.37422853,  93.60000374, 102.95004831,  82.39254295,
           103.34098423, 107.4030093 ,  89.69188072,  93.12794565,
           105.20757742,  96.73119882,  89.34504584,  88.38703996,
           107.86050553,  84.26597687,  96.19063245, 101.49245681,
           106.38199213,  90.62602439, 102.50318892,  90.74182329,
           126.56324422,  84.67809092,  96.29469423, 116.89090548,
            84.43348677,  90.81871969, 106.51514749, 100.46672052,
           100.98868934,  97.58210747, 104.34070541, 102.50931842,
            98.82287726, 106.40686773,  95.79482981,  99.20220174,
            99.17313178, 108.60161182, 109.28917076, 114.76736876,
           103.61626963, 101.64006361, 101.05460305, 100.04676185,
           103.28968449, 123.19138214,  89.86858498,  96.81856919,
            99.9991888 , 105.70110449, 102.83741573,  87.71290484,
            85.38280933,  96.07466685,  93.30147521, 109.91044578,
           104.56268999,  90.80215833,  91.42480997, 101.74250777,
           130.69784727,  86.89417293,  92.10794004, 103.48611524,
           113.24530462, 100.32732633, 108.91050985,  88.06466988,
            97.37662502,  92.95424408,  90.92776364,  99.78495484])




```python
sns.boxplot(x = normal_data)
```




    <Axes: >




    
![png](output_37_1.png)
    


#### Scatter Plots


```python
df_iris.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 150 entries, 0 to 149
    Data columns (total 5 columns):
     #   Column        Non-Null Count  Dtype  
    ---  ------        --------------  -----  
     0   sepal_length  150 non-null    float64
     1   sepal_width   150 non-null    float64
     2   petal_length  150 non-null    float64
     3   petal_width   150 non-null    float64
     4   species       150 non-null    object 
    dtypes: float64(4), object(1)
    memory usage: 6.0+ KB
    


```python
sns.regplot(x = "sepal_length", y = "sepal_width", data = df_iris)
plt.show()
```


    
![png](output_40_0.png)
    



```python
#correlation
numeric_columns = df_iris.select_dtypes(include=['float64'])
correlation_matrix = numeric_columns.corr()
print(correlation_matrix)
```

                  sepal_length  sepal_width  petal_length  petal_width
    sepal_length      1.000000    -0.117570      0.871754     0.817941
    sepal_width      -0.117570     1.000000     -0.428440    -0.366126
    petal_length      0.871754    -0.428440      1.000000     0.962865
    petal_width       0.817941    -0.366126      0.962865     1.000000
    


```python
sns.regplot(x = "petal_length", y = "petal_width", data = df_iris)
plt.show()
```


    
![png](output_42_0.png)
    



```python
sns.regplot(x = "petal_length", y = "petal_width", data = df_iris,
           scatter_kws = {"color":"black"}, line_kws = {"color":"red"})
plt.show()
```


    
![png](output_43_0.png)
    



```python
sns.regplot(x = "petal_length", y = "petal_width", data = df_iris, fit_reg = False,
           scatter_kws = {"color":"black"}, line_kws = {"color":"red"})
plt.show()
```


    
![png](output_44_0.png)
    



```python
sns.regplot(x = "petal_length", y = "petal_width", data = df_iris, ci = 90,
           scatter_kws = {"color":"black"}, line_kws = {"color":"red"})
plt.show()
```


    
![png](output_45_0.png)
    


### Advanced Visualizations

#### seaborn lmplot documentation
#### link : https://seaborn.pydata.org/generated/seaborn.lmplot.html


```python
df_tips.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 244 entries, 0 to 243
    Data columns (total 7 columns):
     #   Column      Non-Null Count  Dtype   
    ---  ------      --------------  -----   
     0   total_bill  244 non-null    float64 
     1   tip         244 non-null    float64 
     2   sex         244 non-null    category
     3   smoker      244 non-null    category
     4   day         244 non-null    category
     5   time        244 non-null    category
     6   size        244 non-null    int64   
    dtypes: category(4), float64(2), int64(1)
    memory usage: 7.4 KB
    


```python
df_tips
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
num_columns = df_tips.select_dtypes(include=['float64', 'int64'])
corr_matrix = num_columns.corr()
print(corr_matrix)
```

                total_bill       tip      size
    total_bill    1.000000  0.675734  0.598315
    tip           0.675734  1.000000  0.489299
    size          0.598315  0.489299  1.000000
    


```python
sns.lmplot(x = "total_bill", y = "tip", data = df_tips)
plt.show()
```


    
![png](output_51_0.png)
    



```python
# difference?
sns.regplot(x = "total_bill", y = "tip", data = df_tips)
plt.show()
```


    
![png](output_52_0.png)
    



```python
sns.lmplot(x = "total_bill", y = "tip", data = df_tips, hue = "sex")
plt.show()
```


    
![png](output_53_0.png)
    



```python
sns.lmplot(x = "total_bill", y = "tip", data = df_tips, hue = "sex",
          markers = ["x","o"])
plt.show()
```


    
![png](output_54_0.png)
    



```python
sns.lmplot(x = "total_bill", y = "tip", data = df_tips, hue = "sex",
          markers = ["x","o"], palette = ["red","black"])
plt.show()
```


    
![png](output_55_0.png)
    



```python
df_tips["time"].value_counts()
```




    time
    Dinner    176
    Lunch      68
    Name: count, dtype: int64




```python
sns.lmplot(x = "total_bill", y = "tip", data = df_tips, hue = "time",
          markers = ["x","o"], palette = ["red","black"])
plt.show()
```


    
![png](output_57_0.png)
    



```python
df_tips["day"].value_counts()
```




    day
    Sat     87
    Sun     76
    Thur    62
    Fri     19
    Name: count, dtype: int64




```python
sns.lmplot(x = "total_bill", y = "tip", data = df_tips, hue = "day")
plt.show()
```


    
![png](output_59_0.png)
    



```python
sns.lmplot(x = "total_bill", y = "tip", data = df_tips, hue = "sex",
          markers = ["*","o"], palette = ["red","black"])
plt.show()
```


    
![png](output_60_0.png)
    



```python
sns.lmplot(x = "total_bill", y = "tip", data = df_tips, hue = "sex", col = "smoker",
          markers = ["*","o"], palette = ["red","black"])
plt.show()
```


    
![png](output_61_0.png)
    



```python
sns.lmplot(x = "total_bill", y = "tip", data = df_tips, hue = "sex", col = "smoker", row = "time",
          markers = ["*","o"], palette = ["red","black"])
plt.show()
```


    
![png](output_62_0.png)
    


#### seaborn Jointplot documentation
#### link : https://seaborn.pydata.org/generated/seaborn.jointplot.html


```python
sns.jointplot(x = "total_bill", y = "tip", data = df_tips, kind = "reg")
plt.show()
```


    
![png](output_64_0.png)
    



```python
sns.jointplot(x = "total_bill", y = "tip", data = df_tips, kind = "kde")
plt.show()
```


    
![png](output_65_0.png)
    



```python
num_columns = df_tips.select_dtypes(include=['float64', 'int64'])
corr_matrix = num_columns.corr()
print(corr_matrix)
```

                total_bill       tip      size
    total_bill    1.000000  0.675734  0.598315
    tip           0.675734  1.000000  0.489299
    size          0.598315  0.489299  1.000000
    


```python
sns.jointplot(x="total_bill", y="tip", data=df_tips, kind="reg")
plt.annotate("Pearsonr = {:.2f}".format(stats.pearsonr(df_tips["total_bill"], df_tips["tip"])[0]),
             xy=(0.5, 0.9), xycoords='axes fraction', fontsize=12)
plt.show()
```


    
![png](output_67_0.png)
    

