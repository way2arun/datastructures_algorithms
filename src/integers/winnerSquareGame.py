"""
Stone Game IV
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile.  On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n. Return True if and only if Alice wins the game otherwise return False, assuming both players play optimally.



Example 1:

Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.
Example 2:

Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).
Example 3:

Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).
Example 4:

Input: n = 7
Output: false
Explanation: Alice can't win the game if Bob plays optimally.
If Alice starts removing 4 stones, Bob will remove 1 stone then Alice should remove only 1 stone and finally Bob removes the last one (7 -> 3 -> 2 -> 1 -> 0).
If Alice starts removing 1 stone, Bob will remove 4 stones then Alice only can remove 1 stone and finally Bob removes the last one (7 -> 6 -> 2 -> 1 -> 0).
Example 5:

Input: n = 17
Output: false
Explanation: Alice can't win the game if Bob plays optimally.


Constraints:

1 <= n <= 10^5
   Hide Hint #1
Use dynamic programming to keep track of winning and losing states. Given some number of stones, Alice can win if she can force Bob onto a losing state.
"""
import functools
import math


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # Solution 1 - 1964 ms
        """
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            j = 1
            while j * j <= i and not dp[i]:
                dp[i] = dp[i - j * j] ^ 1
                j += 1
        return dp[n]
        """

        # Solution 2 - 184 ms
        @functools.lru_cache(None)
        def dp(k):
            if k == 0:
                return -1
            for i in range(int(math.sqrt(k)), 0, -1):
                if dp(k - i * i) < 0:
                    return 1
            return -1

        return dp(n) > 0


# Main Call
solution = Solution()
n = 4
print(solution.winnerSquareGame(n))
