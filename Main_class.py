def deco(color: str):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "end": "\033[0m"
    }

    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{colors.get(color, '')}Calling function: {func.__name__}{colors['end']}")
            return func(*args, **kwargs)
        return wrapper
    return decorator 
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
    @deco("green")
   
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
class AdvancedFileHandler(FileHandler):
    def __init__(self, file_path: str):
        super().__init__(file_path)

    @deco("blue")
    def read_lines(self):
        print("Reading lines using AdvancedFileHandler...")
        return super().read_lines()

    @deco("yellow")
    def concat_multiple(self, *handlers):
        output_path = "multi_output.txt"
        with open(output_path, 'w') as outfile:
            for handler in (self, *handlers):
                with open(handler.file_path, 'r') as f:
                    outfile.write(f.read())
        return AdvancedFileHandler(output_path)


def main():
    file1 = "example_files/file1.txt"
    file2 = "example_files/file2.txt"

    handler1 = AdvancedFileHandler(file1)
    handler2 = AdvancedFileHandler(file2)

    print("\n📄 Reading file1.txt:")
    for line in handler1.read_lines():
        print(" ", line)

    print("\n🔗 Concatenating both files into multi_output.txt...")
    result_handler = handler1.concat_multiple(handler2)

    print(f"\n✅ Concatenated file created at: {result_handler.file_path}\n")

    with open(result_handler.file_path, 'r') as f:
        print("🧾 Combined Content:\n")
        print(f.read())

if __name__ == "__main__":
    main()
