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