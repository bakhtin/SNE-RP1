import datetime
from functools import reduce
import operator
from utils.exceptions import *
import pickle


class Inode(object):

    SOCIALS = {
        'VK': 1,
        'MixCloud': 2,
        'SoundCloud': 3
    }

    def __init__(self, id, size, blocks, creation_date=datetime.datetime.now(), last_modified=datetime.datetime.now()):
        self.id = id
        self.size = size
        self.blocks = blocks
        self.creation_date = creation_date
        self.last_modified = last_modified

    def __str__(self):
        return str(self.id)

    #TODO: think about block update and creation of single/double/triple(opt.) indirect
    def block_update_job(self, array):

    def single_indirect(self, array):

    def double_indirect(self, array):


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
                        print '\t' * indent + "%s %s" % (k, v)
        tree_printer(self.inodes)
        return ''

    @staticmethod
    def _find_path(mapList, tree):
        return reduce(operator.getitem, tree, mapList)

    @staticmethod
    def _path_dissect(path):
        path_components = ['/']
        if not path.startswith('/'):
            raise LookupError("Path must start with /")
        path_components += path.strip('/').split('/')
        return path_components

    def mkdir(self, path):
        path_components = self._path_dissect(path)
        try:
            self._find_path(self.inodes, path_components)
            raise DirectoryAlreadyExists(path)
        except TypeError:
            raise DirectoryAlreadyExists(path)
        except KeyError:
            self._find_path(self.inodes, path_components[:-1])[path_components[-1]] = {}

    def rmdir(self, path):
        pass

    def marshal(self):
        return pickle.dumps(self, -1)

    @staticmethod
    def unmarshal(string):
        return pickle.loads(string)

    def dir_or_inode(self, path):
        try:
            inode = self._find_path(self.inodes, self._path_dissect(path))
        except KeyError or TypeError:
            raise NoSuchPathExists(path)
        return inode

