"""
Pacific Atlantic Water Flow
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.


Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""
import collections
from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # Solution 1 - 280 ms
        """
                :type matrix: List[List[int]]
                :rtype: List[List[int]]
        """
        """
        if not matrix or not matrix[0]:
            return []

        # instead of checking each cell with condition, we can start from ocean cordinates
        # going in increasing order
        # intersection of both of them is the result
        self.R = len(matrix)
        self.C = len(matrix[0])
        self.matrix = matrix

        # cordinates closer to pacific ocean
        pacific = [(0, j) for j in range(self.C)] + [(i, 0) for i in range(1, self.R)]

        # cordinates closer to atlantic ocean
        atlantic = [(i, self.C - 1) for i in range(self.R)] + [(self.R - 1, j) for j in range(self.C - 1)]

        return self.bfs(pacific) & self.bfs(atlantic)
        """
        # Solution 2 - 252 ms
        pacificSet = set()

        def pacificHelper(cord):
            if cord in pacificSet:
                return
            y, x = cord
            pacificSet.add(cord)
            if y > 0:
                if matrix[y][x] <= matrix[y - 1][x]:
                    pacificHelper((y - 1, x))
            if y < len(matrix) - 1:
                if matrix[y][x] <= matrix[y + 1][x]:
                    pacificHelper((y + 1, x))
            if x > 0:
                if matrix[y][x] <= matrix[y][x - 1]:
                    pacificHelper((y, x - 1))
            if x < len(matrix[y]) - 1:
                if matrix[y][x] <= matrix[y][x + 1]:
                    pacificHelper((y, x + 1))

        atlanticSet = set()

        def atlanticHelper(cord):
            if cord in atlanticSet:
                return
            y, x = cord
            atlanticSet.add(cord)
            if y > 0:
                if matrix[y][x] <= matrix[y - 1][x]:
                    atlanticHelper((y - 1, x))
            if y < len(matrix) - 1:
                if matrix[y][x] <= matrix[y + 1][x]:
                    atlanticHelper((y + 1, x))
            if x > 0:
                if matrix[y][x] <= matrix[y][x - 1]:
                    atlanticHelper((y, x - 1))
            if x < len(matrix[y]) - 1:
                if matrix[y][x] <= matrix[y][x + 1]:
                    atlanticHelper((y, x + 1))

        if len(matrix) == 0:
            return []
        for x in range(len(matrix[0])):
            pacificHelper((0, x))
        for y in range(len(matrix)):
            pacificHelper((y, 0))
        for x in range(len(matrix[-1])):
            atlanticHelper((len(matrix) - 1, x))
        for y in range(len(matrix)):
            atlanticHelper((y, len(matrix[y]) - 1))
        res = []
        for val in pacificSet:
            if val in atlanticSet:
                res.append(val)
        return res


def bfs(self, ocean):
        queue = collections.deque(ocean)
        visited = set(ocean)

        while queue:
            r, c = queue.popleft()

            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < self.R and 0 <= nc < self.C and (nr, nc) not in visited and \
                        self.matrix[nr][nc] >= self.matrix[r][c]:
                    queue.append((nr, nc))
                    visited.add((nr, nc))

        return visited


# Main Call
matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
solution = Solution()
print(solution.pacificAtlantic(matrix))