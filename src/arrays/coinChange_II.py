"""
Coin Change
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""
import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Solution 1 - 1504 ms
        """
        INF = math.inf
        dp = [INF] * (amount + 1)
        dp[0] = 0
        for n in range(1, amount + 1):
            for m in coins:
                if n - m >= 0 and dp[n - m] < INF:
                    dp[n] = min(dp[n], 1 + dp[n - m])

        return dp[-1] if dp[-1] < INF else -1
        """
        # Solution 2 - 48 ms
        def helper(count, have, i, res):
            coin = coins[i]
            if count - (have - amount) // coin >= res:
                return res
            need = amount - have
            if need % coin == 0:
                x = count + need // coin
                return x if x < res else res
            if i == 0:
                return res
            for j in range(need // coin, -1, -1):
                sub = helper(count + j, have + coin * j, i - 1, res)
                if sub < res:
                    res = sub
            return res

        coins.sort()
        ret = helper(0, 0, len(coins) - 1, amount + 1)
        return -1 if ret == amount + 1 else ret


# Main Call
coins = [1, 2, 5]
amount = 11

solution = Solution()
print(solution.coinChange(coins, amount))
