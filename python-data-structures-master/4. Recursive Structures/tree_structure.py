class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return self.data

    def inorder(self):
        if self.left is not None:
            yield from self.left.inorder()
        yield self.data
        if self.right is not None:
            yield from self.right.inorder()

    def preorder(self, node):
        if node is not None:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

    def size(self):
        return 1 + (self.left.size()  if self.left  is not None else 0) \
                 + (self.right.size() if self.right is not None else 0)
        

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)

print('tree size: {}'.format(tree.size()))

for data in tree.inorder():
    print(data, end=' ')