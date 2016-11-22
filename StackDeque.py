from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
        
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False
        
    def __len__(self):
        return len(self.stack)
    
    def push(self, value):
        return self.stack.append(value) # O(1)

    def pop(self):
        return self.stack.pop() # O(1)
    
    def __iter__(self):
        return iter(self.stack)
                       
        
    def __repr__(self):
        if len(self.stack) == 0:
            return 'Stack is Empty'
        return 'Stack:[{0:s}]'.format(', '.join(map(str,self.stack)))