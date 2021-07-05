"""
Reshape the Matrix
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the row number and column number of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.



Example 1:


Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Example 2:


Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300
   Hide Hint #1
Do you know how 2d matrix is stored in 1d memory? Try to map 2-dimensions into one.
   Hide Hint #2
M[i][j]=M[n*i+j] , where n is the number of cols. This is the one way of converting 2-d indices into one 1-d index. Now, how will you convert 1-d index into 2-d indices?
   Hide Hint #3
Try to use division and modulus to convert 1-d index into 2-d indices.
   Hide Hint #4
M[i] => M[i/n][n%i] Will it result in right mapping? Take some example and check this formula.
"""
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # Solution 1 - 88 ms
        """
        queue = [cell for row in mat for cell in row] if r * c == len(mat) * len(mat[0]) else []
        return [[queue.pop(0) for _ in range(c)] for _ in range(r)] if queue else mat
        """
        # Solution 2 - 68 ms
        ans = [element for row in mat for element in row]

        if len(ans) == r * c:
            return [ans[i * c:(i + 1) * c] for i in range(r)]
        return mat


# Main Call
solution = Solution()
mat = [[1,2],[3,4]]
r = 1
c = 4
print(solution.matrixReshape(mat, r, c))