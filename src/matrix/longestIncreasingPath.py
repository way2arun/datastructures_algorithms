"""
Longest Increasing Path in a Matrix
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).



Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
"""
import functools
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Solution 1 - 536 ms
        """
        m = len(matrix)
        n = len(matrix[0])
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            # get the max total length
            max_path = 0
            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < m and 0 <= new_j < n:
                    if matrix[new_i][new_j] > matrix[i][j]:
                        max_path = max(dfs(new_i, new_j), max_path)
                cache[(i, j)] = max_path + 1
            return max_path + 1

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res
        """
        # Solution 2 - 320 ms
        if not matrix:
            return 0

        h = len(matrix)
        w = len(matrix[0])
        if not w:
            return 0

        # do not cache matrix, not cachable and too big
        @functools.lru_cache(maxsize=None)
        def lip(i, j):
            nbs = []  # neighbours
            if i > 0: nbs.append((i - 1, j))
            if i < h - 1: nbs.append((i + 1, j))
            if j > 0: nbs.append((i, j - 1))
            if j < w - 1: nbs.append((i, j + 1))

            maxp = 1
            for nb in nbs:
                if matrix[nb[0]][nb[1]] > matrix[i][j]:
                    m = lip(nb[0], nb[1]) + 1
                    maxp = max(maxp, m)
            return maxp

        maxap = 1
        for i in range(h):
            for j in range(w):
                maxap = max(maxap, lip(i, j))

        return maxap

    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])

        @functools.lru_cache(maxsize=None)
        def dfs(i, j):
            val = matrix[i][j]
            return 1 + max(
                dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)

        return max(dfs(x, y) for x in range(M) for y in range(N))


# Main Call
matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
solution = Solution()
print(solution.longestIncreasingPath(matrix))