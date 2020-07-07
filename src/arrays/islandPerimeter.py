"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3383/
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:


"""
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Solution 1 - 672 ms
        """
        self.perimeter = 0
        row = len(grid)
        col = len(grid[0])

        for r in range(row):
            for c in range(col):

                if grid[r][c] == 1:
                    if r == 0 or grid[r - 1][c] != 1:
                        self.perimeter += 1
                    if c == 0 or grid[r][c - 1] != 1:
                        self.perimeter += 1
                    if c == col - 1 or grid[r][c + 1] != 1:
                        self.perimeter += 1
                    if r == row - 1 or grid[r + 1][c] != 1:
                        self.perimeter += 1

        return self.perimeter
        """
        # Solution 2 - 452 ms
        rows = len(grid)
        cols = len(grid[0])
        result = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result += 4
                    if r > 0 and grid[r - 1][c] == 1:
                        result -= 2
                    if c > 0 and grid[r][c - 1] == 1:
                        result -= 2
        return result


# Main Call
solution = Solution()
grid = [[0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]]

print(solution.islandPerimeter(grid))
