"""
Range Sum Query 2D - Immutable
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).


Example 1:


Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-105 <= matrix[i][j] <= 105
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 104 calls will be made to sumRegion.
"""
from typing import List


class NumMatrix:

    # Solution 1 - 284 ms
    """
    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        self.matrix = matrix.copy()
        for i in range(len(matrix)):
            running_sum = 0
            for j in range(len(matrix[0])):
                value = matrix[i][j]
                running_sum = running_sum + value
                self.dp[i][j] = running_sum


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        value = self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]
        print(value)
        return value
    """
    # Solution 2 - 108 ms
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        self.pre_matrix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.pre_matrix[i + 1][j + 1] += self.pre_matrix[i + 1][j] + self.pre_matrix[i][j + 1] - \
                                                 self.pre_matrix[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre_matrix[row2 + 1][col2 + 1] - self.pre_matrix[row2 + 1][col1] - self.pre_matrix[row1][col2 + 1] + \
               self.pre_matrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
matrix = [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3],
          [1, 1, 2, 2], [1, 2, 2, 4]]
numMatrix = NumMatrix(matrix)

numMatrix.sumRegion(2, 1, 4, 3)  # return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2)  # return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4)  # return 12 (i.e sum of the blue rectangle)
