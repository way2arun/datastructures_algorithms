"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3354/
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Solution 1 - 28 ms
        """
        # n = n // 2
        if n > 0 and n % 2 == 0:
            return self.isPowerOfTwo(n / 2)
        elif n == 1:
            return True
        else:
            return False
        """
        # Solution 2 - 12 ms
        if n == 1:
            return True
        i = 2
        while i <= n:
            if i == n:
                return True
            i *= 2
        return False


# Main Call
solution = Solution()
n = 16
print(solution.isPowerOfTwo(n))
n = 218
print(solution.isPowerOfTwo(n))
