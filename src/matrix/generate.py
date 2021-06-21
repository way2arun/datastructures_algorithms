"""
Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Solution 1 - 32 ms
        """
        triangle = [[1]]

        for j in range(1, numRows):
            prev = triangle[-1]
            triangle.append([1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1)] + [1])

        return triangle
        """
        # Solution 2 - 12 ms
        rows = {}
        rows[1] = [1]

        for row in range(2, numRows + 1):
            prevRow = rows[row - 1]
            nextRow = []

            nextRow.append(1)  # Start padding

            # Mid calculation
            for i in range(len(prevRow) - 1):
                nextRow.append(prevRow[i] + prevRow[i + 1])

            nextRow.append(1)  # End padding

            rows[row] = nextRow

        ans = []

        for row in rows.values():
            ans.append(row)

        return ans


# Main Call
numRows = 5
solution = Solution()
print(solution.generate(numRows))