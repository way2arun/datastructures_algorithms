"""
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3357/
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        pointer_1 = 0
        pointer_2 = 0
        pointer_3 = len(nums) - 1
        while pointer_2 <= pointer_3:
            if nums[pointer_2] == 0:
                nums[pointer_1], nums[pointer_2] = nums[pointer_2], nums[pointer_1]
                pointer_1 += 1
                pointer_2 += 1
            elif nums[pointer_2] == 2:
                nums[pointer_2], nums[pointer_3] = nums[pointer_3], nums[pointer_2]
                pointer_3 -= 1
            else:
                pointer_2 += 1
        return nums
        """
        # Solution 2
        p1 = 0
        curr = 0
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p1], nums[curr] = nums[curr], nums[p1]
                p1 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1
        return nums


# Main Call
solution = Solution()
nums = [2, 0, 2, 1, 1, 0]
print(solution.sortColors(nums))
