"""
Add Strings
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.



Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"


Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Solution 1 - 40 ms
        """
        ans = []
        i1, i2 = len(num1) - 1, len(num2) - 1
        carry = 0
        while i1 >= 0 or i2 >= 0 or carry > 0:
            if i1 >= 0:
                carry += ord(num1[i1]) - ord('0')
                i1 -= 1
            if i2 >= 0:
                carry += ord(num2[i2]) - ord('0')
                i2 -= 1
            ans.append(chr(carry % 10 + ord('0')))
            carry //= 10
        return "".join(ans)[::-1]
        """
        # Solution 2 - 12 ms
        return str(int(num1) + int(num2))


# Main Call
num1 = "456"
num2 = "77"
solution = Solution()
print(solution.addStrings(num1, num2))
