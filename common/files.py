
class PatternsToIgnore:
    def __init__(self):
        self.patternsToIgnore = []
        self.read_patterns_to_ignore()

    def read_patterns_to_ignore(self):
        self.read_lines_from_txt("node-ignore.txt")
        self.read_lines_from_txt("python-ignore.txt")

        self.read_lines_from_txt("linux-ignore.txt")
        self.read_lines_from_txt("windows-ignore.txt")

    def read_lines_from_txt(self, path):
        with open(path, "r") as fp:
            line = fp.readline()

            while line:
                if not self.is_line_to_ignore(line):
                    self.patternsToIgnore.append(line.strip())
                line = fp.readline()

    def is_line_to_ignore(self, line):
        return (line.strip().startswith("#") or line.strip() == ""
                or line.find("*") != -1)
