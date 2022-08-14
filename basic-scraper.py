from requests_html import HTMLSession


s = HTMLSession()

url = 'https://themes.woocommerce.com/storefront/product-category/clothing/page/1'

r = s.get(url)

print(r.html.find())