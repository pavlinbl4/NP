from parsing.parse_np_and_download_images import get_all_images
from gui_tools.select_month import select_month


def main():
    # select month
    month_number = select_month()

    # download all images
    get_all_images(month_number)


if __name__ == '__main__':
    main()
