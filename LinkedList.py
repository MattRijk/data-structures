class Node:
	def __init__(self, value, next):
		self.value = value
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_head(self, value):
		# Insert value at beginning
		temp = Node(value, self.head)
		self.head = temp

	def insert_at_end(self, value):
		# Insert value at end
		current = self.head

		if current == None:
			self.head = Node(value, None)
		else:
			while current.next:
				current = current.next
			current.next = Node(value, None)

	def delete(self, value):
		# Delete the first instance of value from the list
		current = self.head 

		if current.value == value:
			self.head = current.next
			current = current.next

		while current.next:
			if current.next.value == value:
				current.next = current.next.next
			if current.next != None:
				current = current.next
			else:
				break

	def print_list(self):
		current = self.head
		while current:
			print current.value,
			current = current.next
		print


ll = LinkedList()
ll.insert_at_head(4)
ll.insert_at_head(3)
ll.insert_at_head(2)

ll.print_list() #2, 3, 4

ll.insert_at_end(5)
ll.print_list() #2, 3, 4, 5

ll.delete(4)
ll.print_list() #3, 5

ll.delete(5)
ll.delete(2)
ll.print_list() #3