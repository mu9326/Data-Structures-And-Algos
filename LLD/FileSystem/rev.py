from abc import ABC, abstractmethod
import operator


# ------------------ File ------------------
class File:
    def __init__(self, name, extension, size):
        self.name = name
        self.extension = extension
        self.size = size


# ------------------ Filters ------------------
class Filter(ABC):
    @abstractmethod
    def match(self, file):
        pass


class NameFilter(Filter):
    def __init__(self, name):
        self.name = name

    def match(self, file):
        return file.name == self.name


class ExtensionFilter(Filter):
    def __init__(self, extension):
        self.extension = extension

    def match(self, file):
        return file.extension == self.extension


class SizeFilter(Filter):
    OPS = {
        ">": operator.gt,
        "<": operator.lt,
        ">=": operator.ge,
        "<=": operator.le,
        "==": operator.eq,
        "!=": operator.ne,
    }

    def __init__(self, properties):
        self.size, op = properties
        self.operator = self.OPS[op]

    def match(self, file):
        return self.operator(file.size, self.size)


# ------------------ FileSystem ------------------
class FileSystem:
    def __init__(self, name, subdirs=None, files=None):
        self.name = name
        self.subdirs = subdirs or []
        self.files = files or []


# ------------------ Search ------------------
class Search:
    # store the objects for each filter in a hashmap
    FILTER_REGISTRY = {
        "NameFilter": NameFilter,
        "ExtensionFilter": ExtensionFilter,
        "SizeFilter": SizeFilter,
    }

    def __init__(self, filters, fileSystem, condition="AND"):
        # extract the objects based on the filters specified
        self.filters = [
            self.FILTER_REGISTRY[name](value) for name, value in filters.items()
        ]
        self.fileSystem = fileSystem
        self.condition = condition

    def check_conditions(self, file):
        # return true if the file matches anyone filter
        if self.condition == "OR":
            return any(f.match(file) for f in self.filters)
        # return true if file matches all the filters
        else:  # default AND
            return all(f.match(file) for f in self.filters)

    def find_files(self):
        result = []
        # start BFS at the root
        queue = [self.fileSystem]

        while queue:
            node = queue.pop(0)
            # check the root's files first
            for f in node.files:
                # if you find a file based on the filter specified
                if self.check_conditions(f):
                    # append it to the res
                    result.append(f.name)
            # if not, add the subdirectory to the queue to repeat the process
            queue.extend(node.subdirs)

        return result


# ------------------ Example ------------------
if __name__ == "__main__":
    f1 = File("abc", "txt", 10)
    f2 = File("cde", "txt", 20)
    f3 = File("def", "pdf", 30)
    f4 = File("ghi", "py", 5)
    f5 = File("uvw", "java", 10)

    # specifiy the root name and the files that will go in the fileSystem (can also add subdirectories)
    root = FileSystem("/", files=[f1, f2, f3, f4, f5])

    # search for the file -- specifies filters hashmap, filesystem, condition (apply any one or all of the filters)
    res = Search(
        {"ExtensionFilter": "java", "SizeFilter": (10, ">=")}, root, "OR"
    ).find_files()

    print(res)  # ['uvw']
