from collections import MutableMapping
import random

class Item:
    '''Lightweight composite to store key-value pairs as map items.'''
    __slots__ = '_key','_value'

    def __init__(self, k, v):
        self._key = k
        self._value = v

    def __eq__(self, other):
        return self._key == other._key # compare items based on their keys

    def __ne__(self, other):
        return not (self == other) # opposite of eq

    def __lt__(self, other):
        return self._key < other._key # compare items based on their keys
    
    def __repr__(self):
        return '{}:{}'.format(str(self._key),str(self._value))

class Map(MutableMapping):
    '''Map implementation using an unordered list.'''

    def __init__(self):
        '''Create an empty map.'''
        self._table = [] # list of Item’s

    def __getitem__(self, k):
        '''Return value associated with key k (raise KeyError if not found).'''
        for item in self._table:
            if k == item._key:
                return item._value
            raise KeyError( 'Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        '''Assign value v to key k, overwriting existing value if present.'''
        for item in self._table:
            if k == item._key: # Found a match:
                item._value = v # reassign value
                return # and quit
        # did not find match for key
        self._table.append(Item(k,v))

    def __delitem__(self, k):
        '''Remove item associated with key k (raise KeyError if not found).'''
        for j in range(len(self._table)):
            if k == self._table[j]._key: # Found a match:
                self._table.pop(j) # remove item
                return # and quit
            raise KeyError( 'Key Error: ' + repr(k))

    def __len__(self):
        '''Return number of items in the map.'''
        return len(self._table)

    def __iter__(self):
        '''Generate iteration of the map s keys.'''
        for item in self._table:
            yield item._key
            
    def __repr__(self):
        return '{}'.format([item for item in self._table])


class HashTable(Map):
    '''Abstract base class for map using hash-table with MAD compression.'''

    def __init__(self, cap=11, p=109345121):
        '''Create an empty hash-table map.'''
        self._table = cap * [ None ]
        self._n = 0 # number of entries in the map
        self._prime = p # prime for MAD compression
        self._scale = 1 + random.randrange(p-1) # scale from 1 to p-1 for MAD
        self._shift = random.randrange(p) # shift from 0 to p-1 for MAD

    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k) # may raise KeyError

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v) # subroutine maintains self. n
        if self._n > len(self._table) // 2: # keep load factor <= 0.5
            self._resize(2 * len(self._table) - 1) # number 2ˆx - 1 is often prime

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k) # may raise KeyError
        self._n -= 1
        
    def __len__(self):
        '''Return number of items in the map.'''
        return len(self._table)


    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError( 'Key Error: ' + repr(k)) # no match found
        return bucket[k] # may raise KeyError

   
    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = Map( ) # bucket is new to the table
            oldsize = len(self._table[j])
            self._table[j][k] = v
            if len(self._table[j]) > oldsize: # key was new to the table
                self._n += 1 # increase overall map size

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError( 'Key Error: ' + repr(k)) # no match found
        del bucket[k] # may raise KeyError
        
    def __iter__(self):
        for bucket in self._table:
            if bucket is not None: # a nonempty slot
                for key in bucket:
                    yield key


    def _resize(self, c): # resize bucket array to capacity c
        old = list(self.items( )) # use iteration to record existing items
        self._table = c * [None] # then reset table to desired capacity
        self._n = 0 # n recomputed during subsequent adds
        for(k,v) in old:
            self[k] = v # reinsert old key-value pair
            
    def __repr__(self):
        return str(self._table)
            
            
H = HashTable()
H['one'] = 1
H['two'] = 2
H['three'] = 3

H['four'] = 4
H['five'] = 5
H['six'] = 88
H