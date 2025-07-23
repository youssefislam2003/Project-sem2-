import pytest
from Main_class import FileHandler
from Main_class import AdvancedFileHandler
import os

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


def test_concat_multiple(tmp_path):
    f1 = tmp_path / "a.txt"
    f2 = tmp_path / "b.txt"
    f3 = tmp_path / "c.txt"

    f1.write_text("Apple\n")
    f2.write_text("Banana\n")
    f3.write_text("Cherry\n")

    handler = AdvancedFileHandler(str(f1))
    result = handler.concat_multiple(
        AdvancedFileHandler(str(f2)),
        AdvancedFileHandler(str(f3))
    )


    with open(result.file_path, 'r') as result_file:
        content = result_file.read()

    assert "Apple" in content and "Cherry" in content and "Banana" in content
def test_read_lines_override(tmp_path):
    file = tmp_path / "file.txt"
    file.write_text("Test\nLine")
    adv_handler = AdvancedFileHandler(str(file))

    lines = list(adv_handler.read_lines())
    assert lines == ["Test", "Line"]

def test_file_not_found():
    handler = FileHandler("non_existent_file.txt")
    with pytest.raises(FileNotFoundError):
        list(handler.read_lines())