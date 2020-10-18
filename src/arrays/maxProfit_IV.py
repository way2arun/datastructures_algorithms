"""
Best Time to Buy and Sell Stock IV
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Notice that you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


Constraints:

0 <= k <= 109
0 <= prices.length <= 104
0 <= prices[i] <= 1000
"""
from typing import List
from heapq import heapify, heappop


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # Solution 1 - 108 ms
        """
        if not prices:
            return 0
        if k > len(prices) // 2:
            buy = prices[0]
            i = 0
            res = 0
            while i < len(prices) - 1:
                while (i < len(prices) - 1 and prices[i] >= prices[i + 1]):
                    i += 1
                buy = prices[i]
                while (i < len(prices) - 1 and prices[i] <= prices[i + 1]):
                    i += 1
                res += prices[i] - buy
            return res
        dp = [[float("inf"), 0] for i in range(k + 1)]
        for i in prices:
            for j in range(1, k + 1):
                dp[j][0] = min(dp[j][0], i - dp[j - 1][1])
                dp[j][1] = max(dp[j][1], i - dp[j][0])
        return dp[-1][-1]
        """
        # Solution 2 - 40 ms
        if len(prices) < 2:
            return 0

        profits = []
        queue = []
        for i in range(1, len(prices)):
            p0, p1 = prices[i - 1], prices[i]
            if p1 <= p0:
                continue

            while queue:
                q0, q1 = queue[-1]
                if p0 < q0:
                    profits.append(q0 - q1)
                    queue.pop()
                else:
                    break

            while queue:
                q0, q1 = queue[-1]
                if q0 <= p0 and q1 < p1:
                    if p0 - q1 < 0:
                        profits.append(p0 - q1)
                    p0, p1 = q0, p1
                    queue.pop()
                else:
                    break

            queue.append((p0, p1))

        profits += [p0 - p1 for p0, p1 in queue]
        heapify(profits)

        answer = 0
        for _ in range(min(len(profits), k)):
            answer -= heappop(profits)
        return answer

        # Time: O(nk), Space: O(n+k)
        #
        # dp[i,k] = max(dp[j, k-1] - p[j]) + p[i]  for 0 <= j <= i
        # Keep track of max term as we go to turn quadratic into linear.
        # For each k, keep track of max profit and max diff.
        #
        # Optimization: for huge k - since max number of trades is bound by n/2,
        # if k exceeds n/2 just make all profitable transactions.

    def maxProfit2(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n / 2 <= k:
            return sum([max(prices[i + 1] - prices[i], 0) for i in range(n - 1)])

        dp = [[0, float('-inf')] for _ in range(k + 1)]

        for price in prices:
            for j in range(1, k + 1):
                profit, maxDiff = dp[j]
                dp[j][0] = max(profit, maxDiff + price)
                dp[j][1] = max(maxDiff, dp[j - 1][0] - price)

        return dp[-1][0]


# Main Call
solution = Solution()

k = 2
prices = [2, 4, 1]
print(solution.maxProfit(k, prices))
