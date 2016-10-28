class Node:
    """Lightweight, nonpublic class for storing a doubly linked node."""
    #slots = element , prev , next # streamline memory

    def __init__(self, value, prev, next): # initialize node’s fields
        self.value = value # user’s element
        self.prev = prev # previous node reference
        self.next = next # next node reference

class LinkedDeque:
    """A base class providing a doubly linked list representation."""
 
    def __init__(self):
        """Create an empty list."""
        self.head = Node(None, None, None)
        self.tail = Node(None, None, None)
        
        self.head.next = self.tail # trailer is after header
        self.tail.prev = self.head # header is before trailer
        self.size = 0 # number of elements

    def __len__(self):
        """Return the number of elements in the list."""
        return self.size

    def isEmpty(self):
        """Return True if list is empty."""
        return self.size == 0

    def insert_between(self, value, predecessor, successor):
        """Add element e between two existing nodes and return new node."""

        newest = Node(value, predecessor, successor) # linked to neighbors
        predecessor.next = newest
        successor.prev = newest
        self.size += 1
        return newest

    def delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        value = node.value # record deleted element
        node.prev = node.next = node.value = None
        return value # return deleted element

    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.isEmpty( ):
            raise Exception("Deque is empty")
        return self.head.next.value # real item just after header

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.isEmpty( ):
            raise Exception("Deque is empty")
        return self.tail.prev.value # real item just before trailer

    def insert_first(self, value):
        """Add an element to the front of the deque."""
        predecessor = self.head
        successor = self.head.next

        newest = Node(value, predecessor, successor) # linked to neighbors
        predecessor.next = newest
        successor.prev = newest
        self.size += 1
        return newest
        
    def insert_last(self, value):
        """Add an element to the back of the deque."""
        predecessor = self.tail.prev
        successor = self.tail
        
        newest = Node(value, predecessor, successor) # linked to neighbors
        predecessor.next = newest
        successor.prev = newest
        self.size += 1
        return newest


    def delete_first(self):
        """ Remove and return the element from the front of the deque.
            Raise Empty exception if the deque is empty."""

        if self.isEmpty():
            raise Exception("Deque is empty")
            
        node = self.head.next
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        element = node.value # record deleted element
        node.prev = node.next = node.value = None
        return element # return deleted element
        

    def delete_last(self):
        """ Remove and return the element from the back of the deque.
            Raise Empty exception if the deque is empty."""

        if self.isEmpty():
            raise Exception("Deque is empty")
        
        node = self.tail.prev
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        element = node.value # record deleted element
        node.prev = node.next = node.value = None
        return element # return deleted element
    
    def __iter__(self):
        """Iterator of values in the list."""
        n = self.head
        while n != None:
            yield n.value
            n = n.next
        
    def __repr__(self):
        """String representation of linked list."""
        if self.size == 0:
            return 'link:[]'

        return 'deque:[{0:s}]'.format(','.join(map(str,self)))
    
d = LinkedDeque()
d.insert_first('one')
d.insert_first('two')
x = d.insert_first('three')

y = d.insert_last('eight')
d.insert_between('one', x, y)
d