"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3387/
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Solution 1 60 ms
        """
        subset = [[]]
        for num in nums:
            subset_length = len(subset)
            for s in subset[:subset_length]:
                subset.append(s + [num])
        return subset
        """
        # Solution 2 - 16 ms
        n = len(nums)
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]

        return output


# Main Call
nums = [1, 2, 3]
solution = Solution()
print(solution.subsets(nums))