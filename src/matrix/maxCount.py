"""
Range Addition II
You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.



Example 1:


Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4
Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.
Example 2:

Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
Output: 4
Example 3:

Input: m = 3, n = 3, ops = []
Output: 9


Constraints:

1 <= m, n <= 4 * 104
1 <= ops.length <= 104
ops[i].length == 2
1 <= ai <= m
1 <= bi <= n
"""
from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # Solution 1 - 107 ms
        """
        min_row = m
        min_col = n
        for i in range(len(ops)):
            min_row = min(min_row, ops[i][0])
            min_col = min(min_col, ops[i][1])
        return min_row * min_col
        """
        # Solution 2 - 52 ms
        leastx = m
        leasty = n
        for coord in ops:
            if coord[0] < leastx:
                leastx = coord[0]
            if coord[1] < leasty:
                leasty = coord[1]
        return leastx * leasty


# Main Call
m = 3
n = 3
ops = [[2, 2], [3, 3]]

solution = Solution()
print(solution.maxCount(m, n, ops))
