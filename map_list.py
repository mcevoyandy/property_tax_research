import folium
import geopy.distance

MAX_DISTANCE = 2.0  # miles

with open('my_location.txt') as loc_file:
    my_loc = [line.rstrip().split(',') for line in loc_file]
my_coords = (float(my_loc[0][0]), float(my_loc[0][1]))
print(my_coords)

with open('lat_long_coords.txt') as coords_file:
    coords_list = [line.rstrip().split(',') for line in coords_file]

results_file = open('my_comps.txt', 'w')

# Center map on Hays County coords returned by Google
my_map = folium.Map(location=[30.1235632, -98.0321392], zoom_start=12, tiles="Stamen Terrain")

for coords in coords_list:
    latitude = coords[1]
    longitude = coords[2]

    icon_color = "red"
    is_comparable = False
    dist = geopy.distance.geodesic(my_coords, (latitude, longitude)).miles
    if dist < MAX_DISTANCE:
        icon_color = "green"
        is_comparable = True

    folium.Marker(
        location=[latitude, longitude],
        popup=f'{coords[0]}',
        tooltip=f'{coords[0]}',
        icon=folium.Icon(color=icon_color)
    ).add_to(my_map)

    print(f'{coords[0]}, {is_comparable}')
    results_file.write(f'{coords[0]}, {is_comparable}\n')

my_map.save('property_tax_map.html')
results_file.close()
