"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
   Hide Hint #1
You should make use of what you have produced already.
   Hide Hint #2
Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
   Hide Hint #3
Or does the odd/even status of the number help you in calculating the number of 1s?
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3343/
"""
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        # Solution 1 - 80 ms
        """
        bits_array = [0] * (num + 1)
        for bit_power in range(0, 32):
            start = 1 << bit_power
            end = 1 << (bit_power + 1)
            if start > num:
                break

            for i in range(start, min(num + 1, end)):
                bits_array[i] = bits_array[i - start] + 1
        return bits_array
        """
        # Solution 2 - 52 ms
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i - (i & -i)] + 1
        return dp


# Main Call
num = 2
soluiton = Solution()
print(soluiton.countBits(num))
