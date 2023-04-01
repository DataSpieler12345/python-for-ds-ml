#!/usr/bin/env python
# coding: utf-8

# # Generating Maps with Python
# 
# Estimated time needed: **30** minutes
# 
# <b>Developer:</b> DataSpieler12345
# 
# ## Objectives
# 
# After completing this lab you will be able to:
# 
# *   Visualize geospatial data with Folium

# ## Introduction
# 
# In this lab, we will learn how to create maps for different objectives. To do that, we will part ways with Matplotlib and work with another Python visualization library, namely **Folium**. What is nice about **Folium** is that it was developed for the sole purpose of visualizing geospatial data. While other libraries are available to visualize geospatial data, such as **plotly**, they might have a cap on how many API calls you can make within a defined time frame. **Folium**, on the other hand, is completely free.

# # Exploring Datasets with *pandas* and Matplotlib<a id="0"></a>
# 
# Toolkits: This lab heavily relies on [*pandas*](http://pandas.pydata.org/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01) and [*Numpy*](http://www.numpy.org/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01) for data wrangling, analysis, and visualization. The primary plotting library we will explore in this lab is [**Folium**](https://github.com/python-visualization/folium/).
# 
# Datasets:
# 
# 1.  San Francisco Police Department Incidents for the year 2016 - [Police Department Incidents](https://data.sfgov.org/Public-Safety/Police-Department-Incidents-Previous-Year-2016-/ritf-b9ki?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01) from San Francisco public data portal. Incidents derived from San Francisco Police Department (SFPD) Crime Incident Reporting system. Updated daily, showing data for the entire year of 2016. Address and location has been anonymized by moving to mid-block or to an intersection.
# 
# 2.  Immigration to Canada from 1980 to 2013 - [International migration flows to and from selected countries - The 2015 revision](http://www.un.org/en/development/desa/population/migration/data/empirical2/migrationflows.shtml?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01) from United Nation's website. The dataset contains annual data on the flows of international migrants as recorded by the countries of destination. The data presents both inflows and outflows according to the place of birth, citizenship or place of previous / next residence both for foreigners and nationals. For this lesson, we will focus on the Canadian Immigration data
# 

# # Downloading and Prepping Data <a id="2"></a>
# 

# Import Primary Modules:

# In[85]:


import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library


# # Introduction to Folium <a id="4"></a>

# Folium is a powerful Python library that helps you create several types of Leaflet maps. The fact that the Folium results are interactive makes this library very useful for dashboard building.
# 
# From the official Folium documentation page:
# 
# > Folium builds on the data wrangling strengths of the Python ecosystem and the mapping strengths of the Leaflet.js library. Manipulate your data in Python, then visualize it in on a Leaflet map via Folium.
# 
# > Folium makes it easy to visualize data that's been manipulated in Python on an interactive Leaflet map. It enables both the binding of data to a map for choropleth visualizations as well as passing Vincent/Vega visualizations as markers on the map.
# 
# > The library has a number of built-in tilesets from OpenStreetMap, Mapbox, and Stamen, and supports custom tilesets with Mapbox or Cloudmade API keys. Folium supports both GeoJSON and TopoJSON overlays, as well as the binding of data to those overlays to create choropleth maps with color-brewer color schemes.
# 

# #### Let's install **Folium**

# **Folium** is not available by default. So, we first need to install it before we are able to import it.

# In[ ]:


get_ipython().system('pip install folium')


# In[87]:


#!pip3 install folium==0.5.0
import folium

print('Folium installed and imported!')


# Generating the world map is straightforward in **Folium**. You simply create a **Folium** *Map* object, and then you display it. What is attractive about **Folium** maps is that they are interactive, so you can zoom into any region of interest despite the initial zoom level.

# In[88]:


# define the world map
world_map = folium.Map()

# display world map
world_map


# Go ahead. Try zooming in and out of the rendered map above.

# You can customize this default definition of the world map by specifying the centre of your map, and the initial zoom level.
# 
# All locations on a map are defined by their respective *Latitude* and *Longitude* values. So you can create a map and pass in a center of *Latitude* and *Longitude* values of **\[0, 0]**.
# 
# For a defined center, you can also define the initial zoom level into that location when the map is rendered. **The higher the zoom level the more the map is zoomed into the center**.
# 
# Let's create a map centered around Canada and play with the zoom level to see how it affects the rendered map.

# In[89]:


# define the world map centered around Canada with a low zoom level
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4)

# display world map
world_map


# Let's create the map again with a higher zoom level.

# In[90]:


# define the world map centered around Canada with a higher zoom level
world_map = folium.Map(location=[56.130, -106.35], zoom_start=8)

# display world map
world_map


# As you can see, the higher the zoom level the more the map is zoomed into the given center.

# **Question**: Create a map of Nicaragua with a zoom level of 4.

# In[91]:


#define Nicaragua geolocation coordinates
Nic_latitude = 12.865416
Nic_longitude = -85.207230

# define the world map centered around Canada with a higher zoom level
Nic_map = folium.Map(location=[Nic_latitude, Nic_longitude], zoom_start=4)

# display world map
Nic_map


# In[92]:


# Moers geolocation coordinates
moers_latitude = 51.453049
moers_longitude = 6.621750

# define the world map centered around Canada with a higher zoom level
moers_map = folium.Map(location=[moers_latitude, moers_longitude], zoom_start=4)

# display world map
moers_map


# Another cool feature of **Folium** is that you can generate different map styles.

# ### A. Stamen Toner Maps
# 
# These are high-contrast B+W (black and white) maps. They are perfect for data mashups and exploring river meanders and coastal zones.
# 

# Let's create a Stamen Toner map of canada with a zoom level of 4.

# In[93]:


# create a Stamen Toner map of the world centered around Canada
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4, tiles='Stamen Toner')

# display map
world_map


# Feel free to zoom in and out to see how this style compares to the default one.
# 

# ### B. Stamen Terrain Maps
# 
# These are maps that feature hill shading and natural vegetation colors. They showcase advanced labeling and linework generalization of dual-carriageway roads.
# 

# Let's create a Stamen Terrain map of Canada with zoom level 4.

# In[94]:


# create a Stamen Toner map of the world centered around Nicaragua
world_map = folium.Map(location=[12.865416, -85.207230], zoom_start=4, tiles='Stamen Terrain')

# display map
world_map


# Feel free to zoom in and out to see how this style compares to Stamen Toner, and the default style.

# Zoom in and notice how the borders start showing as you zoom in, and the displayed country names are in English.

# **Question**: Create a map of Mexico to visualize its hill shading and natural vegetation. Use a zoom level of 6.

# In[95]:


#define Mexico's geolocation coordinates
mexico_latitude = 23.6345 
mexico_longitude = -102.5528

# define the world map centered around Canada with a higher zoom level
mexico_map = folium.Map(location=[mexico_latitude, mexico_longitude], zoom_start=6, tiles='Stamen Terrain')

# display world map
mexico_map


# # Maps with Markers <a id="6"></a>

# Let's download and import the data on police department incidents using *pandas* `read_csv()` method.
# 

# Download the dataset and read it into a *pandas* dataframe:

# In[96]:


import pandas as pd


# In[97]:


df_incidents = pd.read_csv('Police_Department_Incidents_-_Previous_Year__2016_.csv')

print('Dataset downloaded and read into a pandas dataframe')


# In[98]:


df_incidents.head()


# So each row consists of 13 features:
# 
# > 1.  **IncidntNum**: Incident Number
# > 2.  **Category**: Category of crime or incident
# > 3.  **Descript**: Description of the crime or incident
# > 4.  **DayOfWeek**: The day of week on which the incident occurred
# > 5.  **Date**: The Date on which the incident occurred
# > 6.  **Time**: The time of day on which the incident occurred
# > 7.  **PdDistrict**: The police department district
# > 8.  **Resolution**: The resolution of the crime in terms whether the perpetrator was arrested or not
# > 9.  **Address**: The closest address to where the incident took place
# > 10. **X**: The longitude value of the crime location
# > 11. **Y**: The latitude value of the crime location
# > 12. **Location**: A tuple of the latitude and the longitude values
# > 13. **PdId**: The police department ID

# Let's find out how many entries there are in our dataset.
# 

# In[99]:


df_incidents.shape


# So the dataframe consists of 150,500 crimes, which took place in the year 2016. In order to reduce computational cost, let's just work with the first 100 incidents in this dataset.
# 

# In[100]:


# get the first 100 crimes in the df_incidents dataframe
limit = 100
df_incidents = df_incidents.iloc[0:limit, :]


# Let's confirm that our dataframe now consists only of 100 crimes.

# In[101]:


df_incidents.shape


# Now that we reduced the data a little, let's visualize where these crimes took place in the city of San Francisco. We will use the default style, and we will initialize the zoom level to 12.
# 

# In[102]:


# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42


# In[103]:


# create map and display it
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# display the map of San Francisco
sanfran_map


# Now let's superimpose the locations of the crimes onto the map. The way to do that in **Folium** is to create a *feature group* with its own features and style and then add it to the `sanfran_map`.

# In[104]:


# instantiate a feature group for the incidents in the dataframe
incidents = folium.map.FeatureGroup()

# loop through the 100 crimes and add each to the incidents feature group
for lat, lng, in zip(df_incidents.Y, df_incidents.X):
    incidents.add_child(
        folium.features.CircleMarker(
            [lat, lng],
            radius=5, # define how big you want the circle markers to be
            color='yellow',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
    )

# add incidents to map
sanfran_map.add_child(incidents)


# You can also add some pop-up text that would get displayed when you hover over a marker. Let's make each marker display the category of the crime when hovered over.
# 

# In[105]:


# instantiate a feature group for the incidents in the dataframe
incidents = folium.map.FeatureGroup()

# loop through the 100 crimes and add each to the incidents feature group
for lat, lng, in zip(df_incidents.Y, df_incidents.X):
    incidents.add_child(
        folium.features.CircleMarker(
            [lat, lng],
            radius=5, # define how big you want the circle markers to be
            color='yellow',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
    )

# add pop-up text to each marker on the map
latitudes = list(df_incidents.Y)
longitudes = list(df_incidents.X)
labels = list(df_incidents.Category)

for lat, lng, label in zip(latitudes, longitudes, labels):
    folium.Marker([lat, lng], popup=label).add_to(sanfran_map)    
    
# add incidents to map
sanfran_map.add_child(incidents)


# Isn't this really cool? Now you are able to know what crime category occurred at each marker.
# 
# If you find the map to be so congested will all these markers, there are two remedies to this problem. The simpler solution is to remove these location markers and just add the text to the circle markers themselves as follows:
# 

# In[106]:


# create map and display it
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# loop through the 100 crimes and add each to the map
for lat, lng, label in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.features.CircleMarker(
        [lat, lng],
        radius=5, # define how big you want the circle markers to be
        color='yellow',
        fill=True,
        popup=label,
        fill_color='blue',
        fill_opacity=0.6
    ).add_to(sanfran_map)

# show map
sanfran_map


# The other proper remedy is to group the markers into different clusters. Each cluster is then represented by the number of crimes in each neighborhood. These clusters can be thought of as pockets of San Francisco which you can then analyze separately.
# 
# To implement this, we start off by instantiating a *MarkerCluster* object and adding all the data points in the dataframe to this object.
# 

# In[107]:


from folium import plugins

# let's start again with a clean copy of the map of San Francisco
sanfran_map = folium.Map(location = [latitude, longitude], zoom_start = 12)

# instantiate a mark cluster object for the incidents in the dataframe
incidents = plugins.MarkerCluster().add_to(sanfran_map)

# loop through the dataframe and add each data point to the mark cluster
for lat, lng, label, in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.Marker(
        location=[lat, lng],
        icon=None,
        popup=label,
    ).add_to(incidents)

# display map
sanfran_map


# Notice how when you zoom out all the way, all markers are grouped into one cluster, *the global cluster*, of 100 markers or crimes, which is the total number of crimes in our dataframe. Once you start zooming in, the *global cluster* will start breaking up into smaller clusters. Zooming in all the way will result in individual markers.
# 

# # Choropleth Maps <a id="8"></a>
# 
# A `Choropleth` map is a thematic map in which areas are shaded or patterned in proportion to the measurement of the statistical variable being displayed on the map, such as population density or per-capita income. The choropleth map provides an easy way to visualize how a measurement varies across a geographic area, or it shows the level of variability within a region. Below is a `Choropleth` map of the US depicting the population by square mile per state.
# 
# <img src = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/labs/Module%205/images/2000_census_population_density_map_by_state.png" width = 600> 
# 
