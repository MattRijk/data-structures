class Node:
    def __init__(self, value, tail=None):
        self.value = value
        self.next = tail
          
    
class LinkedList:
    def __init__(self, *start):
        self.head = None
        
        for _ in start:
            self.prepend(_)
            
    def prepend(self, value):
        self.head = Node(value, self.head)
        
    def __iter__(self):
        """Iterator of value in LinkedList"""
        n = self.head
        while n != None:
            yield n.value
            n = n.next
    
    def __repr__(self):
        if self.head is None:
            return 'LinkList:[]'
        
        return 'LinkedList:[{0:s}]'.format(','.join(map(str,self)))
        
    def reverseList(self, head):
        result = Node
        node = head
        while node != None:
            tmp = node.next
            node.next = result
            result = node
            node = temp
        return result

n1 = Node('one')
n2 = Node('two')
n1.value
n1.next = n2
n1.next.value

alist = LinkedList()
alist.prepend('one')
alist.prepend('two')
alist    
            