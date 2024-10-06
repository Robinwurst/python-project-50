#!/usr/bin/env python3
from gendiff.parse_arguments import parse_arguments
# from gendiff.generate_diff import generate_diff
from gendiff.difference import get_diff
from gendiff.parse_file import read_file
from gendiff.formats import formating


def generate_diff(first_file_path, second_file_path, format_name='stylish'):
    data1 = read_file(first_file_path)
    data2 = read_file(second_file_path)
    diff = get_diff(data1, data2)

    return formating(diff, format_name)


def main():
    args = parse_arguments()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
