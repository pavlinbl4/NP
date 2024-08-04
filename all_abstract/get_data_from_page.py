import requests
from bs4 import BeautifulSoup
from loguru import logger

main_url = 'https://newprospect.ru'
articles_on_page_selector = "tplarticle"


def work_with_selected_page(count):
    work_url_path = f'?article={count}&pageId=1&hash=cbf05cb35393866fb263316a822d653e4971ece5'
    work_url = f"{main_url}/{work_url_path}"
    logger.info(f"Requesting URL: {work_url}")

    response = requests.get(work_url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'lxml')

        articles = soup.find_all("div", class_=articles_on_page_selector)
        logger.info(f"Found {len(articles)} articles on the page.")

        return articles
    else:
        logger.error(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []


if __name__ == '__main__':
    count = 0
    articles = work_with_selected_page(count)
    for article in articles:
        print(article)