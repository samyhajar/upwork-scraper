from math import prod
from requests_html import HTMLSession


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
    price = r.html.find('p.price' , first=True).text.strip()
    sku = r.html.find('span.sku' , first=True).text.strip()
    cat = r.html.find('span.posted_in' , first=True).text.strip()


    product = {
        'title' : title,
        'price' : price,
        'sku' : sku,
        'cat' : cat,
    }
    return product

print(parse_products('https://themes.woocommerce.com/storefront/product/red-checked-shirt/'))