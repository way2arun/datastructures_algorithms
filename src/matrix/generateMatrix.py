"""
Spiral Matrix II
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.



Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 20
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Solution 1 - 36 ms
        """
        matrix = [[0] * n for _ in range(n)]
        x, y, dx, dy = 0, 0, 1, 0
        for i in range(n * n):
            matrix[y][x] = i + 1
            if not 0 <= x + dx < n or not 0 <= y + dy < n or matrix[y + dy][x + dx] != 0:
                dx, dy = -dy, dx
            x, y = x + dx, y + dy
        return matrix
        """
        # Solution 2 - 12 ms
        return self.generateMatrixb(n, 0, 0, 0, [[0] * n for _ in range(n)], 1)

    def generateMatrixb(self, n, r, c, direc, matrix, num):
        if r < 0 or r == n or c < 0 or c == n or matrix[r][c] != 0:
            return matrix

        matrix[r][c] = num

        EAST = 0
        SOUTH = 1
        WEST = 2
        NORTH = 3

        vR = r
        vC = c

        if direc == EAST:
            vC += 1
        elif direc == SOUTH:
            vR += 1
        elif direc == WEST:
            vC -= 1
        else:
            vR -= 1

        if vR < 0 or vC < 0 or vR == n or vC == n or matrix[vR][vC] != 0:
            direc = (direc + 1) % 4
            if direc == EAST:
                c += 1
            elif direc == SOUTH:
                r += 1
            elif direc == WEST:
                c -= 1
            else:
                r -= 1
        else:
            r = vR
            c = vC

        return self.generateMatrixb(n, r, c, direc, matrix, num + 1)


# Main Call
n = 3
solution = Solution()
print(solution.generateMatrix(n))
