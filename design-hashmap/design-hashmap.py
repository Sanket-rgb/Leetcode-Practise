class MyHashMap:

    def __init__(self):
        self.size = 1000000
        self.table = [None] * self.size
        
    def hash_value(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hv = self.hash_value(key)
        
        self.table[hv] = value

    def get(self, key: int) -> int:
        hv = self.hash_value(key)
        
        if self.table[hv] == None:
            return -1
        else:
            return self.table[hv]

    def remove(self, key: int) -> None:
        hv = self.hash_value(key)
        
        if self.table[hv] != None:
            self.table[hv] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)