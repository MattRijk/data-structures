"""
    Demonstration of Linked Lists in Python.
"""
class LinkedNode:
    
    def __init__(self, value, tail=None):
        self.value = value
        self.next = tail
        
class LinkedList:
    
    def __init__(self, *start):
        self.head = None
        for _ in start:
            self.prepend(_)
            
    def prepend(self, value):
        self.head = LinkedNode(value, self.head)
        
    def pop(self):
        if self.head is None:
            raise Exception("Linked list is empty")
        val = self.head.value
        self.head = self.head.next
        return val
    
    def remove(self, value):
        n = self.head
        last = None
        while n != None:
            if n.value == value:
                if last is None:
                    self.head = self.head.next
                else:
                    last.next = n.next
                return True
            
            last = n    # update last
            n = n.next
        return False
    
    def __len__(self):
        n = self.head
        count = 0
        while n != None:
            count += 1
            n = n.next
        return count
    
    def reverseLinks(self):
        last = None
        n = self.head
        while n != None:
            next = n.next
            n.next = last
            last = n
            n = next
        self.head = last
        
    def __iter__(self):
        n = self.head
        while n != None:
            yield n.value
            n = n.next
    
    def __repr__(self):
        if self.head is None:
            return 'link:[]'
        return '[{0:s}]'.format(', '.join(map(str,self)))