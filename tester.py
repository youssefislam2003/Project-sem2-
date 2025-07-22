import pytest
from Main_class import FileHandler

@pytest.fixture
def temp_text_file(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("Line 1\nLine 2\nLine 3")
    return str(file)

def test_read_lines(temp_text_file):
    handler = FileHandler(temp_text_file)
    lines = list(handler.read_lines())
    assert lines == ["Line 1", "Line 2", "Line 3"]
def test_concat_files(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file1.write_text("Hello\n")
    file2.write_text("World!\n")

    handler1 = FileHandler(str(file1))
    handler2 = FileHandler(str(file2))

    result_handler = handler1 + handler2  # Uses __add__
    with open(result_handler.file_path, 'r') as result:
        content = result.read()

    assert content == "Hello\nWorld!\n"
def test_static_and_class_methods(tmp_path):
    file = tmp_path / "testfile.txt"
    file.write_text("data")
    
    assert FileHandler.is_text_file(str(file)) is True

    handler = FileHandler.from_path(str(file))
    assert isinstance(handler, FileHandler)
    assert handler.file_path == str(file)