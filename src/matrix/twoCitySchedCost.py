"""
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3349/
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.



Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.


Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000
"""
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Solution 1 - 32 ms
        """
        cost_difference = []
        cost_length = len(costs)
        for i in range(cost_length):
            cost_difference.append([costs[i][1] - costs[i][0], i])

        cost_difference.sort(key=lambda x: x[0], reverse=True)
        total_cost = sum([costs[val[1]][0] for val in cost_difference[:cost_length // 2]]) + \
                    sum([costs[val[1]][1] for val in cost_difference[cost_length // 2:]])

        return total_cost
        """
        # Solution 2 - 20 ms
        costs = sorted(costs, key=lambda x: x[0] - x[1])
        n = len(costs)

        return sum(costs[i][0] for i in range(n // 2)) + sum(costs[i][1] for i in range(n // 2, n))


# Main Call
costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
solution = Solution()
print(solution.twoCitySchedCost(costs))
