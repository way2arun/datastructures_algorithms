"""
Best Time to Buy and Sell Stock III
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3426/
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Solution 1 - 68 ms
        """
        if not prices:
            return 0
        first = prices[-1]  # Profit with an action bought and this is the 1st transaction - we sell an action
        second = prices[-1]  # Profit with an action bought and this is the 2nd transaction - we sell an action
        before_transaction = 0  # Profit without an action bought and this is before transactions - we do nothing
        after_first_transaction = 0  # Profit without an action bought and this is after the 1st transaction - we do nothing
        for p in prices[-2::-1]:
            first, second, before_transaction, after_first_transaction = max(first, p + after_first_transaction), max(second, p + 0), max(before_transaction, -p + first), max(after_first_transaction, -p + second)
        return before_transaction
        """
        # Solution 2 - 56 ms
        """
        n = len(prices)
        max_profit = 0

        min_price = float('inf')
        dp = [0] * n
        for i in range(n):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
            dp[i] = max_profit

        max_price = 0
        for i in range(n - 1, 0, -1):
            if prices[i] > max_price:
                max_price = prices[i]
                continue
            curr_max = max_price - prices[i]
            if curr_max + dp[i - 1] > max_profit:
                max_profit = curr_max + dp[i - 1]

        return max_profit
        """
        """
        # Solution 3 - 60 ms
        sell1, sell2, buy1, buy2 = 0, 0, -999999, -999999
        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
        return sell2
        """
        # Solution 3 - 72 ms
        """
        ans, dp = 0, 0
        for i in range(0, len(prices) - 1):
            q = prices[i + 1] - prices[i]
            dp = max(dp + q, q)
            ans = max(ans, dp)
        return ans
        """

        # Solution 4 - 48 ms
        minprice = 9999999999
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice

        return maxprofit


# Main Call
solution = Solution()
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(solution.maxProfit(prices))
