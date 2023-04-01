# Generating Maps with Python

Estimated time needed: **30** minutes

<b>Developer:</b> DataSpieler12345

## Objectives

After completing this lab you will be able to:

*   Visualize geospatial data with Folium

## Introduction

In this lab, we will learn how to create maps for different objectives. To do that, we will part ways with Matplotlib and work with another Python visualization library, namely **Folium**. What is nice about **Folium** is that it was developed for the sole purpose of visualizing geospatial data. While other libraries are available to visualize geospatial data, such as **plotly**, they might have a cap on how many API calls you can make within a defined time frame. **Folium**, on the other hand, is completely free.

# Exploring Datasets with *pandas* and Matplotlib<a id="0"></a>

Toolkits: This lab heavily relies on [*pandas*](http://pandas.pydata.org/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01) and [*Numpy*](http://www.numpy.org/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01) for data wrangling, analysis, and visualization. The primary plotting library we will explore in this lab is [**Folium**](https://github.com/python-visualization/folium/).

Datasets:

1.  San Francisco Police Department Incidents for the year 2016 - [Police Department Incidents](https://data.sfgov.org/Public-Safety/Police-Department-Incidents-Previous-Year-2016-/ritf-b9ki?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01) from San Francisco public data portal. Incidents derived from San Francisco Police Department (SFPD) Crime Incident Reporting system. Updated daily, showing data for the entire year of 2016. Address and location has been anonymized by moving to mid-block or to an intersection.

2.  Immigration to Canada from 1980 to 2013 - [International migration flows to and from selected countries - The 2015 revision](http://www.un.org/en/development/desa/population/migration/data/empirical2/migrationflows.shtml?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01) from United Nation's website. The dataset contains annual data on the flows of international migrants as recorded by the countries of destination. The data presents both inflows and outflows according to the place of birth, citizenship or place of previous / next residence both for foreigners and nationals. For this lesson, we will focus on the Canadian Immigration data


# Downloading and Prepping Data <a id="2"></a>


Import Primary Modules:


```python
import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
```

# Introduction to Folium <a id="4"></a>

Folium is a powerful Python library that helps you create several types of Leaflet maps. The fact that the Folium results are interactive makes this library very useful for dashboard building.

From the official Folium documentation page:

> Folium builds on the data wrangling strengths of the Python ecosystem and the mapping strengths of the Leaflet.js library. Manipulate your data in Python, then visualize it in on a Leaflet map via Folium.

> Folium makes it easy to visualize data that's been manipulated in Python on an interactive Leaflet map. It enables both the binding of data to a map for choropleth visualizations as well as passing Vincent/Vega visualizations as markers on the map.

> The library has a number of built-in tilesets from OpenStreetMap, Mapbox, and Stamen, and supports custom tilesets with Mapbox or Cloudmade API keys. Folium supports both GeoJSON and TopoJSON overlays, as well as the binding of data to those overlays to create choropleth maps with color-brewer color schemes.


#### Let's install **Folium**

**Folium** is not available by default. So, we first need to install it before we are able to import it.


```python
!pip install folium
```


```python
#!pip3 install folium==0.5.0
import folium

print('Folium installed and imported!')
```

    Folium installed and imported!
    

Generating the world map is straightforward in **Folium**. You simply create a **Folium** *Map* object, and then you display it. What is attractive about **Folium** maps is that they are interactive, so you can zoom into any region of interest despite the initial zoom level.


```python
# define the world map
world_map = folium.Map()

# display world map
world_map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;

    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;

        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;

    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-1.12.4.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;

            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_5ab0950c8f4b1503ceeb707c5447ed71 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            &lt;/style&gt;

&lt;/head&gt;
&lt;body&gt;


            &lt;div class=&quot;folium-map&quot; id=&quot;map_5ab0950c8f4b1503ceeb707c5447ed71&quot; &gt;&lt;/div&gt;

&lt;/body&gt;
&lt;script&gt;


            var map_5ab0950c8f4b1503ceeb707c5447ed71 = L.map(
                &quot;map_5ab0950c8f4b1503ceeb707c5447ed71&quot;,
                {
                    center: [0, 0],
                    crs: L.CRS.EPSG3857,
                    zoom: 1,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );





            var tile_layer_ccc3744411375177d51f0076a5ff35c2 = L.tileLayer(
                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,
                {&quot;attribution&quot;: &quot;Data by \u0026copy; \u003ca target=\&quot;_blank\&quot; href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://www.openstreetmap.org/copyright\&quot;\u003eODbL\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            ).addTo(map_5ab0950c8f4b1503ceeb707c5447ed71);

&lt;/script&gt;
&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



Go ahead. Try zooming in and out of the rendered map above.

You can customize this default definition of the world map by specifying the centre of your map, and the initial zoom level.

All locations on a map are defined by their respective *Latitude* and *Longitude* values. So you can create a map and pass in a center of *Latitude* and *Longitude* values of **\[0, 0]**.

For a defined center, you can also define the initial zoom level into that location when the map is rendered. **The higher the zoom level the more the map is zoomed into the center**.

Let's create a map centered around Canada and play with the zoom level to see how it affects the rendered map.


```python
# define the world map centered around Canada with a low zoom level
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4)

# display world map
world_map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;

    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;

        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;

    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-1.12.4.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;

            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_fd6033647a1c9f7169557bda1a050475 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            &lt;/style&gt;

&lt;/head&gt;
&lt;body&gt;


            &lt;div class=&quot;folium-map&quot; id=&quot;map_fd6033647a1c9f7169557bda1a050475&quot; &gt;&lt;/div&gt;

&lt;/body&gt;
&lt;script&gt;


            var map_fd6033647a1c9f7169557bda1a050475 = L.map(
                &quot;map_fd6033647a1c9f7169557bda1a050475&quot;,
                {
                    center: [56.13, -106.35],
                    crs: L.CRS.EPSG3857,
                    zoom: 4,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );





            var tile_layer_c4967445b1299eb40365fe1376b35e7f = L.tileLayer(
                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,
                {&quot;attribution&quot;: &quot;Data by \u0026copy; \u003ca target=\&quot;_blank\&quot; href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://www.openstreetmap.org/copyright\&quot;\u003eODbL\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            ).addTo(map_fd6033647a1c9f7169557bda1a050475);

&lt;/script&gt;
&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



Let's create the map again with a higher zoom level.


```python
# define the world map centered around Canada with a higher zoom level
world_map = folium.Map(location=[56.130, -106.35], zoom_start=8)

# display world map
world_map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;

    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;

        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;

    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-1.12.4.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;

            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_6f92614223069e046700228f06d3367e {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            &lt;/style&gt;

&lt;/head&gt;
&lt;body&gt;


            &lt;div class=&quot;folium-map&quot; id=&quot;map_6f92614223069e046700228f06d3367e&quot; &gt;&lt;/div&gt;

&lt;/body&gt;
&lt;script&gt;


            var map_6f92614223069e046700228f06d3367e = L.map(
                &quot;map_6f92614223069e046700228f06d3367e&quot;,
                {
                    center: [56.13, -106.35],
                    crs: L.CRS.EPSG3857,
                    zoom: 8,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );





            var tile_layer_257571862a35366033bde30ace908527 = L.tileLayer(
                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,
                {&quot;attribution&quot;: &quot;Data by \u0026copy; \u003ca target=\&quot;_blank\&quot; href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://www.openstreetmap.org/copyright\&quot;\u003eODbL\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            ).addTo(map_6f92614223069e046700228f06d3367e);

&lt;/script&gt;
&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



As you can see, the higher the zoom level the more the map is zoomed into the given center.

**Question**: Create a map of Nicaragua with a zoom level of 4.


```python
#define Nicaragua geolocation coordinates
Nic_latitude = 12.865416
Nic_longitude = -85.207230

# define the world map centered around Canada with a higher zoom level
Nic_map = folium.Map(location=[Nic_latitude, Nic_longitude], zoom_start=4)

# display world map
Nic_map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;

    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;

        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;

    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-1.12.4.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;

            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_5fb4a4f0ca42255d681856e9439796d8 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            &lt;/style&gt;

&lt;/head&gt;
&lt;body&gt;


            &lt;div class=&quot;folium-map&quot; id=&quot;map_5fb4a4f0ca42255d681856e9439796d8&quot; &gt;&lt;/div&gt;

&lt;/body&gt;
&lt;script&gt;


            var map_5fb4a4f0ca42255d681856e9439796d8 = L.map(
                &quot;map_5fb4a4f0ca42255d681856e9439796d8&quot;,
                {
                    center: [12.865416, -85.20723],
                    crs: L.CRS.EPSG3857,
                    zoom: 4,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );





            var tile_layer_af66405145e01195f8c7cf13be4aba18 = L.tileLayer(
                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,
                {&quot;attribution&quot;: &quot;Data by \u0026copy; \u003ca target=\&quot;_blank\&quot; href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://www.openstreetmap.org/copyright\&quot;\u003eODbL\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            ).addTo(map_5fb4a4f0ca42255d681856e9439796d8);

&lt;/script&gt;
&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
# Moers geolocation coordinates
moers_latitude = 51.453049
moers_longitude = 6.621750

# define the world map centered around Canada with a higher zoom level
moers_map = folium.Map(location=[moers_latitude, moers_longitude], zoom_start=4)

# display world map
moers_map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;

    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;

        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;

    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-1.12.4.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;

            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_ae75cae15f333a3593f2dbbbb4bf149f {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            &lt;/style&gt;

&lt;/head&gt;
&lt;body&gt;


            &lt;div class=&quot;folium-map&quot; id=&quot;map_ae75cae15f333a3593f2dbbbb4bf149f&quot; &gt;&lt;/div&gt;

&lt;/body&gt;
&lt;script&gt;


            var map_ae75cae15f333a3593f2dbbbb4bf149f = L.map(
                &quot;map_ae75cae15f333a3593f2dbbbb4bf149f&quot;,
                {
                    center: [51.453049, 6.62175],
                    crs: L.CRS.EPSG3857,
                    zoom: 4,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );





            var tile_layer_2e15bc6515537b9da472646d0c35ba77 = L.tileLayer(
                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,
                {&quot;attribution&quot;: &quot;Data by \u0026copy; \u003ca target=\&quot;_blank\&quot; href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://www.openstreetmap.org/copyright\&quot;\u003eODbL\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            ).addTo(map_ae75cae15f333a3593f2dbbbb4bf149f);

&lt;/script&gt;
&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



Another cool feature of **Folium** is that you can generate different map styles.

### A. Stamen Toner Maps

These are high-contrast B+W (black and white) maps. They are perfect for data mashups and exploring river meanders and coastal zones.


Let's create a Stamen Toner map of canada with a zoom level of 4.


```python
# create a Stamen Toner map of the world centered around Canada
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4, tiles='Stamen Toner')

# display map
world_map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;

    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;

        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;

    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-1.12.4.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;

            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_9bc7342ed6055d816ff481ad68cf9ba1 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            &lt;/style&gt;

&lt;/head&gt;
&lt;body&gt;


            &lt;div class=&quot;folium-map&quot; id=&quot;map_9bc7342ed6055d816ff481ad68cf9ba1&quot; &gt;&lt;/div&gt;

&lt;/body&gt;
&lt;script&gt;


            var map_9bc7342ed6055d816ff481ad68cf9ba1 = L.map(
                &quot;map_9bc7342ed6055d816ff481ad68cf9ba1&quot;,
                {
                    center: [56.13, -106.35],
                    crs: L.CRS.EPSG3857,
                    zoom: 4,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );





            var tile_layer_409d49c160c4bbc9f556c6c9184f8771 = L.tileLayer(
                &quot;https://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}.png&quot;,
                {&quot;attribution&quot;: &quot;Map tiles by \u003ca target=\&quot;_blank\&quot; href=\&quot;http://stamen.com\&quot;\u003eStamen Design\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://creativecommons.org/licenses/by/3.0\&quot;\u003eCC BY 3.0\u003c/a\u003e. Data by \u0026copy; \u003ca target=\&quot;_blank\&quot; href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://www.openstreetmap.org/copyright\&quot;\u003eODbL\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            ).addTo(map_9bc7342ed6055d816ff481ad68cf9ba1);

&lt;/script&gt;
&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



Feel free to zoom in and out to see how this style compares to the default one.


### B. Stamen Terrain Maps

These are maps that feature hill shading and natural vegetation colors. They showcase advanced labeling and linework generalization of dual-carriageway roads.


Let's create a Stamen Terrain map of Canada with zoom level 4.


```python
# create a Stamen Toner map of the world centered around Nicaragua
world_map = folium.Map(location=[12.865416, -85.207230], zoom_start=4, tiles='Stamen Terrain')

# display map
world_map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;

    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;

        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;

    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-1.12.4.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;

            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_62d137424a8541604bf238b2517425e8 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            &lt;/style&gt;

&lt;/head&gt;
&lt;body&gt;


            &lt;div class=&quot;folium-map&quot; id=&quot;map_62d137424a8541604bf238b2517425e8&quot; &gt;&lt;/div&gt;

&lt;/body&gt;
&lt;script&gt;


            var map_62d137424a8541604bf238b2517425e8 = L.map(
                &quot;map_62d137424a8541604bf238b2517425e8&quot;,
                {
                    center: [12.865416, -85.20723],
                    crs: L.CRS.EPSG3857,
                    zoom: 4,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );





            var tile_layer_904fb299248f8dc05dcfb22c80b82c4e = L.tileLayer(
                &quot;https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg&quot;,
                {&quot;attribution&quot;: &quot;Map tiles by \u003ca target=\&quot;_blank\&quot; href=\&quot;http://stamen.com\&quot;\u003eStamen Design\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://creativecommons.org/licenses/by/3.0\&quot;\u003eCC BY 3.0\u003c/a\u003e. Data by \u0026copy; \u003ca target=\&quot;_blank\&quot; href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://creativecommons.org/licenses/by-sa/3.0\&quot;\u003eCC BY SA\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            ).addTo(map_62d137424a8541604bf238b2517425e8);

&lt;/script&gt;
&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



Feel free to zoom in and out to see how this style compares to Stamen Toner, and the default style.

Zoom in and notice how the borders start showing as you zoom in, and the displayed country names are in English.

**Question**: Create a map of Mexico to visualize its hill shading and natural vegetation. Use a zoom level of 6.


```python
#define Mexico's geolocation coordinates
mexico_latitude = 23.6345 
mexico_longitude = -102.5528

# define the world map centered around Canada with a higher zoom level
mexico_map = folium.Map(location=[mexico_latitude, mexico_longitude], zoom_start=6, tiles='Stamen Terrain')

# display world map
mexico_map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;

    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;

        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;

    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-1.12.4.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;

            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_e7b0cdcb4aba60070352160422589017 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            &lt;/style&gt;

&lt;/head&gt;
&lt;body&gt;


            &lt;div class=&quot;folium-map&quot; id=&quot;map_e7b0cdcb4aba60070352160422589017&quot; &gt;&lt;/div&gt;

&lt;/body&gt;
&lt;script&gt;


            var map_e7b0cdcb4aba60070352160422589017 = L.map(
                &quot;map_e7b0cdcb4aba60070352160422589017&quot;,
                {
                    center: [23.6345, -102.5528],
                    crs: L.CRS.EPSG3857,
                    zoom: 6,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );





            var tile_layer_aea69b813debd05dcbd32abf9ca53503 = L.tileLayer(
                &quot;https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg&quot;,
                {&quot;attribution&quot;: &quot;Map tiles by \u003ca target=\&quot;_blank\&quot; href=\&quot;http://stamen.com\&quot;\u003eStamen Design\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://creativecommons.org/licenses/by/3.0\&quot;\u003eCC BY 3.0\u003c/a\u003e. Data by \u0026copy; \u003ca target=\&quot;_blank\&quot; href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://creativecommons.org/licenses/by-sa/3.0\&quot;\u003eCC BY SA\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            ).addTo(map_e7b0cdcb4aba60070352160422589017);

&lt;/script&gt;
&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



# Maps with Markers <a id="6"></a>

Let's download and import the data on police department incidents using *pandas* `read_csv()` method.


Download the dataset and read it into a *pandas* dataframe:


```python
import pandas as pd
```


```python
df_incidents = pd.read_csv('Police_Department_Incidents_-_Previous_Year__2016_.csv')

print('Dataset downloaded and read into a pandas dataframe')
```

    Dataset downloaded and read into a pandas dataframe
    


```python
df_incidents.head()
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
      <th>IncidntNum</th>
      <th>Category</th>
      <th>Descript</th>
      <th>DayOfWeek</th>
      <th>Date</th>
      <th>Time</th>
      <th>PdDistrict</th>
      <th>Resolution</th>
      <th>Address</th>
      <th>X</th>
      <th>Y</th>
      <th>Location</th>
      <th>PdId</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>120058272</td>
      <td>WEAPON LAWS</td>
      <td>POSS OF PROHIBITED WEAPON</td>
      <td>Friday</td>
      <td>01/29/2016 12:00:00 AM</td>
      <td>11:00</td>
      <td>SOUTHERN</td>
      <td>ARREST, BOOKED</td>
      <td>800 Block of BRYANT ST</td>
      <td>-122.403405</td>
      <td>37.775421</td>
      <td>(37.775420706711, -122.403404791479)</td>
      <td>12005827212120</td>
    </tr>
    <tr>
      <th>1</th>
      <td>120058272</td>
      <td>WEAPON LAWS</td>
      <td>FIREARM, LOADED, IN VEHICLE, POSSESSION OR USE</td>
      <td>Friday</td>
      <td>01/29/2016 12:00:00 AM</td>
      <td>11:00</td>
      <td>SOUTHERN</td>
      <td>ARREST, BOOKED</td>
      <td>800 Block of BRYANT ST</td>
      <td>-122.403405</td>
      <td>37.775421</td>
      <td>(37.775420706711, -122.403404791479)</td>
      <td>12005827212168</td>
    </tr>
    <tr>
      <th>2</th>
      <td>141059263</td>
      <td>WARRANTS</td>
      <td>WARRANT ARREST</td>
      <td>Monday</td>
      <td>04/25/2016 12:00:00 AM</td>
      <td>14:59</td>
      <td>BAYVIEW</td>
      <td>ARREST, BOOKED</td>
      <td>KEITH ST / SHAFTER AV</td>
      <td>-122.388856</td>
      <td>37.729981</td>
      <td>(37.7299809672996, -122.388856204292)</td>
      <td>14105926363010</td>
    </tr>
    <tr>
      <th>3</th>
      <td>160013662</td>
      <td>NON-CRIMINAL</td>
      <td>LOST PROPERTY</td>
      <td>Tuesday</td>
      <td>01/05/2016 12:00:00 AM</td>
      <td>23:50</td>
      <td>TENDERLOIN</td>
      <td>NONE</td>
      <td>JONES ST / OFARRELL ST</td>
      <td>-122.412971</td>
      <td>37.785788</td>
      <td>(37.7857883766888, -122.412970537591)</td>
      <td>16001366271000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>160002740</td>
      <td>NON-CRIMINAL</td>
      <td>LOST PROPERTY</td>
      <td>Friday</td>
      <td>01/01/2016 12:00:00 AM</td>
      <td>00:30</td>
      <td>MISSION</td>
      <td>NONE</td>
      <td>16TH ST / MISSION ST</td>
      <td>-122.419672</td>
      <td>37.765050</td>
      <td>(37.7650501214668, -122.419671780296)</td>
      <td>16000274071000</td>
    </tr>
  </tbody>
</table>
</div>



So each row consists of 13 features:

> 1.  **IncidntNum**: Incident Number
> 2.  **Category**: Category of crime or incident
> 3.  **Descript**: Description of the crime or incident
> 4.  **DayOfWeek**: The day of week on which the incident occurred
> 5.  **Date**: The Date on which the incident occurred
> 6.  **Time**: The time of day on which the incident occurred
> 7.  **PdDistrict**: The police department district
> 8.  **Resolution**: The resolution of the crime in terms whether the perpetrator was arrested or not
> 9.  **Address**: The closest address to where the incident took place
> 10. **X**: The longitude value of the crime location
> 11. **Y**: The latitude value of the crime location
> 12. **Location**: A tuple of the latitude and the longitude values
> 13. **PdId**: The police department ID

Let's find out how many entries there are in our dataset.



```python
df_incidents.shape
```




    (150500, 13)



So the dataframe consists of 150,500 crimes, which took place in the year 2016. In order to reduce computational cost, let's just work with the first 100 incidents in this dataset.



```python
# get the first 100 crimes in the df_incidents dataframe
limit = 100
df_incidents = df_incidents.iloc[0:limit, :]
```

Let's confirm that our dataframe now consists only of 100 crimes.


```python
df_incidents.shape
```




    (100, 13)



Now that we reduced the data a little, let's visualize where these crimes took place in the city of San Francisco. We will use the default style, and we will initialize the zoom level to 12.



```python
# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42
```


```python
# create map and display it
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# display the map of San Francisco
sanfran_map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;

    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;

        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;

    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-1.12.4.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;

            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_fbfb269e38054ab8d9256217b0f93903 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            &lt;/style&gt;

&lt;/head&gt;
&lt;body&gt;


            &lt;div class=&quot;folium-map&quot; id=&quot;map_fbfb269e38054ab8d9256217b0f93903&quot; &gt;&lt;/div&gt;

&lt;/body&gt;
&lt;script&gt;


            var map_fbfb269e38054ab8d9256217b0f93903 = L.map(
                &quot;map_fbfb269e38054ab8d9256217b0f93903&quot;,
                {
                    center: [37.77, -122.42],
                    crs: L.CRS.EPSG3857,
                    zoom: 12,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );





            var tile_layer_04cfd757ba0b462ab92f2d45cce38b39 = L.tileLayer(
                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,
                {&quot;attribution&quot;: &quot;Data by \u0026copy; \u003ca target=\&quot;_blank\&quot; href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://www.openstreetmap.org/copyright\&quot;\u003eODbL\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);

&lt;/script&gt;
&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



Now let's superimpose the locations of the crimes onto the map. The way to do that in **Folium** is to create a *feature group* with its own features and style and then add it to the `sanfran_map`.


```python
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
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;

    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;

        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;

    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-1.12.4.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;

            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_fbfb269e38054ab8d9256217b0f93903 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            &lt;/style&gt;

&lt;/head&gt;
&lt;body&gt;


            &lt;div class=&quot;folium-map&quot; id=&quot;map_fbfb269e38054ab8d9256217b0f93903&quot; &gt;&lt;/div&gt;

&lt;/body&gt;
&lt;script&gt;


            var map_fbfb269e38054ab8d9256217b0f93903 = L.map(
                &quot;map_fbfb269e38054ab8d9256217b0f93903&quot;,
                {
                    center: [37.77, -122.42],
                    crs: L.CRS.EPSG3857,
                    zoom: 12,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );





            var tile_layer_04cfd757ba0b462ab92f2d45cce38b39 = L.tileLayer(
                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,
                {&quot;attribution&quot;: &quot;Data by \u0026copy; \u003ca target=\&quot;_blank\&quot; href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://www.openstreetmap.org/copyright\&quot;\u003eODbL\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


            var feature_group_434ca95166ce75d0655024f15063aa7b = L.featureGroup(
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


            var circle_marker_c8608ac9405b7ab2a175a889a63a742a = L.circleMarker(
                [37.775420706711, -122.403404791479],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_76154229a82f40e07e998b95ae7758b9 = L.circleMarker(
                [37.775420706711, -122.403404791479],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_087db3db12d3de2fe2e31224cec6bf2c = L.circleMarker(
                [37.7299809672996, -122.388856204292],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_8ac2b6ac8e33fe9475a5f1b9ecd81e84 = L.circleMarker(
                [37.7857883766888, -122.412970537591],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_5b859db49ba6f6acb90b3a52938f98cf = L.circleMarker(
                [37.7650501214668, -122.419671780296],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_0c1fb7f697f9074b1b1505b30d6d312f = L.circleMarker(
                [37.788018555829, -122.426077177375],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_5624dcddc6b5bad031f9c0a399f72210 = L.circleMarker(
                [37.7808789360214, -122.405721454567],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_23f89abda4232e56481a13b49ccd15f8 = L.circleMarker(
                [37.7839805592634, -122.411778295992],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_d36ca9c7359c3ed35efe0e7e0f5cccc6 = L.circleMarker(
                [37.7757876218293, -122.393357241451],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_afc4f01d9a5b31dd96bfbea89834ce04 = L.circleMarker(
                [37.7209669615499, -122.387181635995],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_537264ea3d486f06584f026ad7fed654 = L.circleMarker(
                [37.7644781578695, -122.477376524003],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_6046574fa4e7050923370d38c6452c76 = L.circleMarker(
                [37.7457389429655, -122.477960327299],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_fcb764fac0ee258d7423656766ff74af = L.circleMarker(
                [37.7356970275482, -122.37675765553],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_d1e0e7e4750960936ac0025b30681ea1 = L.circleMarker(
                [37.7292705199592, -122.432325871028],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_842e62b800c069a222ecd351afa55239 = L.circleMarker(
                [37.791642982384, -122.40090869889],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_b3b25335c7db49ea5eee9e532776ac6f = L.circleMarker(
                [37.7837069301545, -122.408595110869],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_c2378070e9971fcc5a605992e622a198 = L.circleMarker(
                [37.7572895904578, -122.406870402082],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_9febe55b6f2bafb8e6c669e3ff11695d = L.circleMarker(
                [37.7489063051829, -122.420354780861],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_de66d12ddab807a375c1f32408ebcd70 = L.circleMarker(
                [37.715765426995, -122.439909766772],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_4c40a55e2b352e2316e8571123122c69 = L.circleMarker(
                [37.7835699386918, -122.408421116922],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_7eb238ee27e8a2eaedc767d117550edd = L.circleMarker(
                [37.7736186276456, -122.422315670749],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_8e2406087045e41f9c218eb31f2076eb = L.circleMarker(
                [37.7928412840447, -122.424519835009],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_aff9dc31a7e4729e72de699f6e4a1270 = L.circleMarker(
                [37.7540986882068, -122.414233849038],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_7e81b1868fdb27d52d848716b77c9312 = L.circleMarker(
                [37.7540986882068, -122.414233849038],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_37292ea4f4775452042c4c39b9087717 = L.circleMarker(
                [37.7714939969416, -122.507750131004],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_48a82b5e6290b6dd15c084bb901a887d = L.circleMarker(
                [37.718302204766, -122.474444639595],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_cc4e9c295099d492d1c0341bef68b80b = L.circleMarker(
                [37.7645752317615, -122.427562596985],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_2583fd92486981e43512f59e5cf9109a = L.circleMarker(
                [37.7874378309112, -122.419203004268],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_d14ba7ca22d4d500feb4bbd0bd6eab92 = L.circleMarker(
                [37.7493688284532, -122.412690142308],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_b65966765a7f34ced68f92597351d650 = L.circleMarker(
                [37.7092010462379, -122.434609280352],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_809abc23640067f74e6bc921a708fbc9 = L.circleMarker(
                [37.7879209375533, -122.410882825551],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_46b2e120b60733cd3bd1032c13984ffd = L.circleMarker(
                [37.8004566471039, -122.401432754722],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_ad1ee2193e1a19ff30b64f178045b584 = L.circleMarker(
                [37.7435550542265, -122.421128029505],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_7cf57b44278c9196f339f0059a8d7062 = L.circleMarker(
                [37.7865647607685, -122.407244087032],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_e48ee9a3a7e98f002b8a18f38c0c0593 = L.circleMarker(
                [37.7615655928045, -122.423803001901],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_a4c4a030eb1ed06326de38c13c2d17ca = L.circleMarker(
                [37.7615655928045, -122.423803001901],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_05f5a7ebef967f5b5157bedd3f8af557 = L.circleMarker(
                [37.7441927508932, -122.444685482273],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_c8a66dada83c9e250667cda9a8542ed9 = L.circleMarker(
                [37.7754692820041, -122.415757039196],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_2fb09305163a9d3dc9367180ac393f55 = L.circleMarker(
                [37.7285280627465, -122.475647460786],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_982475f0a5a6e46a39dea607b75ecd74 = L.circleMarker(
                [37.7428517374449, -122.420967440564],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_6310c878b68ae24b8829f872a05bb90e = L.circleMarker(
                [37.7821198488931, -122.415669661443],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_41a875bdf1562a81494417172351aefc = L.circleMarker(
                [37.7791674218963, -122.406346425632],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_883a468d74ead4c9a8f47d4b1bf53041 = L.circleMarker(
                [37.7657184395282, -122.409529913278],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_ded80aa0f18b219bc6034ab01321f68c = L.circleMarker(
                [37.775420706711, -122.403404791479],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_81906bb06566f1b93647b8109feb6ca5 = L.circleMarker(
                [37.767524308783, -122.410738097315],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_7cb1da676413af8a0cf62cfa5203887d = L.circleMarker(
                [37.767524308783, -122.410738097315],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_97d46557a6999f40c4ec544b00347035 = L.circleMarker(
                [37.7131083433264, -122.444314025188],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_1f0fb1d9a2659fc2bc5afe96ca2bbf23 = L.circleMarker(
                [37.7131083433264, -122.444314025188],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_3a1ab9cc09aa382d56307b79879747a2 = L.circleMarker(
                [37.7660160114103, -122.403644620439],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_b73d9b0bfbf4daea4baae8be8aeb83de = L.circleMarker(
                [37.7660160114103, -122.403644620439],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_e6576f8d7e6f17b20aa3901e26fa1d98 = L.circleMarker(
                [37.7762310404758, -122.414714295579],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_8e999f5d29b4598af3ff4b16a9b8bad3 = L.circleMarker(
                [37.7762310404758, -122.414714295579],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_bd21a6fda0f0dff6f7d43d6d229363c3 = L.circleMarker(
                [37.7775118895695, -122.418045452768],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_0970e7253c7439d9cd76851b06d1cdb4 = L.circleMarker(
                [37.7820238478975, -122.401161555602],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_49a45f9b545bc72991d3430f17771530 = L.circleMarker(
                [37.72700531963, -122.403408669191],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_f908a4841f44af5563d80e071efc816b = L.circleMarker(
                [37.7838344374141, -122.412930522059],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_434b5efabdb21776bbb36f7e8ef56900 = L.circleMarker(
                [37.7530186537446, -122.418587172219],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_d2dfa76f7868947fac9441b9ff9e2f11 = L.circleMarker(
                [37.7740418385041, -122.414370627495],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_9e4774c5e2eec3522038c5436c388bac = L.circleMarker(
                [37.790538993725, -122.403915681571],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_45b0536f3998ea6259911c74788f5ab8 = L.circleMarker(
                [37.7830998244592, -122.419183096362],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_8e9af745e6c0221a4e0d1c773ba0aa55 = L.circleMarker(
                [37.7407360548358, -122.388753046997],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_7f1428978764c06d21614b14338d79a7 = L.circleMarker(
                [37.7749912944366, -122.437799703468],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_51a8d76f699b9d53461bf087546a5fc6 = L.circleMarker(
                [37.7770902743669, -122.421332684633],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_69d385e2068c323af7de9beca51ea577 = L.circleMarker(
                [37.7770902743669, -122.421332684633],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_7a4efbe855bbd92166fc3849da229662 = L.circleMarker(
                [37.7822458223917, -122.446612978839],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_b55fe91403db6f8472cd9d7695667706 = L.circleMarker(
                [37.7300379995128, -122.404594140634],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_c478b282085cda65784e0af177aeb121 = L.circleMarker(
                [37.7953338267436, -122.397373740066],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_558f3c6a42bfe5d3b91af34baf7bb7a1 = L.circleMarker(
                [37.7875158741623, -122.407434989523],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_0f8e7d520e5f208b9dfd84469e70f922 = L.circleMarker(
                [37.7785233776032, -122.403464080033],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_803b7d85953573c19b4001bf8bb8d24a = L.circleMarker(
                [37.7785233776032, -122.403464080033],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_b748d265248f5befd343b51f7c8ec3ab = L.circleMarker(
                [37.773291806903, -122.436614181331],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_47338365040da8c35796e04b17527ca6 = L.circleMarker(
                [37.780527578509, -122.396849015172],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_70e2965697a8bebd0e668248ab3c93ea = L.circleMarker(
                [37.780527578509, -122.396849015172],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_efb6cac50c078d3eeb878e84f09db598 = L.circleMarker(
                [37.7284180706602, -122.450000790445],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_17707744e595b859015511035c303f07 = L.circleMarker(
                [37.7292114647359, -122.400834283031],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_99b763be28ec487e80657278a868df2c = L.circleMarker(
                [37.7880065324392, -122.399802145799],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_7b88920be831af65d8e744bc0b8fd03b = L.circleMarker(
                [37.7239748241609, -122.3949284758],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_99b24e2b8c7bd2a4ae75be3f8d1ad30d = L.circleMarker(
                [37.7239748241609, -122.3949284758],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_266706094335f632f887f1c846388034 = L.circleMarker(
                [37.7239748241609, -122.3949284758],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_8faf11176e72de6f1af7f66e48174ad8 = L.circleMarker(
                [37.7883235449904, -122.41185703254],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_e87a97082535cafe11ff9c11e7c7facc = L.circleMarker(
                [37.7559977339856, -122.409435617106],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_c62bc9c344c42326ade22fbb92983537 = L.circleMarker(
                [37.7870798144443, -122.425883358148],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_5fb3a372c8c454a1da72801512e0bd36 = L.circleMarker(
                [37.7360374466862, -122.415126543001],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_82ca084161b046fbcccb403626930ccd = L.circleMarker(
                [37.712767884821, -122.431928011089],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_68cf5c410f3e567f41a73b831ae399e9 = L.circleMarker(
                [37.7895710255863, -122.402163713618],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_f8b88af0c197aff0de03ce7e1c037af9 = L.circleMarker(
                [37.7307429169559, -122.429306728376],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_e659870f6b6dafcc24b3dbfb3c60ce09 = L.circleMarker(
                [37.7838365565348, -122.413790972781],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_75338a1fe5797de9857ebf89cf56c006 = L.circleMarker(
                [37.7307429169559, -122.429306728376],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_3037f99819c100d56405975b9a78749b = L.circleMarker(
                [37.7373623605213, -122.422067184937],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_76d6b4b292a44b9b17cf9ee18e1e95d5 = L.circleMarker(
                [37.7373623605213, -122.422067184937],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_2abc1fe5eabefa22e631d26b8a1f98d5 = L.circleMarker(
                [37.7859988323798, -122.411747371924],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_cbe380de8bd21c290626a5b341493989 = L.circleMarker(
                [37.7633758058059, -122.420434724553],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_d76dfc812f8310b7a9e13cf9c4ffd93f = L.circleMarker(
                [37.7850226622786, -122.411987643595],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_93b8324fe2cc20a91e03f7aa2d9a6016 = L.circleMarker(
                [37.7746206491065, -122.500380427915],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_b4cf2b11d97032fe50a7cf64ef1a89c5 = L.circleMarker(
                [37.7751918267217, -122.466558780683],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_f494c4e9a97b29796617a78bae55d158 = L.circleMarker(
                [37.7490841729028, -122.486925960114],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_dfa0f8ec3193d60b9371008f4ab8844c = L.circleMarker(
                [37.7685360123583, -122.41561633832],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_7151294bad9ad9ca3e11e168327f04a4 = L.circleMarker(
                [37.7644297714074, -122.449751652563],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_b4ef1e3b6ad2f5d878c248d1911a57c4 = L.circleMarker(
                [37.7644297714074, -122.449751652563],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_4e0141e890b88de1f9ee87ec1e3f536f = L.circleMarker(
                [37.7352681469084, -122.472715759631],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);

&lt;/script&gt;
&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



You can also add some pop-up text that would get displayed when you hover over a marker. Let's make each marker display the category of the crime when hovered over.



```python
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
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;

    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;

        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;

    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-1.12.4.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;

            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_fbfb269e38054ab8d9256217b0f93903 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            &lt;/style&gt;

&lt;/head&gt;
&lt;body&gt;


            &lt;div class=&quot;folium-map&quot; id=&quot;map_fbfb269e38054ab8d9256217b0f93903&quot; &gt;&lt;/div&gt;

&lt;/body&gt;
&lt;script&gt;


            var map_fbfb269e38054ab8d9256217b0f93903 = L.map(
                &quot;map_fbfb269e38054ab8d9256217b0f93903&quot;,
                {
                    center: [37.77, -122.42],
                    crs: L.CRS.EPSG3857,
                    zoom: 12,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );





            var tile_layer_04cfd757ba0b462ab92f2d45cce38b39 = L.tileLayer(
                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,
                {&quot;attribution&quot;: &quot;Data by \u0026copy; \u003ca target=\&quot;_blank\&quot; href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://www.openstreetmap.org/copyright\&quot;\u003eODbL\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


            var feature_group_434ca95166ce75d0655024f15063aa7b = L.featureGroup(
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


            var circle_marker_c8608ac9405b7ab2a175a889a63a742a = L.circleMarker(
                [37.775420706711, -122.403404791479],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_76154229a82f40e07e998b95ae7758b9 = L.circleMarker(
                [37.775420706711, -122.403404791479],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_087db3db12d3de2fe2e31224cec6bf2c = L.circleMarker(
                [37.7299809672996, -122.388856204292],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_8ac2b6ac8e33fe9475a5f1b9ecd81e84 = L.circleMarker(
                [37.7857883766888, -122.412970537591],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_5b859db49ba6f6acb90b3a52938f98cf = L.circleMarker(
                [37.7650501214668, -122.419671780296],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_0c1fb7f697f9074b1b1505b30d6d312f = L.circleMarker(
                [37.788018555829, -122.426077177375],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_5624dcddc6b5bad031f9c0a399f72210 = L.circleMarker(
                [37.7808789360214, -122.405721454567],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_23f89abda4232e56481a13b49ccd15f8 = L.circleMarker(
                [37.7839805592634, -122.411778295992],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_d36ca9c7359c3ed35efe0e7e0f5cccc6 = L.circleMarker(
                [37.7757876218293, -122.393357241451],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_afc4f01d9a5b31dd96bfbea89834ce04 = L.circleMarker(
                [37.7209669615499, -122.387181635995],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_537264ea3d486f06584f026ad7fed654 = L.circleMarker(
                [37.7644781578695, -122.477376524003],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_6046574fa4e7050923370d38c6452c76 = L.circleMarker(
                [37.7457389429655, -122.477960327299],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_fcb764fac0ee258d7423656766ff74af = L.circleMarker(
                [37.7356970275482, -122.37675765553],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_d1e0e7e4750960936ac0025b30681ea1 = L.circleMarker(
                [37.7292705199592, -122.432325871028],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_842e62b800c069a222ecd351afa55239 = L.circleMarker(
                [37.791642982384, -122.40090869889],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_b3b25335c7db49ea5eee9e532776ac6f = L.circleMarker(
                [37.7837069301545, -122.408595110869],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_c2378070e9971fcc5a605992e622a198 = L.circleMarker(
                [37.7572895904578, -122.406870402082],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_9febe55b6f2bafb8e6c669e3ff11695d = L.circleMarker(
                [37.7489063051829, -122.420354780861],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_de66d12ddab807a375c1f32408ebcd70 = L.circleMarker(
                [37.715765426995, -122.439909766772],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_4c40a55e2b352e2316e8571123122c69 = L.circleMarker(
                [37.7835699386918, -122.408421116922],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_7eb238ee27e8a2eaedc767d117550edd = L.circleMarker(
                [37.7736186276456, -122.422315670749],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_8e2406087045e41f9c218eb31f2076eb = L.circleMarker(
                [37.7928412840447, -122.424519835009],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_aff9dc31a7e4729e72de699f6e4a1270 = L.circleMarker(
                [37.7540986882068, -122.414233849038],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_7e81b1868fdb27d52d848716b77c9312 = L.circleMarker(
                [37.7540986882068, -122.414233849038],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_37292ea4f4775452042c4c39b9087717 = L.circleMarker(
                [37.7714939969416, -122.507750131004],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_48a82b5e6290b6dd15c084bb901a887d = L.circleMarker(
                [37.718302204766, -122.474444639595],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_cc4e9c295099d492d1c0341bef68b80b = L.circleMarker(
                [37.7645752317615, -122.427562596985],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_2583fd92486981e43512f59e5cf9109a = L.circleMarker(
                [37.7874378309112, -122.419203004268],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_d14ba7ca22d4d500feb4bbd0bd6eab92 = L.circleMarker(
                [37.7493688284532, -122.412690142308],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_b65966765a7f34ced68f92597351d650 = L.circleMarker(
                [37.7092010462379, -122.434609280352],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_809abc23640067f74e6bc921a708fbc9 = L.circleMarker(
                [37.7879209375533, -122.410882825551],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_46b2e120b60733cd3bd1032c13984ffd = L.circleMarker(
                [37.8004566471039, -122.401432754722],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_ad1ee2193e1a19ff30b64f178045b584 = L.circleMarker(
                [37.7435550542265, -122.421128029505],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_7cf57b44278c9196f339f0059a8d7062 = L.circleMarker(
                [37.7865647607685, -122.407244087032],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_e48ee9a3a7e98f002b8a18f38c0c0593 = L.circleMarker(
                [37.7615655928045, -122.423803001901],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_a4c4a030eb1ed06326de38c13c2d17ca = L.circleMarker(
                [37.7615655928045, -122.423803001901],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_05f5a7ebef967f5b5157bedd3f8af557 = L.circleMarker(
                [37.7441927508932, -122.444685482273],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_c8a66dada83c9e250667cda9a8542ed9 = L.circleMarker(
                [37.7754692820041, -122.415757039196],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_2fb09305163a9d3dc9367180ac393f55 = L.circleMarker(
                [37.7285280627465, -122.475647460786],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_982475f0a5a6e46a39dea607b75ecd74 = L.circleMarker(
                [37.7428517374449, -122.420967440564],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_6310c878b68ae24b8829f872a05bb90e = L.circleMarker(
                [37.7821198488931, -122.415669661443],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_41a875bdf1562a81494417172351aefc = L.circleMarker(
                [37.7791674218963, -122.406346425632],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_883a468d74ead4c9a8f47d4b1bf53041 = L.circleMarker(
                [37.7657184395282, -122.409529913278],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_ded80aa0f18b219bc6034ab01321f68c = L.circleMarker(
                [37.775420706711, -122.403404791479],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_81906bb06566f1b93647b8109feb6ca5 = L.circleMarker(
                [37.767524308783, -122.410738097315],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_7cb1da676413af8a0cf62cfa5203887d = L.circleMarker(
                [37.767524308783, -122.410738097315],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_97d46557a6999f40c4ec544b00347035 = L.circleMarker(
                [37.7131083433264, -122.444314025188],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_1f0fb1d9a2659fc2bc5afe96ca2bbf23 = L.circleMarker(
                [37.7131083433264, -122.444314025188],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_3a1ab9cc09aa382d56307b79879747a2 = L.circleMarker(
                [37.7660160114103, -122.403644620439],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_b73d9b0bfbf4daea4baae8be8aeb83de = L.circleMarker(
                [37.7660160114103, -122.403644620439],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_e6576f8d7e6f17b20aa3901e26fa1d98 = L.circleMarker(
                [37.7762310404758, -122.414714295579],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_8e999f5d29b4598af3ff4b16a9b8bad3 = L.circleMarker(
                [37.7762310404758, -122.414714295579],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_bd21a6fda0f0dff6f7d43d6d229363c3 = L.circleMarker(
                [37.7775118895695, -122.418045452768],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_0970e7253c7439d9cd76851b06d1cdb4 = L.circleMarker(
                [37.7820238478975, -122.401161555602],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_49a45f9b545bc72991d3430f17771530 = L.circleMarker(
                [37.72700531963, -122.403408669191],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_f908a4841f44af5563d80e071efc816b = L.circleMarker(
                [37.7838344374141, -122.412930522059],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_434b5efabdb21776bbb36f7e8ef56900 = L.circleMarker(
                [37.7530186537446, -122.418587172219],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_d2dfa76f7868947fac9441b9ff9e2f11 = L.circleMarker(
                [37.7740418385041, -122.414370627495],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_9e4774c5e2eec3522038c5436c388bac = L.circleMarker(
                [37.790538993725, -122.403915681571],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_45b0536f3998ea6259911c74788f5ab8 = L.circleMarker(
                [37.7830998244592, -122.419183096362],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_8e9af745e6c0221a4e0d1c773ba0aa55 = L.circleMarker(
                [37.7407360548358, -122.388753046997],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_7f1428978764c06d21614b14338d79a7 = L.circleMarker(
                [37.7749912944366, -122.437799703468],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_51a8d76f699b9d53461bf087546a5fc6 = L.circleMarker(
                [37.7770902743669, -122.421332684633],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_69d385e2068c323af7de9beca51ea577 = L.circleMarker(
                [37.7770902743669, -122.421332684633],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_7a4efbe855bbd92166fc3849da229662 = L.circleMarker(
                [37.7822458223917, -122.446612978839],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_b55fe91403db6f8472cd9d7695667706 = L.circleMarker(
                [37.7300379995128, -122.404594140634],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_c478b282085cda65784e0af177aeb121 = L.circleMarker(
                [37.7953338267436, -122.397373740066],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_558f3c6a42bfe5d3b91af34baf7bb7a1 = L.circleMarker(
                [37.7875158741623, -122.407434989523],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_0f8e7d520e5f208b9dfd84469e70f922 = L.circleMarker(
                [37.7785233776032, -122.403464080033],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_803b7d85953573c19b4001bf8bb8d24a = L.circleMarker(
                [37.7785233776032, -122.403464080033],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_b748d265248f5befd343b51f7c8ec3ab = L.circleMarker(
                [37.773291806903, -122.436614181331],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_47338365040da8c35796e04b17527ca6 = L.circleMarker(
                [37.780527578509, -122.396849015172],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_70e2965697a8bebd0e668248ab3c93ea = L.circleMarker(
                [37.780527578509, -122.396849015172],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_efb6cac50c078d3eeb878e84f09db598 = L.circleMarker(
                [37.7284180706602, -122.450000790445],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_17707744e595b859015511035c303f07 = L.circleMarker(
                [37.7292114647359, -122.400834283031],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_99b763be28ec487e80657278a868df2c = L.circleMarker(
                [37.7880065324392, -122.399802145799],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_7b88920be831af65d8e744bc0b8fd03b = L.circleMarker(
                [37.7239748241609, -122.3949284758],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_99b24e2b8c7bd2a4ae75be3f8d1ad30d = L.circleMarker(
                [37.7239748241609, -122.3949284758],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_266706094335f632f887f1c846388034 = L.circleMarker(
                [37.7239748241609, -122.3949284758],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_8faf11176e72de6f1af7f66e48174ad8 = L.circleMarker(
                [37.7883235449904, -122.41185703254],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_e87a97082535cafe11ff9c11e7c7facc = L.circleMarker(
                [37.7559977339856, -122.409435617106],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_c62bc9c344c42326ade22fbb92983537 = L.circleMarker(
                [37.7870798144443, -122.425883358148],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_5fb3a372c8c454a1da72801512e0bd36 = L.circleMarker(
                [37.7360374466862, -122.415126543001],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_82ca084161b046fbcccb403626930ccd = L.circleMarker(
                [37.712767884821, -122.431928011089],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_68cf5c410f3e567f41a73b831ae399e9 = L.circleMarker(
                [37.7895710255863, -122.402163713618],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_f8b88af0c197aff0de03ce7e1c037af9 = L.circleMarker(
                [37.7307429169559, -122.429306728376],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_e659870f6b6dafcc24b3dbfb3c60ce09 = L.circleMarker(
                [37.7838365565348, -122.413790972781],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_75338a1fe5797de9857ebf89cf56c006 = L.circleMarker(
                [37.7307429169559, -122.429306728376],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_3037f99819c100d56405975b9a78749b = L.circleMarker(
                [37.7373623605213, -122.422067184937],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_76d6b4b292a44b9b17cf9ee18e1e95d5 = L.circleMarker(
                [37.7373623605213, -122.422067184937],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_2abc1fe5eabefa22e631d26b8a1f98d5 = L.circleMarker(
                [37.7859988323798, -122.411747371924],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_cbe380de8bd21c290626a5b341493989 = L.circleMarker(
                [37.7633758058059, -122.420434724553],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_d76dfc812f8310b7a9e13cf9c4ffd93f = L.circleMarker(
                [37.7850226622786, -122.411987643595],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_93b8324fe2cc20a91e03f7aa2d9a6016 = L.circleMarker(
                [37.7746206491065, -122.500380427915],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_b4cf2b11d97032fe50a7cf64ef1a89c5 = L.circleMarker(
                [37.7751918267217, -122.466558780683],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_f494c4e9a97b29796617a78bae55d158 = L.circleMarker(
                [37.7490841729028, -122.486925960114],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_dfa0f8ec3193d60b9371008f4ab8844c = L.circleMarker(
                [37.7685360123583, -122.41561633832],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_7151294bad9ad9ca3e11e168327f04a4 = L.circleMarker(
                [37.7644297714074, -122.449751652563],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_b4ef1e3b6ad2f5d878c248d1911a57c4 = L.circleMarker(
                [37.7644297714074, -122.449751652563],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var circle_marker_4e0141e890b88de1f9ee87ec1e3f536f = L.circleMarker(
                [37.7352681469084, -122.472715759631],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_434ca95166ce75d0655024f15063aa7b);


            var marker_bb08b9257ff19bc0f1f4f69e7c85ddfc = L.marker(
                [37.775420706711, -122.403404791479],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_bd7da66ed2ea715877cf7fa6455672bc = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_32bdd4cb464c328d60a8dcf0dd3c6239 = $(`&lt;div id=&quot;html_32bdd4cb464c328d60a8dcf0dd3c6239&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WEAPON LAWS&lt;/div&gt;`)[0];
                popup_bd7da66ed2ea715877cf7fa6455672bc.setContent(html_32bdd4cb464c328d60a8dcf0dd3c6239);



        marker_bb08b9257ff19bc0f1f4f69e7c85ddfc.bindPopup(popup_bd7da66ed2ea715877cf7fa6455672bc)
        ;




            var marker_1032cb62880c6a68c839f97056b1e0f4 = L.marker(
                [37.775420706711, -122.403404791479],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_a745178a078f6489f3e84f0cee13711f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_16d430fad55a6cc3dceb144aedc05f10 = $(`&lt;div id=&quot;html_16d430fad55a6cc3dceb144aedc05f10&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WEAPON LAWS&lt;/div&gt;`)[0];
                popup_a745178a078f6489f3e84f0cee13711f.setContent(html_16d430fad55a6cc3dceb144aedc05f10);



        marker_1032cb62880c6a68c839f97056b1e0f4.bindPopup(popup_a745178a078f6489f3e84f0cee13711f)
        ;




            var marker_f7e281a52e56006a5e9735a1e48fd6eb = L.marker(
                [37.7299809672996, -122.388856204292],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_c5e5d07574953656f0e134a61f537d6e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_5344310bf589fa73806c4920e351171a = $(`&lt;div id=&quot;html_5344310bf589fa73806c4920e351171a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_c5e5d07574953656f0e134a61f537d6e.setContent(html_5344310bf589fa73806c4920e351171a);



        marker_f7e281a52e56006a5e9735a1e48fd6eb.bindPopup(popup_c5e5d07574953656f0e134a61f537d6e)
        ;




            var marker_714b7a4b8038c0478778c6c820da86d9 = L.marker(
                [37.7857883766888, -122.412970537591],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_f8e424917b0c3107c13f81c7c23b4c61 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_fda286a6b1369f02b5815865f1f28047 = $(`&lt;div id=&quot;html_fda286a6b1369f02b5815865f1f28047&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_f8e424917b0c3107c13f81c7c23b4c61.setContent(html_fda286a6b1369f02b5815865f1f28047);



        marker_714b7a4b8038c0478778c6c820da86d9.bindPopup(popup_f8e424917b0c3107c13f81c7c23b4c61)
        ;




            var marker_4f609306a3a8ae1706b24f2277247362 = L.marker(
                [37.7650501214668, -122.419671780296],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_f47a3ef3be505429efa1a86b8f83dae5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_8a21487bc8e47faa32ffa5814278c681 = $(`&lt;div id=&quot;html_8a21487bc8e47faa32ffa5814278c681&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_f47a3ef3be505429efa1a86b8f83dae5.setContent(html_8a21487bc8e47faa32ffa5814278c681);



        marker_4f609306a3a8ae1706b24f2277247362.bindPopup(popup_f47a3ef3be505429efa1a86b8f83dae5)
        ;




            var marker_a71ade947d7a92c37487540e2d573742 = L.marker(
                [37.788018555829, -122.426077177375],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_2f4e351539cd952fd7ad9499ca98db00 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_255c4da8a1967b69a37e38bf8f7accb1 = $(`&lt;div id=&quot;html_255c4da8a1967b69a37e38bf8f7accb1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_2f4e351539cd952fd7ad9499ca98db00.setContent(html_255c4da8a1967b69a37e38bf8f7accb1);



        marker_a71ade947d7a92c37487540e2d573742.bindPopup(popup_2f4e351539cd952fd7ad9499ca98db00)
        ;




            var marker_7969f6c00b2518d7305256a0d67c6206 = L.marker(
                [37.7808789360214, -122.405721454567],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_ccc3a5d3096452d0934783b2b0289770 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_8f8bf69e5e51889748739ad78dc07a95 = $(`&lt;div id=&quot;html_8f8bf69e5e51889748739ad78dc07a95&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_ccc3a5d3096452d0934783b2b0289770.setContent(html_8f8bf69e5e51889748739ad78dc07a95);



        marker_7969f6c00b2518d7305256a0d67c6206.bindPopup(popup_ccc3a5d3096452d0934783b2b0289770)
        ;




            var marker_ff154b1b652fe2f2809633a3531a161a = L.marker(
                [37.7839805592634, -122.411778295992],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_ef69375c4923373a11a85d2c41872b65 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_7da6bae870e11ef60223e3bb8ad8bfb9 = $(`&lt;div id=&quot;html_7da6bae870e11ef60223e3bb8ad8bfb9&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_ef69375c4923373a11a85d2c41872b65.setContent(html_7da6bae870e11ef60223e3bb8ad8bfb9);



        marker_ff154b1b652fe2f2809633a3531a161a.bindPopup(popup_ef69375c4923373a11a85d2c41872b65)
        ;




            var marker_f0e72117c63f0ad6e598774f62249674 = L.marker(
                [37.7757876218293, -122.393357241451],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_32b31b0a3209f3275e5a2f667c82d9c2 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_821d2f7f71b5dd28319c93f022437f4a = $(`&lt;div id=&quot;html_821d2f7f71b5dd28319c93f022437f4a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_32b31b0a3209f3275e5a2f667c82d9c2.setContent(html_821d2f7f71b5dd28319c93f022437f4a);



        marker_f0e72117c63f0ad6e598774f62249674.bindPopup(popup_32b31b0a3209f3275e5a2f667c82d9c2)
        ;




            var marker_dc17cc76c95db77aab87e16cda4c33dd = L.marker(
                [37.7209669615499, -122.387181635995],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_cfd8c2314f5541baf9ab2b091334a7e6 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_46346d3cf14f26d99c932f37aa8e1da8 = $(`&lt;div id=&quot;html_46346d3cf14f26d99c932f37aa8e1da8&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;MISSING PERSON&lt;/div&gt;`)[0];
                popup_cfd8c2314f5541baf9ab2b091334a7e6.setContent(html_46346d3cf14f26d99c932f37aa8e1da8);



        marker_dc17cc76c95db77aab87e16cda4c33dd.bindPopup(popup_cfd8c2314f5541baf9ab2b091334a7e6)
        ;




            var marker_9093dbe5ee9b7b7a61109c6d31a59e50 = L.marker(
                [37.7644781578695, -122.477376524003],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_34eebf2e49cd9261d7efc135b8b0e0c9 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_88504fd121e3a793a48ba4dbc92282f1 = $(`&lt;div id=&quot;html_88504fd121e3a793a48ba4dbc92282f1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_34eebf2e49cd9261d7efc135b8b0e0c9.setContent(html_88504fd121e3a793a48ba4dbc92282f1);



        marker_9093dbe5ee9b7b7a61109c6d31a59e50.bindPopup(popup_34eebf2e49cd9261d7efc135b8b0e0c9)
        ;




            var marker_ffa38659585e70886037ee7768db5d6b = L.marker(
                [37.7457389429655, -122.477960327299],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_75c15702efe7ec9864a25a683f80a98e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_7881c6f90fc1d27cecc38d8c9d6cd80b = $(`&lt;div id=&quot;html_7881c6f90fc1d27cecc38d8c9d6cd80b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_75c15702efe7ec9864a25a683f80a98e.setContent(html_7881c6f90fc1d27cecc38d8c9d6cd80b);



        marker_ffa38659585e70886037ee7768db5d6b.bindPopup(popup_75c15702efe7ec9864a25a683f80a98e)
        ;




            var marker_3bfbe45376bf8e09a2cbf829faee52a4 = L.marker(
                [37.7356970275482, -122.37675765553],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_0e9fff3dc1a46928f01c005672ec353d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_1b6bcd80a209d7b28b0258a23e3b5cb1 = $(`&lt;div id=&quot;html_1b6bcd80a209d7b28b0258a23e3b5cb1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_0e9fff3dc1a46928f01c005672ec353d.setContent(html_1b6bcd80a209d7b28b0258a23e3b5cb1);



        marker_3bfbe45376bf8e09a2cbf829faee52a4.bindPopup(popup_0e9fff3dc1a46928f01c005672ec353d)
        ;




            var marker_5c50d93b57e3948853ceea0421620bbf = L.marker(
                [37.7292705199592, -122.432325871028],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_3fd2db919b5bd8447662d3a7ecc8b1cc = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_2677f8e407bca47a409f4b1f9777de27 = $(`&lt;div id=&quot;html_2677f8e407bca47a409f4b1f9777de27&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_3fd2db919b5bd8447662d3a7ecc8b1cc.setContent(html_2677f8e407bca47a409f4b1f9777de27);



        marker_5c50d93b57e3948853ceea0421620bbf.bindPopup(popup_3fd2db919b5bd8447662d3a7ecc8b1cc)
        ;




            var marker_54aec4ce5e4e4a536c44f1895271e039 = L.marker(
                [37.791642982384, -122.40090869889],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_86350c5f94b0fed2282dfd50bfaaae61 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_1bc8c5551fe41c0c112f530597071280 = $(`&lt;div id=&quot;html_1bc8c5551fe41c0c112f530597071280&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;BURGLARY&lt;/div&gt;`)[0];
                popup_86350c5f94b0fed2282dfd50bfaaae61.setContent(html_1bc8c5551fe41c0c112f530597071280);



        marker_54aec4ce5e4e4a536c44f1895271e039.bindPopup(popup_86350c5f94b0fed2282dfd50bfaaae61)
        ;




            var marker_90aba25a18680c5cc2f7268b30c71297 = L.marker(
                [37.7837069301545, -122.408595110869],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_6f9c544777d9074d6cff58c1c38137f7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_54c5cb1848861862ef253d802030f338 = $(`&lt;div id=&quot;html_54c5cb1848861862ef253d802030f338&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;STOLEN PROPERTY&lt;/div&gt;`)[0];
                popup_6f9c544777d9074d6cff58c1c38137f7.setContent(html_54c5cb1848861862ef253d802030f338);



        marker_90aba25a18680c5cc2f7268b30c71297.bindPopup(popup_6f9c544777d9074d6cff58c1c38137f7)
        ;




            var marker_9875c84e824c206208005b8a016bf3bd = L.marker(
                [37.7572895904578, -122.406870402082],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_d7a6b5edc11c5c4cedabdf17aba88404 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_78606285f9031ce4107bf083acdc11ef = $(`&lt;div id=&quot;html_78606285f9031ce4107bf083acdc11ef&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ROBBERY&lt;/div&gt;`)[0];
                popup_d7a6b5edc11c5c4cedabdf17aba88404.setContent(html_78606285f9031ce4107bf083acdc11ef);



        marker_9875c84e824c206208005b8a016bf3bd.bindPopup(popup_d7a6b5edc11c5c4cedabdf17aba88404)
        ;




            var marker_9c5b44b5a34ced1062594f0c14093adb = L.marker(
                [37.7489063051829, -122.420354780861],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_65c9e771eba66808f4d60574c409cade = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_06560fdd98da902415b38cbb99623e8a = $(`&lt;div id=&quot;html_06560fdd98da902415b38cbb99623e8a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_65c9e771eba66808f4d60574c409cade.setContent(html_06560fdd98da902415b38cbb99623e8a);



        marker_9c5b44b5a34ced1062594f0c14093adb.bindPopup(popup_65c9e771eba66808f4d60574c409cade)
        ;




            var marker_49c3542c74fe6b24e94c47b02679fa6e = L.marker(
                [37.715765426995, -122.439909766772],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_403751895e0ea2e563200f93c8923ec7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_5722069d69aee7842d5ba4f8db93de9b = $(`&lt;div id=&quot;html_5722069d69aee7842d5ba4f8db93de9b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_403751895e0ea2e563200f93c8923ec7.setContent(html_5722069d69aee7842d5ba4f8db93de9b);



        marker_49c3542c74fe6b24e94c47b02679fa6e.bindPopup(popup_403751895e0ea2e563200f93c8923ec7)
        ;




            var marker_64d44cd22ed26ea15777e51a629b8ff8 = L.marker(
                [37.7835699386918, -122.408421116922],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_b2dd20af80c7a0263220fa8a8943c006 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_e76facf34d459041a5bf01f70cfc3180 = $(`&lt;div id=&quot;html_e76facf34d459041a5bf01f70cfc3180&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_b2dd20af80c7a0263220fa8a8943c006.setContent(html_e76facf34d459041a5bf01f70cfc3180);



        marker_64d44cd22ed26ea15777e51a629b8ff8.bindPopup(popup_b2dd20af80c7a0263220fa8a8943c006)
        ;




            var marker_7693d2a26bc079854499ae34380aace6 = L.marker(
                [37.7736186276456, -122.422315670749],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_538ad91d5325726fcce6da0d364dbaa6 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_e18f1aafbc5b0ab9368f66c9fff8364b = $(`&lt;div id=&quot;html_e18f1aafbc5b0ab9368f66c9fff8364b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;FRAUD&lt;/div&gt;`)[0];
                popup_538ad91d5325726fcce6da0d364dbaa6.setContent(html_e18f1aafbc5b0ab9368f66c9fff8364b);



        marker_7693d2a26bc079854499ae34380aace6.bindPopup(popup_538ad91d5325726fcce6da0d364dbaa6)
        ;




            var marker_0fcc55fc00d67e1d03663ae0c772653c = L.marker(
                [37.7928412840447, -122.424519835009],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_48aa3a9e09f9d18164117ff09b95646b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_322365565a7ffaa627d84681b372f04c = $(`&lt;div id=&quot;html_322365565a7ffaa627d84681b372f04c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_48aa3a9e09f9d18164117ff09b95646b.setContent(html_322365565a7ffaa627d84681b372f04c);



        marker_0fcc55fc00d67e1d03663ae0c772653c.bindPopup(popup_48aa3a9e09f9d18164117ff09b95646b)
        ;




            var marker_6f7b676e6a717eff825a88fd9e80418d = L.marker(
                [37.7540986882068, -122.414233849038],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_ddebbcc2a49f652a6700b2a73f5c93b6 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_93f6cdb8257bd729deeae38accba5579 = $(`&lt;div id=&quot;html_93f6cdb8257bd729deeae38accba5579&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;DRUG/NARCOTIC&lt;/div&gt;`)[0];
                popup_ddebbcc2a49f652a6700b2a73f5c93b6.setContent(html_93f6cdb8257bd729deeae38accba5579);



        marker_6f7b676e6a717eff825a88fd9e80418d.bindPopup(popup_ddebbcc2a49f652a6700b2a73f5c93b6)
        ;




            var marker_963ff15fb19b869b93f4cdb0dd1e31d2 = L.marker(
                [37.7540986882068, -122.414233849038],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_c4cf3354c8b18397e95c48e935c6df20 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_aa2cdda3009b13c757e32315667cb7ea = $(`&lt;div id=&quot;html_aa2cdda3009b13c757e32315667cb7ea&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_c4cf3354c8b18397e95c48e935c6df20.setContent(html_aa2cdda3009b13c757e32315667cb7ea);



        marker_963ff15fb19b869b93f4cdb0dd1e31d2.bindPopup(popup_c4cf3354c8b18397e95c48e935c6df20)
        ;




            var marker_02208078451856e06969a07d63353566 = L.marker(
                [37.7714939969416, -122.507750131004],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_f1b1d27f67b9c2497cdf099531e6e5dd = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_aac9e17f882c35aeb46e64e75957f86b = $(`&lt;div id=&quot;html_aac9e17f882c35aeb46e64e75957f86b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_f1b1d27f67b9c2497cdf099531e6e5dd.setContent(html_aac9e17f882c35aeb46e64e75957f86b);



        marker_02208078451856e06969a07d63353566.bindPopup(popup_f1b1d27f67b9c2497cdf099531e6e5dd)
        ;




            var marker_462fb3167fb967ee4b09ec3916703732 = L.marker(
                [37.718302204766, -122.474444639595],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_e82e3145ddf240a2ba64783093935001 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_842be5526c4890bd50d03ee13fddfadf = $(`&lt;div id=&quot;html_842be5526c4890bd50d03ee13fddfadf&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_e82e3145ddf240a2ba64783093935001.setContent(html_842be5526c4890bd50d03ee13fddfadf);



        marker_462fb3167fb967ee4b09ec3916703732.bindPopup(popup_e82e3145ddf240a2ba64783093935001)
        ;




            var marker_17c8b936b59c7cd4b50a0c99676abf8d = L.marker(
                [37.7645752317615, -122.427562596985],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_1953de3da4cdb8e72f0453713b412d2b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_01476b01e48c2e916878dcdb202bc5c4 = $(`&lt;div id=&quot;html_01476b01e48c2e916878dcdb202bc5c4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_1953de3da4cdb8e72f0453713b412d2b.setContent(html_01476b01e48c2e916878dcdb202bc5c4);



        marker_17c8b936b59c7cd4b50a0c99676abf8d.bindPopup(popup_1953de3da4cdb8e72f0453713b412d2b)
        ;




            var marker_a1423e25959017a2a185767c641d70a1 = L.marker(
                [37.7874378309112, -122.419203004268],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_096febe6ed72e66f54d09cb8b68661b3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_712255e44943a0850f12e3191d709cb4 = $(`&lt;div id=&quot;html_712255e44943a0850f12e3191d709cb4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;BURGLARY&lt;/div&gt;`)[0];
                popup_096febe6ed72e66f54d09cb8b68661b3.setContent(html_712255e44943a0850f12e3191d709cb4);



        marker_a1423e25959017a2a185767c641d70a1.bindPopup(popup_096febe6ed72e66f54d09cb8b68661b3)
        ;




            var marker_da8430ca19ad641f4a729663cb4066d7 = L.marker(
                [37.7493688284532, -122.412690142308],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_8cf7c988e31bd26d0fcbcb2f6d353037 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_995b9e1692c2ee268669c8f89fe821a2 = $(`&lt;div id=&quot;html_995b9e1692c2ee268669c8f89fe821a2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_8cf7c988e31bd26d0fcbcb2f6d353037.setContent(html_995b9e1692c2ee268669c8f89fe821a2);



        marker_da8430ca19ad641f4a729663cb4066d7.bindPopup(popup_8cf7c988e31bd26d0fcbcb2f6d353037)
        ;




            var marker_87455f9e06422c708df5a297c8a645eb = L.marker(
                [37.7092010462379, -122.434609280352],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_73494ff0345f8ad939e4a0c4fd78077e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_22941eaa56c2e7ea970627b1c78a2b8e = $(`&lt;div id=&quot;html_22941eaa56c2e7ea970627b1c78a2b8e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_73494ff0345f8ad939e4a0c4fd78077e.setContent(html_22941eaa56c2e7ea970627b1c78a2b8e);



        marker_87455f9e06422c708df5a297c8a645eb.bindPopup(popup_73494ff0345f8ad939e4a0c4fd78077e)
        ;




            var marker_9431898e0c7660516aae891904dcb7a1 = L.marker(
                [37.7879209375533, -122.410882825551],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_36e2055244367673b875da7639a1acc2 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_18ba9bbce262ca858bcd20d45ce7aabb = $(`&lt;div id=&quot;html_18ba9bbce262ca858bcd20d45ce7aabb&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VEHICLE THEFT&lt;/div&gt;`)[0];
                popup_36e2055244367673b875da7639a1acc2.setContent(html_18ba9bbce262ca858bcd20d45ce7aabb);



        marker_9431898e0c7660516aae891904dcb7a1.bindPopup(popup_36e2055244367673b875da7639a1acc2)
        ;




            var marker_22e9e9420aec24a2d9a09fb9ac8da6c8 = L.marker(
                [37.8004566471039, -122.401432754722],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_cf5ac0efd91cb0272ed5342d17abd8a0 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_9d8bf41a96f90061d3b49c6ba37b1a6c = $(`&lt;div id=&quot;html_9d8bf41a96f90061d3b49c6ba37b1a6c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VEHICLE THEFT&lt;/div&gt;`)[0];
                popup_cf5ac0efd91cb0272ed5342d17abd8a0.setContent(html_9d8bf41a96f90061d3b49c6ba37b1a6c);



        marker_22e9e9420aec24a2d9a09fb9ac8da6c8.bindPopup(popup_cf5ac0efd91cb0272ed5342d17abd8a0)
        ;




            var marker_d2f39b6f79f001b4704185195f0b1e4a = L.marker(
                [37.7435550542265, -122.421128029505],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_932fb302e2b181eabe829792e897349e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_75e0372fba3478628120493aa4ef3087 = $(`&lt;div id=&quot;html_75e0372fba3478628120493aa4ef3087&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_932fb302e2b181eabe829792e897349e.setContent(html_75e0372fba3478628120493aa4ef3087);



        marker_d2f39b6f79f001b4704185195f0b1e4a.bindPopup(popup_932fb302e2b181eabe829792e897349e)
        ;




            var marker_e2e07a34f68c9cc3dabc4628e3402b7e = L.marker(
                [37.7865647607685, -122.407244087032],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_29de47e881004913de72f58c5b1ea32c = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_5d6de20d0b9873aa1709de380acb3f6e = $(`&lt;div id=&quot;html_5d6de20d0b9873aa1709de380acb3f6e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_29de47e881004913de72f58c5b1ea32c.setContent(html_5d6de20d0b9873aa1709de380acb3f6e);



        marker_e2e07a34f68c9cc3dabc4628e3402b7e.bindPopup(popup_29de47e881004913de72f58c5b1ea32c)
        ;




            var marker_1662f29121f1253df037cd0355e3f534 = L.marker(
                [37.7615655928045, -122.423803001901],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_1576281844857e961a59153db6830bc8 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_c5504a524d6294d0c867fcfb0994c2f6 = $(`&lt;div id=&quot;html_c5504a524d6294d0c867fcfb0994c2f6&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;RECOVERED VEHICLE&lt;/div&gt;`)[0];
                popup_1576281844857e961a59153db6830bc8.setContent(html_c5504a524d6294d0c867fcfb0994c2f6);



        marker_1662f29121f1253df037cd0355e3f534.bindPopup(popup_1576281844857e961a59153db6830bc8)
        ;




            var marker_912501e38aae247b6b5e7b8817938bc5 = L.marker(
                [37.7615655928045, -122.423803001901],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_42506b0c7ad506319cec2f63fbcf4c13 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_5ea5f5b9e57ab5d70854e9eba4c5b2b4 = $(`&lt;div id=&quot;html_5ea5f5b9e57ab5d70854e9eba4c5b2b4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_42506b0c7ad506319cec2f63fbcf4c13.setContent(html_5ea5f5b9e57ab5d70854e9eba4c5b2b4);



        marker_912501e38aae247b6b5e7b8817938bc5.bindPopup(popup_42506b0c7ad506319cec2f63fbcf4c13)
        ;




            var marker_bfc01a7a1bddadad920e1714736759bf = L.marker(
                [37.7441927508932, -122.444685482273],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_95cb4563dadc6782f11e69d00a267162 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_cae63b5c0c4efc02b13ac78fd8bb8b4a = $(`&lt;div id=&quot;html_cae63b5c0c4efc02b13ac78fd8bb8b4a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_95cb4563dadc6782f11e69d00a267162.setContent(html_cae63b5c0c4efc02b13ac78fd8bb8b4a);



        marker_bfc01a7a1bddadad920e1714736759bf.bindPopup(popup_95cb4563dadc6782f11e69d00a267162)
        ;




            var marker_582e991d23e6c0cef6111e9e8f45d1fd = L.marker(
                [37.7754692820041, -122.415757039196],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_c7875ffedf73b9c19fcf77a9613d2951 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_bf47eab3ace05070665b4802348b1d3e = $(`&lt;div id=&quot;html_bf47eab3ace05070665b4802348b1d3e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_c7875ffedf73b9c19fcf77a9613d2951.setContent(html_bf47eab3ace05070665b4802348b1d3e);



        marker_582e991d23e6c0cef6111e9e8f45d1fd.bindPopup(popup_c7875ffedf73b9c19fcf77a9613d2951)
        ;




            var marker_ed6eec4afe548a0d2769afd1301ad8c9 = L.marker(
                [37.7285280627465, -122.475647460786],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_875eb846617f9cb736f6edea2a93aa72 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_54cafd64fa649b40f358d026df39d1f2 = $(`&lt;div id=&quot;html_54cafd64fa649b40f358d026df39d1f2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ROBBERY&lt;/div&gt;`)[0];
                popup_875eb846617f9cb736f6edea2a93aa72.setContent(html_54cafd64fa649b40f358d026df39d1f2);



        marker_ed6eec4afe548a0d2769afd1301ad8c9.bindPopup(popup_875eb846617f9cb736f6edea2a93aa72)
        ;




            var marker_c515e8eaee8a5e2a095314e70b48b7a6 = L.marker(
                [37.7428517374449, -122.420967440564],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_41c6f702ae216b3022e21e47b6f0a76c = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_1dc66e3fd78706f4492d8336e82ebf53 = $(`&lt;div id=&quot;html_1dc66e3fd78706f4492d8336e82ebf53&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_41c6f702ae216b3022e21e47b6f0a76c.setContent(html_1dc66e3fd78706f4492d8336e82ebf53);



        marker_c515e8eaee8a5e2a095314e70b48b7a6.bindPopup(popup_41c6f702ae216b3022e21e47b6f0a76c)
        ;




            var marker_42ec19b65d5a2f5062827197f584fca1 = L.marker(
                [37.7821198488931, -122.415669661443],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_e749cd4f3a5bfa2b9ae025c2905ba840 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_0e5cb1ead9c050ceb64089eaacf255b1 = $(`&lt;div id=&quot;html_0e5cb1ead9c050ceb64089eaacf255b1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VANDALISM&lt;/div&gt;`)[0];
                popup_e749cd4f3a5bfa2b9ae025c2905ba840.setContent(html_0e5cb1ead9c050ceb64089eaacf255b1);



        marker_42ec19b65d5a2f5062827197f584fca1.bindPopup(popup_e749cd4f3a5bfa2b9ae025c2905ba840)
        ;




            var marker_fb39b2ebd0acc7f1a3c1ba1ff92178dd = L.marker(
                [37.7791674218963, -122.406346425632],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_2ab023ed2b6195b8a9e18bba63a674d4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_129f3f24b5bd619f6d8299176d2f34fa = $(`&lt;div id=&quot;html_129f3f24b5bd619f6d8299176d2f34fa&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_2ab023ed2b6195b8a9e18bba63a674d4.setContent(html_129f3f24b5bd619f6d8299176d2f34fa);



        marker_fb39b2ebd0acc7f1a3c1ba1ff92178dd.bindPopup(popup_2ab023ed2b6195b8a9e18bba63a674d4)
        ;




            var marker_4c8e8667720363cc1d766b894ad3d776 = L.marker(
                [37.7657184395282, -122.409529913278],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_af7b6ed8ea9dfada3b3c213177ffd17e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_8d32c0c1001672d11248dfd64ea9c091 = $(`&lt;div id=&quot;html_8d32c0c1001672d11248dfd64ea9c091&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_af7b6ed8ea9dfada3b3c213177ffd17e.setContent(html_8d32c0c1001672d11248dfd64ea9c091);



        marker_4c8e8667720363cc1d766b894ad3d776.bindPopup(popup_af7b6ed8ea9dfada3b3c213177ffd17e)
        ;




            var marker_a444cf380bb669ab039af10c79adfa4e = L.marker(
                [37.775420706711, -122.403404791479],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_7ff023b55eadfdb9ec875345ef7dda96 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_b6e59620efd1b1c899d8e0e969ea0974 = $(`&lt;div id=&quot;html_b6e59620efd1b1c899d8e0e969ea0974&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_7ff023b55eadfdb9ec875345ef7dda96.setContent(html_b6e59620efd1b1c899d8e0e969ea0974);



        marker_a444cf380bb669ab039af10c79adfa4e.bindPopup(popup_7ff023b55eadfdb9ec875345ef7dda96)
        ;




            var marker_d879d8233ac78b2c18bf29aa12c320dd = L.marker(
                [37.767524308783, -122.410738097315],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_bee625bee705ae87f3052d6fe986d20e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_f9938476a8ed5ea24431c8a700ada65a = $(`&lt;div id=&quot;html_f9938476a8ed5ea24431c8a700ada65a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;BURGLARY&lt;/div&gt;`)[0];
                popup_bee625bee705ae87f3052d6fe986d20e.setContent(html_f9938476a8ed5ea24431c8a700ada65a);



        marker_d879d8233ac78b2c18bf29aa12c320dd.bindPopup(popup_bee625bee705ae87f3052d6fe986d20e)
        ;




            var marker_19d0925c05bb33f114e1d855d73143aa = L.marker(
                [37.767524308783, -122.410738097315],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_ff974c983fefcbaa93d65385c5004773 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_f85339ca64a13340703914585ad3706d = $(`&lt;div id=&quot;html_f85339ca64a13340703914585ad3706d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ARSON&lt;/div&gt;`)[0];
                popup_ff974c983fefcbaa93d65385c5004773.setContent(html_f85339ca64a13340703914585ad3706d);



        marker_19d0925c05bb33f114e1d855d73143aa.bindPopup(popup_ff974c983fefcbaa93d65385c5004773)
        ;




            var marker_4360b2baf466f987219bfb40da4feb42 = L.marker(
                [37.7131083433264, -122.444314025188],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_a75777e8ea1472429ce66d52ff76d4cf = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_0571915001ffd5d1e3c0047fe3601bad = $(`&lt;div id=&quot;html_0571915001ffd5d1e3c0047fe3601bad&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;BURGLARY&lt;/div&gt;`)[0];
                popup_a75777e8ea1472429ce66d52ff76d4cf.setContent(html_0571915001ffd5d1e3c0047fe3601bad);



        marker_4360b2baf466f987219bfb40da4feb42.bindPopup(popup_a75777e8ea1472429ce66d52ff76d4cf)
        ;




            var marker_8be4e742dd57bd5b4cdf4bdc144652b6 = L.marker(
                [37.7131083433264, -122.444314025188],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_edcad76eba6d76ee0b9384647db012e1 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_7b06820d97c8e6894932438751b4379d = $(`&lt;div id=&quot;html_7b06820d97c8e6894932438751b4379d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;DRUG/NARCOTIC&lt;/div&gt;`)[0];
                popup_edcad76eba6d76ee0b9384647db012e1.setContent(html_7b06820d97c8e6894932438751b4379d);



        marker_8be4e742dd57bd5b4cdf4bdc144652b6.bindPopup(popup_edcad76eba6d76ee0b9384647db012e1)
        ;




            var marker_c764d5f7a08e3a1286ecdb13fdfabb8f = L.marker(
                [37.7660160114103, -122.403644620439],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_e666cfd69188b76c27f600c6aa98a2fb = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_f09cb69c6fe717e0c19ab6fe19a9e92e = $(`&lt;div id=&quot;html_f09cb69c6fe717e0c19ab6fe19a9e92e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;MISSING PERSON&lt;/div&gt;`)[0];
                popup_e666cfd69188b76c27f600c6aa98a2fb.setContent(html_f09cb69c6fe717e0c19ab6fe19a9e92e);



        marker_c764d5f7a08e3a1286ecdb13fdfabb8f.bindPopup(popup_e666cfd69188b76c27f600c6aa98a2fb)
        ;




            var marker_481b0e050497d3313815ea75ab055247 = L.marker(
                [37.7660160114103, -122.403644620439],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_ae82581723d4643605633321d48413dc = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_0f0ba2c2f652b6105bd04a23660a23af = $(`&lt;div id=&quot;html_0f0ba2c2f652b6105bd04a23660a23af&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;MISSING PERSON&lt;/div&gt;`)[0];
                popup_ae82581723d4643605633321d48413dc.setContent(html_0f0ba2c2f652b6105bd04a23660a23af);



        marker_481b0e050497d3313815ea75ab055247.bindPopup(popup_ae82581723d4643605633321d48413dc)
        ;




            var marker_1d98fd46db579b1573c41c460065b736 = L.marker(
                [37.7762310404758, -122.414714295579],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_e96ca35af396486d66969ae39e107ef9 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_6b79d7413af821ea2ab2c839b444d9ee = $(`&lt;div id=&quot;html_6b79d7413af821ea2ab2c839b444d9ee&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_e96ca35af396486d66969ae39e107ef9.setContent(html_6b79d7413af821ea2ab2c839b444d9ee);



        marker_1d98fd46db579b1573c41c460065b736.bindPopup(popup_e96ca35af396486d66969ae39e107ef9)
        ;




            var marker_c48698f61fb3c5c0398e6a20429b2cb9 = L.marker(
                [37.7762310404758, -122.414714295579],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_d9ab601866d252ae8055000e6b79dd3a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_09d5d102f60c80b91ab58152f4fb51fc = $(`&lt;div id=&quot;html_09d5d102f60c80b91ab58152f4fb51fc&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;MISSING PERSON&lt;/div&gt;`)[0];
                popup_d9ab601866d252ae8055000e6b79dd3a.setContent(html_09d5d102f60c80b91ab58152f4fb51fc);



        marker_c48698f61fb3c5c0398e6a20429b2cb9.bindPopup(popup_d9ab601866d252ae8055000e6b79dd3a)
        ;




            var marker_e596e7912005ecbc544bd4aeee70af4e = L.marker(
                [37.7775118895695, -122.418045452768],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_1c1732edc5ddec747b1072bf6b92f7e4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_a501eb4c65cac4a97bbf488759af284e = $(`&lt;div id=&quot;html_a501eb4c65cac4a97bbf488759af284e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VEHICLE THEFT&lt;/div&gt;`)[0];
                popup_1c1732edc5ddec747b1072bf6b92f7e4.setContent(html_a501eb4c65cac4a97bbf488759af284e);



        marker_e596e7912005ecbc544bd4aeee70af4e.bindPopup(popup_1c1732edc5ddec747b1072bf6b92f7e4)
        ;




            var marker_cf42c3121ed31e0ca581b5e1ecffa602 = L.marker(
                [37.7820238478975, -122.401161555602],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_843dad71e41f627ce4223f5f16a5c84f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_4fd92611763c45237b737d7251ea623d = $(`&lt;div id=&quot;html_4fd92611763c45237b737d7251ea623d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_843dad71e41f627ce4223f5f16a5c84f.setContent(html_4fd92611763c45237b737d7251ea623d);



        marker_cf42c3121ed31e0ca581b5e1ecffa602.bindPopup(popup_843dad71e41f627ce4223f5f16a5c84f)
        ;




            var marker_98e837104acaa81174e728e078c12863 = L.marker(
                [37.72700531963, -122.403408669191],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_a73474db9e51ed6110e7b3c8407ddc28 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_9f5196cfdc153fa3625f599fdf82ff20 = $(`&lt;div id=&quot;html_9f5196cfdc153fa3625f599fdf82ff20&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_a73474db9e51ed6110e7b3c8407ddc28.setContent(html_9f5196cfdc153fa3625f599fdf82ff20);



        marker_98e837104acaa81174e728e078c12863.bindPopup(popup_a73474db9e51ed6110e7b3c8407ddc28)
        ;




            var marker_5b72a9cfe8040c8cb70df4dc05759cea = L.marker(
                [37.7838344374141, -122.412930522059],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_d9461df5fe21c62ef2187c9d26ffcd12 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_47884c1e368585280b96354e9a6e69e7 = $(`&lt;div id=&quot;html_47884c1e368585280b96354e9a6e69e7&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VANDALISM&lt;/div&gt;`)[0];
                popup_d9461df5fe21c62ef2187c9d26ffcd12.setContent(html_47884c1e368585280b96354e9a6e69e7);



        marker_5b72a9cfe8040c8cb70df4dc05759cea.bindPopup(popup_d9461df5fe21c62ef2187c9d26ffcd12)
        ;




            var marker_931ee30f7f2c7aa4e650fdce93461e1c = L.marker(
                [37.7530186537446, -122.418587172219],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_75044397a54d7eb1635659cc7f335adf = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_319d88fb04d44fc7434b7cb1473fc176 = $(`&lt;div id=&quot;html_319d88fb04d44fc7434b7cb1473fc176&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_75044397a54d7eb1635659cc7f335adf.setContent(html_319d88fb04d44fc7434b7cb1473fc176);



        marker_931ee30f7f2c7aa4e650fdce93461e1c.bindPopup(popup_75044397a54d7eb1635659cc7f335adf)
        ;




            var marker_0e50bc1d1614e2c9f549f40d140fa5af = L.marker(
                [37.7740418385041, -122.414370627495],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_71e9fad3e22e332aab9bcc6e96b0e5e2 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_3305581dcc4fb20c0f2026873958e72c = $(`&lt;div id=&quot;html_3305581dcc4fb20c0f2026873958e72c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;FRAUD&lt;/div&gt;`)[0];
                popup_71e9fad3e22e332aab9bcc6e96b0e5e2.setContent(html_3305581dcc4fb20c0f2026873958e72c);



        marker_0e50bc1d1614e2c9f549f40d140fa5af.bindPopup(popup_71e9fad3e22e332aab9bcc6e96b0e5e2)
        ;




            var marker_7c2d2a1c4e7aaa4c273a81002c3fbece = L.marker(
                [37.790538993725, -122.403915681571],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_ca165c112cf304bc1c90fff86e94b5ef = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_79dd3b13598171d35b260f8cd280a73f = $(`&lt;div id=&quot;html_79dd3b13598171d35b260f8cd280a73f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_ca165c112cf304bc1c90fff86e94b5ef.setContent(html_79dd3b13598171d35b260f8cd280a73f);



        marker_7c2d2a1c4e7aaa4c273a81002c3fbece.bindPopup(popup_ca165c112cf304bc1c90fff86e94b5ef)
        ;




            var marker_caeb0a169ec9781f91dd3dc968cf47f9 = L.marker(
                [37.7830998244592, -122.419183096362],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_01a1a696ee76e8a358bd8bddf4c01308 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_47e96a3959a73adfd40af333c867be4b = $(`&lt;div id=&quot;html_47e96a3959a73adfd40af333c867be4b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_01a1a696ee76e8a358bd8bddf4c01308.setContent(html_47e96a3959a73adfd40af333c867be4b);



        marker_caeb0a169ec9781f91dd3dc968cf47f9.bindPopup(popup_01a1a696ee76e8a358bd8bddf4c01308)
        ;




            var marker_8cb5e436ddb48a5b51eef5ece347bdae = L.marker(
                [37.7407360548358, -122.388753046997],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_a1f47c7aeac29fde3ba1b4d5fd68b61a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_dba9c267ee1b3122837f7c06887f6f2b = $(`&lt;div id=&quot;html_dba9c267ee1b3122837f7c06887f6f2b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_a1f47c7aeac29fde3ba1b4d5fd68b61a.setContent(html_dba9c267ee1b3122837f7c06887f6f2b);



        marker_8cb5e436ddb48a5b51eef5ece347bdae.bindPopup(popup_a1f47c7aeac29fde3ba1b4d5fd68b61a)
        ;




            var marker_57376661ff1e6504aed89743ad6fc4a6 = L.marker(
                [37.7749912944366, -122.437799703468],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_77d6f5135386a5cb3490051882bbc1bc = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_ebb681f9b500211578cac5b967c29596 = $(`&lt;div id=&quot;html_ebb681f9b500211578cac5b967c29596&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_77d6f5135386a5cb3490051882bbc1bc.setContent(html_ebb681f9b500211578cac5b967c29596);



        marker_57376661ff1e6504aed89743ad6fc4a6.bindPopup(popup_77d6f5135386a5cb3490051882bbc1bc)
        ;




            var marker_69ecc49a17efcc3a3a6ba6ee41823aa4 = L.marker(
                [37.7770902743669, -122.421332684633],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_bd94f8280273f1cc86904b4b853cf855 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_c2bb8aa1392e414ac07b3b92b67352df = $(`&lt;div id=&quot;html_c2bb8aa1392e414ac07b3b92b67352df&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;MISSING PERSON&lt;/div&gt;`)[0];
                popup_bd94f8280273f1cc86904b4b853cf855.setContent(html_c2bb8aa1392e414ac07b3b92b67352df);



        marker_69ecc49a17efcc3a3a6ba6ee41823aa4.bindPopup(popup_bd94f8280273f1cc86904b4b853cf855)
        ;




            var marker_95f768b1375788dc901e884a9b7d11e9 = L.marker(
                [37.7770902743669, -122.421332684633],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_99f8159e62ba07c32af3fa6e4c852a67 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_0872b857695ac8932a413ef975b91bc9 = $(`&lt;div id=&quot;html_0872b857695ac8932a413ef975b91bc9&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;MISSING PERSON&lt;/div&gt;`)[0];
                popup_99f8159e62ba07c32af3fa6e4c852a67.setContent(html_0872b857695ac8932a413ef975b91bc9);



        marker_95f768b1375788dc901e884a9b7d11e9.bindPopup(popup_99f8159e62ba07c32af3fa6e4c852a67)
        ;




            var marker_a8e80f23382ac8f7014034374efc4519 = L.marker(
                [37.7822458223917, -122.446612978839],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_9178c90da27f4d13d79f1a35f020a57a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_4eb8f1dca7d06369f39dd5bdb82e5976 = $(`&lt;div id=&quot;html_4eb8f1dca7d06369f39dd5bdb82e5976&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_9178c90da27f4d13d79f1a35f020a57a.setContent(html_4eb8f1dca7d06369f39dd5bdb82e5976);



        marker_a8e80f23382ac8f7014034374efc4519.bindPopup(popup_9178c90da27f4d13d79f1a35f020a57a)
        ;




            var marker_f8714a2f2c808ea616aa229dd6788534 = L.marker(
                [37.7300379995128, -122.404594140634],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_decbc8531dee1760c6f5dbf46c2ca3fb = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_628b58e04af03d0abcf08a68607b6609 = $(`&lt;div id=&quot;html_628b58e04af03d0abcf08a68607b6609&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_decbc8531dee1760c6f5dbf46c2ca3fb.setContent(html_628b58e04af03d0abcf08a68607b6609);



        marker_f8714a2f2c808ea616aa229dd6788534.bindPopup(popup_decbc8531dee1760c6f5dbf46c2ca3fb)
        ;




            var marker_81f1375bfaf7a4adef770f22fcded712 = L.marker(
                [37.7953338267436, -122.397373740066],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_317fa6d1a3108dc56214bea51c043436 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_cb38f3f0a05b6cd82ad6a2c6baf29995 = $(`&lt;div id=&quot;html_cb38f3f0a05b6cd82ad6a2c6baf29995&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_317fa6d1a3108dc56214bea51c043436.setContent(html_cb38f3f0a05b6cd82ad6a2c6baf29995);



        marker_81f1375bfaf7a4adef770f22fcded712.bindPopup(popup_317fa6d1a3108dc56214bea51c043436)
        ;




            var marker_43a2385d51cab7e77b55ef5c8afa48e9 = L.marker(
                [37.7875158741623, -122.407434989523],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_dd87acc9090081ddea74dc4e9e8d8ec3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_2d924a611f82a5ae93feb506f1dfa22f = $(`&lt;div id=&quot;html_2d924a611f82a5ae93feb506f1dfa22f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_dd87acc9090081ddea74dc4e9e8d8ec3.setContent(html_2d924a611f82a5ae93feb506f1dfa22f);



        marker_43a2385d51cab7e77b55ef5c8afa48e9.bindPopup(popup_dd87acc9090081ddea74dc4e9e8d8ec3)
        ;




            var marker_0ee5d61b5ded3d91c2c7d2ac84a5cec4 = L.marker(
                [37.7785233776032, -122.403464080033],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_ea79d18e354e7f509ee92379b520e4cc = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_a8f9e542c1ca45b1817f18b611052c5a = $(`&lt;div id=&quot;html_a8f9e542c1ca45b1817f18b611052c5a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;PROSTITUTION&lt;/div&gt;`)[0];
                popup_ea79d18e354e7f509ee92379b520e4cc.setContent(html_a8f9e542c1ca45b1817f18b611052c5a);



        marker_0ee5d61b5ded3d91c2c7d2ac84a5cec4.bindPopup(popup_ea79d18e354e7f509ee92379b520e4cc)
        ;




            var marker_075ae1cb830d69a4cbf0365cdf45d68a = L.marker(
                [37.7785233776032, -122.403464080033],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_5347d94fe58af0d68f026a6b8c78400e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_ef26282eb9b850d2627371cbbe4ce36e = $(`&lt;div id=&quot;html_ef26282eb9b850d2627371cbbe4ce36e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_5347d94fe58af0d68f026a6b8c78400e.setContent(html_ef26282eb9b850d2627371cbbe4ce36e);



        marker_075ae1cb830d69a4cbf0365cdf45d68a.bindPopup(popup_5347d94fe58af0d68f026a6b8c78400e)
        ;




            var marker_8f6296143e9c9ad3663b84dd87d70f1b = L.marker(
                [37.773291806903, -122.436614181331],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_08d3a3bcb70c2a211fdd120afb0cc287 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_b02f2f2ba66b872aac482ba322d790d3 = $(`&lt;div id=&quot;html_b02f2f2ba66b872aac482ba322d790d3&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_08d3a3bcb70c2a211fdd120afb0cc287.setContent(html_b02f2f2ba66b872aac482ba322d790d3);



        marker_8f6296143e9c9ad3663b84dd87d70f1b.bindPopup(popup_08d3a3bcb70c2a211fdd120afb0cc287)
        ;




            var marker_c45d59a9b0814185a8c2d8bcce919b46 = L.marker(
                [37.780527578509, -122.396849015172],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_e0e6ff447b32717f648b631dc55a2528 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_0090fb29f8561294f54a0e515bf273cd = $(`&lt;div id=&quot;html_0090fb29f8561294f54a0e515bf273cd&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;DRUG/NARCOTIC&lt;/div&gt;`)[0];
                popup_e0e6ff447b32717f648b631dc55a2528.setContent(html_0090fb29f8561294f54a0e515bf273cd);



        marker_c45d59a9b0814185a8c2d8bcce919b46.bindPopup(popup_e0e6ff447b32717f648b631dc55a2528)
        ;




            var marker_1a86d196e0256495929ece43f0f955ba = L.marker(
                [37.780527578509, -122.396849015172],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_3d29909a2835e6c95857eea8d4f1666d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_6e25bc5ed70f8ebd0ccdd99ff076422f = $(`&lt;div id=&quot;html_6e25bc5ed70f8ebd0ccdd99ff076422f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_3d29909a2835e6c95857eea8d4f1666d.setContent(html_6e25bc5ed70f8ebd0ccdd99ff076422f);



        marker_1a86d196e0256495929ece43f0f955ba.bindPopup(popup_3d29909a2835e6c95857eea8d4f1666d)
        ;




            var marker_5d36a381a77b88266129fc1066f9225a = L.marker(
                [37.7284180706602, -122.450000790445],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_871c01d7b29f8e5649385b214fc1df9a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_d66157cab9c65bd97775b34d1132729e = $(`&lt;div id=&quot;html_d66157cab9c65bd97775b34d1132729e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_871c01d7b29f8e5649385b214fc1df9a.setContent(html_d66157cab9c65bd97775b34d1132729e);



        marker_5d36a381a77b88266129fc1066f9225a.bindPopup(popup_871c01d7b29f8e5649385b214fc1df9a)
        ;




            var marker_44d0d0a2dcbe6aaa45ba8ef8f3ed6250 = L.marker(
                [37.7292114647359, -122.400834283031],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_25dcdbcaaba70e4867edbb4a2c07e507 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_8315ca1369bc3a695112402584615ba6 = $(`&lt;div id=&quot;html_8315ca1369bc3a695112402584615ba6&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_25dcdbcaaba70e4867edbb4a2c07e507.setContent(html_8315ca1369bc3a695112402584615ba6);



        marker_44d0d0a2dcbe6aaa45ba8ef8f3ed6250.bindPopup(popup_25dcdbcaaba70e4867edbb4a2c07e507)
        ;




            var marker_96ee2ea520b16e2369e95915a5a8137a = L.marker(
                [37.7880065324392, -122.399802145799],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_3a14876b80b141549d0ec28a45d9d632 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_fb4848bb8fea2495f70f96335e8cea85 = $(`&lt;div id=&quot;html_fb4848bb8fea2495f70f96335e8cea85&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_3a14876b80b141549d0ec28a45d9d632.setContent(html_fb4848bb8fea2495f70f96335e8cea85);



        marker_96ee2ea520b16e2369e95915a5a8137a.bindPopup(popup_3a14876b80b141549d0ec28a45d9d632)
        ;




            var marker_863b45b14ea456fbbb69ea2aafc99fa4 = L.marker(
                [37.7239748241609, -122.3949284758],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_da7f65e49c156ebac7956bddf7e8b8c1 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_37298f5d7fcfb2f36aadf502f134be01 = $(`&lt;div id=&quot;html_37298f5d7fcfb2f36aadf502f134be01&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;SECONDARY CODES&lt;/div&gt;`)[0];
                popup_da7f65e49c156ebac7956bddf7e8b8c1.setContent(html_37298f5d7fcfb2f36aadf502f134be01);



        marker_863b45b14ea456fbbb69ea2aafc99fa4.bindPopup(popup_da7f65e49c156ebac7956bddf7e8b8c1)
        ;




            var marker_e9207a9d769975ba71f1ee18853515e7 = L.marker(
                [37.7239748241609, -122.3949284758],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_3f21876f6555bd5e2c7a2319e485ef22 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_c177addbf5f07ccb8bfb32e7d004be5a = $(`&lt;div id=&quot;html_c177addbf5f07ccb8bfb32e7d004be5a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;SUSPICIOUS OCC&lt;/div&gt;`)[0];
                popup_3f21876f6555bd5e2c7a2319e485ef22.setContent(html_c177addbf5f07ccb8bfb32e7d004be5a);



        marker_e9207a9d769975ba71f1ee18853515e7.bindPopup(popup_3f21876f6555bd5e2c7a2319e485ef22)
        ;




            var marker_b1279e4edbf9e9d669f752cf60be4040 = L.marker(
                [37.7239748241609, -122.3949284758],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_74605e6103c4f6980a8a8031c9091727 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_44b01e0085c9dbd65bb82fd48b99ef3c = $(`&lt;div id=&quot;html_44b01e0085c9dbd65bb82fd48b99ef3c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_74605e6103c4f6980a8a8031c9091727.setContent(html_44b01e0085c9dbd65bb82fd48b99ef3c);



        marker_b1279e4edbf9e9d669f752cf60be4040.bindPopup(popup_74605e6103c4f6980a8a8031c9091727)
        ;




            var marker_055dccf9075ad06c64d506747f6da0c1 = L.marker(
                [37.7883235449904, -122.41185703254],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_bf6f54d2e2afb92223eae9ef73ca695d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_d28f5f9cbeb220df44bdcd5778c932c3 = $(`&lt;div id=&quot;html_d28f5f9cbeb220df44bdcd5778c932c3&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_bf6f54d2e2afb92223eae9ef73ca695d.setContent(html_d28f5f9cbeb220df44bdcd5778c932c3);



        marker_055dccf9075ad06c64d506747f6da0c1.bindPopup(popup_bf6f54d2e2afb92223eae9ef73ca695d)
        ;




            var marker_a14d2f11273851c32acdd21e090e3d91 = L.marker(
                [37.7559977339856, -122.409435617106],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_d071148edafc09130ba0a2ba03a115d1 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_632ad0bb679560699f5574f6e2c2bfd9 = $(`&lt;div id=&quot;html_632ad0bb679560699f5574f6e2c2bfd9&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_d071148edafc09130ba0a2ba03a115d1.setContent(html_632ad0bb679560699f5574f6e2c2bfd9);



        marker_a14d2f11273851c32acdd21e090e3d91.bindPopup(popup_d071148edafc09130ba0a2ba03a115d1)
        ;




            var marker_233336416218d595d17bce6e072ad7a4 = L.marker(
                [37.7870798144443, -122.425883358148],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_a90cef62ba3b78a890e8623af630d38d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_26a55a2744a96010b9020d981ed4fa77 = $(`&lt;div id=&quot;html_26a55a2744a96010b9020d981ed4fa77&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_a90cef62ba3b78a890e8623af630d38d.setContent(html_26a55a2744a96010b9020d981ed4fa77);



        marker_233336416218d595d17bce6e072ad7a4.bindPopup(popup_a90cef62ba3b78a890e8623af630d38d)
        ;




            var marker_1a97fd9faac1c30543f2e5a000a87370 = L.marker(
                [37.7360374466862, -122.415126543001],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_468623a0c7b25d2eb7d70dd6b6368935 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_e7497825f707c28a46ec0d814ea23b54 = $(`&lt;div id=&quot;html_e7497825f707c28a46ec0d814ea23b54&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_468623a0c7b25d2eb7d70dd6b6368935.setContent(html_e7497825f707c28a46ec0d814ea23b54);



        marker_1a97fd9faac1c30543f2e5a000a87370.bindPopup(popup_468623a0c7b25d2eb7d70dd6b6368935)
        ;




            var marker_b20353741d545c68728be467b0d8ec53 = L.marker(
                [37.712767884821, -122.431928011089],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_abd013bb0bb3b11ae3471e6710e75854 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_f8d89c1e6f8f263cd27789076741ba07 = $(`&lt;div id=&quot;html_f8d89c1e6f8f263cd27789076741ba07&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_abd013bb0bb3b11ae3471e6710e75854.setContent(html_f8d89c1e6f8f263cd27789076741ba07);



        marker_b20353741d545c68728be467b0d8ec53.bindPopup(popup_abd013bb0bb3b11ae3471e6710e75854)
        ;




            var marker_42518ebb92c732e8a302c28a8d9079a8 = L.marker(
                [37.7895710255863, -122.402163713618],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_de21c0c9b7ecaeefc03282e1834efc00 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_03f790d338386d4d8c8cdbe1851ac957 = $(`&lt;div id=&quot;html_03f790d338386d4d8c8cdbe1851ac957&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;DRUNKENNESS&lt;/div&gt;`)[0];
                popup_de21c0c9b7ecaeefc03282e1834efc00.setContent(html_03f790d338386d4d8c8cdbe1851ac957);



        marker_42518ebb92c732e8a302c28a8d9079a8.bindPopup(popup_de21c0c9b7ecaeefc03282e1834efc00)
        ;




            var marker_a7deec3a2ba20a9ad66d7d9b95a4aad2 = L.marker(
                [37.7307429169559, -122.429306728376],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_e73d22b0217569020a30195ccfc468ad = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_dc71e8c19a7cdd7ab335c2411b2422fc = $(`&lt;div id=&quot;html_dc71e8c19a7cdd7ab335c2411b2422fc&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_e73d22b0217569020a30195ccfc468ad.setContent(html_dc71e8c19a7cdd7ab335c2411b2422fc);



        marker_a7deec3a2ba20a9ad66d7d9b95a4aad2.bindPopup(popup_e73d22b0217569020a30195ccfc468ad)
        ;




            var marker_e280416e31c50befb6c521e255040077 = L.marker(
                [37.7838365565348, -122.413790972781],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_98b876f84e88e769ad34a6e614cad12f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_5db8117cf5b29091f83490d964ef8620 = $(`&lt;div id=&quot;html_5db8117cf5b29091f83490d964ef8620&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VANDALISM&lt;/div&gt;`)[0];
                popup_98b876f84e88e769ad34a6e614cad12f.setContent(html_5db8117cf5b29091f83490d964ef8620);



        marker_e280416e31c50befb6c521e255040077.bindPopup(popup_98b876f84e88e769ad34a6e614cad12f)
        ;




            var marker_8c46bef612f203d00766324854b60c15 = L.marker(
                [37.7307429169559, -122.429306728376],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_2da22254b5c3dc66f54af986622c116c = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_4a8c9b05805b236a295491f9e734cd1f = $(`&lt;div id=&quot;html_4a8c9b05805b236a295491f9e734cd1f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_2da22254b5c3dc66f54af986622c116c.setContent(html_4a8c9b05805b236a295491f9e734cd1f);



        marker_8c46bef612f203d00766324854b60c15.bindPopup(popup_2da22254b5c3dc66f54af986622c116c)
        ;




            var marker_4f76848cbaa0882b094d73dcdba8e928 = L.marker(
                [37.7373623605213, -122.422067184937],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_076c236b6b48359d1ab43ba0b04ce74b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_632e0438cdad699f41cd556470a73689 = $(`&lt;div id=&quot;html_632e0438cdad699f41cd556470a73689&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;SECONDARY CODES&lt;/div&gt;`)[0];
                popup_076c236b6b48359d1ab43ba0b04ce74b.setContent(html_632e0438cdad699f41cd556470a73689);



        marker_4f76848cbaa0882b094d73dcdba8e928.bindPopup(popup_076c236b6b48359d1ab43ba0b04ce74b)
        ;




            var marker_cb8eb4bf41993c6b42383141e9363d6c = L.marker(
                [37.7373623605213, -122.422067184937],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_96429c200a082103c19c2821c5b0838d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_a49508caddf524112912aa3a285ed842 = $(`&lt;div id=&quot;html_a49508caddf524112912aa3a285ed842&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VANDALISM&lt;/div&gt;`)[0];
                popup_96429c200a082103c19c2821c5b0838d.setContent(html_a49508caddf524112912aa3a285ed842);



        marker_cb8eb4bf41993c6b42383141e9363d6c.bindPopup(popup_96429c200a082103c19c2821c5b0838d)
        ;




            var marker_cb477b7f76b01234abb7ab0e6406b70e = L.marker(
                [37.7859988323798, -122.411747371924],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_3f612fa23b6d752abdf7b7cdd892cf57 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_9c3565a099a963609be53fdc73718b43 = $(`&lt;div id=&quot;html_9c3565a099a963609be53fdc73718b43&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;SUSPICIOUS OCC&lt;/div&gt;`)[0];
                popup_3f612fa23b6d752abdf7b7cdd892cf57.setContent(html_9c3565a099a963609be53fdc73718b43);



        marker_cb477b7f76b01234abb7ab0e6406b70e.bindPopup(popup_3f612fa23b6d752abdf7b7cdd892cf57)
        ;




            var marker_3006de00230f8bf60a32628f69b43c27 = L.marker(
                [37.7633758058059, -122.420434724553],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_28916a99ba9940e593bc8170bf16b136 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_bd40ba525fd37b8748b5c5adeb932ee9 = $(`&lt;div id=&quot;html_bd40ba525fd37b8748b5c5adeb932ee9&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_28916a99ba9940e593bc8170bf16b136.setContent(html_bd40ba525fd37b8748b5c5adeb932ee9);



        marker_3006de00230f8bf60a32628f69b43c27.bindPopup(popup_28916a99ba9940e593bc8170bf16b136)
        ;




            var marker_78cd0e71ff12bfbf71e68e42bdfd89ea = L.marker(
                [37.7850226622786, -122.411987643595],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_3d74fc1ba9caa9df1a031f76e5455c74 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_5f00a889ce34e049f89938a8324fdc1b = $(`&lt;div id=&quot;html_5f00a889ce34e049f89938a8324fdc1b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_3d74fc1ba9caa9df1a031f76e5455c74.setContent(html_5f00a889ce34e049f89938a8324fdc1b);



        marker_78cd0e71ff12bfbf71e68e42bdfd89ea.bindPopup(popup_3d74fc1ba9caa9df1a031f76e5455c74)
        ;




            var marker_1b231c86c84e0aa832becc601eb00914 = L.marker(
                [37.7746206491065, -122.500380427915],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_3440ce8f96fe0c33e17f3dfda53e4027 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_eaf8ae4e90cd91da0dc42fdccc15ddd9 = $(`&lt;div id=&quot;html_eaf8ae4e90cd91da0dc42fdccc15ddd9&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_3440ce8f96fe0c33e17f3dfda53e4027.setContent(html_eaf8ae4e90cd91da0dc42fdccc15ddd9);



        marker_1b231c86c84e0aa832becc601eb00914.bindPopup(popup_3440ce8f96fe0c33e17f3dfda53e4027)
        ;




            var marker_89ad20befc3b5c46f4461473f51cf45f = L.marker(
                [37.7751918267217, -122.466558780683],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_dc2299ccece6d27a83e5ca327c95439c = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_6aa1c4ea9d9a8e508f3ac8bfd987cc84 = $(`&lt;div id=&quot;html_6aa1c4ea9d9a8e508f3ac8bfd987cc84&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ROBBERY&lt;/div&gt;`)[0];
                popup_dc2299ccece6d27a83e5ca327c95439c.setContent(html_6aa1c4ea9d9a8e508f3ac8bfd987cc84);



        marker_89ad20befc3b5c46f4461473f51cf45f.bindPopup(popup_dc2299ccece6d27a83e5ca327c95439c)
        ;




            var marker_6f866574d2d9fec2030ff847a6d95c37 = L.marker(
                [37.7490841729028, -122.486925960114],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_39282c6918727d37321631d395544fdb = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_e793ec273b2ae36dd0669dc2bb89e0c0 = $(`&lt;div id=&quot;html_e793ec273b2ae36dd0669dc2bb89e0c0&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_39282c6918727d37321631d395544fdb.setContent(html_e793ec273b2ae36dd0669dc2bb89e0c0);



        marker_6f866574d2d9fec2030ff847a6d95c37.bindPopup(popup_39282c6918727d37321631d395544fdb)
        ;




            var marker_a57bb2c2952a35cce2683d046a153fa6 = L.marker(
                [37.7685360123583, -122.41561633832],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_ec0e6c6499332776769fe2566ba349f5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_bdf92919cde74ec41fc84836b1d2bc41 = $(`&lt;div id=&quot;html_bdf92919cde74ec41fc84836b1d2bc41&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_ec0e6c6499332776769fe2566ba349f5.setContent(html_bdf92919cde74ec41fc84836b1d2bc41);



        marker_a57bb2c2952a35cce2683d046a153fa6.bindPopup(popup_ec0e6c6499332776769fe2566ba349f5)
        ;




            var marker_a8e3e94403498fa3e645ba4b3c88faff = L.marker(
                [37.7644297714074, -122.449751652563],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_8a5543e9ac381cce1a1b9da3a6d36fee = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_174745617673d3b174a90fa6d9cac3f1 = $(`&lt;div id=&quot;html_174745617673d3b174a90fa6d9cac3f1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;BURGLARY&lt;/div&gt;`)[0];
                popup_8a5543e9ac381cce1a1b9da3a6d36fee.setContent(html_174745617673d3b174a90fa6d9cac3f1);



        marker_a8e3e94403498fa3e645ba4b3c88faff.bindPopup(popup_8a5543e9ac381cce1a1b9da3a6d36fee)
        ;




            var marker_e2dcfd88bbd2697d6aacbfbd6adf31b9 = L.marker(
                [37.7644297714074, -122.449751652563],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_443bd005e4f2f751b9da72d589ddc1b9 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_01c57f5cbbc4be11dc0bc7e52e2326a2 = $(`&lt;div id=&quot;html_01c57f5cbbc4be11dc0bc7e52e2326a2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_443bd005e4f2f751b9da72d589ddc1b9.setContent(html_01c57f5cbbc4be11dc0bc7e52e2326a2);



        marker_e2dcfd88bbd2697d6aacbfbd6adf31b9.bindPopup(popup_443bd005e4f2f751b9da72d589ddc1b9)
        ;




            var marker_52ffd4a89cf1d20f48b68b49f17f9d62 = L.marker(
                [37.7352681469084, -122.472715759631],
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


        var popup_1ed114499c45c44eb429f9a5006fdbe4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_a6bcdb164e371bb23d287a1a1a19be72 = $(`&lt;div id=&quot;html_a6bcdb164e371bb23d287a1a1a19be72&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_1ed114499c45c44eb429f9a5006fdbe4.setContent(html_a6bcdb164e371bb23d287a1a1a19be72);



        marker_52ffd4a89cf1d20f48b68b49f17f9d62.bindPopup(popup_1ed114499c45c44eb429f9a5006fdbe4)
        ;




            var feature_group_2f0221b750172ee94709e71b1e0162a7 = L.featureGroup(
                {}
            ).addTo(map_fbfb269e38054ab8d9256217b0f93903);


            var circle_marker_2ac9e1f9c2945deb14cc9ebe623cad22 = L.circleMarker(
                [37.775420706711, -122.403404791479],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_d4efd97d9334378b51e685cb4da6d1c6 = L.circleMarker(
                [37.775420706711, -122.403404791479],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_22c77cf16954dab5e826f82139103791 = L.circleMarker(
                [37.7299809672996, -122.388856204292],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_fb2d2bcee6780409f1a714bb1dc03e34 = L.circleMarker(
                [37.7857883766888, -122.412970537591],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_ef972e466eefe56d59dfb17d81bae024 = L.circleMarker(
                [37.7650501214668, -122.419671780296],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_4b4efccfa77036dcd61f6da354953658 = L.circleMarker(
                [37.788018555829, -122.426077177375],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_01adc17b422945f0e386d71de0a4c81a = L.circleMarker(
                [37.7808789360214, -122.405721454567],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_093031ff36bcde7064cb4d4507954c87 = L.circleMarker(
                [37.7839805592634, -122.411778295992],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_d0ba24c84dc3c2102ebb33073b2626db = L.circleMarker(
                [37.7757876218293, -122.393357241451],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_64b884023e12c5501d2a5ec1266d7817 = L.circleMarker(
                [37.7209669615499, -122.387181635995],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_7a0132ef5fc78bdfc7078915b28e18ff = L.circleMarker(
                [37.7644781578695, -122.477376524003],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_a8e39d702e1d1b4f920a665d8a2b6c0e = L.circleMarker(
                [37.7457389429655, -122.477960327299],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_112e1f754044a4a9739bd01a237faf3c = L.circleMarker(
                [37.7356970275482, -122.37675765553],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_1c64da937f3bb6b1dbacea9cab805b22 = L.circleMarker(
                [37.7292705199592, -122.432325871028],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_3286733e5eaeb2dd811f06179ab5775b = L.circleMarker(
                [37.791642982384, -122.40090869889],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_5fd719ea6972de451faca34561eed1f2 = L.circleMarker(
                [37.7837069301545, -122.408595110869],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_36efafcdc27fef87baf0a79c6390fbcc = L.circleMarker(
                [37.7572895904578, -122.406870402082],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_f35c05b006c56492b62814e29c25806e = L.circleMarker(
                [37.7489063051829, -122.420354780861],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_8551a6b81b99818bdb5c353e30c5edce = L.circleMarker(
                [37.715765426995, -122.439909766772],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_b4e6564766b8e726daf320055447af14 = L.circleMarker(
                [37.7835699386918, -122.408421116922],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_2802978b1ffbb084c442833b71419a53 = L.circleMarker(
                [37.7736186276456, -122.422315670749],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_ad3f859e14f39d408bfe09132928090f = L.circleMarker(
                [37.7928412840447, -122.424519835009],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_108da0701815f70cac3c14e9f45b66a3 = L.circleMarker(
                [37.7540986882068, -122.414233849038],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_b66b4534dfe92ffeeb33c275b6e19fbb = L.circleMarker(
                [37.7540986882068, -122.414233849038],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_0f764499fadd29a2cf423f7d6f3306b1 = L.circleMarker(
                [37.7714939969416, -122.507750131004],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_04faef4c944519c4e5b25e5e769c8d37 = L.circleMarker(
                [37.718302204766, -122.474444639595],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_91dfca88fa75b5adceb04da83e63a4c8 = L.circleMarker(
                [37.7645752317615, -122.427562596985],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_82373c421c63ada7cdd4e7284230c485 = L.circleMarker(
                [37.7874378309112, -122.419203004268],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_121fa16c5cc599babf08828729444bff = L.circleMarker(
                [37.7493688284532, -122.412690142308],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_0c9fe7f9060a60da6d86b6a75d7b8865 = L.circleMarker(
                [37.7092010462379, -122.434609280352],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_6fbe6c1562782cfcdeade9d765c701db = L.circleMarker(
                [37.7879209375533, -122.410882825551],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_6991b1845e1128e652ae5070eab3b1b2 = L.circleMarker(
                [37.8004566471039, -122.401432754722],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_5fde71c33ff656ed544bd8adc2450351 = L.circleMarker(
                [37.7435550542265, -122.421128029505],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_35a022af405d17094348dd81f821b35f = L.circleMarker(
                [37.7865647607685, -122.407244087032],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_36d727fd3514b6658e8bc8f97719dae2 = L.circleMarker(
                [37.7615655928045, -122.423803001901],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_dfc03b3d4e7e5bd76063b9e8a40de60c = L.circleMarker(
                [37.7615655928045, -122.423803001901],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_8da9e58b7475d2972882e08b6369b633 = L.circleMarker(
                [37.7441927508932, -122.444685482273],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_b2b726ef15c00da5b28e7ffe17aa1e1a = L.circleMarker(
                [37.7754692820041, -122.415757039196],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_6e5f58f40719c32319119b6fe9b61af6 = L.circleMarker(
                [37.7285280627465, -122.475647460786],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_33785f39f2cbe15f21d71a037b0d319f = L.circleMarker(
                [37.7428517374449, -122.420967440564],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_0b6143db9b5beddc48d814ea6d5612f9 = L.circleMarker(
                [37.7821198488931, -122.415669661443],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_a3c92d232fefcb8a5b5694808ecd6484 = L.circleMarker(
                [37.7791674218963, -122.406346425632],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_1f7cf340ed50e9fbee8a007fd965b487 = L.circleMarker(
                [37.7657184395282, -122.409529913278],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_a91c16f0c1a5543542af80fbf01f851f = L.circleMarker(
                [37.775420706711, -122.403404791479],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_128eae6975cd95d4c2b6c95914754b75 = L.circleMarker(
                [37.767524308783, -122.410738097315],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_b7efece611b07a1593f3149a278e6005 = L.circleMarker(
                [37.767524308783, -122.410738097315],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_a3702d15a663666c4d3e905ff5e4f668 = L.circleMarker(
                [37.7131083433264, -122.444314025188],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_5ac5cac14c18de352b9c446cdb1d510c = L.circleMarker(
                [37.7131083433264, -122.444314025188],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_d6938a9bdc488b71ee65f928a055d8ed = L.circleMarker(
                [37.7660160114103, -122.403644620439],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_10131dec7db5c703287e3b7c02030861 = L.circleMarker(
                [37.7660160114103, -122.403644620439],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_827a0a67d4f080c7507a019cad94a02e = L.circleMarker(
                [37.7762310404758, -122.414714295579],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_bb4459b6fe3f80508ef5bdf5a945885d = L.circleMarker(
                [37.7762310404758, -122.414714295579],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_01154a1e441ac827401859832cac4a88 = L.circleMarker(
                [37.7775118895695, -122.418045452768],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_f3ecf9c4227b798c39c558d49fe9c434 = L.circleMarker(
                [37.7820238478975, -122.401161555602],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_b7fa50f88f68dcb53dd82e3c98f924da = L.circleMarker(
                [37.72700531963, -122.403408669191],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_92181e8ae7de5d09c1ad5e66297c2c73 = L.circleMarker(
                [37.7838344374141, -122.412930522059],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_5c29a3baf87794b1ba6ddb01e4c2efbc = L.circleMarker(
                [37.7530186537446, -122.418587172219],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_7b916e790100e8e60ff6bd059c9ce702 = L.circleMarker(
                [37.7740418385041, -122.414370627495],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_c8f72deaeb6362c5dc7d796d9791425d = L.circleMarker(
                [37.790538993725, -122.403915681571],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_bd4877c65c849293447b665bbd9c8c18 = L.circleMarker(
                [37.7830998244592, -122.419183096362],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_ed95a95686359834c2c7e3693c7ba80c = L.circleMarker(
                [37.7407360548358, -122.388753046997],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_8304331166fe3772e033c193b33155c9 = L.circleMarker(
                [37.7749912944366, -122.437799703468],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_f65d4936c15f9d1aa0d049a14c84d9f4 = L.circleMarker(
                [37.7770902743669, -122.421332684633],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_6bf28bb098dfe0cf01944927faae2044 = L.circleMarker(
                [37.7770902743669, -122.421332684633],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_2160e274b375d9c473be1acd3e12af8f = L.circleMarker(
                [37.7822458223917, -122.446612978839],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_57b00bca11eeb3d504e83cbcd729a3c3 = L.circleMarker(
                [37.7300379995128, -122.404594140634],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_7d8aaafc1c32c7a3472ee0c91fdcee8e = L.circleMarker(
                [37.7953338267436, -122.397373740066],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_341470a6168b514c451887bacb361506 = L.circleMarker(
                [37.7875158741623, -122.407434989523],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_83333c667c42f55918166db5a53ea2bf = L.circleMarker(
                [37.7785233776032, -122.403464080033],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_1f175ded693c70d4d7e3eafa40890697 = L.circleMarker(
                [37.7785233776032, -122.403464080033],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_ea57038c37351ad8cf02b973f6ed37cb = L.circleMarker(
                [37.773291806903, -122.436614181331],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_fa9fe66a2b1590b2dad10522e91ccb3c = L.circleMarker(
                [37.780527578509, -122.396849015172],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_199a025c2e0250a91307e422b6e16207 = L.circleMarker(
                [37.780527578509, -122.396849015172],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_3b978d8834038d25438bde57e55f0d8e = L.circleMarker(
                [37.7284180706602, -122.450000790445],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_4a07f62774f60ad28e58de24c45b5ef7 = L.circleMarker(
                [37.7292114647359, -122.400834283031],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_60ec30ccea35da17fe972f3f0c5cbfa0 = L.circleMarker(
                [37.7880065324392, -122.399802145799],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_42652458a69b2f2e8e97abfd4fed4938 = L.circleMarker(
                [37.7239748241609, -122.3949284758],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_a5e1a50f8862014c89aa320282e8dcd6 = L.circleMarker(
                [37.7239748241609, -122.3949284758],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_fc4128d308e1602f113e5065ad50fade = L.circleMarker(
                [37.7239748241609, -122.3949284758],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_f18ec08b055b1274ce944b6013dd6488 = L.circleMarker(
                [37.7883235449904, -122.41185703254],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_a77ef3537d98d7648b0b957424b97c5b = L.circleMarker(
                [37.7559977339856, -122.409435617106],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_79f10e4d400a8abfe2fc1b3dc680244c = L.circleMarker(
                [37.7870798144443, -122.425883358148],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_8199f884a4bd75a6039f11f7302d104b = L.circleMarker(
                [37.7360374466862, -122.415126543001],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_a3c8b4764a52d103bb3ed74a56793580 = L.circleMarker(
                [37.712767884821, -122.431928011089],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_c66c0bb86914f740cc07dd6a23b0e962 = L.circleMarker(
                [37.7895710255863, -122.402163713618],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_257301f97733381ec614ed76eb10f89f = L.circleMarker(
                [37.7307429169559, -122.429306728376],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_405baa6cdd035892be270fd518e626f2 = L.circleMarker(
                [37.7838365565348, -122.413790972781],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_467bffbc4113be17f290df86821ac531 = L.circleMarker(
                [37.7307429169559, -122.429306728376],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_f6c1520902b091632a43cb8670a6c371 = L.circleMarker(
                [37.7373623605213, -122.422067184937],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_6d191b660e41bd4df23c8bc066d55f10 = L.circleMarker(
                [37.7373623605213, -122.422067184937],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_f0e165c265a4429debe0e52d4d11d4f7 = L.circleMarker(
                [37.7859988323798, -122.411747371924],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_a2e6d2daa65cd0b23899c08d1caeb8d4 = L.circleMarker(
                [37.7633758058059, -122.420434724553],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_4522b15aa8254774d76ff21c88243788 = L.circleMarker(
                [37.7850226622786, -122.411987643595],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_b7e635f29a4a2b79f266dded372fd675 = L.circleMarker(
                [37.7746206491065, -122.500380427915],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_845a67cf910c5e0e4419230473b72973 = L.circleMarker(
                [37.7751918267217, -122.466558780683],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_005e3a88ad3c63f55958ca58b3a6b815 = L.circleMarker(
                [37.7490841729028, -122.486925960114],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_83eef58a7c7b98702bde39f0077de072 = L.circleMarker(
                [37.7685360123583, -122.41561633832],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_173b39e45c61faed7aeaa42832e67ee5 = L.circleMarker(
                [37.7644297714074, -122.449751652563],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_aba9ed698670b7dcc63a32e326717924 = L.circleMarker(
                [37.7644297714074, -122.449751652563],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);


            var circle_marker_c61e5555392bfee11ed0ae1e01333d48 = L.circleMarker(
                [37.7352681469084, -122.472715759631],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(feature_group_2f0221b750172ee94709e71b1e0162a7);

&lt;/script&gt;
&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



Isn't this really cool? Now you are able to know what crime category occurred at each marker.

If you find the map to be so congested will all these markers, there are two remedies to this problem. The simpler solution is to remove these location markers and just add the text to the circle markers themselves as follows:



```python
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
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;

    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;

        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;

    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-1.12.4.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;

            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_dc85c4032b54b64749ac39b2e273a510 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            &lt;/style&gt;

&lt;/head&gt;
&lt;body&gt;


            &lt;div class=&quot;folium-map&quot; id=&quot;map_dc85c4032b54b64749ac39b2e273a510&quot; &gt;&lt;/div&gt;

&lt;/body&gt;
&lt;script&gt;


            var map_dc85c4032b54b64749ac39b2e273a510 = L.map(
                &quot;map_dc85c4032b54b64749ac39b2e273a510&quot;,
                {
                    center: [37.77, -122.42],
                    crs: L.CRS.EPSG3857,
                    zoom: 12,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );





            var tile_layer_ee174827cdf7e5013b931834013b8653 = L.tileLayer(
                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,
                {&quot;attribution&quot;: &quot;Data by \u0026copy; \u003ca target=\&quot;_blank\&quot; href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://www.openstreetmap.org/copyright\&quot;\u003eODbL\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


            var circle_marker_fbb60aaae9b2ca6bb4007baeb5fdfd6a = L.circleMarker(
                [37.775420706711, -122.403404791479],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_9c37b0651b0cbafdfb8e540c0898965d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_8e2a42e059ad39803f8299129c74c3e9 = $(`&lt;div id=&quot;html_8e2a42e059ad39803f8299129c74c3e9&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WEAPON LAWS&lt;/div&gt;`)[0];
                popup_9c37b0651b0cbafdfb8e540c0898965d.setContent(html_8e2a42e059ad39803f8299129c74c3e9);



        circle_marker_fbb60aaae9b2ca6bb4007baeb5fdfd6a.bindPopup(popup_9c37b0651b0cbafdfb8e540c0898965d)
        ;




            var circle_marker_b8030d8054829b691e0916496f612257 = L.circleMarker(
                [37.775420706711, -122.403404791479],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_5cd9a8495639dc30ba118e5608e6e451 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_a5a9f46f936b128f5bee1601eda7fe81 = $(`&lt;div id=&quot;html_a5a9f46f936b128f5bee1601eda7fe81&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WEAPON LAWS&lt;/div&gt;`)[0];
                popup_5cd9a8495639dc30ba118e5608e6e451.setContent(html_a5a9f46f936b128f5bee1601eda7fe81);



        circle_marker_b8030d8054829b691e0916496f612257.bindPopup(popup_5cd9a8495639dc30ba118e5608e6e451)
        ;




            var circle_marker_28a6a547a2b46616d018594c29563c89 = L.circleMarker(
                [37.7299809672996, -122.388856204292],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_2d720d83cf2aa2f0c176bba91d520e91 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_bebe41deca29bc0c4e7dc3096bd01554 = $(`&lt;div id=&quot;html_bebe41deca29bc0c4e7dc3096bd01554&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_2d720d83cf2aa2f0c176bba91d520e91.setContent(html_bebe41deca29bc0c4e7dc3096bd01554);



        circle_marker_28a6a547a2b46616d018594c29563c89.bindPopup(popup_2d720d83cf2aa2f0c176bba91d520e91)
        ;




            var circle_marker_d834c3b1a4987f2c7527b43b2a43b202 = L.circleMarker(
                [37.7857883766888, -122.412970537591],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_483fcba058f685cb803d128caa3d7a03 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_fd9d74c66428ae65917db3c930788e8f = $(`&lt;div id=&quot;html_fd9d74c66428ae65917db3c930788e8f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_483fcba058f685cb803d128caa3d7a03.setContent(html_fd9d74c66428ae65917db3c930788e8f);



        circle_marker_d834c3b1a4987f2c7527b43b2a43b202.bindPopup(popup_483fcba058f685cb803d128caa3d7a03)
        ;




            var circle_marker_84710ee64c675e9c37cb367e2e8e41f7 = L.circleMarker(
                [37.7650501214668, -122.419671780296],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_0e9f905eebb102891eed37ae59c434c2 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_e20ebad1a38a040862ceee1d82161c16 = $(`&lt;div id=&quot;html_e20ebad1a38a040862ceee1d82161c16&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_0e9f905eebb102891eed37ae59c434c2.setContent(html_e20ebad1a38a040862ceee1d82161c16);



        circle_marker_84710ee64c675e9c37cb367e2e8e41f7.bindPopup(popup_0e9f905eebb102891eed37ae59c434c2)
        ;




            var circle_marker_a6c00216d3bea1d385b5da40357d7480 = L.circleMarker(
                [37.788018555829, -122.426077177375],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_00f6f14cb45783674f0a23fbc3484fc4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_2c4aa37ce4c89bb26db75e286a55291e = $(`&lt;div id=&quot;html_2c4aa37ce4c89bb26db75e286a55291e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_00f6f14cb45783674f0a23fbc3484fc4.setContent(html_2c4aa37ce4c89bb26db75e286a55291e);



        circle_marker_a6c00216d3bea1d385b5da40357d7480.bindPopup(popup_00f6f14cb45783674f0a23fbc3484fc4)
        ;




            var circle_marker_5234774c5695e571dc3b52e0e7185e18 = L.circleMarker(
                [37.7808789360214, -122.405721454567],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_7992e6871dd28d0c00b55c6f4701ba7c = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_300b4e4ddcfaeb1de8c6a1f04e721b97 = $(`&lt;div id=&quot;html_300b4e4ddcfaeb1de8c6a1f04e721b97&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_7992e6871dd28d0c00b55c6f4701ba7c.setContent(html_300b4e4ddcfaeb1de8c6a1f04e721b97);



        circle_marker_5234774c5695e571dc3b52e0e7185e18.bindPopup(popup_7992e6871dd28d0c00b55c6f4701ba7c)
        ;




            var circle_marker_be9e62665dcf8486fa6397c670db7e3e = L.circleMarker(
                [37.7839805592634, -122.411778295992],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_20c12ad04c8e9eaace5cab7d893401ef = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_112ea41b788958329d12d6fa7b1e1832 = $(`&lt;div id=&quot;html_112ea41b788958329d12d6fa7b1e1832&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_20c12ad04c8e9eaace5cab7d893401ef.setContent(html_112ea41b788958329d12d6fa7b1e1832);



        circle_marker_be9e62665dcf8486fa6397c670db7e3e.bindPopup(popup_20c12ad04c8e9eaace5cab7d893401ef)
        ;




            var circle_marker_14fb9ed1041a1983f4b37e8d91698d48 = L.circleMarker(
                [37.7757876218293, -122.393357241451],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_b9e4fa78b27cd8ab7097a3a0ae6cda2a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_2ed399c66ee0006c79d62ddb4878fa17 = $(`&lt;div id=&quot;html_2ed399c66ee0006c79d62ddb4878fa17&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_b9e4fa78b27cd8ab7097a3a0ae6cda2a.setContent(html_2ed399c66ee0006c79d62ddb4878fa17);



        circle_marker_14fb9ed1041a1983f4b37e8d91698d48.bindPopup(popup_b9e4fa78b27cd8ab7097a3a0ae6cda2a)
        ;




            var circle_marker_8be34e8db885e41c7212c059a5f09a12 = L.circleMarker(
                [37.7209669615499, -122.387181635995],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_f4f565bb69e29bf33ac5e87a7f57e9b2 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_7b737823baebfd42fed846139704545c = $(`&lt;div id=&quot;html_7b737823baebfd42fed846139704545c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;MISSING PERSON&lt;/div&gt;`)[0];
                popup_f4f565bb69e29bf33ac5e87a7f57e9b2.setContent(html_7b737823baebfd42fed846139704545c);



        circle_marker_8be34e8db885e41c7212c059a5f09a12.bindPopup(popup_f4f565bb69e29bf33ac5e87a7f57e9b2)
        ;




            var circle_marker_0698e618e7b49583af50ca4fe59cde01 = L.circleMarker(
                [37.7644781578695, -122.477376524003],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_d70e5d123c47090ae441f73507bd33db = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_ce2ee4e479296c44fb5954327a29ce75 = $(`&lt;div id=&quot;html_ce2ee4e479296c44fb5954327a29ce75&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_d70e5d123c47090ae441f73507bd33db.setContent(html_ce2ee4e479296c44fb5954327a29ce75);



        circle_marker_0698e618e7b49583af50ca4fe59cde01.bindPopup(popup_d70e5d123c47090ae441f73507bd33db)
        ;




            var circle_marker_d04217b38ee6eca0c8d62d0e81f139de = L.circleMarker(
                [37.7457389429655, -122.477960327299],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_41c0e7e05bccaa348625b8302838c58f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_da41643427fee7fed74d6a9e326c5518 = $(`&lt;div id=&quot;html_da41643427fee7fed74d6a9e326c5518&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_41c0e7e05bccaa348625b8302838c58f.setContent(html_da41643427fee7fed74d6a9e326c5518);



        circle_marker_d04217b38ee6eca0c8d62d0e81f139de.bindPopup(popup_41c0e7e05bccaa348625b8302838c58f)
        ;




            var circle_marker_729cb35ef850f92453c80e2746df29e9 = L.circleMarker(
                [37.7356970275482, -122.37675765553],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_24a28d7f446178ad67a51d027d6d8673 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_f517616fbaef77e53dc8e84097400f99 = $(`&lt;div id=&quot;html_f517616fbaef77e53dc8e84097400f99&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_24a28d7f446178ad67a51d027d6d8673.setContent(html_f517616fbaef77e53dc8e84097400f99);



        circle_marker_729cb35ef850f92453c80e2746df29e9.bindPopup(popup_24a28d7f446178ad67a51d027d6d8673)
        ;




            var circle_marker_534b9a10ebd56215adde4ac3ad423952 = L.circleMarker(
                [37.7292705199592, -122.432325871028],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_16d63704df26d689c8f94f6533110851 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_2a60ff15828c20c1dc47f462c70a1e54 = $(`&lt;div id=&quot;html_2a60ff15828c20c1dc47f462c70a1e54&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_16d63704df26d689c8f94f6533110851.setContent(html_2a60ff15828c20c1dc47f462c70a1e54);



        circle_marker_534b9a10ebd56215adde4ac3ad423952.bindPopup(popup_16d63704df26d689c8f94f6533110851)
        ;




            var circle_marker_bbee130e27871220c92cd732fc1da62a = L.circleMarker(
                [37.791642982384, -122.40090869889],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_d2a0d8a9b246740d7a1b5fb611953eab = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_16afc6bdfdf3355a622c61ce78337cd7 = $(`&lt;div id=&quot;html_16afc6bdfdf3355a622c61ce78337cd7&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;BURGLARY&lt;/div&gt;`)[0];
                popup_d2a0d8a9b246740d7a1b5fb611953eab.setContent(html_16afc6bdfdf3355a622c61ce78337cd7);



        circle_marker_bbee130e27871220c92cd732fc1da62a.bindPopup(popup_d2a0d8a9b246740d7a1b5fb611953eab)
        ;




            var circle_marker_51487fbad8503cb0948a6016ddadf1ad = L.circleMarker(
                [37.7837069301545, -122.408595110869],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_c0759bdbc99fd42129305d29b1466363 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_0e587c98e4ffbe919bb062fbbaec01c2 = $(`&lt;div id=&quot;html_0e587c98e4ffbe919bb062fbbaec01c2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;STOLEN PROPERTY&lt;/div&gt;`)[0];
                popup_c0759bdbc99fd42129305d29b1466363.setContent(html_0e587c98e4ffbe919bb062fbbaec01c2);



        circle_marker_51487fbad8503cb0948a6016ddadf1ad.bindPopup(popup_c0759bdbc99fd42129305d29b1466363)
        ;




            var circle_marker_369183ac94de38fa50c4737c762dd480 = L.circleMarker(
                [37.7572895904578, -122.406870402082],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_f6d663f5665e5ef85f8e888cc85310ed = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_b5ad2c855822fe42790e001c378341c8 = $(`&lt;div id=&quot;html_b5ad2c855822fe42790e001c378341c8&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ROBBERY&lt;/div&gt;`)[0];
                popup_f6d663f5665e5ef85f8e888cc85310ed.setContent(html_b5ad2c855822fe42790e001c378341c8);



        circle_marker_369183ac94de38fa50c4737c762dd480.bindPopup(popup_f6d663f5665e5ef85f8e888cc85310ed)
        ;




            var circle_marker_fa3095780abd1b944bbe6219d600b0d1 = L.circleMarker(
                [37.7489063051829, -122.420354780861],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_3ad9eb4889c228aaab5bfcfe79db2b56 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_2dd414ee50b7460b45b890beecc39211 = $(`&lt;div id=&quot;html_2dd414ee50b7460b45b890beecc39211&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_3ad9eb4889c228aaab5bfcfe79db2b56.setContent(html_2dd414ee50b7460b45b890beecc39211);



        circle_marker_fa3095780abd1b944bbe6219d600b0d1.bindPopup(popup_3ad9eb4889c228aaab5bfcfe79db2b56)
        ;




            var circle_marker_65d620de8f7715e6ceabef8b3ffdfd02 = L.circleMarker(
                [37.715765426995, -122.439909766772],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_8fa4c48de6453b98701c048224f0655f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_176b49e13a3939e036193f06746609d7 = $(`&lt;div id=&quot;html_176b49e13a3939e036193f06746609d7&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_8fa4c48de6453b98701c048224f0655f.setContent(html_176b49e13a3939e036193f06746609d7);



        circle_marker_65d620de8f7715e6ceabef8b3ffdfd02.bindPopup(popup_8fa4c48de6453b98701c048224f0655f)
        ;




            var circle_marker_f422ae96dd86f8e6f1c096d170676106 = L.circleMarker(
                [37.7835699386918, -122.408421116922],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_4f6c3516e781837174f253ff1bc5735a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_4eb4bb02134ba2bcf5df8b12c1646eb1 = $(`&lt;div id=&quot;html_4eb4bb02134ba2bcf5df8b12c1646eb1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_4f6c3516e781837174f253ff1bc5735a.setContent(html_4eb4bb02134ba2bcf5df8b12c1646eb1);



        circle_marker_f422ae96dd86f8e6f1c096d170676106.bindPopup(popup_4f6c3516e781837174f253ff1bc5735a)
        ;




            var circle_marker_80a08cda773093468ee253bcbcf8ff80 = L.circleMarker(
                [37.7736186276456, -122.422315670749],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_7caa7495561aca351182c2ecba4b73b1 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_479db299f7dbcebf806faa8a5b4e4f74 = $(`&lt;div id=&quot;html_479db299f7dbcebf806faa8a5b4e4f74&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;FRAUD&lt;/div&gt;`)[0];
                popup_7caa7495561aca351182c2ecba4b73b1.setContent(html_479db299f7dbcebf806faa8a5b4e4f74);



        circle_marker_80a08cda773093468ee253bcbcf8ff80.bindPopup(popup_7caa7495561aca351182c2ecba4b73b1)
        ;




            var circle_marker_8652423d1a5036b8e694f21c23bff873 = L.circleMarker(
                [37.7928412840447, -122.424519835009],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_6a639956499ca496f6136335303b1c76 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_172eb5a6fbca13bd3830ec0b6540a0a9 = $(`&lt;div id=&quot;html_172eb5a6fbca13bd3830ec0b6540a0a9&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_6a639956499ca496f6136335303b1c76.setContent(html_172eb5a6fbca13bd3830ec0b6540a0a9);



        circle_marker_8652423d1a5036b8e694f21c23bff873.bindPopup(popup_6a639956499ca496f6136335303b1c76)
        ;




            var circle_marker_2bd35053a9e3393fc973f4941016a549 = L.circleMarker(
                [37.7540986882068, -122.414233849038],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_8ab550f405e66c22fd6ddd63d689955e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_06f046a0e3b8efe7382962bfd96239fc = $(`&lt;div id=&quot;html_06f046a0e3b8efe7382962bfd96239fc&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;DRUG/NARCOTIC&lt;/div&gt;`)[0];
                popup_8ab550f405e66c22fd6ddd63d689955e.setContent(html_06f046a0e3b8efe7382962bfd96239fc);



        circle_marker_2bd35053a9e3393fc973f4941016a549.bindPopup(popup_8ab550f405e66c22fd6ddd63d689955e)
        ;




            var circle_marker_d8c0d038f2fb58b00ba0584aafe6247f = L.circleMarker(
                [37.7540986882068, -122.414233849038],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_0b970782c98b29007437062466ab0a61 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_710badc086a8792b41ab3e06ef6986a2 = $(`&lt;div id=&quot;html_710badc086a8792b41ab3e06ef6986a2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_0b970782c98b29007437062466ab0a61.setContent(html_710badc086a8792b41ab3e06ef6986a2);



        circle_marker_d8c0d038f2fb58b00ba0584aafe6247f.bindPopup(popup_0b970782c98b29007437062466ab0a61)
        ;




            var circle_marker_739f7217e75f7cf2ed8f9e112e72fb2b = L.circleMarker(
                [37.7714939969416, -122.507750131004],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_5aaf73ae870220fd093f05ab011e029d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_039924d689fb4865964d6a16205451ce = $(`&lt;div id=&quot;html_039924d689fb4865964d6a16205451ce&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_5aaf73ae870220fd093f05ab011e029d.setContent(html_039924d689fb4865964d6a16205451ce);



        circle_marker_739f7217e75f7cf2ed8f9e112e72fb2b.bindPopup(popup_5aaf73ae870220fd093f05ab011e029d)
        ;




            var circle_marker_c59ea3ab9d5d30b6ea185563a54c3e85 = L.circleMarker(
                [37.718302204766, -122.474444639595],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_6655e0f4c2388bdda3399e6c07d9a9a2 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_f5ffbddf8da60343cc522c7eb9949315 = $(`&lt;div id=&quot;html_f5ffbddf8da60343cc522c7eb9949315&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_6655e0f4c2388bdda3399e6c07d9a9a2.setContent(html_f5ffbddf8da60343cc522c7eb9949315);



        circle_marker_c59ea3ab9d5d30b6ea185563a54c3e85.bindPopup(popup_6655e0f4c2388bdda3399e6c07d9a9a2)
        ;




            var circle_marker_f5fa73c9efa7fc587b6bae48b284d1c4 = L.circleMarker(
                [37.7645752317615, -122.427562596985],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_bc519f5e6bd3706577dc0e54d5617932 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_a4727581bd371508c5587091d1b46ddd = $(`&lt;div id=&quot;html_a4727581bd371508c5587091d1b46ddd&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_bc519f5e6bd3706577dc0e54d5617932.setContent(html_a4727581bd371508c5587091d1b46ddd);



        circle_marker_f5fa73c9efa7fc587b6bae48b284d1c4.bindPopup(popup_bc519f5e6bd3706577dc0e54d5617932)
        ;




            var circle_marker_be5109c85569e85d8b1e655f939fb377 = L.circleMarker(
                [37.7874378309112, -122.419203004268],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_34968e89059df8d8f027eb9ccdd6a582 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_ace44f4566794bbe479d303823eb1287 = $(`&lt;div id=&quot;html_ace44f4566794bbe479d303823eb1287&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;BURGLARY&lt;/div&gt;`)[0];
                popup_34968e89059df8d8f027eb9ccdd6a582.setContent(html_ace44f4566794bbe479d303823eb1287);



        circle_marker_be5109c85569e85d8b1e655f939fb377.bindPopup(popup_34968e89059df8d8f027eb9ccdd6a582)
        ;




            var circle_marker_c52f845b785cd592fe8408251fd242bc = L.circleMarker(
                [37.7493688284532, -122.412690142308],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_7f28b9feab8759c5a250d03babe07968 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_cb41f5078a82a47db46660acbd46f3bf = $(`&lt;div id=&quot;html_cb41f5078a82a47db46660acbd46f3bf&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_7f28b9feab8759c5a250d03babe07968.setContent(html_cb41f5078a82a47db46660acbd46f3bf);



        circle_marker_c52f845b785cd592fe8408251fd242bc.bindPopup(popup_7f28b9feab8759c5a250d03babe07968)
        ;




            var circle_marker_3ce7de5375522dd2f592ebdb56b5890f = L.circleMarker(
                [37.7092010462379, -122.434609280352],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_5b4e1d934e3c9bf6701295874c82f041 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_336be340903234ae1d27069a78f8a6bf = $(`&lt;div id=&quot;html_336be340903234ae1d27069a78f8a6bf&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_5b4e1d934e3c9bf6701295874c82f041.setContent(html_336be340903234ae1d27069a78f8a6bf);



        circle_marker_3ce7de5375522dd2f592ebdb56b5890f.bindPopup(popup_5b4e1d934e3c9bf6701295874c82f041)
        ;




            var circle_marker_93e46335c9d92ebcd1fd6ba661544f66 = L.circleMarker(
                [37.7879209375533, -122.410882825551],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_48c59615beb7b3408547ab0f22c45d0b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_958c9389134743d2055c48543feeb4d4 = $(`&lt;div id=&quot;html_958c9389134743d2055c48543feeb4d4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VEHICLE THEFT&lt;/div&gt;`)[0];
                popup_48c59615beb7b3408547ab0f22c45d0b.setContent(html_958c9389134743d2055c48543feeb4d4);



        circle_marker_93e46335c9d92ebcd1fd6ba661544f66.bindPopup(popup_48c59615beb7b3408547ab0f22c45d0b)
        ;




            var circle_marker_ebeee65739f90a9d358ec2ff4931ed47 = L.circleMarker(
                [37.8004566471039, -122.401432754722],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_22f9debacb32151a68d7d68bd2692ce4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_7a352455072e234ad3523986af094364 = $(`&lt;div id=&quot;html_7a352455072e234ad3523986af094364&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VEHICLE THEFT&lt;/div&gt;`)[0];
                popup_22f9debacb32151a68d7d68bd2692ce4.setContent(html_7a352455072e234ad3523986af094364);



        circle_marker_ebeee65739f90a9d358ec2ff4931ed47.bindPopup(popup_22f9debacb32151a68d7d68bd2692ce4)
        ;




            var circle_marker_98b5958918271534d5bce4cb4d1e7edd = L.circleMarker(
                [37.7435550542265, -122.421128029505],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_7515fa0a00bcbffecd6997f15ea92f81 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_8864fb90b9353d1da138d32c20c7ba64 = $(`&lt;div id=&quot;html_8864fb90b9353d1da138d32c20c7ba64&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_7515fa0a00bcbffecd6997f15ea92f81.setContent(html_8864fb90b9353d1da138d32c20c7ba64);



        circle_marker_98b5958918271534d5bce4cb4d1e7edd.bindPopup(popup_7515fa0a00bcbffecd6997f15ea92f81)
        ;




            var circle_marker_a33b71f2b8e9f03cd524c1444b9a04a5 = L.circleMarker(
                [37.7865647607685, -122.407244087032],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_04c71fbd28727b2ffe6b3226743eb39f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_7176ee06d43316bf267d4673bb4c728d = $(`&lt;div id=&quot;html_7176ee06d43316bf267d4673bb4c728d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_04c71fbd28727b2ffe6b3226743eb39f.setContent(html_7176ee06d43316bf267d4673bb4c728d);



        circle_marker_a33b71f2b8e9f03cd524c1444b9a04a5.bindPopup(popup_04c71fbd28727b2ffe6b3226743eb39f)
        ;




            var circle_marker_5e2197c26fd9dbf79370ace7f1ee5786 = L.circleMarker(
                [37.7615655928045, -122.423803001901],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_5b81c1528578800d414088581a70346a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_c1853f2660fd5a53ff65f0c0fe0aba81 = $(`&lt;div id=&quot;html_c1853f2660fd5a53ff65f0c0fe0aba81&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;RECOVERED VEHICLE&lt;/div&gt;`)[0];
                popup_5b81c1528578800d414088581a70346a.setContent(html_c1853f2660fd5a53ff65f0c0fe0aba81);



        circle_marker_5e2197c26fd9dbf79370ace7f1ee5786.bindPopup(popup_5b81c1528578800d414088581a70346a)
        ;




            var circle_marker_31d0d8cf822bdfcc3896bb5f563d5656 = L.circleMarker(
                [37.7615655928045, -122.423803001901],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_9e77563f21305f1a108929837ab9965b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_80df978efaabe0de6303a34365a15a74 = $(`&lt;div id=&quot;html_80df978efaabe0de6303a34365a15a74&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_9e77563f21305f1a108929837ab9965b.setContent(html_80df978efaabe0de6303a34365a15a74);



        circle_marker_31d0d8cf822bdfcc3896bb5f563d5656.bindPopup(popup_9e77563f21305f1a108929837ab9965b)
        ;




            var circle_marker_0b7c65d4e619e8bddf8c8b51daf77af1 = L.circleMarker(
                [37.7441927508932, -122.444685482273],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_75f0e3e569a585913ce353d8e50be6c1 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_e7162170f49f5aa764f538aba2077e9b = $(`&lt;div id=&quot;html_e7162170f49f5aa764f538aba2077e9b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_75f0e3e569a585913ce353d8e50be6c1.setContent(html_e7162170f49f5aa764f538aba2077e9b);



        circle_marker_0b7c65d4e619e8bddf8c8b51daf77af1.bindPopup(popup_75f0e3e569a585913ce353d8e50be6c1)
        ;




            var circle_marker_b72432dcd01e8c5fccf8a2cfd2598ce0 = L.circleMarker(
                [37.7754692820041, -122.415757039196],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_c8ca8f8204060b4126f6109bb6ff59c3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_d5436be9b36043389bfdc4078080c099 = $(`&lt;div id=&quot;html_d5436be9b36043389bfdc4078080c099&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_c8ca8f8204060b4126f6109bb6ff59c3.setContent(html_d5436be9b36043389bfdc4078080c099);



        circle_marker_b72432dcd01e8c5fccf8a2cfd2598ce0.bindPopup(popup_c8ca8f8204060b4126f6109bb6ff59c3)
        ;




            var circle_marker_1a5032fc58259f8c2d76e72e695933fe = L.circleMarker(
                [37.7285280627465, -122.475647460786],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_129854af5d683c8c56440a1891c95216 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_7df9268cc9b03b3d67285193cbc75cf4 = $(`&lt;div id=&quot;html_7df9268cc9b03b3d67285193cbc75cf4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ROBBERY&lt;/div&gt;`)[0];
                popup_129854af5d683c8c56440a1891c95216.setContent(html_7df9268cc9b03b3d67285193cbc75cf4);



        circle_marker_1a5032fc58259f8c2d76e72e695933fe.bindPopup(popup_129854af5d683c8c56440a1891c95216)
        ;




            var circle_marker_b3a3a1d0102752ca49e725a1d59cc655 = L.circleMarker(
                [37.7428517374449, -122.420967440564],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_5ff50d0fcc15a1dd016557f0b5c6c56c = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_829e41dbaeb2ab65ed161c6c71fd92e3 = $(`&lt;div id=&quot;html_829e41dbaeb2ab65ed161c6c71fd92e3&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_5ff50d0fcc15a1dd016557f0b5c6c56c.setContent(html_829e41dbaeb2ab65ed161c6c71fd92e3);



        circle_marker_b3a3a1d0102752ca49e725a1d59cc655.bindPopup(popup_5ff50d0fcc15a1dd016557f0b5c6c56c)
        ;




            var circle_marker_13470681ae7ad502d8f9197b35a589e1 = L.circleMarker(
                [37.7821198488931, -122.415669661443],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_52564588fc1f58d947d700212152f970 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_9b1a6f7bc52bdc21ab03359873a826a2 = $(`&lt;div id=&quot;html_9b1a6f7bc52bdc21ab03359873a826a2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VANDALISM&lt;/div&gt;`)[0];
                popup_52564588fc1f58d947d700212152f970.setContent(html_9b1a6f7bc52bdc21ab03359873a826a2);



        circle_marker_13470681ae7ad502d8f9197b35a589e1.bindPopup(popup_52564588fc1f58d947d700212152f970)
        ;




            var circle_marker_8d635d457e2f39e551b674328603dac8 = L.circleMarker(
                [37.7791674218963, -122.406346425632],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_285ca200222c7680347fd1408ab334f0 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_4e7a032613b547bb7ba20a545c2aca98 = $(`&lt;div id=&quot;html_4e7a032613b547bb7ba20a545c2aca98&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_285ca200222c7680347fd1408ab334f0.setContent(html_4e7a032613b547bb7ba20a545c2aca98);



        circle_marker_8d635d457e2f39e551b674328603dac8.bindPopup(popup_285ca200222c7680347fd1408ab334f0)
        ;




            var circle_marker_ce98e113d62ed42ba33a2b8b9712a9c4 = L.circleMarker(
                [37.7657184395282, -122.409529913278],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_618000f71dffe3b523981ed7d8147ec2 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_10ee6ceebcdafd1ae04d04a614c9e364 = $(`&lt;div id=&quot;html_10ee6ceebcdafd1ae04d04a614c9e364&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_618000f71dffe3b523981ed7d8147ec2.setContent(html_10ee6ceebcdafd1ae04d04a614c9e364);



        circle_marker_ce98e113d62ed42ba33a2b8b9712a9c4.bindPopup(popup_618000f71dffe3b523981ed7d8147ec2)
        ;




            var circle_marker_0875acd46f669e12c0252a6308f3a296 = L.circleMarker(
                [37.775420706711, -122.403404791479],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_970a1adc845f36b94e89cb8c9c5f1f0a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_8fbf619755927a7937ba7873e4f2978e = $(`&lt;div id=&quot;html_8fbf619755927a7937ba7873e4f2978e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_970a1adc845f36b94e89cb8c9c5f1f0a.setContent(html_8fbf619755927a7937ba7873e4f2978e);



        circle_marker_0875acd46f669e12c0252a6308f3a296.bindPopup(popup_970a1adc845f36b94e89cb8c9c5f1f0a)
        ;




            var circle_marker_4172648cce7c02f6a53e68703233cd7a = L.circleMarker(
                [37.767524308783, -122.410738097315],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_d91f52920e7827a769222b35d3e5565f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_167bfda27f1dc73c370da06bdfdf30b4 = $(`&lt;div id=&quot;html_167bfda27f1dc73c370da06bdfdf30b4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;BURGLARY&lt;/div&gt;`)[0];
                popup_d91f52920e7827a769222b35d3e5565f.setContent(html_167bfda27f1dc73c370da06bdfdf30b4);



        circle_marker_4172648cce7c02f6a53e68703233cd7a.bindPopup(popup_d91f52920e7827a769222b35d3e5565f)
        ;




            var circle_marker_35e935ad5784e2f7f2de3f21f4acc4a3 = L.circleMarker(
                [37.767524308783, -122.410738097315],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_c0815821bf376cb7a08eb761765b9d4c = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_54c2a6bf07a9fd0578178d41bb287b66 = $(`&lt;div id=&quot;html_54c2a6bf07a9fd0578178d41bb287b66&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ARSON&lt;/div&gt;`)[0];
                popup_c0815821bf376cb7a08eb761765b9d4c.setContent(html_54c2a6bf07a9fd0578178d41bb287b66);



        circle_marker_35e935ad5784e2f7f2de3f21f4acc4a3.bindPopup(popup_c0815821bf376cb7a08eb761765b9d4c)
        ;




            var circle_marker_684af104b97fbb377f879dc2e1935d01 = L.circleMarker(
                [37.7131083433264, -122.444314025188],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_42428bf3d48475e0890eb15cc244ca0b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_24efc256451f2deecb5f22ccadd28c48 = $(`&lt;div id=&quot;html_24efc256451f2deecb5f22ccadd28c48&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;BURGLARY&lt;/div&gt;`)[0];
                popup_42428bf3d48475e0890eb15cc244ca0b.setContent(html_24efc256451f2deecb5f22ccadd28c48);



        circle_marker_684af104b97fbb377f879dc2e1935d01.bindPopup(popup_42428bf3d48475e0890eb15cc244ca0b)
        ;




            var circle_marker_66852e98f94dec4f2752d86897b255eb = L.circleMarker(
                [37.7131083433264, -122.444314025188],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_33ce8b27e46a2e3bb435eec8cfe1a3a2 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_89019e9982cb2638a3ebe9b511531ccb = $(`&lt;div id=&quot;html_89019e9982cb2638a3ebe9b511531ccb&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;DRUG/NARCOTIC&lt;/div&gt;`)[0];
                popup_33ce8b27e46a2e3bb435eec8cfe1a3a2.setContent(html_89019e9982cb2638a3ebe9b511531ccb);



        circle_marker_66852e98f94dec4f2752d86897b255eb.bindPopup(popup_33ce8b27e46a2e3bb435eec8cfe1a3a2)
        ;




            var circle_marker_b9e8c865e6dc16a7059d6ef831b7e4c9 = L.circleMarker(
                [37.7660160114103, -122.403644620439],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_9329fdb058faa7f8287919ad24fe8862 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_c039adf1e1adbae4a6e2d4094434b8f7 = $(`&lt;div id=&quot;html_c039adf1e1adbae4a6e2d4094434b8f7&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;MISSING PERSON&lt;/div&gt;`)[0];
                popup_9329fdb058faa7f8287919ad24fe8862.setContent(html_c039adf1e1adbae4a6e2d4094434b8f7);



        circle_marker_b9e8c865e6dc16a7059d6ef831b7e4c9.bindPopup(popup_9329fdb058faa7f8287919ad24fe8862)
        ;




            var circle_marker_293b0f4e4b53b1dab3b9a651ed933869 = L.circleMarker(
                [37.7660160114103, -122.403644620439],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_3036c2652c499e216f1cf36170c4e75d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_e03387bc0a21c23cd45fb752463aa07a = $(`&lt;div id=&quot;html_e03387bc0a21c23cd45fb752463aa07a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;MISSING PERSON&lt;/div&gt;`)[0];
                popup_3036c2652c499e216f1cf36170c4e75d.setContent(html_e03387bc0a21c23cd45fb752463aa07a);



        circle_marker_293b0f4e4b53b1dab3b9a651ed933869.bindPopup(popup_3036c2652c499e216f1cf36170c4e75d)
        ;




            var circle_marker_1d37c071863fc7ac3beae86a2a5a0280 = L.circleMarker(
                [37.7762310404758, -122.414714295579],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_31d26a1b10e4c2c4fed12b5aadd8cfd7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_ac2d1837620b3b4e05986c0946568e24 = $(`&lt;div id=&quot;html_ac2d1837620b3b4e05986c0946568e24&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_31d26a1b10e4c2c4fed12b5aadd8cfd7.setContent(html_ac2d1837620b3b4e05986c0946568e24);



        circle_marker_1d37c071863fc7ac3beae86a2a5a0280.bindPopup(popup_31d26a1b10e4c2c4fed12b5aadd8cfd7)
        ;




            var circle_marker_460112161615c842e88a7bc0d267827b = L.circleMarker(
                [37.7762310404758, -122.414714295579],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_233e8e4e9defb190e07305a3984ac85d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_0d6f2df00054023c1b078e24ce281f55 = $(`&lt;div id=&quot;html_0d6f2df00054023c1b078e24ce281f55&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;MISSING PERSON&lt;/div&gt;`)[0];
                popup_233e8e4e9defb190e07305a3984ac85d.setContent(html_0d6f2df00054023c1b078e24ce281f55);



        circle_marker_460112161615c842e88a7bc0d267827b.bindPopup(popup_233e8e4e9defb190e07305a3984ac85d)
        ;




            var circle_marker_e1599f9d65b79a897c64507ab856ae69 = L.circleMarker(
                [37.7775118895695, -122.418045452768],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_9025ec098317f3567cbb0346399f3cdb = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_76677dab78d16b18d406fb7f8b56e4be = $(`&lt;div id=&quot;html_76677dab78d16b18d406fb7f8b56e4be&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VEHICLE THEFT&lt;/div&gt;`)[0];
                popup_9025ec098317f3567cbb0346399f3cdb.setContent(html_76677dab78d16b18d406fb7f8b56e4be);



        circle_marker_e1599f9d65b79a897c64507ab856ae69.bindPopup(popup_9025ec098317f3567cbb0346399f3cdb)
        ;




            var circle_marker_5beb9c7a4835afcfc370435fea595407 = L.circleMarker(
                [37.7820238478975, -122.401161555602],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_145484ae3296973a25f090dfee8f3f2d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_62a9f8ab7b442f69063bd446110d7737 = $(`&lt;div id=&quot;html_62a9f8ab7b442f69063bd446110d7737&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_145484ae3296973a25f090dfee8f3f2d.setContent(html_62a9f8ab7b442f69063bd446110d7737);



        circle_marker_5beb9c7a4835afcfc370435fea595407.bindPopup(popup_145484ae3296973a25f090dfee8f3f2d)
        ;




            var circle_marker_88f80e3a18cfe0985b4c1f1da2cdf8ec = L.circleMarker(
                [37.72700531963, -122.403408669191],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_879f58057451200a9033325bb5575f21 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_ef994eb37c355573d46cfa4af25ed7bb = $(`&lt;div id=&quot;html_ef994eb37c355573d46cfa4af25ed7bb&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_879f58057451200a9033325bb5575f21.setContent(html_ef994eb37c355573d46cfa4af25ed7bb);



        circle_marker_88f80e3a18cfe0985b4c1f1da2cdf8ec.bindPopup(popup_879f58057451200a9033325bb5575f21)
        ;




            var circle_marker_65ae4222dd957d010e06456516387b88 = L.circleMarker(
                [37.7838344374141, -122.412930522059],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_b9058488a7d0b071c97bf896a9e3e6fd = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_62238e2acdd1af1a9ea938d8286ffed8 = $(`&lt;div id=&quot;html_62238e2acdd1af1a9ea938d8286ffed8&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VANDALISM&lt;/div&gt;`)[0];
                popup_b9058488a7d0b071c97bf896a9e3e6fd.setContent(html_62238e2acdd1af1a9ea938d8286ffed8);



        circle_marker_65ae4222dd957d010e06456516387b88.bindPopup(popup_b9058488a7d0b071c97bf896a9e3e6fd)
        ;




            var circle_marker_377d8f5c046b5fe203b1626723375c61 = L.circleMarker(
                [37.7530186537446, -122.418587172219],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_aa41a657e35558545905aa48f35bec5e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_3833797b91164cd07c742aedbea5b5fe = $(`&lt;div id=&quot;html_3833797b91164cd07c742aedbea5b5fe&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_aa41a657e35558545905aa48f35bec5e.setContent(html_3833797b91164cd07c742aedbea5b5fe);



        circle_marker_377d8f5c046b5fe203b1626723375c61.bindPopup(popup_aa41a657e35558545905aa48f35bec5e)
        ;




            var circle_marker_e9032fcaae8a399684a4c72060fb17dc = L.circleMarker(
                [37.7740418385041, -122.414370627495],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_03a3de83a04a105727bed1421b0d2717 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_0514d23e3abc35461f2b31a6df1af520 = $(`&lt;div id=&quot;html_0514d23e3abc35461f2b31a6df1af520&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;FRAUD&lt;/div&gt;`)[0];
                popup_03a3de83a04a105727bed1421b0d2717.setContent(html_0514d23e3abc35461f2b31a6df1af520);



        circle_marker_e9032fcaae8a399684a4c72060fb17dc.bindPopup(popup_03a3de83a04a105727bed1421b0d2717)
        ;




            var circle_marker_4896ab28f39fe5bb8421c9c88496db75 = L.circleMarker(
                [37.790538993725, -122.403915681571],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_01c430fc262585c68177ef75dd04eb99 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_ed6d0d919f2d9be0632f102128259e49 = $(`&lt;div id=&quot;html_ed6d0d919f2d9be0632f102128259e49&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_01c430fc262585c68177ef75dd04eb99.setContent(html_ed6d0d919f2d9be0632f102128259e49);



        circle_marker_4896ab28f39fe5bb8421c9c88496db75.bindPopup(popup_01c430fc262585c68177ef75dd04eb99)
        ;




            var circle_marker_c4b1a64fa1e0dc2312f98b6fc64fd58c = L.circleMarker(
                [37.7830998244592, -122.419183096362],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_f0c5017e3960a46cbb8bb86e3da074d8 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_9faef51a4d23620416f0e741abad91b7 = $(`&lt;div id=&quot;html_9faef51a4d23620416f0e741abad91b7&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_f0c5017e3960a46cbb8bb86e3da074d8.setContent(html_9faef51a4d23620416f0e741abad91b7);



        circle_marker_c4b1a64fa1e0dc2312f98b6fc64fd58c.bindPopup(popup_f0c5017e3960a46cbb8bb86e3da074d8)
        ;




            var circle_marker_7fdfb6838f2d854a784cf189a6640066 = L.circleMarker(
                [37.7407360548358, -122.388753046997],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_590fd14dc7a97d3f5aaf31e5bb5e4d23 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_f50374038f3223f8e279adc58497b76e = $(`&lt;div id=&quot;html_f50374038f3223f8e279adc58497b76e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_590fd14dc7a97d3f5aaf31e5bb5e4d23.setContent(html_f50374038f3223f8e279adc58497b76e);



        circle_marker_7fdfb6838f2d854a784cf189a6640066.bindPopup(popup_590fd14dc7a97d3f5aaf31e5bb5e4d23)
        ;




            var circle_marker_296e91f66f9b444dc73e7d13d02ef1c8 = L.circleMarker(
                [37.7749912944366, -122.437799703468],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_41cd33aa1fe4e8586d9ac31e28d45cb7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_947ecc49a3a850d7cd1ff68419e5ed7f = $(`&lt;div id=&quot;html_947ecc49a3a850d7cd1ff68419e5ed7f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_41cd33aa1fe4e8586d9ac31e28d45cb7.setContent(html_947ecc49a3a850d7cd1ff68419e5ed7f);



        circle_marker_296e91f66f9b444dc73e7d13d02ef1c8.bindPopup(popup_41cd33aa1fe4e8586d9ac31e28d45cb7)
        ;




            var circle_marker_1781a95db1b841feb56f23d986b1ad38 = L.circleMarker(
                [37.7770902743669, -122.421332684633],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_cb5c00f166d1e1bf368111d425155db3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_925fb8f75f11387775cc7a3097fb9bfe = $(`&lt;div id=&quot;html_925fb8f75f11387775cc7a3097fb9bfe&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;MISSING PERSON&lt;/div&gt;`)[0];
                popup_cb5c00f166d1e1bf368111d425155db3.setContent(html_925fb8f75f11387775cc7a3097fb9bfe);



        circle_marker_1781a95db1b841feb56f23d986b1ad38.bindPopup(popup_cb5c00f166d1e1bf368111d425155db3)
        ;




            var circle_marker_1090760752beb09e33942d52b11e73f4 = L.circleMarker(
                [37.7770902743669, -122.421332684633],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_4befbb193b556771f2a313c8d51b48be = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_a17ebaebc8433572f3e8ec8746be5545 = $(`&lt;div id=&quot;html_a17ebaebc8433572f3e8ec8746be5545&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;MISSING PERSON&lt;/div&gt;`)[0];
                popup_4befbb193b556771f2a313c8d51b48be.setContent(html_a17ebaebc8433572f3e8ec8746be5545);



        circle_marker_1090760752beb09e33942d52b11e73f4.bindPopup(popup_4befbb193b556771f2a313c8d51b48be)
        ;




            var circle_marker_130559b09ea2e5430e1599ffae5bfd8a = L.circleMarker(
                [37.7822458223917, -122.446612978839],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_bf7091dbca4be240ebedd8739cacba62 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_4c1a56456e518567df312a2d10c0a894 = $(`&lt;div id=&quot;html_4c1a56456e518567df312a2d10c0a894&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_bf7091dbca4be240ebedd8739cacba62.setContent(html_4c1a56456e518567df312a2d10c0a894);



        circle_marker_130559b09ea2e5430e1599ffae5bfd8a.bindPopup(popup_bf7091dbca4be240ebedd8739cacba62)
        ;




            var circle_marker_8490d55776d64656f25c79f0962f1014 = L.circleMarker(
                [37.7300379995128, -122.404594140634],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_13b5152f9f264791529a0f56a84453ea = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_c59e6833e6918b8d6c80f8c5be1c9e45 = $(`&lt;div id=&quot;html_c59e6833e6918b8d6c80f8c5be1c9e45&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_13b5152f9f264791529a0f56a84453ea.setContent(html_c59e6833e6918b8d6c80f8c5be1c9e45);



        circle_marker_8490d55776d64656f25c79f0962f1014.bindPopup(popup_13b5152f9f264791529a0f56a84453ea)
        ;




            var circle_marker_21f1e60b30e56d1889718f32b4f7f629 = L.circleMarker(
                [37.7953338267436, -122.397373740066],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_0e035f446d04e73f55e9b8dd6c2852bf = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_035efa9dff57d6f4509c5c81763df9a8 = $(`&lt;div id=&quot;html_035efa9dff57d6f4509c5c81763df9a8&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_0e035f446d04e73f55e9b8dd6c2852bf.setContent(html_035efa9dff57d6f4509c5c81763df9a8);



        circle_marker_21f1e60b30e56d1889718f32b4f7f629.bindPopup(popup_0e035f446d04e73f55e9b8dd6c2852bf)
        ;




            var circle_marker_04e9eebe91deda7d3c4a59a3f34a9e91 = L.circleMarker(
                [37.7875158741623, -122.407434989523],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_71db1c75bce24f8a9652c98cc6a94a33 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_221d3d38c553dbc90f29345d46b740a7 = $(`&lt;div id=&quot;html_221d3d38c553dbc90f29345d46b740a7&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_71db1c75bce24f8a9652c98cc6a94a33.setContent(html_221d3d38c553dbc90f29345d46b740a7);



        circle_marker_04e9eebe91deda7d3c4a59a3f34a9e91.bindPopup(popup_71db1c75bce24f8a9652c98cc6a94a33)
        ;




            var circle_marker_10daf8b8235c7d48f81efc848fc91af6 = L.circleMarker(
                [37.7785233776032, -122.403464080033],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_077c6e6027748e849a07e5540ec3dbbf = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_dd9f5104eaaae939441425589bb5137e = $(`&lt;div id=&quot;html_dd9f5104eaaae939441425589bb5137e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;PROSTITUTION&lt;/div&gt;`)[0];
                popup_077c6e6027748e849a07e5540ec3dbbf.setContent(html_dd9f5104eaaae939441425589bb5137e);



        circle_marker_10daf8b8235c7d48f81efc848fc91af6.bindPopup(popup_077c6e6027748e849a07e5540ec3dbbf)
        ;




            var circle_marker_40245b23dbdde0d448c9a9d99e43f1e0 = L.circleMarker(
                [37.7785233776032, -122.403464080033],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_172a9b8b711846fab9914245481c4835 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_16d00a4121196ee9884e25f10f6ad7eb = $(`&lt;div id=&quot;html_16d00a4121196ee9884e25f10f6ad7eb&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_172a9b8b711846fab9914245481c4835.setContent(html_16d00a4121196ee9884e25f10f6ad7eb);



        circle_marker_40245b23dbdde0d448c9a9d99e43f1e0.bindPopup(popup_172a9b8b711846fab9914245481c4835)
        ;




            var circle_marker_217660036e29fa8e4e8bb760996b8901 = L.circleMarker(
                [37.773291806903, -122.436614181331],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_1053471089d94148b76d00b09dd187ec = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_3b1edfd45f1a647b5d50a54561b73505 = $(`&lt;div id=&quot;html_3b1edfd45f1a647b5d50a54561b73505&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_1053471089d94148b76d00b09dd187ec.setContent(html_3b1edfd45f1a647b5d50a54561b73505);



        circle_marker_217660036e29fa8e4e8bb760996b8901.bindPopup(popup_1053471089d94148b76d00b09dd187ec)
        ;




            var circle_marker_50a65cc71c06f821b3c318374d1fb8cd = L.circleMarker(
                [37.780527578509, -122.396849015172],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_1494d37be707a51c0f0d1a2b2a6b42b0 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_544029f5bf9bcd008c4a65f49226273c = $(`&lt;div id=&quot;html_544029f5bf9bcd008c4a65f49226273c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;DRUG/NARCOTIC&lt;/div&gt;`)[0];
                popup_1494d37be707a51c0f0d1a2b2a6b42b0.setContent(html_544029f5bf9bcd008c4a65f49226273c);



        circle_marker_50a65cc71c06f821b3c318374d1fb8cd.bindPopup(popup_1494d37be707a51c0f0d1a2b2a6b42b0)
        ;




            var circle_marker_7c43b0bd7ab3d56c04fe2002f8c309a1 = L.circleMarker(
                [37.780527578509, -122.396849015172],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_95abd47511fd27a6120b939cdad2f8a8 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_e0ceaef6063631d99e09c278d7654253 = $(`&lt;div id=&quot;html_e0ceaef6063631d99e09c278d7654253&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_95abd47511fd27a6120b939cdad2f8a8.setContent(html_e0ceaef6063631d99e09c278d7654253);



        circle_marker_7c43b0bd7ab3d56c04fe2002f8c309a1.bindPopup(popup_95abd47511fd27a6120b939cdad2f8a8)
        ;




            var circle_marker_d63a814768c3eb0def85ce242a6d3afa = L.circleMarker(
                [37.7284180706602, -122.450000790445],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_a001f2b40c7c27850c6ed058daba1278 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_f277cd714a28ab1900c899c477e7ce73 = $(`&lt;div id=&quot;html_f277cd714a28ab1900c899c477e7ce73&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_a001f2b40c7c27850c6ed058daba1278.setContent(html_f277cd714a28ab1900c899c477e7ce73);



        circle_marker_d63a814768c3eb0def85ce242a6d3afa.bindPopup(popup_a001f2b40c7c27850c6ed058daba1278)
        ;




            var circle_marker_b523a86726e81a497779a12a7ad9b3f5 = L.circleMarker(
                [37.7292114647359, -122.400834283031],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_dda231b786820c60be69dfd5defd46c0 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_734361782c350c0595b6fb47e75b53fb = $(`&lt;div id=&quot;html_734361782c350c0595b6fb47e75b53fb&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_dda231b786820c60be69dfd5defd46c0.setContent(html_734361782c350c0595b6fb47e75b53fb);



        circle_marker_b523a86726e81a497779a12a7ad9b3f5.bindPopup(popup_dda231b786820c60be69dfd5defd46c0)
        ;




            var circle_marker_518042c22add98c62988ff550bc71c80 = L.circleMarker(
                [37.7880065324392, -122.399802145799],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_f70470bcd54f8ba66b7332b12f79ab82 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_74384e2d2ecc92c2a7ddf7175bd10227 = $(`&lt;div id=&quot;html_74384e2d2ecc92c2a7ddf7175bd10227&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_f70470bcd54f8ba66b7332b12f79ab82.setContent(html_74384e2d2ecc92c2a7ddf7175bd10227);



        circle_marker_518042c22add98c62988ff550bc71c80.bindPopup(popup_f70470bcd54f8ba66b7332b12f79ab82)
        ;




            var circle_marker_b2a764773dc85f05f069ef69f7c5e87d = L.circleMarker(
                [37.7239748241609, -122.3949284758],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_d491f7f46d6afc0eed7ec008924e439e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_006723cd5dc418e5af45cce2d402586a = $(`&lt;div id=&quot;html_006723cd5dc418e5af45cce2d402586a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;SECONDARY CODES&lt;/div&gt;`)[0];
                popup_d491f7f46d6afc0eed7ec008924e439e.setContent(html_006723cd5dc418e5af45cce2d402586a);



        circle_marker_b2a764773dc85f05f069ef69f7c5e87d.bindPopup(popup_d491f7f46d6afc0eed7ec008924e439e)
        ;




            var circle_marker_8b55c2428bbd48da2bd9d3e2268d8858 = L.circleMarker(
                [37.7239748241609, -122.3949284758],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_c8cc987a0a7ce3fdd966b85a671ec85f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_0d0ccb7f460d92f20bfb1df1cb27c47b = $(`&lt;div id=&quot;html_0d0ccb7f460d92f20bfb1df1cb27c47b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;SUSPICIOUS OCC&lt;/div&gt;`)[0];
                popup_c8cc987a0a7ce3fdd966b85a671ec85f.setContent(html_0d0ccb7f460d92f20bfb1df1cb27c47b);



        circle_marker_8b55c2428bbd48da2bd9d3e2268d8858.bindPopup(popup_c8cc987a0a7ce3fdd966b85a671ec85f)
        ;




            var circle_marker_a59724c77dd98e074d3ff82eb82c4697 = L.circleMarker(
                [37.7239748241609, -122.3949284758],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_d3774ba7593498cdf7dfdcb66b0374da = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_a8ca15b2b138841cb36c2b3e6fe3f017 = $(`&lt;div id=&quot;html_a8ca15b2b138841cb36c2b3e6fe3f017&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_d3774ba7593498cdf7dfdcb66b0374da.setContent(html_a8ca15b2b138841cb36c2b3e6fe3f017);



        circle_marker_a59724c77dd98e074d3ff82eb82c4697.bindPopup(popup_d3774ba7593498cdf7dfdcb66b0374da)
        ;




            var circle_marker_ca11b2a8089c1a3e7607429ded2cfc06 = L.circleMarker(
                [37.7883235449904, -122.41185703254],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_873d03e9fd55b9535aeb21e7028a72c9 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_b01ede53df90faa6140530ac9041758e = $(`&lt;div id=&quot;html_b01ede53df90faa6140530ac9041758e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_873d03e9fd55b9535aeb21e7028a72c9.setContent(html_b01ede53df90faa6140530ac9041758e);



        circle_marker_ca11b2a8089c1a3e7607429ded2cfc06.bindPopup(popup_873d03e9fd55b9535aeb21e7028a72c9)
        ;




            var circle_marker_13bae99d1640ad63fa7b6e513bd8188a = L.circleMarker(
                [37.7559977339856, -122.409435617106],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_75d89a35d5a48235d7b39a0a002a1031 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_7046ef17989e96b977566fee8ed8f972 = $(`&lt;div id=&quot;html_7046ef17989e96b977566fee8ed8f972&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_75d89a35d5a48235d7b39a0a002a1031.setContent(html_7046ef17989e96b977566fee8ed8f972);



        circle_marker_13bae99d1640ad63fa7b6e513bd8188a.bindPopup(popup_75d89a35d5a48235d7b39a0a002a1031)
        ;




            var circle_marker_e665eba2364e7b9ac9f7944b46608b7f = L.circleMarker(
                [37.7870798144443, -122.425883358148],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_dc5f48ac2026c94e99076cdff4e370bb = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_5d366a3b496aef33aaaeef603a22dfd1 = $(`&lt;div id=&quot;html_5d366a3b496aef33aaaeef603a22dfd1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_dc5f48ac2026c94e99076cdff4e370bb.setContent(html_5d366a3b496aef33aaaeef603a22dfd1);



        circle_marker_e665eba2364e7b9ac9f7944b46608b7f.bindPopup(popup_dc5f48ac2026c94e99076cdff4e370bb)
        ;




            var circle_marker_42f3154484fb37a27d7997f1bdeefe98 = L.circleMarker(
                [37.7360374466862, -122.415126543001],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_3b5844159aef696ab4133cfb0864e514 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_4ab9a5b1354b5c9fdecdb9e127d94627 = $(`&lt;div id=&quot;html_4ab9a5b1354b5c9fdecdb9e127d94627&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_3b5844159aef696ab4133cfb0864e514.setContent(html_4ab9a5b1354b5c9fdecdb9e127d94627);



        circle_marker_42f3154484fb37a27d7997f1bdeefe98.bindPopup(popup_3b5844159aef696ab4133cfb0864e514)
        ;




            var circle_marker_1fa22adac3f854d3a82dfbad09f7eb52 = L.circleMarker(
                [37.712767884821, -122.431928011089],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_4be5626a58e6f2c9653a1a9ab0d5c6e0 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_1f0459a97feb58794a15c63df524aea7 = $(`&lt;div id=&quot;html_1f0459a97feb58794a15c63df524aea7&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_4be5626a58e6f2c9653a1a9ab0d5c6e0.setContent(html_1f0459a97feb58794a15c63df524aea7);



        circle_marker_1fa22adac3f854d3a82dfbad09f7eb52.bindPopup(popup_4be5626a58e6f2c9653a1a9ab0d5c6e0)
        ;




            var circle_marker_cd32aa531700a4181ddb11feb0c09af0 = L.circleMarker(
                [37.7895710255863, -122.402163713618],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_c45238f0e74b9655d2771066199172f5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_143650e8c19fe9bc8e2a52fc0226fde6 = $(`&lt;div id=&quot;html_143650e8c19fe9bc8e2a52fc0226fde6&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;DRUNKENNESS&lt;/div&gt;`)[0];
                popup_c45238f0e74b9655d2771066199172f5.setContent(html_143650e8c19fe9bc8e2a52fc0226fde6);



        circle_marker_cd32aa531700a4181ddb11feb0c09af0.bindPopup(popup_c45238f0e74b9655d2771066199172f5)
        ;




            var circle_marker_e382d1de8d9963ef0effaa87551f9de0 = L.circleMarker(
                [37.7307429169559, -122.429306728376],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_785f6fed8d401596e5ffd1a324904ebc = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_cabeca7d89864f975b5a8dc8e5e5bdc4 = $(`&lt;div id=&quot;html_cabeca7d89864f975b5a8dc8e5e5bdc4&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_785f6fed8d401596e5ffd1a324904ebc.setContent(html_cabeca7d89864f975b5a8dc8e5e5bdc4);



        circle_marker_e382d1de8d9963ef0effaa87551f9de0.bindPopup(popup_785f6fed8d401596e5ffd1a324904ebc)
        ;




            var circle_marker_b13e24dc822be4df4d402f8fa8a4de01 = L.circleMarker(
                [37.7838365565348, -122.413790972781],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_e02f16fd1f54800be025ff4a9b1c74b0 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_15b5689e65e6856542bc8c51178f81fd = $(`&lt;div id=&quot;html_15b5689e65e6856542bc8c51178f81fd&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VANDALISM&lt;/div&gt;`)[0];
                popup_e02f16fd1f54800be025ff4a9b1c74b0.setContent(html_15b5689e65e6856542bc8c51178f81fd);



        circle_marker_b13e24dc822be4df4d402f8fa8a4de01.bindPopup(popup_e02f16fd1f54800be025ff4a9b1c74b0)
        ;




            var circle_marker_7036ddce3103805a50728613534a3e0c = L.circleMarker(
                [37.7307429169559, -122.429306728376],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_d699254dae3cb712cfb68e457e926726 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_0fc85a1dd4448680473d1f4b9dd15e3f = $(`&lt;div id=&quot;html_0fc85a1dd4448680473d1f4b9dd15e3f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_d699254dae3cb712cfb68e457e926726.setContent(html_0fc85a1dd4448680473d1f4b9dd15e3f);



        circle_marker_7036ddce3103805a50728613534a3e0c.bindPopup(popup_d699254dae3cb712cfb68e457e926726)
        ;




            var circle_marker_aa8e7b0862f2feb8d123ba018503edf5 = L.circleMarker(
                [37.7373623605213, -122.422067184937],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_80d59ca11c6d66e56c8c5f16074fbb93 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_e36d3e09eed413161aa9f746c6acb778 = $(`&lt;div id=&quot;html_e36d3e09eed413161aa9f746c6acb778&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;SECONDARY CODES&lt;/div&gt;`)[0];
                popup_80d59ca11c6d66e56c8c5f16074fbb93.setContent(html_e36d3e09eed413161aa9f746c6acb778);



        circle_marker_aa8e7b0862f2feb8d123ba018503edf5.bindPopup(popup_80d59ca11c6d66e56c8c5f16074fbb93)
        ;




            var circle_marker_08dfe34615c3d38bae904e9f055e2f75 = L.circleMarker(
                [37.7373623605213, -122.422067184937],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_33fdbcc0bb6748f03ce7cd5ca214ca5d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_5709fc63adf9394d209870aa72219f42 = $(`&lt;div id=&quot;html_5709fc63adf9394d209870aa72219f42&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VANDALISM&lt;/div&gt;`)[0];
                popup_33fdbcc0bb6748f03ce7cd5ca214ca5d.setContent(html_5709fc63adf9394d209870aa72219f42);



        circle_marker_08dfe34615c3d38bae904e9f055e2f75.bindPopup(popup_33fdbcc0bb6748f03ce7cd5ca214ca5d)
        ;




            var circle_marker_8e5031fa3b5cd2963f11e2a9a3e61b9d = L.circleMarker(
                [37.7859988323798, -122.411747371924],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_5f93ae151e9b2ba959defb10226d4679 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_35718aba53a4f54b31a992fa4beab428 = $(`&lt;div id=&quot;html_35718aba53a4f54b31a992fa4beab428&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;SUSPICIOUS OCC&lt;/div&gt;`)[0];
                popup_5f93ae151e9b2ba959defb10226d4679.setContent(html_35718aba53a4f54b31a992fa4beab428);



        circle_marker_8e5031fa3b5cd2963f11e2a9a3e61b9d.bindPopup(popup_5f93ae151e9b2ba959defb10226d4679)
        ;




            var circle_marker_c9b28249b645c626712a71b5c99b4040 = L.circleMarker(
                [37.7633758058059, -122.420434724553],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_01c00dc12d72729b62f69b422c86ead7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_735d81e1e0dfa9f7a5d6ce13eec4aa3f = $(`&lt;div id=&quot;html_735d81e1e0dfa9f7a5d6ce13eec4aa3f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_01c00dc12d72729b62f69b422c86ead7.setContent(html_735d81e1e0dfa9f7a5d6ce13eec4aa3f);



        circle_marker_c9b28249b645c626712a71b5c99b4040.bindPopup(popup_01c00dc12d72729b62f69b422c86ead7)
        ;




            var circle_marker_7bbaefeffce624cb5994bbd1fe153444 = L.circleMarker(
                [37.7850226622786, -122.411987643595],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_befe62ad3a614635574ee608ad8f8fe3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_b69172517068ec7befe3148f87d80d1c = $(`&lt;div id=&quot;html_b69172517068ec7befe3148f87d80d1c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_befe62ad3a614635574ee608ad8f8fe3.setContent(html_b69172517068ec7befe3148f87d80d1c);



        circle_marker_7bbaefeffce624cb5994bbd1fe153444.bindPopup(popup_befe62ad3a614635574ee608ad8f8fe3)
        ;




            var circle_marker_963604712a31885b7a29c8b238489abd = L.circleMarker(
                [37.7746206491065, -122.500380427915],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_65aea6d11cb40736f9bec82b0b533657 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_aeadc20c8bb6ee1a9ed5f8f48934bf5a = $(`&lt;div id=&quot;html_aeadc20c8bb6ee1a9ed5f8f48934bf5a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_65aea6d11cb40736f9bec82b0b533657.setContent(html_aeadc20c8bb6ee1a9ed5f8f48934bf5a);



        circle_marker_963604712a31885b7a29c8b238489abd.bindPopup(popup_65aea6d11cb40736f9bec82b0b533657)
        ;




            var circle_marker_025248788913d8851724ff6232782dd1 = L.circleMarker(
                [37.7751918267217, -122.466558780683],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_9425a0c3f953a1f22712c596734ececd = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_f39c3c4d89d69f11b5079508ce910852 = $(`&lt;div id=&quot;html_f39c3c4d89d69f11b5079508ce910852&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ROBBERY&lt;/div&gt;`)[0];
                popup_9425a0c3f953a1f22712c596734ececd.setContent(html_f39c3c4d89d69f11b5079508ce910852);



        circle_marker_025248788913d8851724ff6232782dd1.bindPopup(popup_9425a0c3f953a1f22712c596734ececd)
        ;




            var circle_marker_738fa593157fd53a959125f92d574ff7 = L.circleMarker(
                [37.7490841729028, -122.486925960114],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_b0929df84be5337f66f0db9187bf579f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_a6ab1c0f49f85b0d26ad4c8f3ad96af3 = $(`&lt;div id=&quot;html_a6ab1c0f49f85b0d26ad4c8f3ad96af3&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_b0929df84be5337f66f0db9187bf579f.setContent(html_a6ab1c0f49f85b0d26ad4c8f3ad96af3);



        circle_marker_738fa593157fd53a959125f92d574ff7.bindPopup(popup_b0929df84be5337f66f0db9187bf579f)
        ;




            var circle_marker_74b2eee00999c7690e5cb478e5a9d7dc = L.circleMarker(
                [37.7685360123583, -122.41561633832],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_ce71de9bd76d364460e5fdffbc0b7427 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_6fdcde0ff7382efbd230b124f9ef843d = $(`&lt;div id=&quot;html_6fdcde0ff7382efbd230b124f9ef843d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_ce71de9bd76d364460e5fdffbc0b7427.setContent(html_6fdcde0ff7382efbd230b124f9ef843d);



        circle_marker_74b2eee00999c7690e5cb478e5a9d7dc.bindPopup(popup_ce71de9bd76d364460e5fdffbc0b7427)
        ;




            var circle_marker_9acd92c31d5100a668d6a088da93b9d4 = L.circleMarker(
                [37.7644297714074, -122.449751652563],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_428c1ec619e47fa4926ee569e07d47f9 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_331cf73672714fcb07e9ada94ca21c84 = $(`&lt;div id=&quot;html_331cf73672714fcb07e9ada94ca21c84&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;BURGLARY&lt;/div&gt;`)[0];
                popup_428c1ec619e47fa4926ee569e07d47f9.setContent(html_331cf73672714fcb07e9ada94ca21c84);



        circle_marker_9acd92c31d5100a668d6a088da93b9d4.bindPopup(popup_428c1ec619e47fa4926ee569e07d47f9)
        ;




            var circle_marker_f6f8f0f08469ffe0985abdf1f00f9734 = L.circleMarker(
                [37.7644297714074, -122.449751652563],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_20dfffd0b9856772af94f8020e3f65e7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_871172fd88a456c654416c9358e28f6b = $(`&lt;div id=&quot;html_871172fd88a456c654416c9358e28f6b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_20dfffd0b9856772af94f8020e3f65e7.setContent(html_871172fd88a456c654416c9358e28f6b);



        circle_marker_f6f8f0f08469ffe0985abdf1f00f9734.bindPopup(popup_20dfffd0b9856772af94f8020e3f65e7)
        ;




            var circle_marker_60f178bf1090e6143a08cc2f8e1b4587 = L.circleMarker(
                [37.7352681469084, -122.472715759631],
                {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;yellow&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;blue&quot;, &quot;fillOpacity&quot;: 0.6, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 5, &quot;stroke&quot;: true, &quot;weight&quot;: 3}
            ).addTo(map_dc85c4032b54b64749ac39b2e273a510);


        var popup_70705efdce8668b5eb96621a3af4e7b4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_2de9bc7df90b3ffdc7a9749f303651c1 = $(`&lt;div id=&quot;html_2de9bc7df90b3ffdc7a9749f303651c1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_70705efdce8668b5eb96621a3af4e7b4.setContent(html_2de9bc7df90b3ffdc7a9749f303651c1);



        circle_marker_60f178bf1090e6143a08cc2f8e1b4587.bindPopup(popup_70705efdce8668b5eb96621a3af4e7b4)
        ;



&lt;/script&gt;
&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



The other proper remedy is to group the markers into different clusters. Each cluster is then represented by the number of crimes in each neighborhood. These clusters can be thought of as pockets of San Francisco which you can then analyze separately.

To implement this, we start off by instantiating a *MarkerCluster* object and adding all the data points in the dataframe to this object.



```python
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
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;

    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;

        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;

    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-1.12.4.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;

            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_efb8007f162a057b2e95e6899a502f07 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            &lt;/style&gt;

    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.1.0/leaflet.markercluster.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.1.0/MarkerCluster.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.1.0/MarkerCluster.Default.css&quot;/&gt;
&lt;/head&gt;
&lt;body&gt;


            &lt;div class=&quot;folium-map&quot; id=&quot;map_efb8007f162a057b2e95e6899a502f07&quot; &gt;&lt;/div&gt;

&lt;/body&gt;
&lt;script&gt;


            var map_efb8007f162a057b2e95e6899a502f07 = L.map(
                &quot;map_efb8007f162a057b2e95e6899a502f07&quot;,
                {
                    center: [37.77, -122.42],
                    crs: L.CRS.EPSG3857,
                    zoom: 12,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );





            var tile_layer_020539c7d85a3703e98cd16786187526 = L.tileLayer(
                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,
                {&quot;attribution&quot;: &quot;Data by \u0026copy; \u003ca target=\&quot;_blank\&quot; href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://www.openstreetmap.org/copyright\&quot;\u003eODbL\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            ).addTo(map_efb8007f162a057b2e95e6899a502f07);


            var marker_cluster_97e67e2f887714098340aa061e17ed56 = L.markerClusterGroup(
                {}
            );
            map_efb8007f162a057b2e95e6899a502f07.addLayer(marker_cluster_97e67e2f887714098340aa061e17ed56);


            var marker_eddb02cfe565be782695b0d7d96fc2bc = L.marker(
                [37.775420706711, -122.403404791479],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_0aa49a3560a3c09f30dfff9dd40208f1 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_f05b5e6c7a8f7c65721d78f6a81465f7 = $(`&lt;div id=&quot;html_f05b5e6c7a8f7c65721d78f6a81465f7&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WEAPON LAWS&lt;/div&gt;`)[0];
                popup_0aa49a3560a3c09f30dfff9dd40208f1.setContent(html_f05b5e6c7a8f7c65721d78f6a81465f7);



        marker_eddb02cfe565be782695b0d7d96fc2bc.bindPopup(popup_0aa49a3560a3c09f30dfff9dd40208f1)
        ;




            var marker_ee9156589c500b282946e65b29153ded = L.marker(
                [37.775420706711, -122.403404791479],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_a80867683c7c6b530d8d678a4ef9128d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_023fbb2d40f460768d1e8d1055619733 = $(`&lt;div id=&quot;html_023fbb2d40f460768d1e8d1055619733&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WEAPON LAWS&lt;/div&gt;`)[0];
                popup_a80867683c7c6b530d8d678a4ef9128d.setContent(html_023fbb2d40f460768d1e8d1055619733);



        marker_ee9156589c500b282946e65b29153ded.bindPopup(popup_a80867683c7c6b530d8d678a4ef9128d)
        ;




            var marker_0b24abf4e6681fd6050035839dd378a9 = L.marker(
                [37.7299809672996, -122.388856204292],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_8f4dafd812fd4243e9f2ebc446c7d82b = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_9e4966ae1bb6134652e427547d933435 = $(`&lt;div id=&quot;html_9e4966ae1bb6134652e427547d933435&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_8f4dafd812fd4243e9f2ebc446c7d82b.setContent(html_9e4966ae1bb6134652e427547d933435);



        marker_0b24abf4e6681fd6050035839dd378a9.bindPopup(popup_8f4dafd812fd4243e9f2ebc446c7d82b)
        ;




            var marker_5eaefcf61a756f2b2e277b1941aa1a6c = L.marker(
                [37.7857883766888, -122.412970537591],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_7e8ee13bbdca6aabcaedbd1575fdde1f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_74e5a3f63d8b9b548bcda59cd0899f8b = $(`&lt;div id=&quot;html_74e5a3f63d8b9b548bcda59cd0899f8b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_7e8ee13bbdca6aabcaedbd1575fdde1f.setContent(html_74e5a3f63d8b9b548bcda59cd0899f8b);



        marker_5eaefcf61a756f2b2e277b1941aa1a6c.bindPopup(popup_7e8ee13bbdca6aabcaedbd1575fdde1f)
        ;




            var marker_9a48e5d3d0b369479029a4538407ab49 = L.marker(
                [37.7650501214668, -122.419671780296],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_ecb8d05101755a1c961e43c99f06eeef = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_f6718d602c045a1dbb46abee8b075645 = $(`&lt;div id=&quot;html_f6718d602c045a1dbb46abee8b075645&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_ecb8d05101755a1c961e43c99f06eeef.setContent(html_f6718d602c045a1dbb46abee8b075645);



        marker_9a48e5d3d0b369479029a4538407ab49.bindPopup(popup_ecb8d05101755a1c961e43c99f06eeef)
        ;




            var marker_59246e4b3b95050d823d455074d999b4 = L.marker(
                [37.788018555829, -122.426077177375],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_a2934dae983ec669e1b4b38d8e933ada = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_798b2108f60cd14f689bc37eba5b03de = $(`&lt;div id=&quot;html_798b2108f60cd14f689bc37eba5b03de&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_a2934dae983ec669e1b4b38d8e933ada.setContent(html_798b2108f60cd14f689bc37eba5b03de);



        marker_59246e4b3b95050d823d455074d999b4.bindPopup(popup_a2934dae983ec669e1b4b38d8e933ada)
        ;




            var marker_a1b4e762d9d65fa7676d9e56a2ef4c74 = L.marker(
                [37.7808789360214, -122.405721454567],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_7fa52d0bf59f49fe25edcefe074762f5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_354f589a53bd1ab6ccd68c3af9da7ac2 = $(`&lt;div id=&quot;html_354f589a53bd1ab6ccd68c3af9da7ac2&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_7fa52d0bf59f49fe25edcefe074762f5.setContent(html_354f589a53bd1ab6ccd68c3af9da7ac2);



        marker_a1b4e762d9d65fa7676d9e56a2ef4c74.bindPopup(popup_7fa52d0bf59f49fe25edcefe074762f5)
        ;




            var marker_4c7d42681116e1e65eb56f01c1d1269d = L.marker(
                [37.7839805592634, -122.411778295992],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_42d5b287fccfac802467700c446d314a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_0f722d460d4d361d623b7f51c7d26f29 = $(`&lt;div id=&quot;html_0f722d460d4d361d623b7f51c7d26f29&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_42d5b287fccfac802467700c446d314a.setContent(html_0f722d460d4d361d623b7f51c7d26f29);



        marker_4c7d42681116e1e65eb56f01c1d1269d.bindPopup(popup_42d5b287fccfac802467700c446d314a)
        ;




            var marker_4e2af2ee07102ba2ade8285b9b65e92a = L.marker(
                [37.7757876218293, -122.393357241451],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_b66282532d9aef5756fb27c7589071fa = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_c50a317c4a8761e22ed850a1260f5b0b = $(`&lt;div id=&quot;html_c50a317c4a8761e22ed850a1260f5b0b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_b66282532d9aef5756fb27c7589071fa.setContent(html_c50a317c4a8761e22ed850a1260f5b0b);



        marker_4e2af2ee07102ba2ade8285b9b65e92a.bindPopup(popup_b66282532d9aef5756fb27c7589071fa)
        ;




            var marker_8a986f0c6633e15f38ddea0d92c91b58 = L.marker(
                [37.7209669615499, -122.387181635995],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_d9c04b705c17e0154c7920e552ec1eae = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_82a77f74cdad8b8954c4959d282467e9 = $(`&lt;div id=&quot;html_82a77f74cdad8b8954c4959d282467e9&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;MISSING PERSON&lt;/div&gt;`)[0];
                popup_d9c04b705c17e0154c7920e552ec1eae.setContent(html_82a77f74cdad8b8954c4959d282467e9);



        marker_8a986f0c6633e15f38ddea0d92c91b58.bindPopup(popup_d9c04b705c17e0154c7920e552ec1eae)
        ;




            var marker_81501aae64da1eb169b8c185c1c64f92 = L.marker(
                [37.7644781578695, -122.477376524003],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_5571eb84028f889480f063002b9f25b1 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_42a558a19a69584804abbd90aed93572 = $(`&lt;div id=&quot;html_42a558a19a69584804abbd90aed93572&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_5571eb84028f889480f063002b9f25b1.setContent(html_42a558a19a69584804abbd90aed93572);



        marker_81501aae64da1eb169b8c185c1c64f92.bindPopup(popup_5571eb84028f889480f063002b9f25b1)
        ;




            var marker_d8507e92b61715b43e348c62b7ae30c0 = L.marker(
                [37.7457389429655, -122.477960327299],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_bf844ac9cb71c3ee2afdaa2b0fc007e7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_94ab8f66fd82729947e02cfb384f2dc3 = $(`&lt;div id=&quot;html_94ab8f66fd82729947e02cfb384f2dc3&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_bf844ac9cb71c3ee2afdaa2b0fc007e7.setContent(html_94ab8f66fd82729947e02cfb384f2dc3);



        marker_d8507e92b61715b43e348c62b7ae30c0.bindPopup(popup_bf844ac9cb71c3ee2afdaa2b0fc007e7)
        ;




            var marker_6c07480044b74838243b247280b33304 = L.marker(
                [37.7356970275482, -122.37675765553],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_cf92634f0a3ac0461f288ef350fecaa3 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_23457fb20cd19e77000db235570a84ef = $(`&lt;div id=&quot;html_23457fb20cd19e77000db235570a84ef&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_cf92634f0a3ac0461f288ef350fecaa3.setContent(html_23457fb20cd19e77000db235570a84ef);



        marker_6c07480044b74838243b247280b33304.bindPopup(popup_cf92634f0a3ac0461f288ef350fecaa3)
        ;




            var marker_d0a2df938190b635e4f8f6d60211da88 = L.marker(
                [37.7292705199592, -122.432325871028],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_5f8ae8183fa70cf12d4b1eebb5da2cb7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_41f6d92106e34d8b95640f92f908082c = $(`&lt;div id=&quot;html_41f6d92106e34d8b95640f92f908082c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_5f8ae8183fa70cf12d4b1eebb5da2cb7.setContent(html_41f6d92106e34d8b95640f92f908082c);



        marker_d0a2df938190b635e4f8f6d60211da88.bindPopup(popup_5f8ae8183fa70cf12d4b1eebb5da2cb7)
        ;




            var marker_d5f1e96853a409d22c1ec2b987757bda = L.marker(
                [37.791642982384, -122.40090869889],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_98503f5782ecb933275b02e38b97c13a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_20bcdc1e90fd9d84cc0fa5c0f660f7c6 = $(`&lt;div id=&quot;html_20bcdc1e90fd9d84cc0fa5c0f660f7c6&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;BURGLARY&lt;/div&gt;`)[0];
                popup_98503f5782ecb933275b02e38b97c13a.setContent(html_20bcdc1e90fd9d84cc0fa5c0f660f7c6);



        marker_d5f1e96853a409d22c1ec2b987757bda.bindPopup(popup_98503f5782ecb933275b02e38b97c13a)
        ;




            var marker_2976eb6522433c45a2fb871706b6b357 = L.marker(
                [37.7837069301545, -122.408595110869],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_6e9f6f6656066cb0c42632e3f5cc56ee = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_58a7b764a0d394b5fc200563e80029a5 = $(`&lt;div id=&quot;html_58a7b764a0d394b5fc200563e80029a5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;STOLEN PROPERTY&lt;/div&gt;`)[0];
                popup_6e9f6f6656066cb0c42632e3f5cc56ee.setContent(html_58a7b764a0d394b5fc200563e80029a5);



        marker_2976eb6522433c45a2fb871706b6b357.bindPopup(popup_6e9f6f6656066cb0c42632e3f5cc56ee)
        ;




            var marker_dc1838451df45afce8184884cb4ec3a4 = L.marker(
                [37.7572895904578, -122.406870402082],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_aa708a574d66494d3aced04dbc2de0b4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_3121e825c600d14de6e42d6ed09539c9 = $(`&lt;div id=&quot;html_3121e825c600d14de6e42d6ed09539c9&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ROBBERY&lt;/div&gt;`)[0];
                popup_aa708a574d66494d3aced04dbc2de0b4.setContent(html_3121e825c600d14de6e42d6ed09539c9);



        marker_dc1838451df45afce8184884cb4ec3a4.bindPopup(popup_aa708a574d66494d3aced04dbc2de0b4)
        ;




            var marker_22a654b5e8e7f10a27fb041675949e5c = L.marker(
                [37.7489063051829, -122.420354780861],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_5015fbb4056a1463b4eb6ea41da09132 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_f0fe9c8bde02cca9e2c157dd07590cfc = $(`&lt;div id=&quot;html_f0fe9c8bde02cca9e2c157dd07590cfc&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_5015fbb4056a1463b4eb6ea41da09132.setContent(html_f0fe9c8bde02cca9e2c157dd07590cfc);



        marker_22a654b5e8e7f10a27fb041675949e5c.bindPopup(popup_5015fbb4056a1463b4eb6ea41da09132)
        ;




            var marker_07eb83e0b5e940f20f3502fdc9ea8560 = L.marker(
                [37.715765426995, -122.439909766772],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_1e2546451d4236c0ba3511b01053224f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_e09afc5cd8855fd407f2e2a47841b16f = $(`&lt;div id=&quot;html_e09afc5cd8855fd407f2e2a47841b16f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_1e2546451d4236c0ba3511b01053224f.setContent(html_e09afc5cd8855fd407f2e2a47841b16f);



        marker_07eb83e0b5e940f20f3502fdc9ea8560.bindPopup(popup_1e2546451d4236c0ba3511b01053224f)
        ;




            var marker_dceb20b1ebffba665d22ac191b2bb54c = L.marker(
                [37.7835699386918, -122.408421116922],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_6aa39d50a4502f1497943d646280af87 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_a081b995491f277e8a832a00aa387598 = $(`&lt;div id=&quot;html_a081b995491f277e8a832a00aa387598&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_6aa39d50a4502f1497943d646280af87.setContent(html_a081b995491f277e8a832a00aa387598);



        marker_dceb20b1ebffba665d22ac191b2bb54c.bindPopup(popup_6aa39d50a4502f1497943d646280af87)
        ;




            var marker_1e8641d0c1f4137bee4b1802ea87288a = L.marker(
                [37.7736186276456, -122.422315670749],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_5b1008df835c1f5897fdac65b3db11b4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_30955fde3f6a658118d97e2538ea2256 = $(`&lt;div id=&quot;html_30955fde3f6a658118d97e2538ea2256&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;FRAUD&lt;/div&gt;`)[0];
                popup_5b1008df835c1f5897fdac65b3db11b4.setContent(html_30955fde3f6a658118d97e2538ea2256);



        marker_1e8641d0c1f4137bee4b1802ea87288a.bindPopup(popup_5b1008df835c1f5897fdac65b3db11b4)
        ;




            var marker_7980aea2937e7a83243d08d13899b12e = L.marker(
                [37.7928412840447, -122.424519835009],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_c460afa52641060ae8b31c959bf829cf = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_700091053d49e9e24165e919acfee532 = $(`&lt;div id=&quot;html_700091053d49e9e24165e919acfee532&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_c460afa52641060ae8b31c959bf829cf.setContent(html_700091053d49e9e24165e919acfee532);



        marker_7980aea2937e7a83243d08d13899b12e.bindPopup(popup_c460afa52641060ae8b31c959bf829cf)
        ;




            var marker_47d183c5bfbf3d3938ba3ec8702cb885 = L.marker(
                [37.7540986882068, -122.414233849038],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_1c9d54ad837dc9afb872dda267409f04 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_fa95d657c441d0319d97c23f67c8a1b7 = $(`&lt;div id=&quot;html_fa95d657c441d0319d97c23f67c8a1b7&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;DRUG/NARCOTIC&lt;/div&gt;`)[0];
                popup_1c9d54ad837dc9afb872dda267409f04.setContent(html_fa95d657c441d0319d97c23f67c8a1b7);



        marker_47d183c5bfbf3d3938ba3ec8702cb885.bindPopup(popup_1c9d54ad837dc9afb872dda267409f04)
        ;




            var marker_8706fa16d6a9f875b2e1e94373d2f0e8 = L.marker(
                [37.7540986882068, -122.414233849038],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_7088e6b8861e50b94364d275fed45eaa = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_17e69d8fbb4507944c90e0907b0b02b1 = $(`&lt;div id=&quot;html_17e69d8fbb4507944c90e0907b0b02b1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_7088e6b8861e50b94364d275fed45eaa.setContent(html_17e69d8fbb4507944c90e0907b0b02b1);



        marker_8706fa16d6a9f875b2e1e94373d2f0e8.bindPopup(popup_7088e6b8861e50b94364d275fed45eaa)
        ;




            var marker_9bef2a0f52e7573d3297ff2fd95808ef = L.marker(
                [37.7714939969416, -122.507750131004],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_861ce93a35c9180664fa9f965fb8d392 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_20a4597971fa157379e851d6a5515285 = $(`&lt;div id=&quot;html_20a4597971fa157379e851d6a5515285&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_861ce93a35c9180664fa9f965fb8d392.setContent(html_20a4597971fa157379e851d6a5515285);



        marker_9bef2a0f52e7573d3297ff2fd95808ef.bindPopup(popup_861ce93a35c9180664fa9f965fb8d392)
        ;




            var marker_548c36ed3e2b51a25b235a9c181ec514 = L.marker(
                [37.718302204766, -122.474444639595],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_9d45764503cfadcd135b7fcb99065a23 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_10e0a318269d841b6852dae0f07ce20f = $(`&lt;div id=&quot;html_10e0a318269d841b6852dae0f07ce20f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_9d45764503cfadcd135b7fcb99065a23.setContent(html_10e0a318269d841b6852dae0f07ce20f);



        marker_548c36ed3e2b51a25b235a9c181ec514.bindPopup(popup_9d45764503cfadcd135b7fcb99065a23)
        ;




            var marker_047cf10b2e52a2336f5afa041ce1ef1d = L.marker(
                [37.7645752317615, -122.427562596985],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_ac961c78921e72fb2aa952f49a77d5f2 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_d613ca4a6daba7ed6feaa45107436b95 = $(`&lt;div id=&quot;html_d613ca4a6daba7ed6feaa45107436b95&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_ac961c78921e72fb2aa952f49a77d5f2.setContent(html_d613ca4a6daba7ed6feaa45107436b95);



        marker_047cf10b2e52a2336f5afa041ce1ef1d.bindPopup(popup_ac961c78921e72fb2aa952f49a77d5f2)
        ;




            var marker_8034e57ba3fda115039700e0212e08ce = L.marker(
                [37.7874378309112, -122.419203004268],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_6f403f81c94a2b653b6e3e06937dce6f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_76aa775d8b6b3e1912615ffba8a6a851 = $(`&lt;div id=&quot;html_76aa775d8b6b3e1912615ffba8a6a851&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;BURGLARY&lt;/div&gt;`)[0];
                popup_6f403f81c94a2b653b6e3e06937dce6f.setContent(html_76aa775d8b6b3e1912615ffba8a6a851);



        marker_8034e57ba3fda115039700e0212e08ce.bindPopup(popup_6f403f81c94a2b653b6e3e06937dce6f)
        ;




            var marker_170f5e5391623f313fac125bbad90d4c = L.marker(
                [37.7493688284532, -122.412690142308],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_353e3bd5531d6fafe15551195c2efbd2 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_e7c36f145de99120bdb7206429f85613 = $(`&lt;div id=&quot;html_e7c36f145de99120bdb7206429f85613&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_353e3bd5531d6fafe15551195c2efbd2.setContent(html_e7c36f145de99120bdb7206429f85613);



        marker_170f5e5391623f313fac125bbad90d4c.bindPopup(popup_353e3bd5531d6fafe15551195c2efbd2)
        ;




            var marker_b9538253b78274360fb62c08a49342fb = L.marker(
                [37.7092010462379, -122.434609280352],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_fcd67a506553c26ad2215c8e4eafda0f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_50f1427ba32a3878e34f4c6053763c79 = $(`&lt;div id=&quot;html_50f1427ba32a3878e34f4c6053763c79&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_fcd67a506553c26ad2215c8e4eafda0f.setContent(html_50f1427ba32a3878e34f4c6053763c79);



        marker_b9538253b78274360fb62c08a49342fb.bindPopup(popup_fcd67a506553c26ad2215c8e4eafda0f)
        ;




            var marker_0b3479f53454898ca62c7ea424e2152c = L.marker(
                [37.7879209375533, -122.410882825551],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_68c3e41a9651d8c64f617411736483d7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_c22d90fba73828da0a7b33088d46dfef = $(`&lt;div id=&quot;html_c22d90fba73828da0a7b33088d46dfef&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VEHICLE THEFT&lt;/div&gt;`)[0];
                popup_68c3e41a9651d8c64f617411736483d7.setContent(html_c22d90fba73828da0a7b33088d46dfef);



        marker_0b3479f53454898ca62c7ea424e2152c.bindPopup(popup_68c3e41a9651d8c64f617411736483d7)
        ;




            var marker_c0a6e703ff0e98bebc76ea256cf86dcd = L.marker(
                [37.8004566471039, -122.401432754722],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_e419ce9c2c0f3603fb9eef21b4a8ef17 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_f56fbc9413c2eab6739b06ddfecbc85f = $(`&lt;div id=&quot;html_f56fbc9413c2eab6739b06ddfecbc85f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VEHICLE THEFT&lt;/div&gt;`)[0];
                popup_e419ce9c2c0f3603fb9eef21b4a8ef17.setContent(html_f56fbc9413c2eab6739b06ddfecbc85f);



        marker_c0a6e703ff0e98bebc76ea256cf86dcd.bindPopup(popup_e419ce9c2c0f3603fb9eef21b4a8ef17)
        ;




            var marker_475c7a4783ecefcb6991f87242a7dfc7 = L.marker(
                [37.7435550542265, -122.421128029505],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_86e40e39c9cdd1c07428b5568f08343e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_5d9f35776fabec978e1665583122f9ef = $(`&lt;div id=&quot;html_5d9f35776fabec978e1665583122f9ef&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_86e40e39c9cdd1c07428b5568f08343e.setContent(html_5d9f35776fabec978e1665583122f9ef);



        marker_475c7a4783ecefcb6991f87242a7dfc7.bindPopup(popup_86e40e39c9cdd1c07428b5568f08343e)
        ;




            var marker_5d58b01a1f32b5de11e269fd163eb220 = L.marker(
                [37.7865647607685, -122.407244087032],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_a16ac52926d19cdd2942cd80edbb2cae = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_c0842f6462879a13d8597dee0ffca8e7 = $(`&lt;div id=&quot;html_c0842f6462879a13d8597dee0ffca8e7&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_a16ac52926d19cdd2942cd80edbb2cae.setContent(html_c0842f6462879a13d8597dee0ffca8e7);



        marker_5d58b01a1f32b5de11e269fd163eb220.bindPopup(popup_a16ac52926d19cdd2942cd80edbb2cae)
        ;




            var marker_cfbcb2c9717d95e605beaa540efa3042 = L.marker(
                [37.7615655928045, -122.423803001901],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_29d7750b4a0f9dfe7cfd16373be239c6 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_aa573faea4e9f904f972256161719422 = $(`&lt;div id=&quot;html_aa573faea4e9f904f972256161719422&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;RECOVERED VEHICLE&lt;/div&gt;`)[0];
                popup_29d7750b4a0f9dfe7cfd16373be239c6.setContent(html_aa573faea4e9f904f972256161719422);



        marker_cfbcb2c9717d95e605beaa540efa3042.bindPopup(popup_29d7750b4a0f9dfe7cfd16373be239c6)
        ;




            var marker_0e25c3c9ef30c4239108e36bcd9e1b17 = L.marker(
                [37.7615655928045, -122.423803001901],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_2b9ec2c54e64bc6931c219ee848861b4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_508ad5e981c15b482eae6041725a8214 = $(`&lt;div id=&quot;html_508ad5e981c15b482eae6041725a8214&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_2b9ec2c54e64bc6931c219ee848861b4.setContent(html_508ad5e981c15b482eae6041725a8214);



        marker_0e25c3c9ef30c4239108e36bcd9e1b17.bindPopup(popup_2b9ec2c54e64bc6931c219ee848861b4)
        ;




            var marker_17ce3d4872d3ea77b1eecc7c7d556c64 = L.marker(
                [37.7441927508932, -122.444685482273],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_62be1c762ca458199d9e9f0e0d09fe73 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_d61a7bd207da8f5d2b1af8b4d37594ae = $(`&lt;div id=&quot;html_d61a7bd207da8f5d2b1af8b4d37594ae&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_62be1c762ca458199d9e9f0e0d09fe73.setContent(html_d61a7bd207da8f5d2b1af8b4d37594ae);



        marker_17ce3d4872d3ea77b1eecc7c7d556c64.bindPopup(popup_62be1c762ca458199d9e9f0e0d09fe73)
        ;




            var marker_ce1e94800fd5ff3282d38eeb14267f0b = L.marker(
                [37.7754692820041, -122.415757039196],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_c56e6e66dce174579416c39d9891eefe = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_dd8454070bd594d976a3a1dafdd924bb = $(`&lt;div id=&quot;html_dd8454070bd594d976a3a1dafdd924bb&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_c56e6e66dce174579416c39d9891eefe.setContent(html_dd8454070bd594d976a3a1dafdd924bb);



        marker_ce1e94800fd5ff3282d38eeb14267f0b.bindPopup(popup_c56e6e66dce174579416c39d9891eefe)
        ;




            var marker_da158ff6a3549d4ca1421dd6f668d587 = L.marker(
                [37.7285280627465, -122.475647460786],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_cd37d1f3d77a9bc37b65469de0765787 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_fc0148e6cd1edf5007b7411afab8db71 = $(`&lt;div id=&quot;html_fc0148e6cd1edf5007b7411afab8db71&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ROBBERY&lt;/div&gt;`)[0];
                popup_cd37d1f3d77a9bc37b65469de0765787.setContent(html_fc0148e6cd1edf5007b7411afab8db71);



        marker_da158ff6a3549d4ca1421dd6f668d587.bindPopup(popup_cd37d1f3d77a9bc37b65469de0765787)
        ;




            var marker_f39528f1c65d654bdfecd0d658185056 = L.marker(
                [37.7428517374449, -122.420967440564],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_0c713ace43656399ed89bbf1eea39793 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_f3031381479a4b20d08b7764d70d6d6d = $(`&lt;div id=&quot;html_f3031381479a4b20d08b7764d70d6d6d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_0c713ace43656399ed89bbf1eea39793.setContent(html_f3031381479a4b20d08b7764d70d6d6d);



        marker_f39528f1c65d654bdfecd0d658185056.bindPopup(popup_0c713ace43656399ed89bbf1eea39793)
        ;




            var marker_0c81bd6adb7fb5437968ccfbf71fbd97 = L.marker(
                [37.7821198488931, -122.415669661443],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_30926cae5cdbf1966dc753f09e1e43d0 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_25e443c0a8f440bfcc47264663730e45 = $(`&lt;div id=&quot;html_25e443c0a8f440bfcc47264663730e45&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VANDALISM&lt;/div&gt;`)[0];
                popup_30926cae5cdbf1966dc753f09e1e43d0.setContent(html_25e443c0a8f440bfcc47264663730e45);



        marker_0c81bd6adb7fb5437968ccfbf71fbd97.bindPopup(popup_30926cae5cdbf1966dc753f09e1e43d0)
        ;




            var marker_64c422d074af25da8596988d568d00bc = L.marker(
                [37.7791674218963, -122.406346425632],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_efab063e7d11893900c3dd6c1143b1eb = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_f88f928829833328ed2a6dd422eb3cc0 = $(`&lt;div id=&quot;html_f88f928829833328ed2a6dd422eb3cc0&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_efab063e7d11893900c3dd6c1143b1eb.setContent(html_f88f928829833328ed2a6dd422eb3cc0);



        marker_64c422d074af25da8596988d568d00bc.bindPopup(popup_efab063e7d11893900c3dd6c1143b1eb)
        ;




            var marker_64faf6414c2ec5488e5eb7eeec9788cb = L.marker(
                [37.7657184395282, -122.409529913278],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_72b627def8e9c9b9daf66579da24d6ed = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_d7de95a98475a3430fd22fcc163d5004 = $(`&lt;div id=&quot;html_d7de95a98475a3430fd22fcc163d5004&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_72b627def8e9c9b9daf66579da24d6ed.setContent(html_d7de95a98475a3430fd22fcc163d5004);



        marker_64faf6414c2ec5488e5eb7eeec9788cb.bindPopup(popup_72b627def8e9c9b9daf66579da24d6ed)
        ;




            var marker_460da0127d5aab5c8376e9237fb2497c = L.marker(
                [37.775420706711, -122.403404791479],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_62fa66c3ab63f90c8377c7a11eb2b0e2 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_cecea6f51ae5cee0ca5c591d56584ad7 = $(`&lt;div id=&quot;html_cecea6f51ae5cee0ca5c591d56584ad7&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_62fa66c3ab63f90c8377c7a11eb2b0e2.setContent(html_cecea6f51ae5cee0ca5c591d56584ad7);



        marker_460da0127d5aab5c8376e9237fb2497c.bindPopup(popup_62fa66c3ab63f90c8377c7a11eb2b0e2)
        ;




            var marker_d97e21a7411c24fbd0d639dbfd2d4ab0 = L.marker(
                [37.767524308783, -122.410738097315],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_df32c235b28fd0892747accb68458614 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_9d78977b9874a5f839bbdfa57242b577 = $(`&lt;div id=&quot;html_9d78977b9874a5f839bbdfa57242b577&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;BURGLARY&lt;/div&gt;`)[0];
                popup_df32c235b28fd0892747accb68458614.setContent(html_9d78977b9874a5f839bbdfa57242b577);



        marker_d97e21a7411c24fbd0d639dbfd2d4ab0.bindPopup(popup_df32c235b28fd0892747accb68458614)
        ;




            var marker_92795286377e01ef394a0bcc2de1bd00 = L.marker(
                [37.767524308783, -122.410738097315],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_e3b833b1351e722562deadcce7e61514 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_33eaf72a8e20340a4d4b54e0730bc9d8 = $(`&lt;div id=&quot;html_33eaf72a8e20340a4d4b54e0730bc9d8&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ARSON&lt;/div&gt;`)[0];
                popup_e3b833b1351e722562deadcce7e61514.setContent(html_33eaf72a8e20340a4d4b54e0730bc9d8);



        marker_92795286377e01ef394a0bcc2de1bd00.bindPopup(popup_e3b833b1351e722562deadcce7e61514)
        ;




            var marker_c680541b61aef92a24206a44e850b453 = L.marker(
                [37.7131083433264, -122.444314025188],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_103e790a4b36d3e8a36325738286d739 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_bc1109ca17d8e62decd27619a53a486f = $(`&lt;div id=&quot;html_bc1109ca17d8e62decd27619a53a486f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;BURGLARY&lt;/div&gt;`)[0];
                popup_103e790a4b36d3e8a36325738286d739.setContent(html_bc1109ca17d8e62decd27619a53a486f);



        marker_c680541b61aef92a24206a44e850b453.bindPopup(popup_103e790a4b36d3e8a36325738286d739)
        ;




            var marker_5756f218b2ebb7415e3b32f1bbd8f520 = L.marker(
                [37.7131083433264, -122.444314025188],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_1cb410dda1e29cecc09c66fe50a27772 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_84a1cc234becf71d3492e4fda93c760d = $(`&lt;div id=&quot;html_84a1cc234becf71d3492e4fda93c760d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;DRUG/NARCOTIC&lt;/div&gt;`)[0];
                popup_1cb410dda1e29cecc09c66fe50a27772.setContent(html_84a1cc234becf71d3492e4fda93c760d);



        marker_5756f218b2ebb7415e3b32f1bbd8f520.bindPopup(popup_1cb410dda1e29cecc09c66fe50a27772)
        ;




            var marker_eac37748d331961ce8fcb307c8116ef9 = L.marker(
                [37.7660160114103, -122.403644620439],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_50beab270483cec900dd01ecc3afa381 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_638956c9192263d842d05ae0ae575370 = $(`&lt;div id=&quot;html_638956c9192263d842d05ae0ae575370&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;MISSING PERSON&lt;/div&gt;`)[0];
                popup_50beab270483cec900dd01ecc3afa381.setContent(html_638956c9192263d842d05ae0ae575370);



        marker_eac37748d331961ce8fcb307c8116ef9.bindPopup(popup_50beab270483cec900dd01ecc3afa381)
        ;




            var marker_b9e77caf74b633e05eec21e92c06a266 = L.marker(
                [37.7660160114103, -122.403644620439],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_47d593552781911d92b4182cb527e380 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_6268511709f6b831d8bb2728c0537762 = $(`&lt;div id=&quot;html_6268511709f6b831d8bb2728c0537762&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;MISSING PERSON&lt;/div&gt;`)[0];
                popup_47d593552781911d92b4182cb527e380.setContent(html_6268511709f6b831d8bb2728c0537762);



        marker_b9e77caf74b633e05eec21e92c06a266.bindPopup(popup_47d593552781911d92b4182cb527e380)
        ;




            var marker_7874cc88f59ee04b8cb5ff431a9620fa = L.marker(
                [37.7762310404758, -122.414714295579],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_6c543176e3d0e7120c205dd6f549e51a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_e25606222cbee271fb6d7657b2687f0a = $(`&lt;div id=&quot;html_e25606222cbee271fb6d7657b2687f0a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_6c543176e3d0e7120c205dd6f549e51a.setContent(html_e25606222cbee271fb6d7657b2687f0a);



        marker_7874cc88f59ee04b8cb5ff431a9620fa.bindPopup(popup_6c543176e3d0e7120c205dd6f549e51a)
        ;




            var marker_4c5cc943f2dbf960f06c6d0b24acabc7 = L.marker(
                [37.7762310404758, -122.414714295579],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_3f159de3e41910efa10e5deb5b6c2cd7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_973f9efc9eaec84d7320304e77b2ba0e = $(`&lt;div id=&quot;html_973f9efc9eaec84d7320304e77b2ba0e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;MISSING PERSON&lt;/div&gt;`)[0];
                popup_3f159de3e41910efa10e5deb5b6c2cd7.setContent(html_973f9efc9eaec84d7320304e77b2ba0e);



        marker_4c5cc943f2dbf960f06c6d0b24acabc7.bindPopup(popup_3f159de3e41910efa10e5deb5b6c2cd7)
        ;




            var marker_aaa51281152b8433b48e2b4dc3e3a6f8 = L.marker(
                [37.7775118895695, -122.418045452768],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_da971ff46b5dae16fa28c664d8ec5421 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_43c6f410a3eea6bfd4d0bcd6571746f8 = $(`&lt;div id=&quot;html_43c6f410a3eea6bfd4d0bcd6571746f8&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VEHICLE THEFT&lt;/div&gt;`)[0];
                popup_da971ff46b5dae16fa28c664d8ec5421.setContent(html_43c6f410a3eea6bfd4d0bcd6571746f8);



        marker_aaa51281152b8433b48e2b4dc3e3a6f8.bindPopup(popup_da971ff46b5dae16fa28c664d8ec5421)
        ;




            var marker_fc8827016ad9c9ad383aa0b269d246db = L.marker(
                [37.7820238478975, -122.401161555602],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_0a2471962ead742070e075e9b92888c1 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_cf75b39d452787b5160b2c718aefa8eb = $(`&lt;div id=&quot;html_cf75b39d452787b5160b2c718aefa8eb&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_0a2471962ead742070e075e9b92888c1.setContent(html_cf75b39d452787b5160b2c718aefa8eb);



        marker_fc8827016ad9c9ad383aa0b269d246db.bindPopup(popup_0a2471962ead742070e075e9b92888c1)
        ;




            var marker_7e0c78d4c5f3437f0dcfa6417865188f = L.marker(
                [37.72700531963, -122.403408669191],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_168e4424c8db38e748988bccbe35a51f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_5c2d2a4d87a94e6ae748e9294a529044 = $(`&lt;div id=&quot;html_5c2d2a4d87a94e6ae748e9294a529044&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_168e4424c8db38e748988bccbe35a51f.setContent(html_5c2d2a4d87a94e6ae748e9294a529044);



        marker_7e0c78d4c5f3437f0dcfa6417865188f.bindPopup(popup_168e4424c8db38e748988bccbe35a51f)
        ;




            var marker_908c553677c4ff60c1416777c95a9d24 = L.marker(
                [37.7838344374141, -122.412930522059],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_6aca518656a49b563c59c5d9700d84d1 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_19a4a55d852a461bbe61cd2a84bbcd81 = $(`&lt;div id=&quot;html_19a4a55d852a461bbe61cd2a84bbcd81&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VANDALISM&lt;/div&gt;`)[0];
                popup_6aca518656a49b563c59c5d9700d84d1.setContent(html_19a4a55d852a461bbe61cd2a84bbcd81);



        marker_908c553677c4ff60c1416777c95a9d24.bindPopup(popup_6aca518656a49b563c59c5d9700d84d1)
        ;




            var marker_302f305f4c32de5a93820ac95920b75f = L.marker(
                [37.7530186537446, -122.418587172219],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_9157c7742812149a0d04a1d07afc19a6 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_96ede7033da7a33dfec3a424e1c6b08e = $(`&lt;div id=&quot;html_96ede7033da7a33dfec3a424e1c6b08e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_9157c7742812149a0d04a1d07afc19a6.setContent(html_96ede7033da7a33dfec3a424e1c6b08e);



        marker_302f305f4c32de5a93820ac95920b75f.bindPopup(popup_9157c7742812149a0d04a1d07afc19a6)
        ;




            var marker_1259d52c4b8eb3be8745ee4c5c862736 = L.marker(
                [37.7740418385041, -122.414370627495],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_820fe061b79c23686af40697419d3687 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_526ecc5994760a9c4f87d6325f332a59 = $(`&lt;div id=&quot;html_526ecc5994760a9c4f87d6325f332a59&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;FRAUD&lt;/div&gt;`)[0];
                popup_820fe061b79c23686af40697419d3687.setContent(html_526ecc5994760a9c4f87d6325f332a59);



        marker_1259d52c4b8eb3be8745ee4c5c862736.bindPopup(popup_820fe061b79c23686af40697419d3687)
        ;




            var marker_c3a8213a84c4fd4b035957b2f89f5a83 = L.marker(
                [37.790538993725, -122.403915681571],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_da1c2aaed7e80fc6ef7d793877d048d0 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_8c831aa960e3516579a16fefe86645c1 = $(`&lt;div id=&quot;html_8c831aa960e3516579a16fefe86645c1&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ASSAULT&lt;/div&gt;`)[0];
                popup_da1c2aaed7e80fc6ef7d793877d048d0.setContent(html_8c831aa960e3516579a16fefe86645c1);



        marker_c3a8213a84c4fd4b035957b2f89f5a83.bindPopup(popup_da1c2aaed7e80fc6ef7d793877d048d0)
        ;




            var marker_b02937a31efc41629fd62e8f8b20e6bf = L.marker(
                [37.7830998244592, -122.419183096362],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_92d72b01296c41728bce307668f8b446 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_212bc7234cbe38c725d59531f393ba74 = $(`&lt;div id=&quot;html_212bc7234cbe38c725d59531f393ba74&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_92d72b01296c41728bce307668f8b446.setContent(html_212bc7234cbe38c725d59531f393ba74);



        marker_b02937a31efc41629fd62e8f8b20e6bf.bindPopup(popup_92d72b01296c41728bce307668f8b446)
        ;




            var marker_e4d2cb2e61b07467a5a581efab19bdc3 = L.marker(
                [37.7407360548358, -122.388753046997],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_332aa55d5d718d8e43790b9f5d61984c = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_2716dcc43317cbdfa605daf1e54784df = $(`&lt;div id=&quot;html_2716dcc43317cbdfa605daf1e54784df&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_332aa55d5d718d8e43790b9f5d61984c.setContent(html_2716dcc43317cbdfa605daf1e54784df);



        marker_e4d2cb2e61b07467a5a581efab19bdc3.bindPopup(popup_332aa55d5d718d8e43790b9f5d61984c)
        ;




            var marker_3f50b6cddcfb867e36d85627f2113373 = L.marker(
                [37.7749912944366, -122.437799703468],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_9bf9b7d990227b931fa397a9c56b79cf = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_ad6977f4df7a9cb9b1895e673bc89d3b = $(`&lt;div id=&quot;html_ad6977f4df7a9cb9b1895e673bc89d3b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_9bf9b7d990227b931fa397a9c56b79cf.setContent(html_ad6977f4df7a9cb9b1895e673bc89d3b);



        marker_3f50b6cddcfb867e36d85627f2113373.bindPopup(popup_9bf9b7d990227b931fa397a9c56b79cf)
        ;




            var marker_084c5140e16749cfa695ee8dd062af1b = L.marker(
                [37.7770902743669, -122.421332684633],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_374567d64987d8561e5d0cfabcbd2b5a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_72ac3b49d9af7f4964bde1ff3b1cd779 = $(`&lt;div id=&quot;html_72ac3b49d9af7f4964bde1ff3b1cd779&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;MISSING PERSON&lt;/div&gt;`)[0];
                popup_374567d64987d8561e5d0cfabcbd2b5a.setContent(html_72ac3b49d9af7f4964bde1ff3b1cd779);



        marker_084c5140e16749cfa695ee8dd062af1b.bindPopup(popup_374567d64987d8561e5d0cfabcbd2b5a)
        ;




            var marker_c744b1f36e542412ee5db72efb1385b8 = L.marker(
                [37.7770902743669, -122.421332684633],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_2bb3898f1350c23823c7c8e9d70368b8 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_70722722ff99dd5eee7aa0bd22905d7e = $(`&lt;div id=&quot;html_70722722ff99dd5eee7aa0bd22905d7e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;MISSING PERSON&lt;/div&gt;`)[0];
                popup_2bb3898f1350c23823c7c8e9d70368b8.setContent(html_70722722ff99dd5eee7aa0bd22905d7e);



        marker_c744b1f36e542412ee5db72efb1385b8.bindPopup(popup_2bb3898f1350c23823c7c8e9d70368b8)
        ;




            var marker_7903ca96a45402eab72c7461f12bae27 = L.marker(
                [37.7822458223917, -122.446612978839],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_1508b1b6af6b2788b14bd386676de627 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_468a3809c2795c255fcf68879dee8c34 = $(`&lt;div id=&quot;html_468a3809c2795c255fcf68879dee8c34&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_1508b1b6af6b2788b14bd386676de627.setContent(html_468a3809c2795c255fcf68879dee8c34);



        marker_7903ca96a45402eab72c7461f12bae27.bindPopup(popup_1508b1b6af6b2788b14bd386676de627)
        ;




            var marker_08378ec321c3f6796e5d3444f747dffb = L.marker(
                [37.7300379995128, -122.404594140634],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_1f66b11a8843bcf7145f691e6a25039e = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_c95606a705ec67aba9ee74b4e7dfb599 = $(`&lt;div id=&quot;html_c95606a705ec67aba9ee74b4e7dfb599&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_1f66b11a8843bcf7145f691e6a25039e.setContent(html_c95606a705ec67aba9ee74b4e7dfb599);



        marker_08378ec321c3f6796e5d3444f747dffb.bindPopup(popup_1f66b11a8843bcf7145f691e6a25039e)
        ;




            var marker_629968cb399fb093f1d911dcb966751d = L.marker(
                [37.7953338267436, -122.397373740066],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_8d0eaa9a9a3cf79004958bddf01fb96f = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_a969ee9b66d28df6622507f2d7cdc014 = $(`&lt;div id=&quot;html_a969ee9b66d28df6622507f2d7cdc014&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_8d0eaa9a9a3cf79004958bddf01fb96f.setContent(html_a969ee9b66d28df6622507f2d7cdc014);



        marker_629968cb399fb093f1d911dcb966751d.bindPopup(popup_8d0eaa9a9a3cf79004958bddf01fb96f)
        ;




            var marker_fc1c29eb91038c3337e9980d89bc1b3f = L.marker(
                [37.7875158741623, -122.407434989523],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_daea3cbd7dfa95c70e5cc2126461c840 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_7848cff7d709e13ff9725bf254d6f128 = $(`&lt;div id=&quot;html_7848cff7d709e13ff9725bf254d6f128&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_daea3cbd7dfa95c70e5cc2126461c840.setContent(html_7848cff7d709e13ff9725bf254d6f128);



        marker_fc1c29eb91038c3337e9980d89bc1b3f.bindPopup(popup_daea3cbd7dfa95c70e5cc2126461c840)
        ;




            var marker_ecad77739ee1ce9d71cb4ceae4626f59 = L.marker(
                [37.7785233776032, -122.403464080033],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_d38aeef45ef13d9ba19c18d3d86f7180 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_e51c273866433bc728a8d67b0b0818db = $(`&lt;div id=&quot;html_e51c273866433bc728a8d67b0b0818db&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;PROSTITUTION&lt;/div&gt;`)[0];
                popup_d38aeef45ef13d9ba19c18d3d86f7180.setContent(html_e51c273866433bc728a8d67b0b0818db);



        marker_ecad77739ee1ce9d71cb4ceae4626f59.bindPopup(popup_d38aeef45ef13d9ba19c18d3d86f7180)
        ;




            var marker_77121ef130d1c58a89ca16a8c55d9cdf = L.marker(
                [37.7785233776032, -122.403464080033],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_e7d0a5cd74e6e0baa412add5e523b88d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_ee66240a9a15f8b312c772d0c17fc151 = $(`&lt;div id=&quot;html_ee66240a9a15f8b312c772d0c17fc151&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_e7d0a5cd74e6e0baa412add5e523b88d.setContent(html_ee66240a9a15f8b312c772d0c17fc151);



        marker_77121ef130d1c58a89ca16a8c55d9cdf.bindPopup(popup_e7d0a5cd74e6e0baa412add5e523b88d)
        ;




            var marker_4edc40bb1a1b637bca46cf4459ab531d = L.marker(
                [37.773291806903, -122.436614181331],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_823979dfd29a777200261f4907be574d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_77c71af0bdbfaa4f0fdec840edb372aa = $(`&lt;div id=&quot;html_77c71af0bdbfaa4f0fdec840edb372aa&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_823979dfd29a777200261f4907be574d.setContent(html_77c71af0bdbfaa4f0fdec840edb372aa);



        marker_4edc40bb1a1b637bca46cf4459ab531d.bindPopup(popup_823979dfd29a777200261f4907be574d)
        ;




            var marker_06b65179cbe41ec434e04203840f31fe = L.marker(
                [37.780527578509, -122.396849015172],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_5fd7ab977d3ad9af841b042842c66f87 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_7a0a0fd8899449c383837dbdbd89f50a = $(`&lt;div id=&quot;html_7a0a0fd8899449c383837dbdbd89f50a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;DRUG/NARCOTIC&lt;/div&gt;`)[0];
                popup_5fd7ab977d3ad9af841b042842c66f87.setContent(html_7a0a0fd8899449c383837dbdbd89f50a);



        marker_06b65179cbe41ec434e04203840f31fe.bindPopup(popup_5fd7ab977d3ad9af841b042842c66f87)
        ;




            var marker_2d0944f0d9807247a2030882c85c75c3 = L.marker(
                [37.780527578509, -122.396849015172],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_4e39f45b25f16152955cc88ac64cd74c = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_96b58ab45c4f23fef357252b13d109f5 = $(`&lt;div id=&quot;html_96b58ab45c4f23fef357252b13d109f5&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;WARRANTS&lt;/div&gt;`)[0];
                popup_4e39f45b25f16152955cc88ac64cd74c.setContent(html_96b58ab45c4f23fef357252b13d109f5);



        marker_2d0944f0d9807247a2030882c85c75c3.bindPopup(popup_4e39f45b25f16152955cc88ac64cd74c)
        ;




            var marker_f0297535d1eb2c70aae8a745832cc65f = L.marker(
                [37.7284180706602, -122.450000790445],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_62240012eb44ece1a142107d9afe4290 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_3823d5648a8c6b539f73eb01c363c7d6 = $(`&lt;div id=&quot;html_3823d5648a8c6b539f73eb01c363c7d6&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_62240012eb44ece1a142107d9afe4290.setContent(html_3823d5648a8c6b539f73eb01c363c7d6);



        marker_f0297535d1eb2c70aae8a745832cc65f.bindPopup(popup_62240012eb44ece1a142107d9afe4290)
        ;




            var marker_239a704990733a5379f07937b5acbcc7 = L.marker(
                [37.7292114647359, -122.400834283031],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_26aed6850ad7a81b58772d93591a3a7d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_d3b021f2d6c991505900caf1eb028fd8 = $(`&lt;div id=&quot;html_d3b021f2d6c991505900caf1eb028fd8&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_26aed6850ad7a81b58772d93591a3a7d.setContent(html_d3b021f2d6c991505900caf1eb028fd8);



        marker_239a704990733a5379f07937b5acbcc7.bindPopup(popup_26aed6850ad7a81b58772d93591a3a7d)
        ;




            var marker_74e2015b677986002e61a5067129be4c = L.marker(
                [37.7880065324392, -122.399802145799],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_233f2bc1495e05b16375ca2ab2003e41 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_b565ff77337a7b97e5d636ccc4465f4c = $(`&lt;div id=&quot;html_b565ff77337a7b97e5d636ccc4465f4c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_233f2bc1495e05b16375ca2ab2003e41.setContent(html_b565ff77337a7b97e5d636ccc4465f4c);



        marker_74e2015b677986002e61a5067129be4c.bindPopup(popup_233f2bc1495e05b16375ca2ab2003e41)
        ;




            var marker_6c42ef0438e1f14a4c1bd40b5a3bdb75 = L.marker(
                [37.7239748241609, -122.3949284758],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_3fcec76e72400b844e87fe67d33770bd = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_595445f5e273810ef1a234de81140bcf = $(`&lt;div id=&quot;html_595445f5e273810ef1a234de81140bcf&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;SECONDARY CODES&lt;/div&gt;`)[0];
                popup_3fcec76e72400b844e87fe67d33770bd.setContent(html_595445f5e273810ef1a234de81140bcf);



        marker_6c42ef0438e1f14a4c1bd40b5a3bdb75.bindPopup(popup_3fcec76e72400b844e87fe67d33770bd)
        ;




            var marker_df1023a472ed1d3f9e1078dfb57a23aa = L.marker(
                [37.7239748241609, -122.3949284758],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_f634c28f552d973fa15df345b3186334 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_0e31f2139fef7747394ad3236a03cd06 = $(`&lt;div id=&quot;html_0e31f2139fef7747394ad3236a03cd06&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;SUSPICIOUS OCC&lt;/div&gt;`)[0];
                popup_f634c28f552d973fa15df345b3186334.setContent(html_0e31f2139fef7747394ad3236a03cd06);



        marker_df1023a472ed1d3f9e1078dfb57a23aa.bindPopup(popup_f634c28f552d973fa15df345b3186334)
        ;




            var marker_45a3d7be1e07525651a2261108a99e95 = L.marker(
                [37.7239748241609, -122.3949284758],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_f49123fcc390482f2b6ddb3ca899193d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_355a6bdf2a8bfd645538fe337184e34f = $(`&lt;div id=&quot;html_355a6bdf2a8bfd645538fe337184e34f&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_f49123fcc390482f2b6ddb3ca899193d.setContent(html_355a6bdf2a8bfd645538fe337184e34f);



        marker_45a3d7be1e07525651a2261108a99e95.bindPopup(popup_f49123fcc390482f2b6ddb3ca899193d)
        ;




            var marker_9654bdb10021f2b5be00f4efe60a59ea = L.marker(
                [37.7883235449904, -122.41185703254],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_3da9b18d1b5f0d457b3119d2057e9cb7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_8b3479de272282fdf3a960834af0f273 = $(`&lt;div id=&quot;html_8b3479de272282fdf3a960834af0f273&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_3da9b18d1b5f0d457b3119d2057e9cb7.setContent(html_8b3479de272282fdf3a960834af0f273);



        marker_9654bdb10021f2b5be00f4efe60a59ea.bindPopup(popup_3da9b18d1b5f0d457b3119d2057e9cb7)
        ;




            var marker_e15df7bf9e07b29120355a1445c65de6 = L.marker(
                [37.7559977339856, -122.409435617106],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_832e447620fa3c30a88ef0ab72387154 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_a953c9bbc2c5249a4d654c8216a43495 = $(`&lt;div id=&quot;html_a953c9bbc2c5249a4d654c8216a43495&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_832e447620fa3c30a88ef0ab72387154.setContent(html_a953c9bbc2c5249a4d654c8216a43495);



        marker_e15df7bf9e07b29120355a1445c65de6.bindPopup(popup_832e447620fa3c30a88ef0ab72387154)
        ;




            var marker_789b31b8a80565f128609af6da02241b = L.marker(
                [37.7870798144443, -122.425883358148],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_cbf9a128acb44bd73d649891e5cecf3d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_0a971d831cc001bff71b2e3c56c48661 = $(`&lt;div id=&quot;html_0a971d831cc001bff71b2e3c56c48661&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_cbf9a128acb44bd73d649891e5cecf3d.setContent(html_0a971d831cc001bff71b2e3c56c48661);



        marker_789b31b8a80565f128609af6da02241b.bindPopup(popup_cbf9a128acb44bd73d649891e5cecf3d)
        ;




            var marker_3b590fcfccb2aa8471c3d24efc722884 = L.marker(
                [37.7360374466862, -122.415126543001],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_1b3311aa6cb058d34f1c5a693285eef9 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_42f0f647d2fcd51141233fcf95138876 = $(`&lt;div id=&quot;html_42f0f647d2fcd51141233fcf95138876&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_1b3311aa6cb058d34f1c5a693285eef9.setContent(html_42f0f647d2fcd51141233fcf95138876);



        marker_3b590fcfccb2aa8471c3d24efc722884.bindPopup(popup_1b3311aa6cb058d34f1c5a693285eef9)
        ;




            var marker_55ab93ceed62d647d53782fb64d66fbf = L.marker(
                [37.712767884821, -122.431928011089],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_55921cad3c55f7a66da50851b0bd7642 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_449bc7a12cc6ec3491597327a6c8b81d = $(`&lt;div id=&quot;html_449bc7a12cc6ec3491597327a6c8b81d&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_55921cad3c55f7a66da50851b0bd7642.setContent(html_449bc7a12cc6ec3491597327a6c8b81d);



        marker_55ab93ceed62d647d53782fb64d66fbf.bindPopup(popup_55921cad3c55f7a66da50851b0bd7642)
        ;




            var marker_7f8fbcd14d5a3f989ad1be85b3ba395c = L.marker(
                [37.7895710255863, -122.402163713618],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_b4cdca6d607dd55e8fcfbd02575a81d7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_8bf9f4c5d48967513402180621d2501c = $(`&lt;div id=&quot;html_8bf9f4c5d48967513402180621d2501c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;DRUNKENNESS&lt;/div&gt;`)[0];
                popup_b4cdca6d607dd55e8fcfbd02575a81d7.setContent(html_8bf9f4c5d48967513402180621d2501c);



        marker_7f8fbcd14d5a3f989ad1be85b3ba395c.bindPopup(popup_b4cdca6d607dd55e8fcfbd02575a81d7)
        ;




            var marker_e30d614bf5a5529ddbc4f1f6cafcda08 = L.marker(
                [37.7307429169559, -122.429306728376],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_4e554aeef12c950ec77a3f7127c9ec3a = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_553ba78263f96f434a8d328d00fd69b0 = $(`&lt;div id=&quot;html_553ba78263f96f434a8d328d00fd69b0&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_4e554aeef12c950ec77a3f7127c9ec3a.setContent(html_553ba78263f96f434a8d328d00fd69b0);



        marker_e30d614bf5a5529ddbc4f1f6cafcda08.bindPopup(popup_4e554aeef12c950ec77a3f7127c9ec3a)
        ;




            var marker_6cc0cc746be57d64b68454786b3f98f7 = L.marker(
                [37.7838365565348, -122.413790972781],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_3b989ac886b3dccd928a25c4687a9b08 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_463de80b9021c2ede206b4d4b1bb320c = $(`&lt;div id=&quot;html_463de80b9021c2ede206b4d4b1bb320c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VANDALISM&lt;/div&gt;`)[0];
                popup_3b989ac886b3dccd928a25c4687a9b08.setContent(html_463de80b9021c2ede206b4d4b1bb320c);



        marker_6cc0cc746be57d64b68454786b3f98f7.bindPopup(popup_3b989ac886b3dccd928a25c4687a9b08)
        ;




            var marker_c4cad3223f576ba3e015d8c517da5ed2 = L.marker(
                [37.7307429169559, -122.429306728376],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_ead5bc98bfaf4bdb39673067459e7396 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_35ab3080a71a2dafcf8145e530df631e = $(`&lt;div id=&quot;html_35ab3080a71a2dafcf8145e530df631e&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_ead5bc98bfaf4bdb39673067459e7396.setContent(html_35ab3080a71a2dafcf8145e530df631e);



        marker_c4cad3223f576ba3e015d8c517da5ed2.bindPopup(popup_ead5bc98bfaf4bdb39673067459e7396)
        ;




            var marker_e6427c2ef919128dff5741e74a13fbd9 = L.marker(
                [37.7373623605213, -122.422067184937],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_14844471dbb87c57b7ed9ddc754a30d5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_45e8f81b6d756c15cfa98e374f839552 = $(`&lt;div id=&quot;html_45e8f81b6d756c15cfa98e374f839552&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;SECONDARY CODES&lt;/div&gt;`)[0];
                popup_14844471dbb87c57b7ed9ddc754a30d5.setContent(html_45e8f81b6d756c15cfa98e374f839552);



        marker_e6427c2ef919128dff5741e74a13fbd9.bindPopup(popup_14844471dbb87c57b7ed9ddc754a30d5)
        ;




            var marker_1e7403654967a583048a0a48c09969b1 = L.marker(
                [37.7373623605213, -122.422067184937],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_1e83562101502704c82c1c9c02b16838 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_b85d6a6fc1ad2906ac242919c6dc2402 = $(`&lt;div id=&quot;html_b85d6a6fc1ad2906ac242919c6dc2402&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;VANDALISM&lt;/div&gt;`)[0];
                popup_1e83562101502704c82c1c9c02b16838.setContent(html_b85d6a6fc1ad2906ac242919c6dc2402);



        marker_1e7403654967a583048a0a48c09969b1.bindPopup(popup_1e83562101502704c82c1c9c02b16838)
        ;




            var marker_21576ef632afeceb2e5f8aa071c653bf = L.marker(
                [37.7859988323798, -122.411747371924],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_923a0844d6410fca513df29543fb89c7 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_f62395fda4d9f265a0c58d16047fb128 = $(`&lt;div id=&quot;html_f62395fda4d9f265a0c58d16047fb128&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;SUSPICIOUS OCC&lt;/div&gt;`)[0];
                popup_923a0844d6410fca513df29543fb89c7.setContent(html_f62395fda4d9f265a0c58d16047fb128);



        marker_21576ef632afeceb2e5f8aa071c653bf.bindPopup(popup_923a0844d6410fca513df29543fb89c7)
        ;




            var marker_e63b42ccefab975c805b47ebad9dd57a = L.marker(
                [37.7633758058059, -122.420434724553],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_db57c7b983699b49297bad3a8a4237d6 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_5f8458939ce1731307211f523078d6f9 = $(`&lt;div id=&quot;html_5f8458939ce1731307211f523078d6f9&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_db57c7b983699b49297bad3a8a4237d6.setContent(html_5f8458939ce1731307211f523078d6f9);



        marker_e63b42ccefab975c805b47ebad9dd57a.bindPopup(popup_db57c7b983699b49297bad3a8a4237d6)
        ;




            var marker_7d8f39f045acab920e425a2356bbff64 = L.marker(
                [37.7850226622786, -122.411987643595],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_7f55ba98beb918080928c33707a493e5 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_8be5274524f27e7a4c7d011a05971881 = $(`&lt;div id=&quot;html_8be5274524f27e7a4c7d011a05971881&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_7f55ba98beb918080928c33707a493e5.setContent(html_8be5274524f27e7a4c7d011a05971881);



        marker_7d8f39f045acab920e425a2356bbff64.bindPopup(popup_7f55ba98beb918080928c33707a493e5)
        ;




            var marker_96e06720e4b3fb8dceecaf7252f8fc09 = L.marker(
                [37.7746206491065, -122.500380427915],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_4ef605b67369fd09cc9c644932497663 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_27548e7b3c9f36dd6194ddddd80a60b6 = $(`&lt;div id=&quot;html_27548e7b3c9f36dd6194ddddd80a60b6&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_4ef605b67369fd09cc9c644932497663.setContent(html_27548e7b3c9f36dd6194ddddd80a60b6);



        marker_96e06720e4b3fb8dceecaf7252f8fc09.bindPopup(popup_4ef605b67369fd09cc9c644932497663)
        ;




            var marker_bf015554d9cd5526f1603400bdb3f339 = L.marker(
                [37.7751918267217, -122.466558780683],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_5e906a32d96bda71a9da330015c092df = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_b5c49d90dd08cbe8faec612e93ff945b = $(`&lt;div id=&quot;html_b5c49d90dd08cbe8faec612e93ff945b&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;ROBBERY&lt;/div&gt;`)[0];
                popup_5e906a32d96bda71a9da330015c092df.setContent(html_b5c49d90dd08cbe8faec612e93ff945b);



        marker_bf015554d9cd5526f1603400bdb3f339.bindPopup(popup_5e906a32d96bda71a9da330015c092df)
        ;




            var marker_d52c6e9ea8b37139acba553796213ec9 = L.marker(
                [37.7490841729028, -122.486925960114],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_2dba708b7f187764d1fb376831d1c7b0 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_5a555f0864954f2123109876fe48d80c = $(`&lt;div id=&quot;html_5a555f0864954f2123109876fe48d80c&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;OTHER OFFENSES&lt;/div&gt;`)[0];
                popup_2dba708b7f187764d1fb376831d1c7b0.setContent(html_5a555f0864954f2123109876fe48d80c);



        marker_d52c6e9ea8b37139acba553796213ec9.bindPopup(popup_2dba708b7f187764d1fb376831d1c7b0)
        ;




            var marker_c8cdca9e4c9d1e6411899ddac836937a = L.marker(
                [37.7685360123583, -122.41561633832],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_f6a7b46a19205f562ebfe22c25823133 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_859dd9080b89e7ff592dc29de25ea7ce = $(`&lt;div id=&quot;html_859dd9080b89e7ff592dc29de25ea7ce&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;NON-CRIMINAL&lt;/div&gt;`)[0];
                popup_f6a7b46a19205f562ebfe22c25823133.setContent(html_859dd9080b89e7ff592dc29de25ea7ce);



        marker_c8cdca9e4c9d1e6411899ddac836937a.bindPopup(popup_f6a7b46a19205f562ebfe22c25823133)
        ;




            var marker_26dce3d3780a6b3b23d97ac520cfffbb = L.marker(
                [37.7644297714074, -122.449751652563],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_2cfeb82ee70a6a5a6c6451558516e254 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_d793e48a6a24ce80f03aed3368fe0b92 = $(`&lt;div id=&quot;html_d793e48a6a24ce80f03aed3368fe0b92&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;BURGLARY&lt;/div&gt;`)[0];
                popup_2cfeb82ee70a6a5a6c6451558516e254.setContent(html_d793e48a6a24ce80f03aed3368fe0b92);



        marker_26dce3d3780a6b3b23d97ac520cfffbb.bindPopup(popup_2cfeb82ee70a6a5a6c6451558516e254)
        ;




            var marker_3273807ff1cb2905eb6ff6ddfea47de5 = L.marker(
                [37.7644297714074, -122.449751652563],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_12503e6359c96d14183e1548160e8ee4 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_fa3d7124840e69226b72046f7b0c3d35 = $(`&lt;div id=&quot;html_fa3d7124840e69226b72046f7b0c3d35&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_12503e6359c96d14183e1548160e8ee4.setContent(html_fa3d7124840e69226b72046f7b0c3d35);



        marker_3273807ff1cb2905eb6ff6ddfea47de5.bindPopup(popup_12503e6359c96d14183e1548160e8ee4)
        ;




            var marker_e6c340c3bf85c8db3f617b91ddf7dcb5 = L.marker(
                [37.7352681469084, -122.472715759631],
                {}
            ).addTo(marker_cluster_97e67e2f887714098340aa061e17ed56);


        var popup_8c7a462c40a3cbfb81adddca0c280499 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});



                var html_2d2f7e2bba9166570628cc265cf2c642 = $(`&lt;div id=&quot;html_2d2f7e2bba9166570628cc265cf2c642&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;LARCENY/THEFT&lt;/div&gt;`)[0];
                popup_8c7a462c40a3cbfb81adddca0c280499.setContent(html_2d2f7e2bba9166570628cc265cf2c642);



        marker_e6c340c3bf85c8db3f617b91ddf7dcb5.bindPopup(popup_8c7a462c40a3cbfb81adddca0c280499)
        ;



&lt;/script&gt;
&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



Notice how when you zoom out all the way, all markers are grouped into one cluster, *the global cluster*, of 100 markers or crimes, which is the total number of crimes in our dataframe. Once you start zooming in, the *global cluster* will start breaking up into smaller clusters. Zooming in all the way will result in individual markers.


# Choropleth Maps <a id="8"></a>

A `Choropleth` map is a thematic map in which areas are shaded or patterned in proportion to the measurement of the statistical variable being displayed on the map, such as population density or per-capita income. The choropleth map provides an easy way to visualize how a measurement varies across a geographic area, or it shows the level of variability within a region. Below is a `Choropleth` map of the US depicting the population by square mile per state.

<img src = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/labs/Module%205/images/2000_census_population_density_map_by_state.png" width = 600> 

