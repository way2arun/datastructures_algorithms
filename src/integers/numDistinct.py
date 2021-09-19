"""
Distinct Subsequences
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.



Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag


Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
"""
from functools import lru_cache


@lru_cache(None)
def get_distinct_subsequence(i, j):
    """
    i -> s : larger
    j -> t : smaller
    """
    if j < 0:
        return 1

    if i < 0:
        return 0

    if s[i] == t[j]:
        return get_distinct_subsequence(i - 1, j) + get_distinct_subsequence(i - 1, j - 1)

    return get_distinct_subsequence(i - 1, j)


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Solution 1 - 360 ms
        """
        @lru_cache(None)
        def dp(i, j):
            if i == -1: return j == -1
            if j == -1: return j == -1
            return dp(i - 1, j) + (s[i] == t[j]) * dp(i - 1, j - 1)

        return dp(len(s) - 1, len(t) - 1)
        """
        # Solution 2 - 32 ms
        l1 = len(s)
        l2 = len(t)

        if l1 <= l2 and s != t:
            return 0

        if s == t:
            return 1

        get_distinct_subsequence.cache_clear()
        return get_distinct_subsequence(l1 - 1, l2 - 1)


# Main Call
s = "babgbag"
t = "bag"
solution = Solution()
print(solution.numDistinct(s, t))
