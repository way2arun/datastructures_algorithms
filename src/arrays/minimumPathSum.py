"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""
from typing import List




class Solution:
    # # Runtime O(n^2), 96 ms
    def minPathSum(self, grid: List[List[int]]) -> int:
        # check the row and col of the matrix
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        # Traverse through the row and col
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                # Check the min
                if row > 0 and col > 0:
                    grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
                elif row > 0:
                    grid[row][col] += grid[row - 1][col]
                elif col > 0:
                    grid[row][col] += grid[row][col - 1]
        return grid[len(grid) - 1][len(grid[0]) - 1]

    # Best Solution 68 ms
    def minPathSum2(self, grid2: List[List[int]]) -> int:
        for col in range(1, len(grid2[0])):
            grid2[0][col] += grid2[0][col - 1]

        for row in range(1, len(grid2)):
            grid2[row][0] += grid2[row - 1][0]

        for row in range(1, len(grid2)):
            for col in range(1, len(grid2[0])):
                grid2[row][col] += min(grid2[row - 1][col], grid2[row][col - 1])
        # return the minimum path
        return grid2[-1][-1]


# Main Call
solution = Solution()
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
result = solution.minPathSum(grid)
print(result)

grid2 = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
result = solution.minPathSum2(grid2)
print(result)
