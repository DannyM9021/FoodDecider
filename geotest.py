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



import requests
import json
import googlemaps

APIKEY = "AIzaSyCREubepe3S9zdisc8Lt65VzpNdseuQKmo"

def findPlaces(loc=("33.7939","-118.1192"),radius=4000, pagetoken = None):
   lat, lng = loc
   type = "restaurant"
   url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type={type}&key={APIKEY}{pagetoken}".format(lat = lat, lng = lng, radius = radius, type = type,APIKEY = APIKEY, pagetoken = "&pagetoken="+pagetoken if pagetoken else "")
   print(url)
   response = requests.get(url)
   res = json.loads(response.text)
   # print(res)
   print("here results ---->>> ", len(res["results"]))

   for result in res["results"]:
      info = ";".join(map(str,[result["name"],result["geometry"]["location"]["lat"],result["geometry"]["location"]["lng"],result.get("rating",0),result["place_id"]]))
      print(info)

   for result in res["results"]:
      # https://developers.google.com/maps/documentation/places/web-service/search-nearby#AddressComponent
      # go to the link above and look at attributes table, if want more, add it into my_fields 
      my_fields = ['name','formatted_phone_number','type','formatted_address']
      place_detail = (googlemaps.Client(key = APIKEY)).place(place_id = result["place_id"],fields = my_fields)
      print(place_detail)

       
   pagetoken = res.get("next_page_token",None)

   print("here -->> ", pagetoken)

   return pagetoken

# pagetoken = "CpQFhwIAADQWOcVI1wll-B869Z24El48rXw18gKoab_keD65V18zFEvPjKIfrS79Pc_vXJcZQtOuF0RObQG20ph-GE3ssP3k1fu8zsYbw5g3UPbSjAvQLdXkdD1qAWztXj7hc5Kxc4pYRyGM1_ljVOHg3Py_zSlYscnoNjCvRua2MDQgusCsEquNqGREFdvhjDkbeMhEFYxHucTnIn96OxIJEpamePTHsBooYyPBaa_ejGZ_C99QeDjpSkSKBgEe3aL1uWKlYhsGKh7biQUR5rKsKPodwccLIrW8Gr5tag3NH0sLPExHHvqzlpkj--KIuydTVjPH7u2zHxmPByServ2S5xjXYUBRr-ly3e1xPsVMhZZH9TxfttCIHLscBvpvCswIfaGYdl3bEzsrFISfpp0rpKtlp9gWGY7Tbk2n6s3etCHQEHn2qmM8bsJwkZV81pUWN0j9C9RX-ywOyIKY2yp1w_Iq1mRwOwY4mckbicOoooHiV6JER4xe7Kizw9hbXOnezn_NMk15TLwRoXlfL1s73uwogo-VWE8c-V1HqRpWQSyudRhLwhOEclrICXIdxICOgTgYO1z57xCEerw3QUL_7MPDrlbbh_AlX8I6Jfe8IhQ1Fkqu_njatm6aBTjkp2CSqlvZJpI_Lrv330VcyFEqBkGn7NJew3I9xofSrBaXFa8ABi6DXQm6-yC32OEyf7GHNXINjT1IB0yh6KR6c0qzaqiqOzKcuuai9XqEMQNNKyi6EuhzH5TP9YA56N3JhnXRFhs2aWHZhLlieVI6_uqzpZSgYjUem8aQrMTlmHw0kIYU8I-Ca041C4Zm2gMezwygRrhzsOoAmbmu96nft0KuIWTB3A_xGVKYQ2qjb2KRM7nsglnSEhDoNs8EhvuIm0FQs30YSCp5GhRO3b3Tn5rsLuwiWgu8hwEGhL0S1A"
pagetoken = None

while True:
     pagetoken = findPlaces(pagetoken=pagetoken)
     import time
     time.sleep(5)

     if not pagetoken:
         break


