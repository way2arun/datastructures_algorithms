"""
Flip String to Monotone Increasing
A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.



Example 1:

Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.


Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
"""
from functools import lru_cache


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # Solution 1 - 6264 ms
        """
        s = [int(i) for i in s] + [1]

        @lru_cache(None)
        def dp(i, k):
            if i == -1: return 0
            return min([dp(i - 1, j) + int(k != s[i]) for j in range(k + 1)])

        return dp(len(s) - 1, 1)
        """
        # Solution 2 - 32 ms
        """
                0 1
                1 1
                0 0 
                """
        sl = list(s)
        l = len(s)
        c = 0
        si = sl.index('1')
        c1 = 0
        c0 = 0
        c = 0
        for i in range(si, l):
            if sl[i] == '1':
                if c1 < c0:
                    c += c1
                    c1 = 0
                    c0 = 0
                c1 += 1
            else:
                c0 += 1

        return c + min(c1, c0)


# Main Call
solution = Solution()
s = "00011000"
print(solution.minFlipsMonoIncr(s))