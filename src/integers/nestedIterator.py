"""
Flatten Nested List Iterator
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.


Example 1:

Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].


Constraints:

1 <= nestedList.length <= 500
The values of the integers in the nested list is in the range [-106, 106].
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from collections import deque





#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    # Solution 1 - 64 ms
    """
    def __init__(self, nestedList):
        self.deq = nestedList[::-1]

    def FixDeque(self):
        last = self.deq.pop()
        for e in last.getList()[::-1]:
            self.deq.append(e)

    def next(self):
        first = self.deq[-1]
        if first.isInteger():
            self.deq.pop()
            return first.getInteger()
        else:
            self.FixDeque()
            return self.next()

    def hasNext(self):
        while self.deq and not self.deq[-1].isInteger():
            self.FixDeque()
        return self.deq
    """

    def __init__(self, nestedList: [NestedInteger]):
        def _flatten(nested, flat):
            for ni in nested:
                if ni.isInteger():
                    flat.append(ni.getInteger())
                else:
                    _flatten(ni.getList(), flat)
            return

        self.current = 0
        self.flattened = []
        _flatten(nestedList, self.flattened)
        # print(self.flattened)

    def next(self) -> int:
        result = self.flattened[self.current]
        self.current += 1
        return result

    def hasNext(self) -> bool:
        return self.current < len(self.flattened)


# Your NestedIterator object will be instantiated and called as such:
nestedList = [[1, 1], 2, [1, 1]]
i, v = NestedIterator(nestedList), []
while i.hasNext():
    v.append(i.next())