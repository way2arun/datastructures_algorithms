"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3312/

"""
from typing import List
import time


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        # 40 ms 188 ms
        if not matrix or not matrix[0]:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])

        temp = [[0 for col in range(cols + 1)] for row in range(rows + 1)]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    temp[i][j] = min(temp[i - 1][j - 1], temp[i - 1][j], temp[i][j - 1]) + 1
                else:
                    temp[i][j] = 0
        return max([max(row) for row in temp]) ** 2
        """
        # 156 ms
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        max_width = 0
        for row in range(rows):
            width = 0
            for col in range(cols):
                # populates heights arr
                if matrix[row][col] == '1':
                    heights[col] += 1
                else:
                    heights[col] = 0
                # calculates max square width using greedy approach
                if heights[col] > max_width:
                    width += 1
                    if width > max_width:
                        max_width, width = width, 0
                else:
                    width = 0
        return max_width * max_width


# Main Call
solution = Solution()
matrix = [
    "10100",
    "10111",
    "11111",
    "10010"
]
start = time.time()
print(solution.maximalSquare(matrix))
end = time.time()
print("Elapsed time was %g seconds" % (end - start))
