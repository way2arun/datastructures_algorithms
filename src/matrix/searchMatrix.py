"""
 Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false
Example 3:

Input: matrix = [], target = 0
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
0 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Solution 1 - 36 ms
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix[0]), len(matrix)
        beg, end = 0, m * n - 1
        while beg < end:
            mid = (beg + end) // 2
            if matrix[mid // m][mid % m] < target:
                beg = mid + 1
            else:
                end = mid
        return matrix[beg // m][beg % m] == target
        """
        # Solution 2 -  28 ms
        if len(matrix) > 0:
            n = len(matrix)
            m = len(matrix[0])

            low = 0
            high = n * m - 1
            while low <= high:
                mid = low + (high - low) // 2
                if matrix[mid // m][mid % m] == target:
                    return True
                elif matrix[mid // m][mid % m] > target:
                    high = mid - 1
                elif matrix[mid // m][mid % m] < target:
                    low = mid + 1
            else:
                return False
        else:
            return False


# Main Call
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
target = 3
solution = Solution()
print(solution.searchMatrix(matrix, target))
