"""
Burst Balloons
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

This is quite difficult problem! Let us consider dp[i][j] the maximum number of coins we can get, popping balls from i to j, not including i and j. Why it is enough to keep these values? Let us look at the last popped balloon with number k. Then our balloons are separated into two groups: to the left of this balloon and the the right and we can write:

dp[i][j] = max(nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]) for k in (i+1,j),

where k is the index of the last balloon burst in (i, j).

Complexity: time complexity is O(n^3) and space complexity is O(n^2).

You can see that code is very short, but it is in my opinion very diffucult to find this solution. How you can think in problems like this? First of all we are given, that n<500, which is quite small and we can try to understand what complexity we can expect. It is for sure not 2^500, so what is rest some polynomials and/or logarithms. So what we can expect is either O(n^2) or O(n^3), but no more than this. So at this moment we usually have 2 choises: either greedy or dp. It is not obvious how to do greedy for me, so the choise is dp. Now we can think that repeating subproblem is what is the answer on range (i, j). However the last step is something you can not invent quickly if you do not have experience in these type of problems. I can give you only intuition here: it is good idea to look at some extremal characteristic here: by this word I mean some object, which is either first/last, biggest/smallest and so on. Here our characteristic is last popped ballon on range, not the first we expect in simpler dp problems. Once you understand this logic, some other problems similar to this will be slightly simpler.

664 Strange Printer
546 Remove Boxes
1000 Minimum Cost to Merge Stones
"""
from functools import lru_cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Solution 1 - 424 ms
        """
        A = [1] + nums + [1]

        @lru_cache(None)
        def dfs(i, j):
            return max([A[i] * A[k] * A[j] + dfs(i, k) + dfs(k, j) for k in range(i + 1, j)] or [0])

        return dfs(0, len(A) - 1)
        """
        # Solution 2 - 192 ms
        if not nums:
            return 0
        nums = [1] + [n for n in nums if n > 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for w in range(2, n):
            for l in range(n - w):
                r = l + w
                border = nums[l] * nums[r]
                m = 0
                for mid in range(l + 1, r):
                    cur = dp[l][mid] + nums[mid] * border + dp[mid][r]
                    if cur > m:
                        m = cur
                dp[l][r] = m
        return dp[0][-1]



# Main Call
solution = Solution()
nums = [3, 1, 5, 8]

print(solution.maxCoins(nums))
