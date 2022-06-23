import csv
import re
from cgitb import strong

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


url = "https://www.newegg.com/p/pl?d=3080&n=8000"
source = requests.get(url, headers = headers).text

soup = BeautifulSoup(source, 'html.parser')


page_text = soup.find(class_="list-tool-pagination-text").strong
pages =  int(str(page_text).split('/')[-2].split('>')[-1][:-1])
#print(pages)


items_found = {}

for page in range(2,pages + 1):

    url = f"https://www.newegg.com/p/pl?d=3080&n=8000&page={page}"
    source = requests.get(url, headers = headers).text

    soup = BeautifulSoup(source, 'html.parser')
    search_term = "3080"
    div = soup.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")

    items = div.find_all(text=re.compile(search_term))

    for item in items:
        parent = item.parent
        if parent.name != "a":
            continue
        link = parent['href']
        #next_parent = list(parent.parent.next_siblings)
        next_parent = item.find_parent(class_="item-container")
        price = next_parent.find(class_="price-current").strong.string

        items_found[item] = {"price" : int(price.replace(",","")), "link" : link} #convert price in int value
        #items_found[item] = {"price" : price, "link" : link}

sorted_items = sorted(items_found.items(), key=lambda x: x[1]["price"])
#sorted_items = items_found
#print(sorted_items)
#print(items_found)

# for item in sorted_items:
#     print(item[0])
#     print(item[1]["price"])
#     print(item[1]["link"])
#     print("============================")


file_name = 'newegg-com-multipage-scrapping.csv'

with open(file_name, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Sr.No', 'GPU Name', 'Prices', 'link'])

    for i in range(1,len(sorted_items)):
        writer.writerow([ i, sorted_items[i][0], sorted_items[i][1]['price'], sorted_items[i][1]['link']])


# for i in range(1,3):
#     print(sorted_items[i][0])
#     print(sorted_items[i][1]['price'])
#     print("===============")
