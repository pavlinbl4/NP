import requests
from bs4 import BeautifulSoup
from loguru import logger

main_url = 'https://newprospect.ru'

count = None
work_url_path = f'?article={count}&pageId=1&hash=cbf05cb35393866fb263316a822d653e4971ece5'

articles_on_page_selector = ("div", 'class_="row gy-3 gy-lg-4"')


def work_with_selected_page(count):
    work_url: str = f"{main_url}/{work_url_path}"
    logger.info(work_url)
    html = requests.get(work_url).text
    soup = BeautifulSoup(html, 'lxml')

    logger.info(articles_on_page_selector)
    articles = soup.find_all(articles_on_page_selector)

    return articles


if __name__ == '__main__':
    print(work_with_selected_page(1))
