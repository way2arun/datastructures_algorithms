"""
Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
   Hide Hint #1
Well for some problems, the best way really is to come up with some algorithms for simulation. Basically, you need to simulate what the problem asks us to do.
   Hide Hint #2
We go boundary by boundary and move inwards. That is the essential operation. First row, last column, last row, first column and then we move inwards by 1 and then repeat. That's all, that is all the simulation that we need.
   Hide Hint #3
Think about when you want to switch the progress on one of the indexes. If you progress on
i
out of
[i, j]
, you'd be shifting in the same column. Similarly, by changing values for
j
, you'd be shifting in the same row. Also, keep track of the end of a boundary so that you can move inwards and then keep repeating. It's always best to run the simulation on edge cases like a single column or a single row to see if anything breaks or not.

"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Solution 1 - 32 ms
        """
        n, m = len(matrix[0]), len(matrix)
        x, y, dx, dy = 0, 0, 1, 0
        ans = []
        for _ in range(m * n):
            if not 0 <= x + dx < n or not 0 <= y + dy < m or matrix[y + dy][x + dx] == "*":
                dx, dy = -dy, dx

            ans.append(matrix[y][x])
            matrix[y][x] = "*"
            x, y = x + dx, y + dy

        return ans
        """
        # Solution 2 - 12 ms
        m, n = len(matrix), len(matrix[0])
        i_start, i_end = 0, m - 1
        j_start, j_end = 0, n - 1

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = []

        i, j = i_start, j_start
        while True:
            flag = False
            while j <= j_end:
                res.append(matrix[i][j])
                j += 1
                flag = True
            if not flag:
                break
            i_start += 1
            i, j = i_start, j_end
            # print(res)

            flag = False
            while i <= i_end:
                res.append(matrix[i][j])
                i += 1
                flag = True
            if not flag:
                break
            j_end -= 1
            j = j_end
            i, j = i_end, j_end
            # print(res)

            flag = False
            while j >= j_start:
                res.append(matrix[i][j])
                j -= 1
                flag = True
            if not flag:
                break
            i_end -= 1
            i = i_end
            i, j = i_end, j_start
            # print(res)

            flag = False
            while i >= i_start:
                res.append(matrix[i][j])
                i -= 1
                flag = True
            if not flag:
                break
            j_start += 1
            j = j_start
            i, j = i_start, j_start
            # print(res)

        return res


# Main Call
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
solution = Solution()
print(solution.spiralOrder(matrix))