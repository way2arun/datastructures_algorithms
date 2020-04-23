"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3308/

"""


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # 64 ms
        """
        if m != n:
            return self.rangeBitwiseAnd(m >> 1, n >> 1) << 1
        else:
            return m
        """
        # 32 ms
        total = 0
        while m != n:
            m >>= 1
            n >>= 1
            total += 1
        return m << total


# Main Call
solution = Solution()
m = 5
n = 7
result = solution.rangeBitwiseAnd(m, n)
print(result)
