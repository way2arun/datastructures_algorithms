"""
Shortest Path in a Grid with Obstacles Elimination
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.



Example 1:

Input:
grid =
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]],
k = 1
Output: 6
Explanation:
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
Example 2:

Input:
grid =
[[0,1,1],
 [1,1,1],
 [1,0,0]],
k = 1
Output: -1
Explanation:
We need to eliminate at least two obstacles to find such a walk.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] == 0 or 1
grid[0][0] == grid[m - 1][n - 1] == 0
   Hide Hint #1
Use BFS.
   Hide Hint #2
BFS on (x,y,r) x,y is coordinate, r is remain number of obstacles you can remove.

"""
import heapq
from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # Solution 1 - 76 ms
        """
        m, n = len(grid), len(grid[0])
        Q, v = deque([(0, 0, 0, k)]), set()

        if k >= m + n - 2: return m + n - 2

        while Q:
            steps, x, y, k = Q.popleft()
            if (x, y) == (n - 1, m - 1): return steps

            for dx, dy in (x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y):
                if 0 <= dx < n and 0 <= dy < m and k - grid[dy][dx] >= 0:
                    new = (dx, dy, k - grid[dy][dx])
                    if new not in v:
                        v.add(new)
                        Q.append((steps + 1,) + new)

        return -1
        """
        # Solution 2 - 44 ms
        rows = len(grid) - 1
        cols = len(grid[0]) - 1
        q = [(rows + cols, 0, (0, 0, k))]
        seen = set((0, 0, k))

        if k >= rows + cols:
            return rows + cols

        while q:
            est, step, (x, y, k) = heapq.heappop(q)

            if est - step <= k:
                return est

            for i, j in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if 0 <= x + i <= rows and 0 <= y + j <= cols:
                    a = x + i
                    b = y + j
                    state = (a, b, k - grid[a][b])
                    if k - grid[a][b] >= 0 and state not in seen:
                        heapq.heappush(q, ((rows - a + cols - b) + step + 1, step + 1, state))
                        seen.add(state)

        return -1


# Main Call
grid = [[0, 0, 0],
 [1, 1, 0],
 [0, 0, 0],
 [0, 1, 1],
 [0, 0, 0]]
k = 1
solution = Solution()
print(solution.shortestPath(grid, k))