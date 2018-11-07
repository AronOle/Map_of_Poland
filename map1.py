import folium
import pandas

data = pandas.read_csv('citys2.txt')
lat = list(data['Latitude'])
lon = list(data['Longitude'])
name = list(data['Name'])

data2 = pandas.read_csv('cathedrals.txt')
lat2 = list(data2['Latitude'])
lon2 = list(data2['Longitude'])
name2 = list(data2['Name'])

map = folium.Map(location = [51.7681, 19.508],zoom_start=6, tiles="OpenStreetMap")

fg = folium.FeatureGroup(name='Towns Worth Visiting')

for lt, ln, ne in zip(lat, lon, name):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(ne), icon=folium.Icon(color='red')))


fg2 = folium.FeatureGroup(name='Cathedral Worth Visiting')

for lt2, ln2, ne2 in zip(lat2, lon2, name2):
    fg2.add_child(folium.Marker(location=[lt2, ln2], popup=str(ne2), icon=folium.Icon(color='black')))


map.add_child(fg)
map.add_child(fg2)
map.add_child(folium.LayerControl())
map.save('map1.html')
