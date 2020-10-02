'''
Given a ternary tree, create a doubly linked list out of it. 
A ternary tree is just like binary tree but instead of having two nodes, 
it has three nodes i.e. left, middle, right.

The doubly linked list should holds following properties -

1. Left pointer of ternary tree should act as prev pointer of doubly linked list.
2. Middle pointer of ternary tree should not point to anything.
3. Right pointer of ternary tree should act as next pointer of doubly linked list.
4. Each node of ternary tree is inserted into doubly linked list before its subtrees and for any node,
its left child will be inserted first, followed by mid and right child (if any).
'''
from dll import DLL
from dll import Node

class TernaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.mid = None

def preorder(root, dll):
    if root:
        dll.append(root.data),
        preorder(root.left, dll)
        preorder(root.mid, dll)
        preorder(root.right, dll)

def ternaryTreeToDll(root):
    result = DLL()
    preorder(root, result)
    return result

a = TernaryTreeNode(30)
a.left = TernaryTreeNode(5)
a.mid = TernaryTreeNode(11)
a.right = TernaryTreeNode(63)
a.left.left = TernaryTreeNode(1)
a.left.mid = TernaryTreeNode(4)
a.left.right = TernaryTreeNode(8)
a.mid.left = TernaryTreeNode(6)
a.mid.mid = TernaryTreeNode(7)
a.mid.right = TernaryTreeNode(15)
a.right.left = TernaryTreeNode(31)
a.right.mid = TernaryTreeNode(55)
a.right.right = TernaryTreeNode(65)
ternaryTreeToDll(a).printList()



