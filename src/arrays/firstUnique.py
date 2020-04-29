"""
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.


Example 1:

Input:
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output:
[null,2,null,2,null,3,null,-1]

Explanation:
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1

Example 2:

Input:
["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
Output:
[null,-1,null,null,null,null,null,17]

Explanation:
FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique(); // return -1
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
firstUnique.showFirstUnique(); // return 17

Example 3:

Input:
["FirstUnique","showFirstUnique","add","showFirstUnique"]
[[[809]],[],[809],[]]
Output:
[null,809,null,-1]

Explanation:
FirstUnique firstUnique = new FirstUnique([809]);
firstUnique.showFirstUnique(); // return 809
firstUnique.add(809);          // the queue is now [809,809]
firstUnique.showFirstUnique(); // return -1



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^8
1 <= value <= 10^8
At most 50000 calls will be made to showFirstUnique and add.
   Hide Hint #1
Use doubly Linked list with hashmap of pointers to linked list nodes. add unique number to the linked list. When add is called check if the added number is unique then it have to be added to the linked list and if it is repeated remove it from the linked list if exists. When showFirstUnique is called retrieve the head of the linked list.
   Hide Hint #2
Use queue and check that first element of the queue is always unique.
   Hide Hint #3
Use set or heap to make running time of each function O(logn).

https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3313/
"""
import collections
from collections import Counter, deque
from typing import List


class FirstUnique:
    # 904 ms
    def __init__(self, nums: List[int]):
        self.c = Counter(nums)
        self.d = deque(nums)

    def showFirstUnique(self) -> int:
        while self.d and self.c[self.d[0]] != 1:
            self.d.popleft()
        return self.d[0] if self.d else -1

    def add(self, value: int) -> None:
        self.c[value] += 1
        self.d.append(value)

    """
    #896 ms
    def __init__(self, nums: List[int]):
        self.d = collections.OrderedDict()
        for num in nums:
            self.d[num] = self.d.get(num, 0) + 1
        self.removed = set()
        for key in list(self.d.keys()):
            if self.d[key] > 1:
                self.removed.add(key)
                self.d.pop(key)

        print(self.d)
        print(next(iter(self.d)))

    def showFirstUnique(self) -> int:
        return next(iter(self.d)) if self.d else -1

    def add(self, value: int) -> None:
        if value not in self.removed:
            if value in self.d:
                self.d.pop(value)
                self.removed.add(value)
            else:
                self.d[value] = 1
    """
    """
    # 900 ms
    def __init__(self, nums: List[int]):
        self.queue = collections.deque()
        self.dictionary = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if len(self.queue) == 0:
            return -1
        while len(self.queue) > 0 and self.queue[0] in self.dictionary and self.dictionary[self.queue[0]] >= 2:
            self.queue.popleft()
        if len(self.queue) == 0:
            return -1
        return self.queue[0]

    def add(self, value: int) -> None:
        if value in self.dictionary:
            self.dictionary[value] += 1
        else:
            self.dictionary[value] = 1

        self.queue.append(value)
    """

# Main Call
nums = ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]

firstUnique = FirstUnique(nums)
print(firstUnique.showFirstUnique())
firstUnique.add(5)
print(firstUnique.showFirstUnique())
firstUnique.add(2)
print(firstUnique.showFirstUnique())
firstUnique.add(3)
print(firstUnique.showFirstUnique())

