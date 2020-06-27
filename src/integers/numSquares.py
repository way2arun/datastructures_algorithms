"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3373/

"""


class Solution:
    _dp = [0]

    def numSquares(self, n: int) -> int:
        # Solution 1 -
        """
        result = [0] + [float('inf')] * (n)
        for n in range(1, n + 1):
            counter = 1
            while counter * counter <= n:
                result[n] = min(result[n], result[n - counter * counter] + 1)
                counter += 1
        return result[n]
        """
        # Solution 2 -
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i * i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1,
        return dp[n]


# Main Call
n = 12
solution = Solution()
print(solution.numSquares(n))
n = 13
print(solution.numSquares(n))
