"""
(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.

https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3306/



Example 1:



Input: mat = [[0,0],[1,1]]
Output: 0
Example 2:



Input: mat = [[0,0],[0,1]]
Output: 1
Example 3:



Input: mat = [[0,0],[0,0]]
Output: -1
Example 4:



Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1


Constraints:

1 <= mat.length, mat[i].length <= 100
mat[i][j] is either 0 or 1.
mat[i] is sorted in a non-decreasing way.
   Hide Hint #1
1. (Binary Search) For each row do a binary search to find the leftmost one on that row and update the answer.
   Hide Hint #2
2. (Optimal Approach) Imagine there is a pointer p(x, y) starting from top right corner. p can only move left or down. If the value at p is 0, move down. If the value at p is 1, move left. Try to figure out the correctness and time complexity of this algorithm.


"""

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
from typing import List


class BinaryMatrix(object):
    def __init__(self, matrix):
        self.mat = matrix
        self.rows = len(self.mat)
        self.cols = len(self.mat[0])

    def get(self, x: int, y: int) -> int:
        for r in range(self.rows):
            for c in range(self.cols):
                if x == r and y == c:
                    value = self.mat[r][c]
        return value

    def dimensions(self) -> List[int]:
        return [self.rows, self.cols]


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: BinaryMatrix) -> int:
        # 96 ms
        binaryMatrix = BinaryMatrix(binaryMatrix)
        rows, cols = binaryMatrix.dimensions()
        print(rows)
        print(cols)

        left_most_col = -1
        if rows == 0 or cols == 0:
            return left_most_col

        current_row = 0
        current_col = cols - 1

        while current_row < rows and current_col >= 0:
            if binaryMatrix.get(current_row, current_col) == 1:
                left_most_col = current_col
                current_col = current_col - 1
            else:
                current_row = current_row + 1

        # return the left most column with 1
        return left_most_col


# Main Call

# Testing Binary Matrix
input_mat = [[0, 0], [1, 1]]
matrix = BinaryMatrix(input_mat)
rows, cols = matrix.dimensions()
print(rows, cols)
value = matrix.get(1, 1)
print(value)


solution = Solution()
result = solution.leftMostColumnWithOne(input_mat)
print(result)
