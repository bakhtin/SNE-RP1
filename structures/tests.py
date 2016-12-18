from inode import Inode, Tree

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

    tree.inodes['/']['home'].update({'1.jpg': a})
    tree.inodes['/']['home'].update({'2.jpg': b})
    tree.inodes['/']['home'].update({'3.jpg': c})

    print tree