import re
import requests
import time

with open('property_id_list.txt') as property_list_file:
    property_list = [line.rstrip() for line in property_list_file]

main_url = 'https://esearch.hayscad.com//Property/View/'

address_file = open('property_tax_addresses.txt', 'w')

count = 0
for property in property_list:
    # Create full url & find parcel address in returned html
    url = main_url + property
    r = requests.get(url)
    pattern = re.compile('<tr><th>Address:</th><td>(.*)</td></tr>')
    result = pattern.search(r.text)

    # Write results to file with parcel ID
    output = property + ", " + result.group(1)
    print(f'{count}/{len(property_list)} : {url} - {output}')
    address_file.write(output + '\n')
    count = count + 1

    # Sleep so server doesn't block us for too many connections
    time.sleep(2)

address_file.close()
