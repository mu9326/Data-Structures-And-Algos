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
    def __init__(self, name, subDirectories=None, files=None):
        self.name = name
        self.subDirectory = subDirectories if subDirectories else []
        self.files = files if files else []

    def add_file(self, path_list, file):
        """
        path_list: list of directory names representing the path to the target directory
                   e.g. ['/', 'subdir1'] or ['subdir1']
        file: File object to add
        """
        if not path_list or path_list[0] == self.name:
            path_list = path_list[1:]  # remove current directory if matches

        if not path_list:
            # Current directory is target, add file
            self.files.append(file)
            return True

        # Search in subdirectories
        for subdir in self.subDirectory:
            if subdir.name == path_list[0]:
                return subdir.add_file(path_list[1:], file)

        # If subdirectory does not exist, optionally create it
        new_subdir = FileSystem(path_list[0])
        self.subDirectory.append(new_subdir)
        return new_subdir.add_file(path_list[1:], file)

    def delete_file(self, path_list, file_name):
        """
        path_list: list of directory names representing the path to the target directory
        file_name: name of the file to remove
        """
        if not path_list or path_list[0] == self.name:
            path_list = path_list[1:]  # remove current directory if matches

        if not path_list:
            # Current directory is target, delete file if exists
            for i, f in enumerate(self.files):
                if f.get_name() == file_name:
                    self.files.pop(i)
                    return True
            return False  # file not found

        # Search in subdirectories
        for subdir in self.subDirectory:
            if subdir.name == path_list[0]:
                return subdir.delete_file(path_list[1:], file_name)

        return False  # subdirectory not found


# Search class has three attributes -
# - directory (which is a list that contains the files that we need to search for)
# - filter (the filter instance from NameFilter, SizeFilter, ExtensionFilter)
# - fileSystem object (e.g. the root directory or a directory with some other name)
# - condition (whether we want to saltisfy ALL the filters or just ANY ONE filter)

# filter_classes = [
#     ExtensionFilter("java"),
#     SizeFilter((10, ">="))
# ]


class Search:
    def __init__(self, directory, filter, fileSystem, condition=None):
        self.directory = directory
        self.filters = filter
        self.fileSystem = fileSystem
        self.condition = condition

    def check_conditions(self, file, instances, condition):
        if condition is None:
            return instances[0].match(file)
        elif condition == "AND":
            return all([instance.match(file) for instance in instances])
        else:
            return any([instance.match(file) for instance in instances])

    def find_files(self, name):
        root = self.fileSystem
        queue = [root]
        res = []

        filter_classes = []
        for filter, value in self.filters.items():
            filter_classes.append(globals().get(filter)(value))

        # filter_classes = [
        #     ExtensionFilter("java"),
        #     SizeFilter((10, ">="))
        # ]

        while queue:
            node = queue.pop(0)

            for each_file in node.files:
                if self.check_conditions(each_file, filter_classes, self.condition):
                    res.append(each_file.get_name())

            for each_subdirectory in node.subdirectories:
                queue.append(each_subdirectory)

        return res
