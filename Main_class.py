class FileHandler:
    def __init__(self, file_path: str):
        self._file_path = file_path

    @property
    def file_path(self):
        """Getter for file path"""
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        """Setter for file path"""
        self._file_path = value

    def __str__(self):
        return f"FileHandler({self._file_path})"

    def read_lines(self):
        """Generator that reads lines one at a time"""
        with open(self._file_path, 'r') as f:
            for line in f:
                yield line.strip()
                