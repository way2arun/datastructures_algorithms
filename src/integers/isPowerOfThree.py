"""
 Power of Three
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.



Example 1:

Input: n = 27
Output: true
Example 2:

Input: n = 0
Output: false
Example 3:

Input: n = 9
Output: true
Example 4:

Input: n = 45
Output: false


Constraints:

-231 <= n <= 231 - 1


Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Solution 1 - 52 ms
        """
        if n <= 0:
            return False
        return (3 ** 19) % n == 0
        """
        # Solution 2 - 28 ms
        if n == 1 or n == 3:
            return True
        if n == 0:
            return False

        while True:
            if n % 3 != 0:
                return False
            n = n / 3
            if n == 3:
                return True


# Main Call
n = 27
solution = Solution()
print(solution.isPowerOfThree(n))