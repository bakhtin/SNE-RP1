from inode import Inode, Tree
import pickle

if __name__ == "__main__":

    # Inode test
    a = Inode(123, 555211, range(11200, 11210))
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
