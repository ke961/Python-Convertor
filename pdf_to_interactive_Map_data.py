from pypdf import PdfReader

import re

reader = PdfReader("korea_places.pdf")
text= reader.pages[0].extract_text()
places= re.findall(r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b', text)

print(places)

for p in set(places):
    print({"location": p})