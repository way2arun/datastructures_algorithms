"""
Design HashMap
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);
hashMap.put(2, 2);
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found)

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
"""
import math


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Solution - 884 ms
        """
        self.golden_ratio = 1.618
        self.table_size = 65536
        self.table = [[] for _ in range(self.table_size)]
        self.hash = lambda i: i * math.ceil(self.golden_ratio * self.table_size) % self.table_size
        """
        # Solution 2 - 176 ms
        self.dict = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # Solution - 884 ms
        """
        self.remove(key)  # use the function you wrote already!
        hkey = self.hash(key)
        self.table[hkey].append((key, value))
        """
        # Solution 2 - 176 ms
        self.dict[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        # Solution - 884 ms
        """
        hkey = self.hash(key)
        ix = -1
        for i, x in enumerate(self.table[hkey]):
            if x[0] == key:
                ix = i
        return -1 if ix == -1 else self.table[hkey][ix][1]
        """
        # Solution 2 - 176 ms
        if key in self.dict:
            return self.dict[key]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        # Solution - 884 ms
        """
        hkey = self.hash(key)
        ix = -1
        for i, x in enumerate(self.table[hkey]):
            if x[0] == key:
                ix = i
        if ix >= 0:
            del self.table[hkey][ix]
        """
        # Solution 2 - 176 ms
        if key in self.dict:
            del self.dict[key]


# Main Call
obj = MyHashMap()
key = 1
value = 1
obj.put(key, value)
param_2 = obj.get(key)
print(param_2)
obj.remove(key)
