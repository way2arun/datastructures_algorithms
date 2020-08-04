"""
Power of Four
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3412/
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # Solution 1 - 48 ms
        # return 0 < num == 0b1010101010101010101010101010101 & num and num & (num - 1) == 0

        # Solution 2
        """
        if num < 0:
            return False
        binary_value = bin(num)
        return binary_value[::-1].find('1') % 2 == 0 and binary_value.count('1') == 1
        """

        # Solution 3 - 12 ms

        if num < 1:
            return False
        while num % 4 == 0:
            num /= 4
        return True if num == 1 else False

        # Solution 4 - 16 ms
        """
        if num <= 0:
            return False
        z = bin(num)[::-1]
        if z.count('1') > 1:
            return False
        p = z.index('1')
        return p % 2 == 0
        """


# Main Call
solution = Solution()
num = 16
print(solution.isPowerOfFour(num))

num = 5
print(solution.isPowerOfFour(num))
