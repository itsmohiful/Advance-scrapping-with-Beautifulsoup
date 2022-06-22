import re

import requests
from bs4 import BeautifulSoup

url = "https://www.newegg.com/gigabyte-geforce-rtx-3070-ti-gv-n307tgaming-oc-8g/p/N82E16814932443?Item=N82E16814932443&cm_sp=Homepage_SS-_-P1_14-932-443-_-06212022"

#url = "https://www.ebay.com/itm/323889652331"

result = requests.get(url)
#print(result.text)

soup = BeautifulSoup(result.text, "html.parser")
#print(soup.prettify())

price = soup.find_all(text=re.compile("$"))
price = soup.find_all(text="$")
parent_tag = price[0].parent
strong = parent_tag.find("strong")
print(strong.string)



# script = soup.find_all("script")
# main_script=script[6]
# print(soup.find_all(attrs={"value":"93100.0000"}))


# for price in soup.find_all(text="৳"):
#     print(price)
