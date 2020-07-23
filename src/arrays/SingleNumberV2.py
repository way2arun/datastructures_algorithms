"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3399/
Single Number III
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""
from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Solution 1 - 60 ms
        """
        output = defaultdict(int)
        for num in range(len(nums)):
            if output[nums[num]] == 1:
                del output[nums[num]]
            else:
                output[nums[num]] += 1
        return output.keys()
        """
        # Solution 2 - 48 ms
        d = {}
        for x in nums:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        res = []
        for k, v in d.items():
            if v == 1:
                res.append(k)
        return res


# Main Call
nums = [1, 2, 1, 3, 2, 5]
solution = Solution()
print(solution.singleNumber(nums))
