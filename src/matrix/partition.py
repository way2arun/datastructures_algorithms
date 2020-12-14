"""
Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]


Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
"""
from typing import List


class Solution:
    def dfs(self, s, partition, result):
        if not s:
            ## base case aka stop condition
            # add into result when we meet a empty string
            result.append(partition[::])
            return
        ## general cases:
        # scan each possible split index

        for i in range(1, len(s) + 1):

            prefix, postfix = s[:i], s[i:]

            if self.is_palindrome(prefix):
                # current prefix is palindrome, keep trying to make more partition in DFS
                partition.append(prefix)
                self.dfs(postfix, partition, result)
                partition.pop()

    def is_palindrome(self, s):

        # helper function to chceck palindrome
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        # Solution 1  - 660 ms
        """
        # record for solution
        result = []

        # make palindrome partition in DFS
        self.dfs(s, [], result)
        return result
        """
        # Solution 2 - 44 ms
        if not s:
            return []
        dp = {0: [[]], 1: [[s[0]]]}
        for i in range(1, len(s)):
            dp[i + 1] = []
            for j in range(0, i + 1):
                if self.is_palindrome(s[j:i + 1]):
                    for prev in dp[j]:
                        dp[i + 1].append(prev + [s[j:i + 1]])
        return dp[len(s)]


# Main Call
s = "aab"
solution = Solution()
print(solution.partition(s))
