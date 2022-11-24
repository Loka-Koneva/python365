import bs4
import logging
import requests

logging.basicConfig(level=logging.DEBUG)
log = logging.Logger('wb')


class Client:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3'
        }

    def load_page(self, pade: int=None):
        url = 'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/dzhinsy-dzhegginsy'
        result = self.session.get(url=url)
        result.raise_for_status()
        return result.text

    def parse_page(self, text: str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        conteiner = soup.select('div.product-card.j-card-item')
        for block in conteiner:
            self.parse_block(block=block)

    def parse_block(self, block):
        log.info(block)
        log.info('='*25)

    def run(self):
        text = self.load_page()
        self.parse_page(text=text)


if __name__ == '__main__':
    parser = Client()
    parser.run()

