import requests
from bs4 import BeautifulSoup
from .models import TestModel


def parsing():

    list_of_names = []

    r = requests.get(url='https://kakzovut.ru/man.html').text
    soup = BeautifulSoup(r, features='html.parser')
    names_list = soup.find_all('div', {'class': 'nameslist'})
    for s in names_list:
        name = s.find('a').text
        list_of_names.append(name)

    return list_of_names


