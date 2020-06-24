"""
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3370/
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


class Solution:
    def numTrees(self, n: int) -> int:
        # Solution 1 - 16 ms
        """
        combination = [1] * (n + 1)
        for i in range(2, n + 1):
            combination[i] = sum(combination[j] * combination[i - 1 - j] for j in range(i))
        return combination[n]
        """
        # Solution 2 - 12 ms
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]

        return dp[-1]


# Main Call
solution = Solution()
n = 3
print(solution.numTrees(n))