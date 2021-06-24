"""
 Out of Boundary Paths
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent four cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.



Example 1:


Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6
Example 2:


Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12


Constraints:

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow <= m
0 <= startColumn <= n
   Hide Hint #1
WIll traversing every path is fesaible? There are many possible paths for a small matrix. Try to optimize it.
   Hide Hint #2
Can we use some space to store the number of paths and updating them after every move?
   Hide Hint #3
One obvious thing: ball will go out of boundary only by crossing it. Also, there is only one possible way ball can go out of boundary from boundary cell except corner cells. From corner cell ball can go out in two different ways. Can you use this thing to solve the problem?

"""
from functools import lru_cache
from itertools import product


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # Solution 1 - 136 ms
        """
        if maxMove == 0:
            return 0
        dpCurr = [[0] * (n + 2) for _ in range(m + 2)]
        dpLast = [[0] * (n + 2) for _ in range(m + 2)]
        for i in range(1, m + 1):
            dpCurr[i][1] += 1
            dpCurr[i][n] += 1
        for j in range(1, n + 1):
            dpCurr[1][j] += 1
            dpCurr[m][j] += 1
        ans = dpCurr[startRow + 1][startColumn + 1]
        for d in range(maxMove - 1):
            dpCurr, dpLast = dpLast, dpCurr
            for i, j in product(range(1, m + 1), range(1, n + 1)):
                dpCurr[i][j] = (dpLast[i - 1][j] + dpLast[i + 1][j] + dpLast[i][j - 1] + dpLast[i][j + 1]) % 1000000007
            ans = (ans + dpCurr[startRow + 1][startColumn + 1]) % 1000000007
        return ans
        """
        # Solution 2 - 76 ms
        @lru_cache(None)
        def dfs(i, j, u):
            # if u <= 0 or i < 0 or i >= m or j < 0 or j >= n:
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            elif u <= 0:
                return 0
            return dfs(i - 1, j, u - 1) + dfs(i + 1, j, u - 1) + dfs(i, j - 1, u - 1) + dfs(i, j + 1, u - 1)

        return dfs(startRow, startColumn, maxMove) % (10 ** 9 + 7)


# Main Call
m = 2
n = 2
maxMove = 2
startRow = 0
startColumn = 0

solution = Solution()
print(solution.findPaths(m, n, maxMove, startRow, startColumn))