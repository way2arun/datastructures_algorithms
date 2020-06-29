"""
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/543/week-5-june-29th-june-30th/3375/
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?



Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28


Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Solution 1 28 ms
        """
        matrix = [[0 for i in range(m + 1)] for i in range(n + 1)]
        for x in range(1, n + 1):
            for y in range(1, m + 1):
                if x == 1 or y == 1:
                    matrix[x][y] = 1
                else:
                    matrix[x][y] = matrix[x - 1][y] + matrix[x][y - 1]
        return matrix[-1][-1]
        """
        # Solution 2
        """
        x = (m - 1) + (n - 1)
        y = n - 1
        ans = self.factorial(x) // (self.factorial(y) * self.factorial(x - y))
        return int(ans)
        """
        # Solution 3 8 ms
        grid = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            grid[0][i] = 1

        for i in range(n):
            grid[i][0] = 1

        for r in range(1, n):
            for c in range(1, m):
                grid[r][c] = grid[r - 1][c] + grid[r][c - 1]

        return grid[n - 1][m - 1]

    def factorial(self, number):
        res = 1
        for i in range(number, 0, -1):
            res *= i
        return res


# Main Call
solution = Solution()
m = 7
n = 3
print(solution.uniquePaths(m, n))
