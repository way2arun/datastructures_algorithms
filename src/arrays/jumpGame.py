"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3310/
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 68 ms
        # if nums_length is 1, we don't have to do anything
        if len(nums) == 1:
            return True

        # if the nums[0] is zero, we can't move forward
        if nums[0] == 0:
            return False

        # if last element is zero, we don't need to check it, we're guaranteed
        # to reach it if nums[-2] is not zero, if nums[-2] is zero, we'll be
        # checking later in this code whether we're stuck at it or not,
        # if we'll be stuck at it, program will return False anyways.
        if not nums[-1]:
            nums.pop()

        # checking if there any 0's in the nums array, if not it's a clear win
        if 0 not in nums:
            return True

        # start from tail
        index = len(nums) - 1
        while index > 0:
            # look for zero, we only check if elements to the left of zero
            if nums[index]:
                index -= 1
                continue
            zero = index  # index is zero
            # while elements to the left of zero can only reach this zero or shorter
            # we keep going left to look for a number that can jump past this zero
            # if we find it, we go to top of while loop to look for another zero
            while index >= 0 and nums[index] <= zero - index:
                index -= 1
            # if we are not able to find this number that can jump past zero at nums[0]
            # i will change into -1, this is the only condition we fail the jump game.
            if index == -1:
                return False
        # if no failure is found, it means all zero can be jumped past, so we can win.
        return True
        """
        # 96 ms
        if len(nums) == 0:
            return False
        last_index = 0
        nums_length = len(nums)
        for index in range(nums_length):
            if last_index < index:
                return False
            last_index = max(last_index, index + nums[index]) # Get the max of last_index and index + nums[index]
            if last_index >= nums_length - 1:  # if it is greater than or equal to  the nums length,
                return True
        return True
        """


# Main Call
solution = Solution()
nums = [2, 3, 1, 1, 4]
result = solution.canJump(nums)
print(result)
nums = [3, 2, 1, 0, 4]
result = solution.canJump(nums)
print(result)
