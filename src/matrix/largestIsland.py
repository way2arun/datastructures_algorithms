"""
Making A Large Island
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.



Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.


Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
"""
from collections import deque
from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.size = [0] * n

    def isExist(self, u):
        return self.parent[u] >= 0

    def add(self, u):
        if self.isExist(u): return  # Only add if not existed yet!
        self.parent[u] = u
        self.size[u] = 1

    def find(self, u):
        if self.parent[u] == u: return u
        self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        if self.size[pu] <= self.size[pv]:  # Merge the smaller component to the bigger component
            self.parent[pu] = pv  # Merge u into v
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu  # Merge v into u
            self.size[pu] += self.size[pv]
        return True


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # Solution 1 - 5192 ms
        """
        DIR = [0, 1, 0, -1, 0]
        m, n, ans = len(grid), len(grid[0]), 0
        uf = UnionFind(m * n)

        def landNeighbors(r, c):
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                neiId = nr * n + nc
                if nr < 0 or nr == m or nc < 0 or nc == n or not uf.isExist(neiId): continue
                yield neiId

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0: continue
                curId = r * n + c
                uf.add(curId)
                for neiId in landNeighbors(r, c):
                    uf.union(curId, neiId)
                p = uf.find(curId)
                ans = max(ans, uf.size[p])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1: continue
                neiParents = set()
                for neiId in landNeighbors(r, c):
                    neiParents.add(uf.find(neiId))
                sizeFormed = 1  # Start with 1, which is matrix[r][c] when turning from 0 into 1
                for p in neiParents:
                    sizeFormed += uf.size[p]
                ans = max(ans, sizeFormed)
        return ans
        """
        # Solution 2 - 2004 ms
        n = len(grid)
        grd0 = [[0] * (n + 2)]
        grd1 = [[0] + i + [0] for i in grid]
        grd2 = [[0] * (n + 2)]

        grd = grd0 + grd1 + grd2

        def mark_island(grd, i, j, mark):
            s = 0
            cells = deque()
            cells.append((i, j))
            nulls = set()

            while True:
                try:
                    ii, jj = cells.popleft()
                    if grd[ii][jj] == 1:
                        s += 1
                        grd[ii][jj] = mark
                        for nx, ny in ((ii - 1, jj), (ii + 1, jj), (ii, jj - 1), (ii, jj + 1)):
                            if grd[nx][ny] == 1:
                                cells.append((nx, ny))
                            elif grd[nx][ny] < 1:
                                nulls.add((nx, ny))

                except Exception:
                    for ii, jj in nulls:
                        grd[ii][jj] -= s
                    return

        mark = 1
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if grd[i][j] == 1:
                    mark += 1
                    mark_island(grd, i, j, mark)

        answer = 1
        answer -= min([min(l) for l in grd])

        return min(n * n, answer)


# Main Call
grid = [[1, 0], [0, 1]]
solution = Solution()
print(solution.largestIsland(grid))
