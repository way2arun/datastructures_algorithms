"""
Stone Game
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.



Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation:
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.


Constraints:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
"""
from functools import lru_cache
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Solution 1 - 524 ms
        """
        @lru_cache(None)
        def dp(left, right):
            if left > right: return (0, 0)

            pickLeft = dp(left + 1, right)
            pickRight = dp(left, right - 1)

            if piles[left] + pickLeft[1] > piles[right] + pickRight[
                1]:  # If the left choice has higher score than the right choice
                return piles[left] + pickLeft[1], pickLeft[0]  # then pick left

            return piles[right] + pickRight[1], pickRight[0]  # else pick right

        alexScore, leeScore = dp(0, len(piles) - 1)
        return alexScore > leeScore
        """
        # Solution 2 - 52 ms
        memo = {}

        def helper(alex, lee, start, end):
            if start > end:
                return alex > lee
            if (start, end) in memo:
                return memo[(start, end)]
            ret = (helper(alex + piles[start], lee + piles[end], start + 1, end - 1) or
                   helper(alex + piles[start], lee + piles[start + 1], start + 2, end) or
                   helper(alex + piles[end], lee + piles[start], start + 1, end - 1) or
                   helper(alex + piles[end], lee + piles[end - 1], start, end - 2))
            memo[(start, end)] = ret
            return ret

        return helper(0, 0, 0, len(piles) - 1)


# Main Call
piles = [5, 3, 4, 5]
solution = Solution()
print(solution.stoneGame(piles))
