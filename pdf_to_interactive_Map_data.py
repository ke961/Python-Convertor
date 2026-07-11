from pypdf import PdfReader
from geopy.geocoders import Nominatim
import re
import time 





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

