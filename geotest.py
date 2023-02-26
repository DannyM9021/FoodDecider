# import geocoder
# g = geocoder.geonames('Mountain View, CA', maxRows=5)
# print(len(g))
# for result in g:
#   print(result.address, result.latlng)

import os  
import socket 
import geocoder

# # IP = socket.gethostbyname(hostname)
# # print(IP)
# print(os.system('ipconfig'))


# # g = geocoder.google('Long Beach, CA')
# # print(g.latlng)
# # print(g.city)

import requests
import json

def get():
    endpoint = 'https://ipinfo.io/json'
    response = requests.get(endpoint, verify = True)

    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'
        exit()

    data = response.json()

    return data['ip']

#get my ip
my_ip = get()

#print my ip
print(my_ip)

g = geocoder.ip(my_ip)
g = geocoder.ip('me')
print(g.latlng)
print(g.city)