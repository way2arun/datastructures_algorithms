"""
Set Matrix Zeroes
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.



Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1


Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
   Hide Hint #1
If any cell of the matrix has a zero we can record its row and column number using additional memory. But if you don't want to use extra memory then you can manipulate the array instead. i.e. simulating exactly what the question says.
   Hide Hint #2
Setting cell values to zero on the fly while iterating might lead to discrepancies. What if you use some other integer value as your marker? There is still a better approach for this problem with 0(1) space.
   Hide Hint #3
We could have used 2 sets to keep a record of rows/columns which need to be set to zero. But for an O(1) space solution, you can use one of the rows and and one of the columns to keep track of this information.
   Hide Hint #4
We can use the first cell of every row and column as a flag. This flag would determine whether a row or column has been set to zero.

"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Solution 1 - 132 ms
        """
        m, n = len(matrix[0]), len(matrix)
        r1 = any(matrix[0][j] == 0 for j in range(m))
        c1 = any(matrix[i][0] == 0 for i in range(n))
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0: matrix[i][0] = matrix[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] * matrix[0][j] == 0: matrix[i][j] = 0

        if r1:
            for i in range(m): matrix[0][i] = 0

        if c1:
            for j in range(n): matrix[j][0] = 0

        print(matrix)
        """
        # Solution 2 - 104 ms
        x_zeros = []
        x_len = len(matrix[0])
        y_len = len(matrix)
        for y in range(y_len):
            if 0 in matrix[y]:
                x_zeros0 = []
                for j in range(matrix[y].count(0)):
                    if len(x_zeros0) == 0:
                        x_zeros0.append(matrix[y].index(0))
                    else:
                        x_zeros0.append(matrix[y].index(0, x_zeros0[-1] + 1))
                x_zeros += x_zeros0
                matrix[y] = [0 for _ in range(x_len)]
        x_zeros = list(set(x_zeros))
        for y in range(y_len):
            if matrix[y][0] != 0:
                for x in x_zeros: matrix[y][x] = 0
        print(matrix)


# Main Call
solution = Solution()
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
solution.setZeroes(matrix)
