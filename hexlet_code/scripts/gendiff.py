#!/usr/bin/env python3
from hexlet_code.parse_arguments import parse_arguments
from hexlet_code.generate_diff import generate_diff


def main():
    args = parse_arguments()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
