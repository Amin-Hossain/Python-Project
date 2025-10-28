import phonenumbers as ph
import opencage
import folium

from opencage.geocoder import OpenCageGeocode
from phonenumbers import geocoder
from phonenumbers import carrier


number=input("Enter the target number: ")
pep_num=ph.parse(number)
location=geocoder.description_for_number(pep_num,"en")
print(location)
print(carrier.name_for_number(pep_num,"en"))
key='Your Key'

geocoder=OpenCageGeocode(key)
query = str(location)
result=geocoder.geocode(query)
lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']
print(lat,lng)

myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)
myMap.save("my_location.html")
