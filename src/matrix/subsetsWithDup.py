"""
Subsets II
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Solution 1 - 36 ms
        """
        nums.sort()
        ans = set()
        ans.add(tuple())

        for num in nums:
            newSubsets = set()
            for subset in ans:  # Loop previous subsets from ans
                newSubsets.add(tuple(list(subset) + [num]))
            for subset in newSubsets:  # Add new subsets to ans
                ans.add(subset)
        return ans
        """
        # Solution 2 - 16 ms
        nums.sort()

        ans = []
        self.backtrack([], nums, 0, ans)
        return ans

    def backtrack(self, curr, nums, idx, ans):
        ans.append(curr[:])
        if idx >= len(nums):
            return
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            curr.append(nums[i])
            self.backtrack(curr, nums, i + 1, ans)
            curr.pop()


# Main Call
nums = [1, 2, 2]
solution = Solution()
print(solution.subsetsWithDup(nums))