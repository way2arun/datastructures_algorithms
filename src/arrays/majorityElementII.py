"""
Majority Element II
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3469/
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
   Hide Hint #1
How many majority elements could it possibly have?
Do you have a better hint? Suggest it!
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Solution 1 - 124 ms
        """
        n = len(nums) // 3
        d = dict()
        res = []
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in d:
            if d[i] > n:
                res.append(i)
        return res
        """
        # Solution 2 - 92 ms

        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                if nums.count(n) > len(nums) // 3]
        """
        # Solution 3 - 100 ms
        r = len(nums) / 3
        ans = []
        for e in list(set(nums)):
            if nums.count(e) > r:
                ans.append(e)

        return ans
        """


# Main Call
solution = Solution()
nums = [3, 2, 3]
print(solution.majorityElement(nums))
nums = [1, 1, 1, 3, 3, 2, 2, 2]
print(solution.majorityElement(nums))
