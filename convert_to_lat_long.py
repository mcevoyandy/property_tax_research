import geopy
import time

lat_long_file = open('lat_long_coords.txt', 'w')

with open('property_tax_addresses.txt', 'r') as address_list:
    addresses = [line.rstrip().split(',') for line in address_list]

# Use Google API, free version noted with geopy getting started comes up with a lot of errors
google_api_key = None
with open('my_api_key.txt', 'r') as api_key_file:
    google_api_key = api_key_file.readline()

print(google_api_key)


locator = geopy.geocoders.GoogleV3(google_api_key)
count = 0
for address in addresses:
    id = address[0]
    street = f'{address[1]}, {address[2]}, {address[3]}'

    try:
        location = locator.geocode(street)
        print(f'{count}/{len(addresses)}: {location.latitude}, {location.longitude}')
        lat_long_file.write(f'{id}, {location.latitude}, {location.longitude}\n')
    except:
        print(f'{count}/{len(addresses)}: FAILED: {id}, {street}')
        lat_long_file.write(f'{id}, {street}\n')

    # TODO: check distance from home address, some addresses aren't found in
    count = count + 1

    # Sleep so server doesn't block us
    time.sleep(2)

lat_long_file.close()
address_list.close()
