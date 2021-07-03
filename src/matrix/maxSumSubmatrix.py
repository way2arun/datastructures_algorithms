"""
Max Sum of Rectangle No Larger Than K
Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than k.



Example 1:


Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).
Example 2:

Input: matrix = [[2,2,-1]], k = 3
Output: 3


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-100 <= matrix[i][j] <= 100
-105 <= k <= 105


Follow up: What if the number of rows is much larger than the number of columns?
"""
import math

from itertools import accumulate
from typing import List

from sortedcontainers import SortedList


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # Solution 1 - 7004 ms
        """
        M = len(matrix)
        N = len(matrix[0])
        CSr = [None for _ in matrix]
        for i, row in enumerate(matrix):
            CSr[i] = list(accumulate(row, initial=0))

        best = float('-inf')

        for r1 in range(M):
            Srow = [0] * (N + 1)
            for r2 in range(r1 + 1, M + 1):
                Srow = [a + b for a, b in zip(Srow, CSr[r2 - 1])]
                SL = SortedList(Srow)
                for c in range(N):
                    target = k + Srow[c]
                    SL.remove(Srow[c])
                    j = SL.bisect(target) - 1
                    if j < 0:
                        continue
                    best = max(best, SL[j] - Srow[c])

        return best
        """
        # Solution 2 - 348 ms
        row_size, col_size = len(matrix), len(matrix[0])
        if any(k in row for row in matrix):
            return k
        ans = -math.inf

        for y1 in range(col_size):

            prefix_sums = [0] * row_size

            for y2 in range(y1, col_size):
                for row in range(row_size):
                    prefix_sums[row] += matrix[row][y2]
                if all(x >= 0 for x in prefix_sums):
                    # Use sliding window
                    left = 0
                    curr_sum = 0
                    for right, x in enumerate(prefix_sums):
                        curr_sum += x
                        while left <= right and curr_sum > k:
                            curr_sum -= prefix_sums[left]
                            left += 1
                        if left <= right and ans < curr_sum <= k:
                            ans = curr_sum
                    continue

                result_big = -math.inf
                result_small = math.inf

                cur_big_sum = 0
                cur_small_sum = 0

                for x in prefix_sums:

                    if cur_big_sum < 0:
                        cur_big_sum = x
                    else:
                        cur_big_sum += x

                    if cur_big_sum > result_big:
                        result_big = cur_big_sum

                    if cur_small_sum > 0:
                        cur_small_sum = x
                    else:
                        cur_small_sum += x

                    if cur_small_sum < result_small:
                        result_small = cur_small_sum

                if result_big <= k:
                    ans = max(ans, result_big)
                    if ans == k:
                        return k
                    continue
                if result_small > k:
                    continue

                cur, my_arr, local_res = 0, [0], ans
                for x in prefix_sums:
                    cur += x
                    if my_arr[-1] >= cur - k:
                        local_res = max(local_res, cur - my_arr[bisect.bisect_left(my_arr, cur - k)])
                    bisect.insort(my_arr, cur)
                ans = local_res
                if ans == k:
                    return k
        return ans


# Main Call
solution = Solution()
matrix = [[1,0,1],[0,-2,3]]
k = 2
print(solution.maxSumSubmatrix(matrix, k))