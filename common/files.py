import os


class PatternsToIgnore:
    def __init__(self):
        self.patterns_to_ignore = []
        self.read_patterns_to_ignore()

    def read_patterns_to_ignore(self):
        self.read_lines_from_txt("node-ignore.txt")
        self.read_lines_from_txt("python-ignore.txt")

        self.read_lines_from_txt("linux-ignore.txt")
        self.read_lines_from_txt("windows-ignore.txt")

        self.patterns_to_ignore.extend([
            f"{os.sep}.git", f"{os.sep}.idea", f"{os.sep}__MACOSX"
        ])

    def read_lines_from_txt(self, path):
        current_folder = os.path.dirname(os.path.abspath(__file__))
        path_file = os.path.join(current_folder, path)

        with open(path_file, "r") as fp:
            line = fp.readline()

            while line:
                if not self.is_line_to_ignore(line):
                    line_formatted = line.strip().replace("/", f"{os.sep}")

                    index_last = line_formatted.rfind(f"{os.sep}")
                    if index_last != -1:
                        line_formatted = line_formatted[:index_last]

                    line_formatted = f"{os.sep}{line_formatted}"

                    self.patterns_to_ignore.append(line_formatted)

                line = fp.readline()

    @staticmethod
    def is_line_to_ignore(line):
        return (line.strip().startswith("#") or line.strip() == ""
                or line.find("*") != -1)

    def is_path_to_ignore(self, path):
        for pattern in self.patterns_to_ignore:
            if path.find(pattern) != -1:
                return True

        return False


# TODO: remove me!
p = PatternsToIgnore()
for pp in p.patterns_to_ignore:
    print(pp)
