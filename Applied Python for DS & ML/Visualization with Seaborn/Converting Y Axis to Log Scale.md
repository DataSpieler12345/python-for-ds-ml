```python
import seaborn as sns
```


```python
name = ['Manuel','Björn','Juan','Benjamin','Thorsten','Bobby','Michelle','Peter','Blake','Paul']
salary = [10000000,8000000,7500000,500000,250000,100000,70000,50000,20000,5000]
```


```python
sns.barplot(x=name,y=salary)
```




    <Axes: >




    
![png](output_2_1.png)
    



```python
g = sns.barplot(x=name,y=salary)
g.set_yscale("log")
```


    
![png](output_3_0.png)
    



```python

```
