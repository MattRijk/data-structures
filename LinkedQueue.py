class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next  = next

    def __str__(self):
        return str(self.value)

class LinkedQueue:
    
    def __init__(self):
        self.length = 0
        self.head = None

    def isEmpty(self):
        return self.length == 0

    def enqueue(self, value):
        node = Node(value)
        if self.head is None:
            # If list is empty the new node goes first
            self.head = node
        else:
            # Find the last node in the list
            last = self.head
            while last.next:
                last = last.next
            # Append the new node
            last.next = node
        self.length += 1

    def dequeue(self):
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        return value
    
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
        return 'linked queue:[{0:s}]'.format(', '.join(map(str,self)))
    
q = LinkedQueue()
q.enqueue('one')
q.enqueue('two')
q.dequeue()
q