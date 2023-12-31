import requests


def downloader(image_link, path_to_file):
    try:
        r = requests.get(image_link, stream=True)
        with open(path_to_file, "bw") as f:
            for chunk in r.iter_content(9000):
                f.write(chunk)
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    downloader('https://newprospect.ru/upload/sprint.editor/70c/sbnik7qnbu1mpqsskqzn10nv3slc52r7.jpg',
               "downloaded_jpeg.JPG")
