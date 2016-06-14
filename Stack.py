# List as Stack
# Stack is abstract data type
#   - push(v) to add value to top of stack
#   - pop() removes topmost value and returns it
#   - isEmpty() determines if stack is empty
    
    
class Stack:
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, v):
        self.stack.append(v)
        
    def pop(self):
        return self.stack.pop()
    

    def __repr__(self):
        return str(self.stack)
    
s = Stack()
s.push('one')
s.push('two')
s.push('three')
s
s.pop()
s