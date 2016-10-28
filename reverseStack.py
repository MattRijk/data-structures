"""
Stack: ReverseStack(Stack: values)
    Stack: new_stack
    While (<values is not empty>)
        new_stack.Push(values.Pop())
    End While
    Return new_stack
End ReverseStack
"""

class Stack:
    def __init__(self):
        self.value = None
        self.stack = []
        
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False
        
    def add(self, value):
        return self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()
        
    def __repr__(self):
        return str(self.stack)
pass

s1 = Stack()
s1.add('one')
s1.add('two')
s1.add('three')
s1.add('four')
s1

def reverseStack(stack):
    s = Stack()
    while stack.isEmpty() == False:
        s.add(stack.pop())
    return s

reverseStack(s1)