# Tournaments Science of Selecting a Winner
# 8 Teams in a single-elimination tournament
#   - who is the best team?
#   - 28 possible games(8*7/2)
# create a set of brackets
# 7 total games leads to winner
#  - 3-tier structure
#  - Note that log(8) = 3

# Heap-Based Structure
# Tree=based structure with following properties
# Heap: each node has value smaller than either child
# Shape: Tree filled by level, left to right

# Min-Heap Structure
# Minimal structure has impressive characteristics
# - Min in O(1) # you can find the smallest element in constant time
# - Add and Remove in O(log n)

Heap Array Representation
Elements stored in contiguous array A
- Root is A[0]
- Left child of A[i] is A[2*i+1]
- Right child of A[i] is A[2*i+2]
- Parent of A[i] is A[(i-1)//2]

# Heap requires less than 1/3rd of the space
class Heap:
	def __init__(self, value):
		self.arry = list(values)
		self.size = len(self.array)

class BinaryNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self):
		self.root = None

# Heap Construction
# Only consider internal nodes 
# Ensure A[i] maintains heap propery
# Do this in reverse order from last internal node to root
# Not sorting behavior 
#  - Start with full array
#  - Enforce heap propery only
"""
	Show how to implement Heap
"""
class Heap: 
	def __init__(self, value=None): # bottom up heapify
	"""Construct list from values"""
		if values is None:
			self.ar = []
		else:
			self.ar = list(values)
		self.n = len(self.ar)
	
		start = self.n//2 - 1
		for i in range(start, -1, -1):
			self.heapify(i)
	def isEmpty():
		"""Determine if heap is empty."""

	def __len__(self):
		"""Return size of heap."""

	def pop(self):
		if self.n == 0:
			raise ValueError("Heap is empty.")
		val = self.ar[0]
		self.n -=1
		self.ar[0] = self.ar[self.n]
		self.heapify(0)
		return val

    def add(self, value):
        """Add value to heap and repair heap."""
        if self.n == len(self.ar):
            self.ar.append(value)
        else:
            self.ar[self.n] = value
        i = self.n
        self.n += 1
        
        # Correct structure to root
        while i > 0:
            parent = (i-1) // 2
            if self.ar[i] < self.ar[parent]:
                self.ar[i],self.ar[parent] = self.ar[parent],self.ar[i]
                i = parent
            else:
                break
        
    def heapify(self, i):
        """Heapify sub-array [i, end)."""
        left = 2*i+1
        right = 2*i+2

        # Find smallest element of A[i], A[left], and A[right]
        if left < self.n and self.ar[left] < self.ar[i]:
            smallest = left
        else:
            smallest = i

        if right < self.n and self.ar[right] < self.ar[smallest]:
            smallest = right

        # If smallest is not already the parent then swap and propagate
        if smallest != i:
            self.ar[i],self.ar[smallest] = self.ar[smallest],self.ar[i]
            self.heapify (smallest)

    def __repr__(self):
        """Return representation of heap as array."""
        return 'heap:[' + ','.join(map(str,self.ar[:self.n])) + ']'


