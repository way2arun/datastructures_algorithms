"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3388/
Reverse bits of a given 32 bits unsigned integer.



Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.


Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the input represents the signed integer -3 and the output represents the signed integer -1073741825.


Follow up:

If this function is called many times, how would you optimize it?
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        # Solution 1 - 60 ms
        """
        stack = []
        while n:
            x = n % 2
            n //= 2
            stack.append(str(x))
        stack = stack[::] + ['0'] * (32 - len(stack))
        b = ''.join(stack)
        return int(b, 2)
        """
        # Solution 2 - 8 ms
        """
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n
        """

        # Solution 3 - 12 ms
        res = 0
        for i in range(32):
            res += n & 1
            n = n >> 1
            if i != 31:
                res = res << 1
        return res


# Main Call
solution = Solution()
"""
Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
"""
n = 0b00000010100101000001111010011100
print(n)
print(bin(n))
result = solution.reverseBits(n)
print(result)
print(bin(result))