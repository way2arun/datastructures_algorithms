"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    self.depth_first_search(grid, row, col)
                    res += 1
        return res

    def depth_first_search(self, grid, r, c):
        directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        grid[r][c] = "0"
        for direction in directions:
            row, col = r + direction[0], c + direction[1]
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                if grid[row][col] == "1":
                    self.depth_first_search(grid, row, col)

    def numIslands_2ndSolution(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0

        last_islands = []  # islands found in the last line
        count_islands = []  # distinct islands
        for i in range(m):
            # find islands in this line
            curr_islands = []
            s = None
            for j in range(n):
                if grid[i][j] == "1":
                    if s is None:
                        s = j
                else:
                    if s is not None:
                        curr_islands.append([s, j, None])
                        s = None
            if s is not None:
                curr_islands.append([s, n, None])
            # find overlap with last island
            ilast = 0
            icurr = 0
            while ilast < len(last_islands) and icurr < len(curr_islands):
                slast, elast, last_index = last_islands[ilast]
                scurr, ecurr, curr_index = curr_islands[icurr]
                if slast < ecurr and scurr < elast:  # overlap
                    if curr_index is None:
                        curr_islands[icurr][-1] = last_index  # same island as last_island
                    elif curr_index != last_index:
                        count_islands[max(curr_index, last_index)] = 0  # remove duplicate island id
                        # note: always remove the larger id
                elif ecurr <= slast:  # curr < last
                    if curr_index is None:
                        curr_islands[icurr][-1] = len(count_islands)
                        count_islands.append(1)
                if elast <= ecurr:  # move pointer.
                    # if elast <= ecurr, then the last_island is impossible to overlap with any other curr_island
                    # therefore, we move ilast forward. vice versa
                    ilast += 1
                else:
                    icurr += 1
            # index new islands
            while icurr < len(curr_islands):
                if curr_islands[icurr][-1] is None:
                    curr_islands[icurr][-1] = len(count_islands)
                    count_islands.append(1)
                icurr += 1
            # search next line
            last_islands = curr_islands
        return sum(count_islands + [0, ])  # + [0, ] is to avoid error when len(count_islands) == 0

# Main Call


if __name__ == '__main__':
    solution = Solution()
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    # solution 1 DFS - 164 ms
    result = solution.numIslands(grid)
    print(result)

    # Second solution 100 ms
    grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    result = solution.numIslands_2ndSolution(grid)
    print(result)
