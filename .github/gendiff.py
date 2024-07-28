import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate difference between two files.')
    parser.add_argument('-h', '--help', action='help', help='Show this help message and exit.')
    parser.add_argument('first_file', help='Path to the first file.')
    parser.add_argument('second_file', help='Path to the second file.')

    args = parser.parse_args()

    if args.help:
        parser.print_help()
        return

    # Your logic to generate difference between two files goes here
    print(f'Generating difference between {args.first_file} and {args.second_file}')


if __name__ == '__main__':
    main()