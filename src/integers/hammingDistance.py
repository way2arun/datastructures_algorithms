"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3381/
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
https://en.wikipedia.org/wiki/Hamming_distance
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Solution 1 - With XOR
        print(bin(x^y)[2:])
        #return bin(x^y).count("1")

        # Solution 2 - without XOR - 60 ms
        """
        ans = 0
        while x != y:
            ans += 1 - int(x % 2 == y % 2)
            x = x // 2
            y = y // 2
        return ans
        """

        # Solution 3  - 12 ms
        numDifferences = 0
        print("here it is", 0x01)
        while x > 0 or y > 0:
            print(x & 0x01)
            print(y & 0x01)
            if (x & 0x01) != (y & 0x01):
                numDifferences += 1
            x >>= 1
            y >>= 1
        return numDifferences


# Main Call
solution = Solution()
x = 1
y = 4
print(solution.hammingDistance(x, y))
