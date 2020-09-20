"""
Unique Paths III
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3466/
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.



Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation:
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.


Note:

1 <= grid.length * grid[0].length <= 20
"""
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Solution 1 - 44 ms
        """
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])

        # 1. profiling
        obs = 0
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v == 1:
                    rs, cs = r, c  # start
                elif v == -1:
                    obs += 1  # obstacles
                elif v == 2:
                    re, ce = r, c  # end

        # 2. backtrack
        tot = m * n - obs - 1  # total steps
        ans = 0

        def backtrack(r=rs, c=cs, steps=0):
            nonlocal tot, m, n, ans
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                rn, cn = r + dr, c + dc
                if not (0 <= rn < m and 0 <= cn < n and grid[rn][cn] in (0, 2)):
                    continue
                if grid[rn][cn] == 2:
                    if steps + 1 == tot:
                        ans += 1
                    continue
                grid[rn][cn] = -1
                backtrack(rn, cn, steps + 1)
                grid[rn][cn] = 0

        backtrack()
        return ans
        """
        # Solution 2 - 28 ms
        m = len(grid)
        n = len(grid[0])

        cntTarget = 0
        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:
                    xStart = i
                    yStart = j

                if grid[i][j] == 2:
                    xEnd = i
                    yEnd = j

                if grid[i][j] == -1:
                    cntTarget += 1
        cntTarget = m * n - cntTarget

        numSol = [0]
        cnt = 1
        # grid[xStart][yStart] = -1
        # his = []
        self.search(grid, xStart, yStart, numSol, cnt, cntTarget)

        return numSol[0]

    def search(self, grid, x, y, numSol, cnt, cntTarget):
        # print(x, y)
        if grid[x][y] < 0:
            # print("?6", x, y, grid[x][y])
            return
        if grid[x][y] == 2:
            if cnt == cntTarget:
                numSol[0] += 1
                # print(his)
            return
        grid[x][y] = -2
        # his.append((x, y))
        if (x + 1) < len(grid):
            # grid[x + 1][y] = -2
            self.search(grid, x + 1, y, numSol, cnt + 1, cntTarget)
            # grid[x + 1][y] = 0
        # else:
        #     print("?1", x, y)

        if (x - 1) >= 0:
            # grid[x - 1][y] = -2
            self.search(grid, x - 1, y, numSol, cnt + 1, cntTarget)
            # grid[x - 1][y] = 0
        # else:
        #     print("?2", x, y)
        if (y + 1) < len(grid[0]):
            # grid[x][y + 1] = -2
            self.search(grid, x, y + 1, numSol, cnt + 1, cntTarget)
            # grid[x][y + 1] = 0
        # else:
        #     print("?3", x, y)
        if (y - 1) >= 0:
            # grid[x][y - 1] = -2
            self.search(grid, x, y - 1, numSol, cnt + 1, cntTarget)
            # grid[x][y - 1] = 0
        # else:
        #     print("?4", x, y)
        grid[x][y] = 0
        # his.pop()


# Main Call
solution = Solution()
grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
print(solution.uniquePathsIII(grid))
