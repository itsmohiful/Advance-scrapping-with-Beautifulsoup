import re

import requests
from bs4 import BeautifulSoup

url = "https://www.mobiledokan.com/oppo/oppo-f21-pro-5g/"

url = "https://www.newegg.com/gigabyte-geforce-rtx-3070-ti-gv-n307tgaming-oc-8g/p/N82E16814932443?Item=N82E16814932443&cm_sp=Homepage_SS-_-P1_14-932-443-_-06212022"

result = requests.get(url)

soup = BeautifulSoup(result.text, "html.parser")
#print(soup.prettify())

tag = soup.find("p")
tag['class'] = 'khamokha'

# print(tag.attrs)

tag = soup.find_all(["p", "div", "li"])

tag = soup.find_all(["td"], text="Time:")


tag = soup.find_all(class_="medium-text")

tag = soup.find_all(text="$")
tag = soup.find_all(text=re.compile("\$.*"))
print(tag)
