#!/usr/bin/env python3
import sys
from gendiff.cli import parse_arguments
from gendiff.generate_diff import generate_diff


def main():
    try:
        args = parse_arguments()
        diff = generate_diff(args.first_file, args.second_file, args.format)
        print(diff)
        sys.exit(0)
    except ValueError as e:
        print(e)
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
