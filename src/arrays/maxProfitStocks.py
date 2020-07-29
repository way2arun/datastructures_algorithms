"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/548/week-5-july-29th-july-31st/3405/
Best Time to Buy and Sell Stock with Cooldown
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Solution 1 - 48 ms
        """
        if len(prices) == 0:
            return 0

        stocks = [{"buy": 0, "watch": 0, "sell": 0} for i in range(len(prices))]

        highest = None  # highest value in a buy day so far
        for day, price in enumerate(prices):
            if day == 0:
                stocks[day]["buy"] = -price
                highest = -price
            else:
                stocks[day]["buy"] = stocks[day - 1]["watch"] - price
                stocks[day]["watch"] = max(stocks[day - 1]["watch"], stocks[day - 1]["sell"])
                stocks[day]["sell"] = highest + price
                highest = max(highest, stocks[day]["buy"])

        return max(stocks[-1]["sell"], stocks[-1]["watch"])
        """
        # Solution 2 - 28 ms
        if not prices:
            return 0
        dp_pre = [0] * 3
        dp_cur = [0] * 3
        # corner cases
        dp_pre[0] = 0
        dp_pre[1] = -prices[0]
        dp_pre[2] = 0
        #  print(dp_pre)
        # transition equations
        for i in range(1, len(prices)):
            dp_cur[0] = max(dp_pre[0], dp_pre[2])
            dp_cur[1] = max(dp_pre[1], dp_pre[0] - prices[i])
            dp_cur[2] = dp_pre[1] + prices[i]

            dp_pre = dp_cur[:]
        #    print(dp_pre)

        return max(dp_pre[0], dp_pre[2])


# Main Call
prices = [1, 2, 3, 0, 2]
solution = Solution()
print(solution.maxProfit(prices))
