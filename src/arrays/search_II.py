"""
Search in Rotated Sorted Array II
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Solution 1 - 52 ms
        """
        if not nums:
            return False
        if len(nums) == 1:
            return nums[0] == target
        if nums[0] == target or nums[-1] == target:
            return True
        if nums[0] == nums[-1]:
            return target in nums

        # Use binary search to find offset point
        # The target will either be in A[start:finish] or absent
        # O(log N)
        if nums[0] < nums[-1]:  # no offset in the array
            start, finish = 0, len(nums) - 1
        else:  # there is offset in the array
            left, right = 0, len(nums) - 1
            while left < right - 1:
                mid = (left + right) >> 1
                if nums[mid] >= nums[0]:
                    left = mid
                else:
                    right = mid
            if nums[right] < nums[left]: left = right
            start, finish = (0, left - 1) if nums[0] < target else (left, len(nums) - 1)

        # Now you know the range to search for, just apply binary search again
        # O(log N)
        while start < finish - 1:
            mid = (start + finish) >> 1
            if nums[mid] < target:
                start = mid
            else:
                finish = mid
        return nums[start] == target or nums[finish] == target
        """
        # Solution 2 - 28 ms
        n = len(nums)
        if n == 0: return False
        end = n - 1
        start = 0
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            if not nums[start] != nums[mid]:
                start += 1
                continue
            pivotArray = nums[start] <= nums[mid]
            targetArray = nums[start] <= target
            if pivotArray ^ targetArray:
                if pivotArray:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
        return False


# Main Call
nums = [2, 5, 6, 0, 0, 1, 2]
target = 0

solution = Solution()
print(solution.search(nums, target))
