"""Prefix Tree a pointer based alternative"""
wordkey = '\n' # any character not 'a' .. 'z'

class PrefixTree:
    def __init__(self):
        self.head = {}
        
    def add(self, value):
        """Add value to prefix tree. Return TRUE if updated."""
        d = self.head
        
        while len(value) > 0:
            c = value[0]
            if c not in d:
                d[c] = {}
                
            d = d[c]
            value = value[1:]
        
        if wordkey in d:
            return False
        
        d[wordkey] = True
        return True
    
    def __contains__(self, value):
        """ determine if value in prefix tree"""
        
        d = self.head
        while len(value) > 0:
            c = value[0]
            if c not in d:
                return False
            
            d = d[c]
            value = value[1:]
            
        return wordkey in d

d = PrefixTree()
d.add('inch')
'add' in d