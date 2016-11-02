class KVPair:
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __eq__(self,other):
        if type(self) != type(other):
            return False

        return self.key == other.key

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value

    def __hash__(self):
        return hash(self.key)

class HashMap:

    def __init__(self):
        self.hSet = hashset.HashSet()

    def __len__(self):
        return len(self.hSet)

    def __contains__(self,item):
        return HashSet.__KVPair(item,None) in self.hSet

    def not__contains__(self,item):
        return item not in self.hSet

    def __setitem__(self,key,value):
        self.hSet.add(HashMap.__KVPair(key,value))

    def __getitem__(self,key):
        if HashMap.KVPair(key,None) in self.hSet:
            val = self.hSet[HashMap.KVPair(key,None)].getValue()
            return val

        raise KeyError("Key " + str(key) + " not in HashMap")

    def __iter__(self):
        for x in self.hSet:
            yield x.getKey()