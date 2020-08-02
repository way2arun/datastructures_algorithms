"""
Design HashSet
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3410/
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet.
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);
hashSet.add(2);
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);
hashSet.contains(2);    // returns true
hashSet.remove(2);
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.
"""


class MyHashSet:

    # Solution 1 - 300 ms
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Solution 1 - 300 ms
        self.val = [False] * (1000000 - 1)
        # Solution 2 - 136 ms
        self.hash_set = bytearray(1000001)

    def add(self, key: int) -> None:
        # Solution 1 -  300 ms
        self.val[key] = True
        # Solution 2 - 136 ms
        if not self.hash_set[key]:
            # set to True for existence of incoming element
            self.hash_set[key] = True

    def remove(self, key: int) -> None:
        # Solution 1 - 300 ms
        self.val[key] = False
        # Solution 2 - 136 ms
        if self.hash_set[key]:
            # clear to False for removal
            self.hash_set[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        # Solution 1 - 300 ms
        #return self.val[key]

        # Solution 2 - 136 ms
        if self.hash_set[key]:
            return True

        else:
            return False


# Main Call
hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(2)
print(hashSet.contains(1))
print(hashSet.contains(3))
hashSet.add(2)
print(hashSet.contains(2))
hashSet.remove(2)
print(hashSet.contains(2))
