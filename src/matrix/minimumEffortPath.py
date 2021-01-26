"""
Path With Minimum Effort
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.



Example 1:



Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:



Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.


Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
   Hide Hint #1
Consider the grid as a graph, where adjacent cells have an edge with cost of the difference between the cells.
   Hide Hint #2
If you are given threshold k, check if it is possible to go from (0, 0) to (n-1, m-1) using only edges of ≤ k cost.
   Hide Hint #3
Binary search the k value.

"""
import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Solution 1 - 1260 ms
        """
        m, n = len(heights), len(heights[0])
        best = [[float("inf")] * n for _ in range(m)]
        best[0][0] = 0
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        q = [(0, 0, 0)]
        end = (m - 1, n - 1)
        while q:
            effort, i, k = heapq.heappop(q)
            if (i, k) == end:
                return effort

            for x, y in directions:
                nxt_i, nxt_k = i + x, k + y
                if 0 <= nxt_i < m and 0 <= nxt_k < n:
                    nxt_effort = max(effort, abs(heights[nxt_i][nxt_k] - heights[i][k]))
                    if nxt_effort < best[nxt_i][nxt_k]:
                        best[nxt_i][nxt_k] = nxt_effort
                        heapq.heappush(q, (nxt_effort, nxt_i, nxt_k))
        """
        # Solution 2 - 452 ms
        m = len(heights)
        n = len(heights[0])
        boundary = [(0, 0, 0)]
        visited = set()
        ans = 0
        todo = []
        while True:
            if todo:
                a, i, j = todo.pop()
            else:
                a, i, j = heapq.heappop(boundary)
                ans = a
            if (i, j) == (m - 1, n - 1):
                return ans
            for x, y in ((i, j - 1), (i - 1, j), (i + 1, j), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n:
                    if (x, y) not in visited:
                        d = abs(heights[x][y] - heights[i][j])
                        if d <= ans:
                            todo.append((d, x, y))
                        else:
                            heapq.heappush(boundary, (d, x, y))
            visited.add((i, j))




# Main Call
heights = [[1,2,3],[3,8,4],[5,3,5]]
solution = Solution()
print(solution.minimumEffortPath(heights))