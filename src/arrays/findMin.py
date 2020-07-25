"""
Find Minimum in Rotated Sorted Array II
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3401/
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
Would allow duplicates affect the run-time complexity? How and why?

"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Solution 1 - 76 ms
        """
        l = 0
        num_length = len(nums) - 1
        while num_length - l > 1:
            if nums[l] < nums[num_length]:
                return nums[l]
            d = (num_length + l) // 2
            if nums[d] == nums[l]:
                l += 1
            elif nums[d] > nums[l]:
                l = d
            else:
                num_length = d

        return min(nums[num_length], nums[l])
        """
        # Solution 2 36 ms
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[lo] == nums[mid] == nums[hi]:
                lo += 1
                hi -= 1
            elif nums[hi] >= nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return nums[lo]


# Main Call

solution = Solution()
nums = [1,3,5]
print(solution.findMin(nums))