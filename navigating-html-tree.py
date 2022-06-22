import re

import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/"
result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

tbody = doc.tbody
tr = tbody.tr
td = tr.td

trs = tbody.contents    #convert in list

sibling = trs[0].next_sibling   #next single sibling

dec = trs[0].descendants

child = trs[0].children

conts = trs[0].contents

siblings = list(trs[0].next_siblings)   #next all siblings

parent = sibling.parent
name = parent.name

prices = {}

#print(conts)
for tr in trs[:10]:

    #print(tr.contents)
    # for td in tr.contents[2:4]:
    #     print(td.p)

    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    price = price.a.string
    
    prices [fixed_name] = price
    #print()


print(prices)
