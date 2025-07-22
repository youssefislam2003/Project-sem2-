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

        with open(self._file_path, 'r') as f:
            for line in f:
                yield line.strip()

    def concat_files(self, other):
        output_path = "output.txt"
        with open(output_path, 'w') as outfile:
            for path in [self._file_path, other._file_path]:
                with open(path, 'r') as infile:
                    outfile.write(infile.read())
        return FileHandler(output_path)

    def __add__(self, other):
        return self.concat_files(other)
    @staticmethod
    def is_text_file(filename):
        return filename.endswith('.txt')

    @classmethod
    def from_path(cls, path):
        return cls(path)