import csv

def get_mac_address_map():
    file_handler = open('./assets/officers.csv', 'rb')
    reader = csv.reader(file_handler)

    mac_address_map = {}

    for row in reader:
        mac_address_map[row[0]] = row[1]

    return mac_address_map
