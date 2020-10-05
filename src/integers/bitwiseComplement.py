"""
Complement of Base 10 Integer
Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary is "010" in binary.

For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.



Example 1:

Input: 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
Example 2:

Input: 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
Example 3:

Input: 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.


Note:

0 <= N < 10^9
This question is the same as 476: https://leetcode.com/problems/number-complement/
   Hide Hint #1
A binary number plus its complement will equal 111....111 in binary. Also, N = 0 is a corner case.
"""


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        # Solution 1 - 32 ms
        """
        if N == 0:
            return 1
        return (2 ** self.digits_count(N)) - 1 - N
        """
        # Solution 2 - 12 ms

        if N == 0:
            return 1
        if N == 1:
            return 0
        up = 2
        while up <= N:
            up = up << 1
        return up - 1 - N

        # Solution 3 - 16 ms
        """
        a = bin(N)
        # print(a,type(a))
        s = ""
        for i in range(2, len(a)):
            if a[i] == '1':
                s += '0'
            else:
                s += '1'

        while s[0] == '0':
            s = s[1:]
            if len(s) == 0:
                return 0
        s = s[::-1]
        # print(s)
        r = 0
        for i in range(len(s)):
            r += int(s[i]) * 2 ** i
        return r
        """

    def digits_count(self, n):
        if n == 0:
            return 0
        return 1 + self.digits_count(n >> 1)






# Main Call
solution = Solution()
N = 5
print(solution.bitwiseComplement(N))
N= 10
print(solution.bitwiseComplement(N))
N = 7
print(solution.bitwiseComplement(N))
