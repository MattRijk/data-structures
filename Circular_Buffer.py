# information hiding
# separating structure from function
# Using a Circular buffer -> Queue behavior
    # - add to the end 
    # - remove fron the front
    # - these operations become O(1) always

class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None]*size
        self.low = 0
        self.high = 0
        self.count = 0
        
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == self.size
    
    def add(self, value):
        if self.isFull():
            self.low = (self.low+1) % self.size
        else:
            self.count += 1
        self.buffer[self.high] = value
        self.high = (self.high+1) % self.size
    
    def remove(self):
        if self.count == 0:
            raise Exception("Circular buffer is empty")
        value = self.buffer[self.low]
        self.low = (self.low+1) % self.size
        self.count -= 1
        return value
    
    def __iter__(self):
        idx = self.low
        num = self.count
        while num > 0:
            yield self.buffer[idx]
            idx = (idx+1) % self.size
            num -= 1
            
    def __repr__(self):
        if self.isEmpty():
            return 'cb:[]'
        return 'cb:[' + ','.join(map(str,self)) + ']'
        

c = CircularBuffer(5)
c.add(10)
c.add(20)
c.add(8)
c.add(5)
c.add(7)
c.add(13)

c.buffer
c.high
c.low
c.remove()
c