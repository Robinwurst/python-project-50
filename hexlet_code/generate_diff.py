from hexlet_code.difference import get_diff
from hexlet_code.parse_file import get_data


def generate_diff(first_file_path, second_file_path):
    data1 = get_data(first_file_path)
    data2 = get_data(second_file_path)
    diff = get_diff(data1, data2)

    return diff
