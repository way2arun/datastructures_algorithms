"""
Best Time to Buy and Sell Stock with Transaction Fee
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6


Constraints:

1 < prices.length <= 5 * 104
0 < prices[i], fee < 5 * 104
   Hide Hint #1
Consider the first K stock prices. At the end, the only legal states are that you don't own a share of stock, or that you do. Calculate the most profit you could have under each of these two cases.

"""
from cmath import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Solution 1 - 636 ms
        """
        profit = 0
        buyprice, sellprice = inf, -inf
        for p in prices:
            if p < buyprice or p < sellprice - fee:
                profit += max(0, sellprice - buyprice - fee)
                buyprice = p
                sellprice = -inf
            elif p > sellprice:
                sellprice = p

        profit += max(0, sellprice - buyprice - fee)
        return profit
        """
        # Solution 2 - 556 ms
        profit = 0
        curMin = prices[0]

        for price in prices:
            if price < curMin:
                curMin = price
            elif price > curMin + fee:
                profit += price - curMin - fee
                curMin = price - fee

        return profit


# Main Call
prices = [1, 3, 2, 8, 4, 9]
fee = 2

solution = Solution()
print(solution.maxProfit(prices, fee))