"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3377/
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Solution 1 - 932 ms
        """
        if n <= 0:
            return 0
        count = 1
        while n:
            if n >= count:
                n -= count
                count += 1
            else:
                break
        return count - 1
        """
        # Solution 2 16 ms
        l = 1
        r = 65536
        while l < r:
            mid = (l + r) >> 1
            if mid * (mid + 1) // 2 <= n:
                l = mid + 1
            else:
                r = mid
        return l - 1


# Main Call
solution = Solution()
n = 5
print(solution.arrangeCoins(n))
