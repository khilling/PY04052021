import os
import requests
from bs4 import BeautifulSoup
import re
from random import choice as takeRandomElement


def __get_page_content(url):
    print(url)
    return requests.get(url).content.decode('utf-8', errors='ignore')


def __get_page_soup(url):
    html_doc = __get_page_content(url)
    return BeautifulSoup(html_doc)


def get_rbc_articles(url='https://tv.rbc.ru/'):
    soup = __get_page_soup(url)
    articles = soup.find_all('a', id=re.compile('id_newsfeed'))
    return list(map(lambda page: page['href'], filter(lambda page: 'rbc' in page['href'], articles)))


def get_yaplakal_articles(url='https://www.yaplakal.com/'):
    soup = __get_page_soup(url)
    open('soup.html', 'w').write(str(soup))
    articles = []
    for item in soup.find_all('a'):
        try:
            if item['class'] == ['subtitle']:
                articles.append('https:' + item.get('href'))
        except:
            pass
    return articles


def get_random_article(get_articles_function, name):
    article = takeRandomElement(get_articles_function())
    article_html = __get_page_content(article)
    f = open(os.getcwd() + '/flaskr/templates/' + name + '.html', 'w')
    f.write(article_html)
    f.close()


def yaplakal():
    get_random_article(get_yaplakal_articles, 'yaplakal')
    return 'yaplakal.html'


def rbc():
    get_random_article(get_rbc_articles, 'rbc')
    return 'rbc.html'


def update():
    open(os.getcwd() + '/flaskr/templates/text.html', 'w').close()
