import csv
import re
from cgitb import strong

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


url = "https://www.amazon.in/HP-Pavilion-Micro-Edge-Graphics-14-dv1000TU/dp/B09KGQY5BS/ref=sr_1_1_sspa?keywords=Laptops&qid=1655919115&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzM0Q3OU8yQVkzQU5aJmVuY3J5cHRlZElkPUEwNjc0NzQwMTdaVzdTMVQ0WUNXWSZlbmNyeXB0ZWRBZElkPUEwMTI1OTMyM01EQThYTjlUQzBOTCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
source = requests.get(url, headers = headers).text

soup = BeautifulSoup(source, 'html.parser')


product_name = soup.find(id="titleSection").span.string

price = soup.find(class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay").span.string

img = soup.find(class_="imgTagWrapper").img.attrs['src']

rating = soup.find(id="acrCustomerReviewLink").span.string
print(rating)


file_name = 'single-product-amazon-scrapping.csv'

with open(file_name, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['No', 'product Name', 'Price', 'Image link', 'Ratings'])
    writer.writerow([ 1, product_name, price, img, rating])
