from pypdf import PdfReader

import re

reader = PdfReader("file.pdf")
text= reader.pages[0].extract_text()
places= re.findall(r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b', text)

print(places)