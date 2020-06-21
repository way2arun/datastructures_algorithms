"""
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3367/
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.



Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)


Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
"""
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # Solution 1 76 ms
        """
        row = len(dungeon)
        col = len(dungeon[0])
        answer = [[0] * col for i in range(row)]

        answer[row - 1][col - 1] = 1 if dungeon[row - 1][col - 1] > 0 else 1 - dungeon[row - 1][col - 1]

        for r in range(row - 2, -1, -1):
            answer[r][col - 1] = max(answer[r + 1][col - 1] - dungeon[r][col - 1], 1)
        for c in range(col - 2, -1, -1):
            answer[row - 1][c] = max(answer[row - 1][c + 1] - dungeon[row - 1][c], 1)

        for r in range(row - 2, -1, -1):
            for c in range(col - 2, -1, -1):
                answer[r][c] = max(min(answer[r + 1][c], answer[r][c + 1]) - dungeon[r][c], 1)

        return answer[0][0]
        """
        # Solution 2 56 ms
        if not dungeon:
            return 0

        num_row, num_col = len(dungeon), len(dungeon[0])
        dp = [float('inf')] * num_col
        dp[num_col - 1] = 1

        for row in reversed(range(num_row)):
            for col in reversed(range(num_col)):
                if row == num_row - 1 and col == num_col - 1:
                    dp[col] = max(1, 1 - dungeon[row][col])
                elif row == num_row - 1:
                    dp[col] = max(1, dp[col + 1] - dungeon[row][col])
                elif col == num_col - 1:
                    dp[col] = max(1, dp[col] - dungeon[row][col])
                else:
                    dp[col] = max(1, min(dp[col], dp[col + 1]) - dungeon[row][col])

        return dp[0]


# Main Call
solution = Solution()
dungeon = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
print(solution.calculateMinimumHP(dungeon))
