from gendiff.difference import get_diff
from gendiff.utils import read_file, get_extension, parse
from gendiff.formats import formating


def generate_diff(first_file_path, second_file_path, format_name='stylish'):
    ext1 = get_extension(first_file_path)
    ext2 = get_extension(second_file_path)

    data1 = read_file(first_file_path)
    data2 = read_file(second_file_path)

    parsed_data1 = parse(data1, ext1)
    parsed_data2 = parse(data2, ext2)

    diff = get_diff(parsed_data1, parsed_data2)

    return formating(diff, format_name)
