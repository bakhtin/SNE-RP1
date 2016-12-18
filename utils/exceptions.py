class DirectoryAlreadyExists(Exception):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return "cannot create directory: `%s`. File exists" % self.path

class NoSuchPathExists(Exception):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return "cannot access `%s`: No such file or directory" % self.path

# class FileAlreadyExists(Exception):
#     def __init__(self, file_name):
#         self.file_name = file_name
#
#     def __str__(self):
#         return "cannot create directory `%s`: File exists" % self.file_name