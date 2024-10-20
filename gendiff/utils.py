import json
import yaml
import os.path as path


def get_data_format(file_path):
    data_format = path.splitext(file_path)[1].lower()
    if data_format not in ['.json', '.yml', '.yaml']:
        raise ValueError(f'Unknown format: {data_format}')
    return data_format[1:]


def read_file(file_path):

    with open(file_path, 'r') as file:
        data = file.read()

    return data


def parse(data, data_format):
    if data_format == 'json':
        return json.loads(data)
    elif data_format in ['yml', 'yaml']:
        return yaml.safe_load(data)
