"""
Cherry Pickup II
Given a rows x cols matrix grid representing a field of cherries. Each cell in grid represents the number of cherries that you can collect.

You have two robots that can collect cherries for you, Robot #1 is located at the top-left corner (0,0) , and Robot #2 is located at the top-right corner (0, cols-1) of the grid.

Return the maximum number of cherries collection using both robots  by following the rules below:

From a cell (i,j), robots can move to cell (i+1, j-1) , (i+1, j) or (i+1, j+1).
When any robot is passing through a cell, It picks it up all cherries, and the cell becomes an empty cell (0).
When both robots stay on the same cell, only one of them takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in the grid.


Example 1:



Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output: 24
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.
Example 2:



Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
Output: 28
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
Total of cherries: 17 + 11 = 28.
Example 3:

Input: grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]
Output: 22
Example 4:

Input: grid = [[1,1],[1,1]]
Output: 4


Constraints:

rows == grid.length
cols == grid[i].length
2 <= rows, cols <= 70
0 <= grid[i][j] <= 100
   Hide Hint #1
Use dynammic programming, define DP[i][j][k]: The maximum cherries that both robots can take starting on the ith row, and column j and k of Robot 1 and 2 respectively.
"""
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # Solution 1 - 752 ms
        """
        n = len(grid)
        m = len(grid[0])
        # Add extra column at start and end to make the DP code below easier
        # as we wont have to worry about array index going out of bounds
        dp = [[[-1 for i in range(m + 2)] for j in range(m + 2)] for k in range(2)]
        curr = 1
        for row in range(n - 1, -1, -1):
            nxt = (curr + 1) % 2
            for c1 in range(m, 0, -1):
                for c2 in range(m, 0, -1):
                    maxval = 0
                    if row != n - 1:
                        # We have 2 robots which can move in 3 directions at each step
                        # This gives us total of 9 possible next states
                        maxval = max(maxval, \
                                     dp[nxt][c1][c2], dp[nxt][c1][c2 + 1], dp[nxt][c1][c2 - 1], \
                                     dp[nxt][c1 + 1][c2], dp[nxt][c1 + 1][c2 + 1], dp[nxt][c1 + 1][c2 - 1], \
                                     dp[nxt][c1 - 1][c2], dp[nxt][c1 - 1][c2 + 1], dp[nxt][c1 - 1][c2 - 1])
                    curr_cherries = 0
                    if c1 == c2:
                        curr_cherries = grid[row][c1 - 1]
                    else:
                        curr_cherries = grid[row][c1 - 1] + grid[row][c2 - 1]
                    dp[curr][c1][c2] = maxval + curr_cherries
            curr = nxt
        return max(0, dp[(curr + 1) % 2][1][m])
        """
        # Solution 2 - 296 ms
        n, m = len(grid), len(grid[0])
        dp = [[0] * (m + 2) for _ in range(m + 2)]
        dp[0][m - 1] = grid[0][0] + grid[0][m - 1]

        for i in range(1, n):  # each level
            tmp = [[0] * (m + 2) for _ in range(m + 2)]
            # each time, you can move one more to left or right, so the most one is i+1 or m-1-i
            for j in range(min(i + 1, m)):  # robot 1'col,
                for k in range(max(m - i - 1, 0), m):  # robot 2'col
                    if j != k:
                        tmp[j][k] = max(dp[j - 1][k], dp[j][k], dp[j + 1][k],
                                        dp[j - 1][k - 1], dp[j][k - 1], dp[j + 1][k - 1],
                                        dp[j - 1][k + 1], dp[j][k + 1], dp[j + 1][k + 1])
                        tmp[j][k] += grid[i][j] + grid[i][k]

            dp = tmp[:][:]

        return max(max(i) for i in dp)


# Main Call
grid = [[1, 0, 0, 3], [0, 0, 0, 3], [0, 0, 3, 3], [9, 0, 3, 3]]
solution = Solution()
print(solution.cherryPickup(grid))
