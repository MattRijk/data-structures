
class Node(object):
    
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleList(object):
    
    head = None
    tail = None
    
    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
            
    def remove(self, node_value):
        current_node = self.head
        
        while current_node is not None:
            if current_node.data == node_value:
                # if it is not the first element
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev 
                else:
                    # otherwise we have no prev (it's None), head is next one, and prev becomes None
                    self.head = current_node.next
                    current_node.next.prev = None
                    
            current_node = current_node.next
            
    def show(self):
        print "Showing list data:"
        current_node= self.head
        while current_node is not None:
            print current_node.data, " -> ",
            current_node = current_node.next
        print None
        
d = DoubleList()

d.append("One")
d.append("Two")
d.append("Three")
d.append("Four")

d.show()

d.remove("Three")

d.show()



        