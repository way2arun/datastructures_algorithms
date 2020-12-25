"""
Diagonal Traverse
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.



Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:



Note:

The total number of elements of the given matrix will not exceed 10,000.
"""
import itertools
from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # Solution 1 - 208 ms
        """
        ans = []

        M = len(matrix)
        if M == 0:
            return ans
        N = len(matrix[0])

        up = [0, 0]
        down = [0, 0]  # start points of up and down paths
        isUp = False  # is traversal from up or down

        while (up[0] < M and up[1] < N) and (down[0] < M and down[1] < N):
            if isUp:
                (i, j) = (up[0], up[1])
            else:
                (i, j) = (down[0], down[1])

            while 0 <= i < M and 0 <= j < N:
                ans.append(matrix[i][j])
                if isUp:
                    i += 1
                    j -= 1
                else:
                    i -= 1
                    j += 1

            # move both up and down paths to next
            if up[1] == N - 1:
                up[0] += 1
            else:
                up[1] += 1

            if down[0] == M - 1:
                down[1] += 1
            else:
                down[0] += 1

            isUp = not isUp

        return ans
        """
        # Solution 2 - 168 ms
        """
        if not matrix or not matrix[0]:
            return []
        r = len(matrix)
        c = len(matrix[0])
        # count = 0
        seq = []
        row = col = 0
        upward = True

        # seq.append(matrix[i][j])
        for k in range(r * c):
            # print(row, col)
            seq.append(matrix[row][col])
            if upward:
                if row - 1 >= 0 and col + 1 < c:
                    row -= 1
                    col += 1
                elif not (row - 1 >= 0 or col + 1 < c):
                    upward = False
                    row += 1
                elif col + 1 < c:
                    upward = False
                    col += 1
                # elif row-1 >= 0:
                else:
                    upward = False
                    row += 1
            else:
                if col - 1 >= 0 and row + 1 < r:
                    col -= 1
                    row += 1
                elif not (col - 1 >= 0 or row + 1 < r):
                    upward = True
                    col += 1
                elif row + 1 < r:
                    upward = True
                    row += 1
                # elif col-1 >=0:
                else:
                    upward = True
                    col += 1
        return seq
        """

        # Solution 3 - 164 ms

        if not matrix:
            return []

        R, C = len(matrix), len(matrix[0])

        groups = [[] for _ in range(R + C)]

        for r in range(R):
            for c in range(C):
                groups[r + c].append(matrix[r][c])

        for r in range(0, R + C, 2):
            groups[r].reverse()

        return itertools.chain.from_iterable(groups)


# Main Call
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

solution = Solution()
print(solution.findDiagonalOrder(matrix))
mat = solution.findDiagonalOrder(matrix)
results = [x for x in itertools.combinations(mat, 9)]
print(results)
