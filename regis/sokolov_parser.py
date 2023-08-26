import json
import os

from bs4 import BeautifulSoup
from selenium import webdriver


def request_article(article):
    data = {}

    url = "https://sokolov.ru/"

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Remote(command_executor=os.environ['driver_url'], options=options)
    driver.close()  # this prevents the dummy browser
    driver.session_id = os.environ['driver_session_id']

    driver.get(url + 'products-search/text/?text=' + str(article))

    while True:
        try:
            html = driver.page_source
            html = BeautifulSoup(html, "html.parser")
            if 'ничего не найдено' in html.body.find('h1', attrs={'itemprop': 'name'}).text:
                return json.dumps(data)
            driver.get(url + html.body.find('a', attrs={'class': 'ProductListItem_product-link__EPUga'})['href'])
            break
        except (TypeError, AttributeError):
            pass

    data.update(images=[])

    while True:
        try:
            html = driver.page_source
            html = BeautifulSoup(html, "html.parser")

            divs = html.body.find_all('div', attrs={'class': 'sklv-slider__preview'})

            flag = 0

            for div in divs:
                child = div.findChild('img')
                try:
                    array = data['images']
                    array.append(child['data-src'])
                    data['images'] = array
                    flag = 1
                except TypeError:
                    pass
            if flag:
                break
        except (TypeError, AttributeError):
            pass

    while True:
        try:
            data.update(text=(html.body.find(
                'div', attrs={'class': 'sklv-product-page__second'}).find(
                'div').find_all(
                'div')[1].text.split('О бренде')[0].split('Характеристики')[1]))
            break
        except AttributeError:
            pass
    driver.get('data:,')
    return json.dumps(data)
