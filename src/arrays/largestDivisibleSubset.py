"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]

https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3359/
"""
from math import sqrt
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        if not nums:
            return nums
        # Sort the nums
        nums.sort()
        print(nums)
        temp_list = [1 for i in range(len(nums))]
        answer = []
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    temp_list[i] = max(temp_list[i], temp_list[j] + 1)
        for i in range(1, max(temp_list) + 1):
            answer.append(nums[temp_list.index(i)])
        return answer
        """
        # Solution 2 - 112 ms
        if not nums or len(nums) == 0:
            return []
        nums = sorted(nums)
        dp = {}
        for i in range(len(nums)):
            if nums[i] == 1:
                dp[1] = 1
                continue

            for j in range(1, int(sqrt(nums[i])) + 1):
                tmp = nums[i] % j
                if tmp == 0:
                    dp[nums[i]] = max(dp.get(j, 0) + 1, dp.get(nums[i] // j, 0) + 1, dp.get(nums[i], 1))

        #  reconstruct the result
        rs = []
        max_len = max(dp.values())
        while max_len > 0:
            for x in dp:
                if dp[x] == max_len:
                    rs.append(x)
                    break
            max_len -= 1
        return rs[::-1]


# Main Call
solution = Solution()
nums = [1, 2, 3]
print(solution.largestDivisibleSubset(nums))
nums = [1, 2, 4, 8]
print(solution.largestDivisibleSubset(nums))
