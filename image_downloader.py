import csv
import os
import requests


def image_downloader(csv_file_path, month, month_number, current_year, folder_path):
    os.makedirs(f"{folder_path}/{current_year}_{month_number}", exist_ok=True)
    with open(csv_file_path, 'r') as input_file:
        reader = csv.reader(input_file)
        for row in reader:
            if month in row[0]:
                image_link = row[2]
                try:
                    r = requests.get(image_link, stream=True)
                    with open(
                            f"{folder_path}/{current_year}_{month_number}/{row[0]}__{row[1]}.JPG",
                            "bw") as f:
                        for chunk in r.iter_content(9000):
                            f.write(chunk)
                except Exception as ex:
                    print(ex)


if __name__ == '__main__':
    image_downloader('/Volumes/big4photo/Documents/NewProspect/NP.csv',
                     'июля', 7, 2023, '/Volumes/big4photo/Documents/NewProspect')


# https://newprospect.ru/upload/resize_cache/iblock/953/758_493_2/5iq84jvywtyyn7a3vehkopbmttwdd3ml.JPG
