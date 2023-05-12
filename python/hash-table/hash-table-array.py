class HashTable:
    def __init__(self, size):
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % len(self.table)

    ''' Note that to handle collisions (that is, when two different keys are mapped to the same index in the hash table), 
        the implementation uses a linked list to store the key-value pairs corresponding to each index in the hash table. 
        When two different keys are mapped to the same index, the lists are simply concatenated. '''
    def add(self, key, value):
        hash = self._hash_function(key)
        bucket = self.table[hash]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    # Implements get, exists and remove here


hashTable = HashTable(10)

hashTable.add("10", "Brazil")
hashTable.add("10", "Germany")
hashTable.add("11", "Argentina")