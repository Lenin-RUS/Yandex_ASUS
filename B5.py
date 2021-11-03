def height(node):
    if node is None:
        return -1
    else:
        i_left = height(node.left)
        i_right = height(node.right)
        return 1 + max(i_left, i_right)

def solution(root):
    left=0
    right=0
    if root.left:
        left=height(root.left)-1
    if root.right:
        right=height(root.right)-1
    if abs(left-right)<=1:
        return True
    else:
        return False


class Node:
    def __init__(self, value=0, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


node10 = Node(840, None, None)
node9 = Node(708, None, None)
node8 = Node(609, None, None)
node7 = Node(568, None, node8)
node6 = Node(626, None, None)
node5 = Node(649, node6, node9)
node4 = Node(818, node5, node10)
node3 = Node(270, None, None)
node2 = Node(355, node3, None)
node1 = Node(460, node2, node4)

print(solution(node1))