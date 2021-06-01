"""
Max Area of Island
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""
from itertools import product
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Solution 1 - 164 ms
        """
        ans, n, m = 0, len(grid), len(grid[0])

        def trav(i: int, j: int) -> int:
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0: return 0
            grid[i][j] = 0
            return 1 + trav(i - 1, j) + trav(i, j - 1) + trav(i + 1, j) + trav(i, j + 1)

        for i, j in product(range(n), range(m)):
            if grid[i][j]: ans = max(ans, trav(i, j))
        return ans
        """
        # Solution 2 - 100 ms
        num_rows = len(grid)

        if num_rows < 1:
            return 0

        num_columns = len(grid[0])

        grid_copy = grid.copy()

        max_area = 0
        for row in range(num_rows):
            for column in range(num_columns):
                if grid_copy[row][column] == 1:
                    grid_copy[row][column] = 0
                    stack = [(row, column)]
                    area = 0
                    while stack:
                        r, c = stack.pop()
                        area += 1
                        if r > 0 and grid_copy[r - 1][c] == 1:
                            stack.append((r - 1, c))
                            grid_copy[r - 1][c] = 0
                        if r < num_rows - 1 and grid_copy[r + 1][c] == 1:
                            stack.append((r + 1, c))
                            grid_copy[r + 1][c] = 0
                        if c > 0 and grid_copy[r][c - 1] == 1:
                            stack.append((r, c - 1))
                            grid_copy[r][c - 1] = 0
                        if c < num_columns - 1 and grid_copy[r][c + 1] == 1:
                            stack.append((r, c + 1))
                            grid_copy[r][c + 1] = 0
                    max_area = max(max_area, area)

        return max_area


# Main Call
grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

solution = Solution()
print(solution.maxAreaOfIsland(grid))