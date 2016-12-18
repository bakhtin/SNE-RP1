import datetime
from functools import reduce
import operator
from utils.exceptions import *


class Inode(object):
    def __init__(self, id, size, blocks, creation_date=datetime.datetime.now(), last_modified=datetime.datetime.now()):
        self.id = id
        self.size = size
        self.blocks = blocks
        self.creation_date = creation_date
        self.last_modified = last_modified

    def __str__(self):
        return str(self.id)


class Tree(object):
    def __init__(self):
        self.inodes = {'/': {}}

    def __str__(self):
        def tree_printer(tree, indent=0):
            for k, v in tree.iteritems():
                    if isinstance(v, dict):
                        print '\t' * indent + str(k)
                        tree_printer(v, indent+1)
                    else:
                        print '\t' * (indent+1) + "%s %s" % (k, v)
        tree_printer(self.inodes)
        return ''

    def _check_path_exists(self, tree, mapList):
        try:
            return reduce(operator.getitem, mapList, tree)
        except KeyError:
            return False

    def mkdir(self, path):
        path_components = ['/']
        if not path.startswith('/'):
            raise LookupError("Path must start with /")
        path = path.strip('/').split('/')
        path_components+=path
        if not self._check_path_exists(self.inodes, path_components):
            self._check_path_exists(self.inodes, path_components[:-1])[path_components[-1]] = {}
        else:
            raise DirectoryAlreadyExists
