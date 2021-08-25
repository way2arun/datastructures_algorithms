"""
Sum of Square Numbers
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.



Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
Example 3:

Input: c = 4
Output: true
Example 4:

Input: c = 2
Output: true
Example 5:

Input: c = 1
Output: true


Constraints:

0 <= c <= 231 - 1
"""
from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Solution 1 - 140 ms
        """
        for a in range(int(sqrt(c)) + 1):
            b = sqrt(c - a * a)
            if b == int(b):
                return True
        return False
        """
        # Solution 2 - 104  ms
        l = 0
        r = int(c ** 0.5)
        while l <= r:
            res = (l * l) + (r * r)
            if res < c:
                l = l + 1
            elif res > c:
                r = r - 1
            else:
                return True
        return False

# Main Call
c = 5
solution = Solution()
print(solution.judgeSquareSum(c))