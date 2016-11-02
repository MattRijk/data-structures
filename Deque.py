# Deque using double linked list

class Node:
    
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next
  
class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, value):
        """Function to add an element to the tail of the list """
        new_node = Node(value, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def addleft(self, value):
        """Function to add an element to the head of the list """
        new_node = Node(value, None, None)
        
        if self.head == None:
            self.head = self.tail = new_node
            self.head.prev = self.tail.next = None    
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
            
    def popleft(self): 
        """ Function to delete a node from head """
        if self.head is None:
            return None
    
        n = self.head
        if self.head.next is not None:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
        
        return n

            
    def pop(self):
        """ Function to delete a node from tail """
        if self.head is None:
            return None
        
        n = self.tail
        
        if self.tail.prev is not None:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = None
        
        return n 
            

    def remove(self, val): # O(n)
		""" Function to delete a node item from list """
        if self.head is None:
            return None
        
        n = self.head
        
        while n is not None:
            if n.value == val:
                # if it is not the first element
                if n.prev is not None:
                    n.prev.next = n.next 
                else:
                    # otherwise we have no prev (it's None), head is next one, and prev becomes None
                    self.head = n.next
                    n.next.prev = None
            n = n.next
			
    def find(self, value):
		""" Function to find a node in list """
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False
		
	def reverse(self):
		""" Function to reverse items in list """
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
            
    def __iter__(self):
        """Iterator of values in the list."""
        n = self.head
        while n != None:
            yield n.value
            n = n.next
        
    def __repr__(self):
        """String representation of linked list."""
        if self.head is None:
            return 'link:[]'

        return 'deque:[{0:s}]'.format(','.join(map(str,self)))
        
A = Deque()      
A.add('one') # add to back 
A.add('two')
A.add('three')
A.add('four')

A.addleft('eight') # add to front

# deque:[eight,one,two,three,four]

A.remove('two')
A.pop()
A.popleft()
A.remove('one')

A.add('two')
A.add('twelve')
A.add('four')

# deque:[three,two,twelve,four]
A.reverse()
A
A.find('two')