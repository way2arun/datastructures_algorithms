"""
Candy
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.



Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.


Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Solution 1 - 152 ms
        """
        candies = [1] * len(ratings)
        if len(ratings) == 1:
            return 1

        if ratings[0] > ratings[1] and candies[0] == candies[1]:
            candies[0] += 1

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1

        return sum(candies)
        """
        # Solution 2- 128 ms
        last = -1
        level = 0
        run = 1
        total = 0
        for rating in ratings:
            if rating > last:
                if run == 1:
                    level += 1
                else:
                    level = 2
                run = 1
                total += level
            elif rating == last:
                run = 1
                level = 1
                total += 1
            else:
                total += run
                run += 1
                if (level < run):
                    total += 1
            last = rating
        return total

# Main Call
solution = Solution()
ratings = [1,0,2]
print(solution.candy(ratings))