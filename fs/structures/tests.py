from inode import Inode, Tree

if __name__ == "__main__":

    # Inode test
    a = Inode(id=123, size=555211, blocks={1: range(11200, 11210), 2: range(11200, 11210), 3: range(11200, 11210)})
    b = Inode(124, 110001, range(11200, 11210))
    c = Inode(125, 4451, range(11200, 11210))

    # Tree test
    tree = Tree()

    tree.mkdir('/home')
    tree.mkdir('/home/horn')
    tree.mkdir('/home/test')
    tree.mkdir('/dom')
    tree.mkdir('/home/test/dir1')

    tree.inodes['/']['home']['test'].update({'1.jpg': a})
    tree.inodes['/']['home'].update({'2.jpg': b})
    tree.inodes['/']['home'].update({'3.jpg': c})

    print tree

    # serialization
    f = open('tree', 'wb')
    f.write(tree.marshal())
    f.close()

    # deserialization
    f = open('tree')
    tree_str = f.read()
    print tree.unmarshal(tree_str)

    sub = tree.inodes
    path_components = tree._path_dissect('/home/3.jpg')
    for i in path_components[:-1]:
        sub = sub[i]
    t = sub.pop(path_components[-1])



    print t