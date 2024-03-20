# Importing pandas

import pandas as pd

# Creating a data frame
df = pd.read_csv(r'D:\CODING STAGE\PYTHON\PythonforDataScience\Python_Working_with_Data\worldcities.csv')
print(df) # complete df
print(df.head()) # para ver el head del data frame 

# Slicing in data frame = se lee, 0:2 = son las filas del df y 0:3 = columnas
z = df.ix[0:2,0:3]
print(z)

# Slicing
z = df.ix[0:1,"city":"city_ascii"] # cambiando el nombre  la columna 1 del df

# Creating a nuevo df con un sola columna que es population
population_df = df[['population']]
print(population_df)  # devuelve el resultado con los datos del nuevo df de la columna population
print(population_df.head()) # devuelve el head del df population

# Creating a DF con multiples columnas 
country_city_population_df = df[["country", "city", "population"]]
print(country_city_population_df)
print(country_city_population_df.head())

# Accessing to first row, first column 
first_row1 = country_city_population_df.ix[1,"country"]
print(first_row1)

first_row = country_city_population_df.ix[0,0]
print(first_row)

# Accessing to second row, first column 
second_row = country_city_population_df.ix[1,0]
print(second_row)

# Accessing to first row, third column 
first_row_third_column = country_city_population_df.ix[0,2]

# Accessing to second row, third column 
second_row_third_column = country_city_population_df.ix[1,2]

