import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help='path to the first file')
    parser.add_argument('second_file', type=str, help='path to the second file')
    parser.add_argument('-f', '--format', type=str, default='stylish', help='set format of output')
    return parser.parse_args()
