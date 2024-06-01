from bs4 import BeautifulSoup
import csv
import requests
from datetime import datetime
from pathlib import Path

from parsing.image_downloader import image_downloader


def make_documents_folder(name):
    folder_path = Path.home() / "Documents" / f"{name}"
    folder_path.mkdir(parents=True, exist_ok=True)
    return folder_path


def get_html(url):
    req = requests.get(url)
    req.raise_for_status()  # Raise an exception for non-2xx status codes
    return req.text



def write_csv(data, csv_file_path):
    with open(csv_file_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow((data["date"], data["name"], data["url"]))


def get_data(html, csv_file_path):
    soup = BeautifulSoup(html, 'lxml')
    articles = soup.find_all('div', class_="l-page__main-news--item")
    for article in articles:
        article_date = article.find(class_="l-page__main-news--date").text.split()[-3:]  # дата публикации
        article_name = article.find('div', class_="l-page__main-news--title").text  # заголовки статей
        image_src = article.find('img').get('src')
        image_link = f'https://newprospect.ru{image_src}'  # ссылка на изображение
        article_date_lookfine = " ".join(article_date)
        data = {"date": article_date_lookfine,
                "name": article_name,
                "url": image_link}
        write_csv(data, csv_file_path)


def date_convert(month_number):
    months = {
        1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня',
        7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'
    }
    return months.get(month_number, 'Invalid month')


def get_all_images(month_number=datetime.now().month):
    folder_path = make_documents_folder('NewProspect')
    csv_file_path = folder_path / "NP.csv"
    month = date_convert(month_number)

    current_year = datetime.now().year
    url = "https://newprospect.ru"
    for i in range(5):
        get_data(get_html(url),csv_file_path)
        soup = BeautifulSoup(get_html(url), 'lxml')
        url = "https://newprospect.ru" + soup.find('li', class_='l-nav__pagination-item next').find('a').get('href')
    print('CSV file created')
    image_downloader(csv_file_path, month, month_number, current_year, folder_path)
    print('Images downloaded - please select you images and run "create_report" script')


if __name__ == '__main__':



    get_all_images(4)
