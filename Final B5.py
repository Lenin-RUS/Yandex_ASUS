my_node = [None, None, None, None]

def find_my_node(root, key):
    if root.left:
        if root.left.value == key:
            my_node[0] = root
            my_node[1] = root.left
        if root.value > key:
            find_my_node(root.left, key)

    if root.right:
        if root.right.value == key:
            my_node[0] = root
            my_node[1] = root.right
        if root.value < key:
            find_my_node(root.right, key)


def find_max_from_left(node):
    if node.right:
        my_node[2] = node
        find_max_from_left(node.right)
    else:
        my_node[3] = node


def remove(root, key):
    if root==None:
        return root

    if root.value == key:
        my_node[1] = root
    else:
        find_my_node(root, key)

    if my_node[1]:
        if my_node[1].left:
            my_node[2] = my_node[1]
            find_max_from_left(my_node[1].left)
    else:
        return root

    if not my_node[0]:
        # Если удаляем самый верхний элемент
        if my_node[3]:
            root = my_node[3]
            my_node[2].right = my_node[3].left
            my_node[3].left = my_node[1].left
            my_node[3].right = my_node[1].right
        else:
            root = my_node[1].right
        return root

    if my_node[3]:
        if my_node[0].left == my_node[1]:
            my_node[0].left = my_node[3]
        else:
            my_node[0].right = my_node[3]

        if my_node[2] == my_node[1]:
            my_node[3].right = my_node[1].right
        else:
            my_node[2].right = my_node[3].left
            my_node[3].left = my_node[1].left
            my_node[3].right = my_node[1].right
    else:
        if my_node[0].left == my_node[1]:
            my_node[0].left = my_node[1].right
        else:
            my_node[0].right = my_node[1].right
    return root


class Node:
    def __init__(self, value=0, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


node10 = Node(840, None, None)
node9 = Node(708, None, None)
node8 = Node(609, None, None)
node7 = Node(568, None, node8)
node6 = Node(626, node7, None)
node5 = Node(649, node6, node9)
node4 = Node(818, node5, node10)
node3 = Node(270, None, None)
node2 = Node(355, node3, None)
node1 = Node(460, node2, node4)

my_node = [None, None, None, None]

root = node1
target = 568
root = remove(root, target)
pass
