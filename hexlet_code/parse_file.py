import json


def get_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return parse(data)


def parse(data):
    return json.loads(data)
