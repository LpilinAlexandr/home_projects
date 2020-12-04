import requests
from lxml import html
from io import StringIO

class Proxy:

    """
    Получает прокси для парсера
    """

    proxy_url = 'https://www.ip-adress.com/proxy-list'

    def __init__(self):
        self.new_list = []
        response = requests.get(self.proxy_url)
        content = html.parse(StringIO(response.text)).getroot()
        table = content.find_class('htable proxylist')
        link_iter = html.iterlinks(table[0])
        text_value = table[0].xpath('//tr/td/text()')
        self.proxy_list = [link[0].text_content() for link in link_iter]
        for i in range(0, len(text_value), 3):
            port = str(text_value[i])
            proxy = self.proxy_list[0]
            self.new_list.append(f"{proxy}{port}")
            self.proxy_list.pop(0)



    def get_proxy(self, url):
        for proxy in self.new_list:
            print('ПРобую: ', proxy)
            proxies =  {
                "http": f'http://{proxy}',
                "https": f'http://{proxy}'
            }
            try:
                response = requests.get(url, proxies=proxies, timeout=3)
                if response.status_code == 200:
                    return proxy
            except:
                # print('ПРокси не валидный', proxies)
                continue
        print('Не осталось проксей :(')

    def check_proxy_work(self, url):
        """
        Зайти с валидного прокси на яндекс интернетометр и найти там свой айпи
        """
        proxy = self.get_proxy(url)
        print(proxy)
        response = requests.get('https://2ip.ru/', proxies=proxy)
        print(response.content)
