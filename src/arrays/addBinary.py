"""
Add Binary
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3395/
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Solution 1 - 48 ms
        """
        res = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            sum1 = carry
            if i >= 0:
                sum1 += ord(a[i]) - ord('0')
            if j >= 0:
                sum1 += ord(b[j]) - ord('0')
            i, j = i - 1, j - 1
            carry = 1 if sum1 > 1 else 0
            res += str(sum1 % 2)
        if carry != 0:
            res += str(carry)
        return res[::-1]
        """
        # Solution 2 -  8 ms
        """
        return bin(int(a, 2) + int(b, 2))[2:]
        """
        # Solution 3 - 12 ms
        """
        c = int(a, 2)
        d = int(b, 2)
        e = bin(c + d)
        return str(e).replace("0b", '')
        """
        # Solution 4 - 16 ms
        a = int(a, 2)
        b = int(b, 2)
        while b != 0:
            ans = a ^ b
            carry = (a & b) << 1
            a = ans
            b = carry
        return format(a, "0b")


# Main Call
solution = Solution()
a = "11"
b = "1"
print(solution.addBinary(a, b))
