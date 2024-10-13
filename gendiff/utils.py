import json
import yaml
import os.path as path


def get_extension(file_path):
    extension = path.splitext(file_path)[1].lower()
    if extension not in ['.json', '.yml', '.yaml']:
        raise ValueError(f'Unknown extension: {extension}')
    return extension


def read_file(file_path):
    if not path.exists(file_path):
        raise FileNotFoundError(f"Path not found: {file_path}")

    with open(file_path, 'r') as file:
        data = file.read()

    return data


def parse(data, extension):
    if extension == '.json':
        return json.loads(data)
    elif extension in ['.yml', '.yaml']:
        return yaml.safe_load(data)
