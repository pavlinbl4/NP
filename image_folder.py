from pathlib import Path
from icecream import ic


def input_folder(path_to_folder):
    for row, image_path in enumerate(Path(path_to_folder).glob("*.JPG"), 1):
        ic(image_path)


if __name__ == '__main__':
    input_folder(r'/Users/evgeniy/Documents/NewProspect/2023_12')
