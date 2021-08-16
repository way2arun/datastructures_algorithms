"""
Range Sum Query - Immutable
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).


Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3


Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= left <= right < nums.length
At most 104 calls will be made to sumRange.
"""
from typing import List


class NumArray:

    """
    # Solution 1 - 76 ms
    def __init__(self, nums: List[int]):
        self.preSum = nums  # pass by pointer!
        for i in range(len(nums) - 1):
            self.preSum[i + 1] += self.preSum[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0: return self.preSum[right]
        return self.preSum[right] - self.preSum[left - 1]
    """
    # Solution 2 - 72 ms
    def __init__(self, nums: List[int]):

        self.sumLeft = [0] * len(nums)
        self.sumLeft[0] = nums[0]
        for i in range(1, len(nums)):
            self.sumLeft[i] = nums[i] + self.sumLeft[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sumLeft[right]

        return self.sumLeft[right] - self.sumLeft[left - 1]


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))
