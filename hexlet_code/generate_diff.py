from hexlet_code.difference import get_diff
from hexlet_code.parse_file import read_file
from hexlet_code.formats import formating


def generate_diff(first_file_path, second_file_path, format_name='stylish'):
    data1 = read_file(first_file_path)
    data2 = read_file(second_file_path)
    diff = get_diff(data1, data2)

    return formating(diff, format_name)
