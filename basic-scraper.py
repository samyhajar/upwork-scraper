from math import prod
from requests_html import HTMLSession
import csv


s = HTMLSession()


def get_product_links(page):
    url = f'https://themes.woocommerce.com/storefront/product-category/clothing/page/{page}'

    links = []
    r = s.get(url)
    products = r.html.find('ul.products li')
    for item in products:
      links.append(item.find('a', first=True).attrs['href'])
    return links

page1 = get_product_links(1)
#print(page1)

def parse_products(url):



    r = s.get(url)

    title = r.html.find('h1.product_title.entry-title' , first=True).text.strip()
    price = r.html.find('p.price' , first=True).text.strip().replace('\n', ' / ')

    cat = r.html.find('span.posted_in' , first=True).text.strip()
    try:
      sku = r.html.find('span.sku' , first=True).text.strip()
    except AttributeError as err:
      sku = 'None'
      #print(err)

    product = {
        'title' : title,
        'price' : price,
        'sku' : sku,
        'cat' : cat,
    }
    return product





results = []
for x in range(1,5):
  print('Getting Page', x)
  urls = get_product_links(x)
  for url in urls:
    results.append(parse_products(url))
  print('Total results', len(results))
