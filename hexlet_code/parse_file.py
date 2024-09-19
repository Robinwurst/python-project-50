import json


def read_file(path_file):
    with open(path_file) as file:
        data = file.read()
    return parse(data)


def parse(data):
    return json.loads(data)
