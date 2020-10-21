import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    # print(type(el))
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el), icon=folium.Icon(color='red')))


map.add_child(fg) #allows to add layer controll feature later on by creating feature group and then mapping add_child with fg

map.save("Map1.html")