"""
Number of Submatrices That Sum to Target
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.



Example 1:


Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
Example 3:

Input: matrix = [[904]], target = 0
Output: 0


Constraints:

1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
   Hide Hint #1
Using a 2D prefix sum, we can query the sum of any submatrix in O(1) time. Now for each (r1, r2), we can find the largest sum of a submatrix that uses every row in [r1, r2] in linear time using a sliding window.

"""
from itertools import combinations, accumulate
from typing import List, Counter


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # Solution 1 - 3440 ms
        """
        m, n = len(matrix), len(matrix[0])
        dp, ans = {}, 0
        for k in range(m):
            t = [0] + list(accumulate(matrix[k]))
            for i, j in combinations(range(n + 1), 2):
                dp[i, j, k] = dp.get((i, j, k - 1), 0) + t[j] - t[i]

        for i, j in combinations(range(n + 1), 2):
            T = Counter([0])
            for k in range(m):
                ans += T[dp[i, j, k] - target]
                T[dp[i, j, k]] += 1

        return ans
        """
        # Solution 2 - 613 ms
        ps = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ps[i + 1][j] = ps[i][j] + matrix[i][j]
        res = 0
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix) + 1):
                col_sum = {0: 1}
                cur_sum = 0
                for k in range(len(matrix[0])):
                    cur_sum += ps[j][k] - ps[i][k]
                    if cur_sum - target in col_sum:
                        res += col_sum[cur_sum - target]
                    if cur_sum in col_sum:
                        col_sum[cur_sum] += 1
                    else:
                        col_sum[cur_sum] = 1
        return res


# Main Call
matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
target = 0

solution = Solution()
print(solution.numSubmatrixSumTarget(matrix, target))
