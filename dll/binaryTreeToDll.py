'''
Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place. 
The left and right pointers in nodes are to be used as previous and next pointers respectively 
in converted DLL. The order of nodes in DLL must be same as Inorder of the given Binary Tree. 
The first node of Inorder traversal (left most node in BT) must be head node of the DLL.
'''
from dll import DLL
from dll import Node

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root, dll):
    if root:
        inorder(root.left, dll)
        if dll.head is None:
            dll.head = root
            dll.tail = root
        else:
            dll.tail.next = root
            dll.tail = root
        inorder(root.right, dll)

def btToDll(root):
    result = DLL()
    inorder(root, result)
    return result

def btToDllInPlace(root, head):
    if root is None:
        return
    btToDllInPlace(root.right, head)
    root.right = head[0]
    if head[0]:
        head[0].left = root
    head[0] = root
    btToDllInPlace(root.left, head)
    

root = TreeNode(10)
root.left = TreeNode(12)
root.right = TreeNode(15)
root.left.left = TreeNode(25)
root.left.right = TreeNode(30)
root.right.left = TreeNode(36)
#btToDll(root).printList()
head = [None]
btToDllInPlace(root, head)
current = head[0]
while current:
    print current.data,
    current = current.right
