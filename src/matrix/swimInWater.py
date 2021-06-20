"""
Swim in Rising Water
On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
Note:

2 <= N <= 50.
grid[i][j] is a permutation of [0, ..., N*N - 1].
   Hide Hint #1
Use either Dijkstra's, or binary search for the best time T for which you can reach the end if you only step on squares at most T.
"""
from heapq import heappop, heappush
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Solution 1 - 96 ms
        """
        N, heap, visited, res = len(grid), [(grid[0][0], 0, 0)], set([(0, 0)]), 0

        for i in range(N * N):
            val, x, y = heappop(heap)
            res = max(res, val)
            if x == N - 1 and y == N - 1: return res
            neib_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dx, dy in neib_list:
                if (x + dx, y + dy) not in visited and 0 <= x + dx < N and 0 <= y + dy < N:
                    heappush(heap, (grid[x + dx][y + dy], x + dx, y + dy))
                    visited.add((x + dx, y + dy))
        """
        # Solution 2 - 88 ms
        ans = 0
        n = len(grid)
        mh = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        while mh:
            val, x, y = heappop(mh)
            if x == y == n - 1:
                return val
            for i, j in ((x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= i < n and 0 <= j < n and (i, j) not in visited:
                    visited.add((i, j))
                    heappush(mh, (max(val, grid[i][j]), (i), (j)))


# Main Call
grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
solution = Solution()
print(solution.swimInWater(grid))

