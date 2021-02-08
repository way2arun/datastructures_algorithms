"""
Peeking Iterator
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Example:

Assume that the iterator is initialized to the beginning of the list: [1,2,3].

Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.
You call next() the final time and it returns 3, the last element.
Calling hasNext() after that should return false.
Follow up: How would you extend your design to be generic and work with all types, not just integer?

   Hide Hint #1
Think of "looking ahead". You want to cache the next element.
   Hide Hint #2
Is one variable sufficient? Why or why not?
   Hide Hint #3
Test your design with call order of peek() before next() vs next() before peek().
   Hide Hint #4
For a clean implementation, check out Google's guava library source code. https://github.com/google/guava/blob/703ef758b8621cfbab16814f01ddcc5324bdea33/guava-gwt/src-super/com/google/common/collect/super/com/google/common/collect/Iterators.java#L1125

"""


# Below is the interface for Iterator, which is already defined for you.
#
class Iterator:
     def __init__(self, nums):
         """
         Initializes an iterator object to the beginning of a list.
         :type nums: List[int]
         """

     def hasNext(self):
         """
         Returns true if the iteration has more elements.
         :rtype: bool
         """

     def next(self):
         """
         Returns the next element in the iteration.
         :rtype: int
         """

class PeekingIterator:

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        # Solution 1 - 32 ms
        """
        self.iterator = iterator
        self.to_peek = self.iterator.next() if self.iterator.hasNext() else None
        """
        # Solution 2 - 12 ms
        self.pk = None
        self.iter = iterator
        if self.iter.hasNext():
            self.pk = self.iter.next()


    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        #return self.to_peek
        return self.pk

    def next(self):
        """
        :rtype: int
        """
        """
        temp = self.to_peek
        self.to_peek = self.iterator.next() if self.iterator.hasNext() else None
        return temp
        """
        temp = self.pk
        if self.iter.hasNext():
            self.pk = self.iter.next()
        else:
            self.pk = None
        return temp


    def hasNext(self):
        """
        :rtype: bool
        """
        #return self.to_peek is not None

        return self.pk is not None
# Your PeekingIterator object will be instantiated and called as such:
# ["PeekingIterator","next","peek","next","next","hasNext"]
nums = [[[1,2,3]],[],[],[],[],[]]
iter = PeekingIterator(Iterator(nums))
print(iter.hasNext())
while iter.hasNext():
     val = iter.peek()   # Get the next element but not advance the iterator.
     iter.next()         # Should return the same value as [val].
     print(val)
