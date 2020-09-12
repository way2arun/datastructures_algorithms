"""
Combination Sum III
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3457/
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # Solution 1 - 32 ms
        """
        self.sol = []
        self.BackTrack(k, n, [])
        return self.sol
        """
        # Solution 2 - 12 ms

        res = []
        self.dfs(range(1, 10), k, n, 0, [], res)
        return res

        # Solution 3 - 16 ms
        """
        output = []
        self.combination_sum_3(k, n, 1, output, [])
        return output
        """

    def combination_sum_3(self, numbers_left, target, minimum, output, path):
        if target == 0 and numbers_left == 0:
            output.append(path)
            return
        elif target < 0 or numbers_left < 0:
            return
        # Go from minimum to 9, inclusive
        for i in range(minimum, 10):
            if i > target:
                break
            self.combination_sum_3(numbers_left - 1, target - i, i + 1, output, path + [i])

    def BackTrack(self, k, n, curr_sol):
        if n < 0 or k < 0: return
        if n == 0 and k == 0:
            self.sol.append(curr_sol)

        start = curr_sol[-1] + 1 if curr_sol else 1

        for i in range(start, 10):
            self.BackTrack(k - 1, n - i, curr_sol + [i])

    def dfs(self, nums, k, n, index, path, res):
        if k < 0 or n < 0:  # backtracking
            return
        if k == 0 and n == 0:
            res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, k - 1, n - nums[i], i + 1, path + [nums[i]], res)


# Main Call
k = 3
n = 7
solution = Solution()
print(solution.combinationSum3(k, n))
