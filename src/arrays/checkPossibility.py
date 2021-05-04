"""
Non-decreasing Array
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).



Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.


Constraints:

n == nums.length
1 <= n <= 104
-105 <= nums[i] <= 105
"""
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # Solution 1 - 180 ms
        """
        err = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if err or (1 < i < len(nums) - 1 and nums[i - 2] > nums[i] and nums[i + 1] < nums[i - 1]):
                    return False
                err = 1
        return True
        """
        # Solution 2 - 156 ms
        res = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                res += 1
                if 0 < i < len(nums) - 2 and nums[i - 1] > nums[i + 1] and nums[i] > nums[i + 2]:
                    return False
        return res < 2


# Main Call
nums = [4, 2, 3]
solution = Solution()
print(solution.checkPossibility(nums))