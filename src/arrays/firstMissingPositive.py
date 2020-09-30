"""
First Missing Positive
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/558/week-5-september-29th-september-30th/3478/
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Follow up:

Your algorithm should run in O(n) time and uses constant extra space.

   Hide Hint #1
Think about how you would solve the problem in non-constant space. Can you apply that logic to the existing space?
   Hide Hint #2
We don't care about duplicates or non-positive integers
   Hide Hint #3
Remember that O(2n) = O(n)
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Solution 1 - 36 ms
        """
        if not nums:
            return 1
        maxm = max(max(nums), 0)
        for i in range(1, maxm + 2):
            if i not in nums:
                return i
        """
        # Solution 2 - 16 ms
        if not nums:
            return 1
        s = set(nums)
        for i in range(1, len(nums) + 2):  # [1]
            if i not in s:
                return i
                break
        """
        # Solution 3 - 20 ms
        n = len(nums)

        # Base case.
        if 1 not in nums:
            return 1
        '''
        # nums = [1]
        if n == 1:
            return 2
        '''
        # Replace negative numbers, zeros,
        # and numbers larger than n by 1s.
        # After this convertion nums will contain
        # only positive numbers.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        # Use index as a hash key and number sign as a presence detector.
        # For example, if nums[1] is negative that means that number `1`
        # is present in the array.
        # If nums[2] is positive - number 2 is missing.
        for i in range(n):
            a = abs(nums[i])
            # If you meet number a in the array - change the sign of a-th element.
            # Be careful with duplicates : do it only once.
            if a == n:
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])

        # Now the index of the first positive number
        # is equal to first missing positive.
        for i in range(1, n):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return n

        return n + 1
        """


# Main Call
solution = Solution()
nums = [1, 2, 0]
print(solution.firstMissingPositive(nums))
