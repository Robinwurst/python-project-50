import pytest
from hexlet_code import generate_diff

import pytest

from hexlet_code.parse_file import read_file

file1, file2 = read_file


def test_plain():
    sample = './tests/fixtures/plain_result.txt'

    with open(sample) as sample:
        sample_content = sample.read()
    assert generate_diff(file1, file2) != sample_content
