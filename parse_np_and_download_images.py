from bs4 import BeautifulSoup
import csv
import requests
from datetime import datetime
from pathlib import Path
from image_downloader import image_downloader
from tqdm import tqdm, trange, tqdm_gui
import os
import datetime
import locale
from datetime import datetime


def make_documets_folder(name):
    (Path.home() / "Documents" / f"{name}").mkdir(parents=True, exist_ok=True)
    return Path.home() / "Documents" / f"{name}"


def get_html(url):
    req = requests.get(url)
    return req.text


def write_csv(data, csv_file_path):
    with open(csv_file_path, 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow((data["date"], data["name"], data["url"]))


def get_data(html, csv_file_path):
    soup = BeautifulSoup(html, 'lxml')
    articles = soup.find_all('div', class_="l-page__main-news--item")
    for title in articles:
        article_date = title.find(class_="l-page__main-news--date").text.split()[-3:]  # дата публикации
        article_name = title.find('div', class_="l-page__main-news--title").text  # заголовки статей
        image_src = title.find('img').get('src')
        image_link = f'https://newprospect.ru{image_src}'  # ссылка на изображение
        article_date_lookfine = " ".join(article_date)
        data = {"date": article_date_lookfine,
                "name": article_name,
                "url": image_link}
        write_csv(data, csv_file_path)

def month_information():
    now = datetime.now()

    # Set locale to Russian
    locale.setlocale(locale.LC_TIME, 'ru_RU')

    # Get month name in Russian
    month_name = now.strftime("%B")
    print(month_name)


def date_convert(month_number):  # функция преобразует введенный номер месяца в его название
    voc = {1: 'января',
           2: 'февраля',
           3: 'марта',
           4: 'апреля',
           5: 'мая',
           6: 'июня',
           7: 'июля',
           8: 'августа',
           9: 'сентября',
           10: 'октября',
           11: 'ноября',
           12: 'декабря'}
    month_name = voc[month_number]
    return month_name


def get_all_images(month_number):
    url = "https://newprospect.ru"
    current_year = datetime.now().year

    folder_path = make_documets_folder('NewProspect')

    month = date_convert(month_number)
    csv_file_path = f"{folder_path}/NP.csv"
    for i in trange(5,colour='blue', ncols = 100, desc='Main cycle'):
        get_data(get_html(url), csv_file_path)
        soup = BeautifulSoup(get_html(url), 'lxml')
        url = "https://newprospect.ru" + soup.find('li', class_='l-nav__pagination-item next').find('a').get('href')
    # print('CSV file created')
    image_downloader(csv_file_path, month, month_number, current_year, folder_path)
    print('Images downloaded - please select you images and run "create_report" script')
    os.remove(csv_file_path)
    return folder_path


if __name__ == '__main__':
    # get_all_images(3)
    month_information()




