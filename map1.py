import folium
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[38.58, -99.09], [36.58, -97.09]]:
    fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='red')))


map.add_child(fg) #allows to add layer controll feature later on by creating feature group and then mapping add_child with fg

map.save("Map1.html")