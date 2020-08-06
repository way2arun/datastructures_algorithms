"""
Find All Duplicates in an Array
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3414/
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Solution 1 - 468 ms
        """
        result = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                result.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return result
        """
        # Solution 2 - 332 ms
        """
        res = []
        dataMap = {}

        for num in nums:
            if num in dataMap:
                res.append(num)
            else:
                dataMap[num] = 1

        return res
        """

        # Solution 3 - 336 ms
        already_seen = set()
        duplicates = set()
        for num in nums:
            if num in already_seen:
                duplicates.add(num)
            else:
                already_seen.add(num)
        return duplicates


# Main Call
solution = Solution()
nums = [4,3,2,7,8,2,3,1]
print(solution.findDuplicates(nums))