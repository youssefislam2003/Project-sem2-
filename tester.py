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