"""
Matchsticks to Square
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.



Example 1:


Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.


Constraints:

1 <= matchsticks.length <= 15
0 <= matchsticks[i] <= 109
   Hide Hint #1
Treat the matchsticks as an array. Can we split the array into 4 equal halves?
   Hide Hint #2
Every matchstick can belong to either of the 4 sides. We don't know which one. Maybe try out all options!
   Hide Hint #3
For every matchstick, we have to try out each of the 4 options i.e. which side it can belong to. We can make use of recursion for this.
   Hide Hint #4
We don't really need to keep track of which matchsticks belong to a particular side during recursion. We just need to keep track of the length of each of the 4 sides.
   Hide Hint #5
When all matchsticks have been used we simply need to see the length of all 4 sides. If they're equal, we have a square on our hands!
"""
from functools import lru_cache
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # Solution 1 - 988 ms
        """
        N = len(matchsticks)
        basket, rem = divmod(sum(matchsticks), 4)
        if rem or max(matchsticks) > basket: return False

        @lru_cache(None)
        def dfs(mask):
            if mask == 0: return 0
            for j in range(N):
                if mask & 1 << j:
                    neib = dfs(mask ^ 1 << j)
                    if neib >= 0 and neib + matchsticks[j] <= basket:
                        return (neib + matchsticks[j]) % basket
            return -1

        return dfs((1 << N) - 1) == 0
        """
        # Solution 2 - 52 ms
        n, sm = len(matchsticks), sum(matchsticks)
        if n < 4 or sm % 4:
            return False
        q = sm // 4
        mask = 0
        matchsticks.sort(reverse=True)

        @lru_cache(None)
        def dp(i, cur, mask):
            if i == 4:
                return True
            for j in range(n):
                if mask & (1 << j):
                    continue
                if cur + matchsticks[j] == q:
                    if dp(i + 1, 0, mask | (1 << j)):
                        return True
                elif cur + matchsticks[j] < q:
                    if dp(i, cur + matchsticks[j], mask | (1 << j)):
                        return True
                else:
                    break
            return False

        return dp(0, 0, 0)


# Main Call
solution = Solution()
matchsticks = [1, 1, 2, 2, 2]
print(solution.makesquare(matchsticks))