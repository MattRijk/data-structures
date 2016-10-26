"""
Preorder tree traversal algorithm
- Visit the node
- Recursively visit its children


PreorderTraverse(node)
    Visit node
    PreorderTraverse(node.LeftChild)
    PreorderTraverse(node.RightChild)
"""
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def preorder(self, node):
        if node is not None:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)
            
    def __str__(self):
        return str(self.data)

node = Node(1)
data = node.preorder(node)
data