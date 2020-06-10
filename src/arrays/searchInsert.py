"""
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3356/
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Solution 1 - 48 ms
        """
        start = 0
        end = len(nums)
        while start < end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid + 1
        return start
        """
        # Solution 2 - 28 ms
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        if start == len(nums) - 1 and target > nums[-1]:
            return len(nums)
        return start


# Main Call
solution = Solution()
nums = [1, 3, 5, 6]
target = 5
print(solution.searchInsert(nums, target))
