"""
Concatenation of Consecutive Binary Numbers
Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.



Example 1:

Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1.
Example 2:

Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.
Example 3:

Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 109 + 7, the result is 505379714.


Constraints:

1 <= n <= 105
   Hide Hint #1
Express the nth number value in a recursion formula and think about how we can do a fast evaluation.

"""
from math import floor, log2

dp=[0]
mod = 1000000000 + 7
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # Solution 1 - 1764 ms
        """
        binary_list = list()
        for i in range(1, n + 1):
            binary_list.append(bin(i).replace("0b", ""))  # convert each number to binary

        binary_number = "".join(binary_list)  # concatenate the binary representations
        number = int(binary_number, 2)  # convert to decimal number
        return number % ((10 ** 9) + 7)
        """
        # Solution 2 - 52 ms
        if n > len(dp) - 1:
            ans = dp[len(dp) - 1]
            l = floor(log2(len(dp))) + 1
            for i in range(len(dp), n + 1):
                ans <<= l
                ans += i
                ans %= mod
                dp.append(ans)
                if (i & (i + 1)) == 0: l += 1
        return dp[n]


# Main Call
n = 3
solution = Solution()
print(solution.concatenatedBinary(n))