import glob
from icecream import ic


def any_case_extension(extension: str):
    letters_list = [x for x in extension]
    return ''.join(['[' + x.lower() + x.upper() + ']' for x in letters_list])


def find_files_by_extension(path_to_folder: str, extension: str):
    return glob.glob(f'{path_to_folder}/*.{any_case_extension(extension)}')


def find_files_by_extension_recursive(path_to_folder: str, extension: str, ):
    # It looks like your glob pattern is not actually specifying to search recursively.
    # To search subfolders recursively with glob, you need to use the ** notation:
    return glob.glob(f'{path_to_folder}/**/*.{any_case_extension(extension)}', recursive=True)


files = glob.glob(f'{Path().home}/Downloads/*.[jJ][pP][gG]') + glob.glob('/Users/evgeniy/Downloads/*.[jJ][pP][eE][gG]')
print(files)

if __name__ == '__main__':
    assert (any_case_extension('jpeg')) == '[jJ][pP][eE][gG]'
    assert (any_case_extension('JPEG')) == '[jJ][pP][eE][gG]'

