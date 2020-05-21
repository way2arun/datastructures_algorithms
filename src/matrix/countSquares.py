"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.



Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.


Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
   Hide Hint #1
Create an additive table that counts the sum of elements of submatrix with the superior corner at (0,0).
   Hide Hint #2
Loop over all subsquares in O(n^3) and check if the sum make the whole array to be ones, if it checks then add 1 to the answer.
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3336/
"""
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        rows = len(matrix)
        cols = len(matrix[0])
        grid = [[0] * (cols + 1) for _ in range(rows + 1)]

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    grid[row + 1][col + 1] = 0
                if matrix[row][col] == 1:
                    grid[row + 1][col + 1] = 1 + min(grid[row][col + 1], grid[row + 1][col], grid[row][col])

        count_ones = [n for array in grid for n in array]
        return sum(count_ones)
        """
        # Solution 2
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] and matrix[i][j - 1] and matrix[i - 1][j - 1]:
                    k = min(matrix[i - 1][j], matrix[i][j - 1])
                    matrix[i][j] = k + 1 if matrix[i - k][j - k] else k

        return sum(sum(row) for row in matrix)


# Main Call
matrix = [
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 0]
]
solution = Solution()
print(solution.countSquares(matrix))
