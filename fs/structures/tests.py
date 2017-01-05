from inode import Inode, Tree
from api.functions import splitFile, upload_to_vk, download_from_vk, upload_main_inode
from cache import LRUCache

if __name__ == "__main__":

    # Inode test
    a = Inode(size=8, blocks={1: range(11200, 11210), 2: range(11200, 11210), 3: range(11200, 11210)})
    b = Inode(size=30, blocks={1: range(11200, 11210), 2: range(11200, 11210), 3: range(11200, 11210)})
    c = Inode(size=12, blocks={1: range(11200, 11210), 2: range(11200, 11210), 3: range(11200, 11210)})
    c1 = Inode(size=15, blocks={1: range(11200, 11210), 2: range(11200, 11210), 3: range(11200, 11210)})
    d = Inode(size=2, blocks={1: range(11200, 11210), 2: range(11200, 11210), 3: range(11200, 11210)})

    # Tree test
    tree = Tree()
    #upload_main_inode(tree.marshal())
    # tree.mkdir('/home')
    # tree.mkdir('/home/horn')
    # tree.mkdir('/home/test')
    # tree.mkdir('/dom')
    # tree.mkdir('/home/test/dir1')
    #
    # tree.inodes['/']['home']['test'].update({'1.jpg': a})
    # tree.inodes['/']['home'].update({'2.jpg': b})
    # tree.inodes['/']['home'].update({'3.jpg': c})
    # tree.inodes['/']['home'].update({'3.jpg': d})

    # print tree

    # serialization
    #f = open('tree', 'wb')
    #f.write(tree.marshal())
    #f.close()

    # deserialization
    # f = open('tree')
    # tree_str = f.read()
    # print tree.unmarshal(tree_str)

    #upload_main_inode(tree.marshal())
    #tree_str = download_from_vk(tree=True)

    #print Tree.unmarshal(tree_str)

    cache = LRUCache(capacity=66)
    cache.set(a.id, (a.size, '/tmp/2.jpg'))
    cache.set(b.id, b)
    cache.set(c.id, c)
    cache.set(c1.id, c1)
    # hit the cache. c should be popped.
    cache.get(a.id)
    cache.get(b.id)
    cache.get(c1.id)
    cache.set(d.id, d)

    cache.get(a.id)