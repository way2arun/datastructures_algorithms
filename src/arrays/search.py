"""
Binary Search
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Solution 1 - 236 ms
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target: return mid
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
        """
        # Solution 2 - 212 ms
        """
        l = 0
        r = len(nums)
        while l < r - 1:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m
            else:
                l = m
        if nums[l] == target:
            return l
        else:
            return -1
        """

        # Solution 3 - 208 ms

        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + ((right - left) >> 1)
            if nums[pivot] == target:
                return pivot
            if nums[pivot] < target:
                left = pivot + 1
            else:
                right = pivot - 1
        return -1


# Main Call
solution = Solution()
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(solution.search(nums, target))
