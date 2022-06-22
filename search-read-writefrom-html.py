import re

import requests
from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f,"html.parser")


tags = doc.find_all("input", type="text")
for tag in tags:
    #print("all attributes: ",tag.attrs)
    tag['placeholder'] = "i changed placeholder"
	

with open("changed-placeholder.html", "w") as file:
    file.write(str(doc))


