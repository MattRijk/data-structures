# hierarchical
# recursive

class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.numLeft = 0
        
    def adjustCount(self, value, delta):
        if value < self.value:
            self.numLeft += delta
            if self.left:
                self.left.adjustCount(value, delta)
        elif value > self.value:
            if self.right:
                self.right.adjustCount(value, delta)
        
    def add(self, value):
        if value <= self.value:
            # add to left
            self.left = self.addToSubTree(self.left, value)
        elif value > self.value:
            # add to right
            self.right = self.addToSubTree(self.right, value)

    
    def addToSubTree(self, parent, value):
        if parent is None:
            return BinaryNode(value)
        parent.add(value)
        return parent
    
    def remove(self, value):
        if value < self.value:
            self.left = self.removeFromParent(self.left, value)
        elif value > self.value:
            self.right = self.removeFromParent(self.right, value)
        else:
            if self.left is None:
                return self.right
            
            # find largest value in left subtree
            child = self.left
            while child.right:
                child = child.right
                
            childKey = child.value
            self.left = self.removeFromParent(self.left, childKey)
            self.value = childKey
            
        return self
    
    def removeFromParent(self, parent, value):
        if parent:
            return parent.remove(value)
        return None
    
    def inorder(self):
        if self.left:
            for v in self.left.inorder():
                yield v
        yield self.value
        
        if self.right:
            for v in self.right.inorder():
                yield v
                
    
# O log(n)
# search
# add
# remove
# iterate

class BinaryTree:
    def __init__(self, *start):
        self.root = None
        
        for _ in start:
            self.add(_)
    
    def getMin(self):
        if self.root is None:
            raise ValueError("Binary Tree is Empty")
        n = self.root
        while n.left:
            n = n.left
        return n.value
    
    def getMax(self):
        if self.root is None:
            raise ValueError("Binary Tree is Empty")
        n = self.root
        while n.right:
            n = n.right
        return n.value

    def add(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
            return True
        else:
            if value in self:
                return False
            ret = self.root.add(value)
            self.root.adjustCount(value, +1)
    
    def remove(self, value):
        if value in self:
            self.root = self.root.remove(value)
            self.root.adjustCount(value, -1)
            
            
    def __iter__(self):
        if self.root:
            for v in self.root.inorder():
                yield v
    
    def __contains__(self, target):
        node = self.root
        while node is not None:
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                return True
        return False

# find value closest to a certain target
    def closest(self, target):
        if self.root is None:
            return None
        # start at top
        node = self.root
        best = node
        distance = abs(self.root.value - target)
        while node:
            if abs(node.value - target) < distance:
                best = node
                distance = abs(node.value < target)
            
            
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else: 
                return target
        return best.value

        
b = BinaryTree(7, 5, 1, 2)
b
b.add(3)

b.root.value
7 in b
b.root.value
b.root.left.left.value
b.getMin()
b.getMax()
b.remove(3)
b.closest(3)
for _ in b:
    print(_)