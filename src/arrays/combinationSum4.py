"""
 Combination Sum IV
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The answer is guaranteed to fit in a 32-bit integer.



Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000


Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?
"""
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Solution 1 - 40 ms
        """
        dp = [1] + [0] * (target)
        for i in range(len(dp)):
            if not dp[i]: continue
            for n in nums:
                if i + n <= target:
                    dp[i + n] += dp[i]
        return dp[-1]
        """
        # Solution 2 - 24 ms
        memo = [0] * (target + 1)
        memo[0] = 1
        for t in range(target + 1):
            for n in nums:
                prevT = t - n
                if prevT < 0:
                    continue
                memo[t] += memo[prevT]
        return memo[target]


    # Main Call
nums = [1, 2, 3]
target = 4

solution = Solution()
print(solution.combinationSum4(nums, target))