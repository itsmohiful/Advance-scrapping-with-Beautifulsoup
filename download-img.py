import csv
import re
from cgitb import strong

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


url = "https://www.amazon.in/s?bbn=976420031&rh=n%3A976419031%2Cn%3A1389375031&dc&qid=1655932442&rnid=976420031&ref=lp_976420031_nr_n_7"
source = requests.get(url, headers = headers).text

soup = BeautifulSoup(source, 'html.parser')

title = soup.find_all(class_="a-section octopus-pc-asin-title")
#title = soup.find_all(class_="a-section octopus-pc-asin-title").span.string
#price = soup.find(class_="a-section octopus-pc-asin-price").span.span.next_sibling.span.next_sibling.contents[0]

price = soup.find_all(class_="a-price-whole")

img = soup.find_all(class_="octopus-pc-item-image octopus-pc-item-image-v3")
#imgs = img.attrs['src']
rating = soup.find_all(class_="a-size-mini a-color-tertiary")
# for rating in ratings:
#     print(rating.string)
#     print()

# for i in range(0,65):
#     titles = title[i].span.string
#     prices = "₹"+price[i].contents[0]
#     images = img[i].attrs['src']
#     ratings = rating[i].string
#     print(ratings)

file_name = "amazon-multiple-products-scrapping.csv"

with open(file_name, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Sr.No', 'Product Name', 'Prices', 'Image ulrs', 'ratings'])

    for i in range(1,65):
        titles = title[i].span.string
        prices = "₹"+price[i].contents[0]
        images = img[i].attrs['src']
        ratings = rating[i].string

        writer.writerow([i, titles, prices, images, ratings])
