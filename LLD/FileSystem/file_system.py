# API - Search the File System

# Searching Files based on Name, Extension and Size

# input for the search (directory)

from abc import ABC, abstractmethod


# File object class
# Attributes:
# - name
# - extension
# - size

# Methods:
# - getters


class File:
    def __init__(self, name, type, size):
        self.name = name
        self.extension = type
        self.size = size

    def get_name(self):
        return self.name

    def get_extension(self):
        return self.extension

    def get_size(self):
        return self.size


# Filter class (Abstract class)
# Defines one method
# - match(file) --> matches the file based on name, size, extension


class Filter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def match(self, file):
        pass


# NameFilter filters based on the name
class NameFilter(Filter):
    def __init__(self, name):
        self.name = name

    def match(self, file):
        return file.get_name() == self.name


# SizeFilter filters based on size and the operator provided
class SizeFilter(Filter):
    def __init__(self, properties):
        self.size = properties[0]
        self.operator = properties[1]

    def match(self, file):
        return eval(str(file.get_size()) + str(self.operator) + str(self.size))


# ExtensionFilter filters based on the extension
class ExtensionFilter(Filter):
    def __init__(self, extension):
        self.extension = extension

    def match(self, file):
        return file.get_extension() == self.extension


# --------------------------------------------
# In some designs, a FileSystemNode class is used for both files and directories, and then you need a flag
# like isDirectory to distinguish.
# But here, you already have two separate classes:
# File → for files
# FileSystem → for directories
# So every FileSystem instance is implicitly a directory.
# You don’t need isDirectory at all.
# --------------------------------------------
# FileSystem class has three attributes -
# - name
# - list of subDirectories
# - list of Files
class FileSystem:
    def __init__(self, name, isDirectory=False, subDirectories=[], files=[]):
        self.name = name
        self.isDirectory = isDirectory
        self.subDirectory = subDirectories
        self.files = files

    def add_file(self, directory, sub_directory, file):
        pass

    def delete_file(self, directory, sub_directory, file):
        pass


# Search class has three attributes -
# - directory (which is a list that contains the files that we need to search for)
# - filter (the filter instance from NameFilter, SizeFilter, ExtensionFilter)
# - fileSystem object (e.g. the root directory or a directory with some other name)
# - condition (whether we want to saltisfy ALL the filters or just ANY ONE filter)
class Search:
    # Constructor initializes the search object with a directory, filters, file system, and an optional condition
    def __init__(self, directory, filter, fileSystem, condition=None):
        self.directory = directory  # The starting directory for the search
        # A dictionary of filters (e.g., {"SizeFilter": [1000, ">="]})
        self.filters = filter
        # The root of the file system (custom object, not built-in)
        self.fileSystem = fileSystem
        self.condition = condition  # Logical condition for combining filters ("AND"/"OR"), default is None

    # Method to check whether a file satisfies the filter conditions
    def check_conditions(self, file, instances, condition):
        if condition is None:
            # If no condition provided, just apply the first filter
            return instances[0].match(file)
        elif condition == "AND":
            # If condition is AND, all filters must match
            return all([instance.match(file) for instance in instances])
        else:
            # Otherwise (assuming OR), at least one filter must match
            return any([instance.match(file) for instance in instances])

    # Method to perform file search using BFS (Breadth-First Search)
    def find_files(self):
        root = self.fileSystem  # Start from the root of the file system
        queue = [root]  # Queue for BFS traversal, initialized with the root directory

        filter_classes = []  # List to hold instantiated filter objects
        for filter, value in self.filters.items():
            # Look up the filter class by name (string) from globals() and instantiate it with the given value
            filter_classes.append(globals().get(filter)(value))

        res = []  # List to store names of files that match the filters

        # BFS traversal of directories
        while queue:
            # For each file in the current directory
            for each_file in root.files:
                # Check conditions using the active filters
                # ⚠ BUG here: you're passing `each_file` instead of `self.condition`
                if self.check_conditions(each_file, filter_classes, each_file):
                    res.append(
                        each_file.get_name()
                    )  # If file matches, add its name to results

            node = queue.pop(0)  # Remove the first directory from the queue
            for each_subdirectory in node.subDirectory:
                queue.append(
                    each_subdirectory
                )  # Add its subdirectories to the queue for traversal

        return res  # Return the list of matching file names


if __name__ == "__main__":
    # Simulation
    f1 = File("abc", "txt", 10)
    f2 = File("cde", "txt", 20)
    f3 = File("def", "pdf", 30)
    f4 = File("ghi", "py", 5)
    f5 = File("uvw", "java", 10)

    directory_files = [f1, f2, f3, f4, f5]
    fileSystem = FileSystem("/", True, [], directory_files)

    # res = Search(directory_files, {"NameFilter": "abc"}, fileSystem).find_files()
    # print(res)

    # res = Search(directory_files, {"SizeFilter": (10, ">=")}, fileSystem).find_files()
    # print(res)

    res = Search(
        directory_files,
        {"ExtensionFilter": "java", "SizeFilter": (10, ">=")},
        fileSystem,
        "OR",
    ).find_files()
    print(res)
