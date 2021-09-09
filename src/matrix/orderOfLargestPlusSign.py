"""
Largest Plus Sign
You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.

Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.



Example 1:


Input: n = 5, mines = [[4,2]]
Output: 2
Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.
Example 2:


Input: n = 1, mines = [[0,0]]
Output: 0
Explanation: There is no plus sign, so return 0.


Constraints:

1 <= n <= 500
1 <= mines.length <= 5000
0 <= xi, yi < n
All the pairs (xi, yi) are unique.
   Hide Hint #1
For each direction such as "left", find left[r][c] = the number of 1s you will see before a zero starting at r, c and walking left. You can find this in N^2 time with a dp. The largest plus sign at r, c is just the minimum of left[r][c], up[r][c] etc.

"""
from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # Solution 1 - 4358 ms
        """
        grid = [[1 for j in range(n)] for i in range(n)]
        ans = 0
        # Preprocessor grids
        left = [[0 for j in range(n + 2)] for i in range(n + 2)]
        right = [[0 for j in range(n + 2)] for i in range(n + 2)]
        top = [[0 for j in range(n + 2)] for i in range(n + 2)]
        bottom = [[0 for j in range(n + 2)] for i in range(n + 2)]

        # We have to work on mines
        for i in range(len(mines)):
            grid[mines[i][0]][mines[i][1]] = 0

        # TOp- down proccesing
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if grid[i - 1][j - 1] == 0:
                    continue
                left[i][j] = left[i][j - 1] + 1
                top[i][j] = top[i - 1][j] + 1

        # Bottom - Up proccesing
        for i in range(n, 0, -1):
            for j in range(n, 0, -1):
                if grid[i - 1][j - 1] == 0:
                    continue

                right[i][j] = right[i][j + 1] + 1
                bottom[i][j] = bottom[i + 1][j] + 1

                tempans = min(left[i][j], right[i][j], bottom[i][j], top[i][j])

                ans = max(ans, tempans)

        return ans
        """
        # Solution 2 - 256 ms
        # print(tuple(mines[0]))

        if len(mines) == n * n:
            return 0
        rows = [[-1, n] for _ in range(n)]
        cols = [[-1, n] for _ in range(n)]
        for r, c in mines:
            rows[r].append(c)
            cols[c].append(r)
        for i in range(n):
            rows[i].sort()
            cols[i].sort()
        cols = [iter(col) for col in cols]
        up_b = [next(col) for col in cols]
        down_b = [next(col) for col in cols]
        mxp = 0
        for r in range(n):
            for i in range(len(rows[r]) - 1):
                left_b = rows[r][i]
                right_b = rows[r][i + 1]
                for c in range(left_b + mxp + 1, right_b - mxp):
                    while down_b[c] <= r:
                        up_b[c] = down_b[c]
                        down_b[c] = next(cols[c])
                    mxp = max(mxp, min(c - left_b, right_b - c, r - up_b[c], down_b[c] - r))
        return mxp


# Main Call
n = 5
mines = [[4, 2]]
solution = Solution()
print(solution.orderOfLargestPlusSign(n, mines))