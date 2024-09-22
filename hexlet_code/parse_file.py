import json
import yaml


def read_file(path_file):
    with open(path_file) as file:
        data = file.read()
    return parse(data)


def parse(data):
    if data == 'json':
        return json.load(data)
    if data == 'yml' or 'yaml':
        return yaml.safe_load(data)
