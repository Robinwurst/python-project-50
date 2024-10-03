import pytest
from pathlib import Path
from hexlet_code.generate_diff import generate_diff


@pytest.fixture
def prepared_files(request):
    file1, file2, expected, format_name = request.param

    fixtures_path = Path(__file__).parent / "fixtures"

    file1_path = fixtures_path / file1
    file2_path = fixtures_path / file2
    expected_path = fixtures_path / expected

    if not file1_path.exists():
        raise FileNotFoundError(f"File not found: {file1_path}")
    if not file2_path.exists():
        raise FileNotFoundError(f"File not found: {file2_path}")
    if not expected_path.exists():
        raise FileNotFoundError(f"File not found: {expected_path}")

    with open(expected_path) as result_file:
        return (
            str(file1_path),
            str(file2_path),
            result_file.read(),
            format_name
        )


@pytest.mark.parametrize(
    argnames='prepared_files',
    argvalues=[
        ('file1.json', 'file2.json', 'result_stylish', 'stylish'),
        ('file1.yml', 'file2.yml', 'result_stylish', 'stylish'),
        ('file1.json', 'file2.json', 'result_plain', 'plain'),
        ('file1.yml', 'file2.yml', 'result_plain', 'plain'),
        ('file1.json', 'file2.json', 'result_json', 'json')
    ],
    indirect=True
)
def test_generate_diff(prepared_files):
    file1, file2, result_render, format_name = prepared_files

    assert result_render == generate_diff(file1, file2, format_name)
