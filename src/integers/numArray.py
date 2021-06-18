"""
Range Sum Query - Mutable
Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).


Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8


Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 104 calls will be made to update and sumRange.
"""
from typing import List
import numpy as np

class NumArray:
    # Solution 1 - 2648 ms
    """
    def __init__(self, nums: List[int]):
        self.nums = np.array(nums)

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return np.sum(self.nums[left: right + 1])
    """
    # Solution 2  - this is a working code, but getting time limit exceeded while executing on leetcode engine.
    """

    def __init__(self, nums: List[int]):
        self.nums = nums

        # create a prefix sum array
        # if nums = [2,1,3], then prefix = [0, 2, 3, 6]

        self.prefix = [0]
        for i in nums:
            self.prefix.append(self.prefix[-1] + i)
        self.n = len(self.prefix)

    def update(self, index: int, val: int) -> None:
        # get the difference between the previous value and the current update value
        # it is used to add this difference to the prefix sum array
        diff = val - self.nums[index]

        # aslo update the nums array as next time when this element will be updated, we dont want to
        # get the difference from the initial value of nums but from the latest updated value
        self.nums[index] = val

        # adjust the prefix sum
        for i in range(index + 1, self.n):
            self.prefix[i] += diff

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
    """
    # Solution 3 - 920 ms
    def __init__(self, nums: List[int]):
        self.nums = nums  # [:]
        self.total = sum(self.nums)

    def update(self, index: int, val: int) -> None:
        self.total -= self.nums[index] - val  # self.total += val
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        if len(self.nums) / 2 > (right - left):
            return sum(self.nums[left:right + 1])
        return self.total - sum(self.nums[0:left]) - sum(self.nums[right + 1:])


# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 5]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
obj.update(1, 2)
print(obj.sumRange(0, 2))

