from pypdf import PdfReader
from geopy.geocoders import Nominatim
import re
import time 
import folium





#Read PDF
reader = PdfReader("korea_places.pdf")



text= ""
for page in reader.pages:
    page_text= page.extract_text ()
    if page_text:
        text+= page_text+"\n"


#Extract place names using regex
places= re.findall(r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b', text)
places= list(set(places))  # Remove duplicates
print ("Places extracted from PDF:")
print(places)


#Geocoder
geolocation=Nominatim(user_agent="korea_map")

#Creat Map centered on south korea

m = folium.Map (location=[36.5, 127.5], zoom_start=7)

for place in places:
    try:
        location= geolocation.geocode(f"{place}, South Korea")
        


        if location:
            print(f"Geocoded {place}: {location.latitude}, {location.longitude}")
            folium.Marker([location.latitude, location.longitude], tooltip=place, popup=place).add_to(m)



        time.sleep(1)  # To avoid hitting the rate limit of the geocoding service
    except Exception as e:
        print(f"Error geocoding {place}: {e}")



m.save("korea_places_map.html")
print("Map saved as korea_places_map.html")

