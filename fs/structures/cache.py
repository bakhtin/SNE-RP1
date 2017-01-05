import collections


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity  # in bytes
        self.cache = collections.OrderedDict()
        self.__free = capacity

    def get(self, node_id):
        try:
            node = self.cache.pop(node_id)
            self.cache[node_id] = node
            return node
        except KeyError:
            raise

    def set(self, node_id, (node_size, path_in_cache)):
        if node_size > self.capacity:
            raise MemoryError("File is too large to put in the cache")
        try:
            yield self.cache.pop(node_id)[1]
        except KeyError:
            while self.__free < node_size:
                last_node = self.cache.popitem(last=False)
                self.__free += last_node[0]
                yield last_node[1]
        self.cache[node_id] = (node_size, path_in_cache)
        self.__free -= node_size
