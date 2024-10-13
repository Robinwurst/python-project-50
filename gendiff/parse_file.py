import json
import yaml
import os.path as path


def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return parse(data, get_extension(file_path))


def parse(data, extension):
    if extension == '.json':
        return json.loads(data)
    elif extension in ['.yml', '.yaml']:
        return yaml.safe_load(data)
    else:
        raise ValueError('Unknown extension')


def get_extension(file_path):
    return path.splitext(file_path)[1]

# def validate_extension(file_path):
#     extension = get_extension(file_path)
#     if extension not in ['.json', '.yml', '.yaml']:
#         raise ValueError('Unknown extension')
