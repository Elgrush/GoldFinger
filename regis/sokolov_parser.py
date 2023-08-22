import json
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver import Chrome


def request_article(article):
    data = {}

    # start by defining the options
    options = webdriver.ChromeOptions()
    options.headless = True  # it's more scalable to work in headless mode
    # normally, selenium waits for all resources to download
    # we don't need it as the page also populated with the running javascript code.
    options.page_load_strategy = 'none'

    # pass the defined options and service objects to initialize the web driver
    driver = Chrome(options=options)
    driver.implicitly_wait(5)

    url = "https://sokolov.ru/"

    driver.get(url + 'products-search/text/?text=' + str(article))

    while True:
        try:
            html = driver.page_source
            html = BeautifulSoup(html, "html.parser")
            if 'ничего не найдено' in html.body.find('h1', attrs={'itemprop': 'name'}).text:
                driver.close()
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

    driver.close()
    while True:
        try:
            data.update(text=(html.body.find(
                'div', attrs={'class': 'sklv-product-page__second'}).find(
                'div').find_all(
                'div')[1].text.split('О бренде')[0].split('Характеристики')[1]))
            break
        except AttributeError:
            pass
    return json.dumps(data)
