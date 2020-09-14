"""
House Robber
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3459/
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 400
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Solution 1 - 40 ms
        """
        if len(nums) == 0:
            return 0
        arr = [0, nums[0]]
        for i in range(1, len(nums)):
            arr.append(max(arr[i], nums[i] + arr[i - 1]))
        return arr[-1]
        """
        # Solution 2 - 12 ms
        if not nums:
            return 0

        dp = [0] * (len(nums))
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + (dp[i - 2] if i > 1 else 0))
        return dp[-1]

        # Solution 3 - 16 ms
        """
        if len(nums) == 0:
            return 0
        if len(nums) < 3:
            return max(nums)
        max_money = [0] * len(nums)
        max_money[0] = nums[0]
        max_money[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            max_money[i] = nums[i] + max_money[i - 2] if nums[i] + max_money[i - 2] > max_money[i - 1] else max_money[
                i - 1]
        return max_money[-1]
        """


# Main Call
nums = [1, 2, 3, 1]
solution = Solution()
print(solution.rob(nums))
