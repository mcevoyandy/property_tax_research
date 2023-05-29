import folium

with open('lat_long_coords.txt') as coords_file:
    coords_list = [line.rstrip().split(',') for line in coords_file]

# Center map on Hays County coords returned by Google
my_map = folium.Map(location=[30.1235632, -98.0321392], zoom_start=12, tiles="Stamen Terrain")

for coords in coords_list:
    latitude = coords[1]
    longitude = coords[2]

    folium.Marker(
        location=[latitude, longitude],
        popup=f'{coords[0]}',
        tooltip=f'{coords[0]}'
    ).add_to(my_map)


my_map.save('property_tax_map.html')
