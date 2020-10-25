from pprint import pprint

import bs4
import requests
import time
import re
import http.client

http.client._MAXHEADERS = 1000


MY_REGULAR = re.compile(r"href=\"([\w\S]+)\"")

URL = 'https://focus-auto.ru'
SHOP = '/shop/ford/'

MY_DICT = {}

def get_request(url, page=''):
    result = requests.get(f'https://focus-auto.ru{url}{page}')
    return result.text


def next_page(url):
    """На каждой категории берёт всё со страницы и так по каждой странице"""
    i = 0
    next = True
    product_list = []
    while next:
        i += 1
        new_page = f"?page={i}"
        page = get_request(url=url, page=new_page)
        html_doc = bs4.BeautifulSoup(page, features='html.parser')
        final_all_tags = html_doc.find_all('h3', {'class': 'product_name'})
        if len(final_all_tags) < 1:
            next = False
        for _ in final_all_tags:
            matches = re.search(MY_REGULAR, str(_))
            product_list.append(matches[1])
    return product_list

html_doc = bs4.BeautifulSoup(get_request(SHOP), features='html.parser')
all_tags = html_doc.find_all('a', {'class': 'catalog_item'})

for tag in all_tags:
    time.sleep(0.3)
    new_page = tag.get('href')
    car_name = new_page.split('/')[-2]
    MY_DICT[car_name] = []
    new_page_items = get_request(new_page)
    html_doc = bs4.BeautifulSoup(new_page_items, features='html.parser')
    new_all_tags = html_doc.find_all('a', {'class': 'catalog_item'})
    for new_tag in new_all_tags:
        time.sleep(0.3)
        new_tag.get('href')
        product_list = next_page(url=new_tag.get('href'))
        MY_DICT[car_name].extend(product_list)
    print(car_name, len(MY_DICT[car_name]))
    # pprint(MY_DICT[car_name])

