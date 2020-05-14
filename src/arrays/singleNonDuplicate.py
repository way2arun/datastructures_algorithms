"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.



Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10


Note: Your solution should run in O(log n) time and O(1) space.
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3327/
"""
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        # Solution 1 - 72 ms
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right + 1) // 2
            if nums[middle] != nums[middle - 1] and nums[middle] != nums[middle + 1]:
                return nums[middle]
            if nums[middle - 1] == nums[middle]:
                middle -= 1
            if (middle - left) % 2 == 0:
                left = middle + 2
            else:
                right = middle - 1

        return nums[left]
        """
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = 2 * ((left + right) // 4)
            if nums[middle] == nums[middle + 1]:
                left = middle + 2
            else:
                right = middle
        return nums[left]
        """
        """

        # Solution 2 using bit wise operator
        ans = 0
        for i in nums:
            ans ^= i
        return ans
        """
        # Solution 3
        print(set(nums))
        print(sum(nums))
        print(sum(set(nums)) * 2 )
        return sum(set(nums)) * 2 - sum(nums)


# Main Call
solution = Solution()
nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
print(solution.singleNonDuplicate(nums))
nums = [3, 3, 7, 7, 10, 11, 11]
print(solution.singleNonDuplicate(nums))
nums = [1,1,2,3,3]
print(solution.singleNonDuplicate(nums))
