class Node:
    def __init__(self, value, tail=None):
        self.value = value
        self.next = tail
        
    def __repr__(self):
        return str(self.value)
        
        
class LinkedStack:
    """ Reversing a singly linked list of a list-stack """
        
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def push(self, val):
        self.head = Node(val, self.head)
        self.size += 1
        
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        val = self.head.value
        self.head = self.head.next
        self.size -= 1
        return val
            
    def find(self, node):
        temp = self.head
        while None != temp and temp.value != node:
            temp = temp.next
        return temp
        
        
        
    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.head.value 
    
    def __iter__(self):
        node = self.head
        while node != None:
            yield node.value
            node = node.next      
        
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

  
    def __repr__(self):
        if self.head is None:
            return 'LinkList:[]'
        
        return 'LinkedList:[{0:s}]'.format(','.join(map(str,self)))
    
            
        

    
n1= Node('one')
n2= Node('two')
n3= Node('three')
n4= Node('four')
n5= Node('five')

stack = LinkedStack()
# stack.push(n1)
# stack.push(n2)
# stack.push(n3)
# stack.push(n4)
# stack.push(n5)


print('')

# three
# two
# one
#stack

#stack.reverse()
# reversed pointers
# one
# two
# three

stack.pop()
stack

#print(stack.find(n4))

#output
# LinkedList:[three,two,one]

# LinkedList:[one,two,three]