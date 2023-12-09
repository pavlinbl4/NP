import csv
import os
import requests
from tqdm import tqdm


def downloader(image_url: str, folder_path: str, image_name: str):
    try:
        r = requests.get(image_url, stream=True)
        with open(
                f"{folder_path}/{image_name}.JPG",
                "bw") as f:
            for chunk in r.iter_content(9000):
                f.write(chunk)
    except Exception as ex:
        print(ex)


def image_downloader(csv_file_path, month, month_number, current_year, folder_path):
    # create folder to downloading images
    path_to_folder = f"{folder_path}/{current_year}_{month_number}"
    os.makedirs(path_to_folder, exist_ok=True)

    # read data from csv file
    with open(csv_file_path, 'r') as input_file:
        reader = csv.reader(input_file)

        for row in tqdm(reader, colour='blue', ncols=1000, desc="Image downloading"):

            if month in row[0]:
                image_url = row[2]
                downloader(image_url, path_to_folder, f'{row[0]}__{row[1]}')


if __name__ == '__main__':
    image_downloader('/Volumes/big4photo/Documents/NewProspect/NP.csv',
                     'июля', 7, 2023, '/Volumes/big4photo/Documents/NewProspect')
