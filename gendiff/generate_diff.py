from gendiff.difference import get_diff
from gendiff.formatters.json import make_json
from gendiff.utils import read_file, get_data_format, parse
from gendiff.formatters import stylish, plain


def generate_diff(first_file_path, second_file_path, format_name='stylish'):
    ext1 = get_data_format(first_file_path)
    ext2 = get_data_format(second_file_path)

    data1 = read_file(first_file_path)
    data2 = read_file(second_file_path)

    parsed_data1 = parse(data1, ext1)
    parsed_data2 = parse(data2, ext2)

    diff = get_diff(parsed_data1, parsed_data2)

    return get_format(diff, format_name)


def get_format(diff, format_name):
    if format_name == 'stylish':
        return stylish.stylish(diff)
    elif format_name == 'plain':
        return plain.plain(diff)
    elif format_name == 'json':
        return make_json(diff)
    else:
        raise ValueError('Wrong format')
