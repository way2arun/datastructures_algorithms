"""
Pascal's Triangle II
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3421/
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?

"""
import math
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Solution 1 - 24 ms
        """
        fact = 1
        for r in range(2, rowIndex + 1):
            fact *= r

        a = 1
        b = fact
        result = []
        for r in range(rowIndex + 1):
            result.append(fact // (a * b))
            if r < rowIndex:
                a *= (r + 1)
                b //= (rowIndex - r)

        return result
        """
        # Solution 2 - 8 ms

        if rowIndex == 0:
            return [1]

        pascal_triangle = [[1]]
        for i in range(1, rowIndex + 1):
            row = [1]
            for j in range(1, i):
                row.append(pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j])
            row.append(1)
            pascal_triangle.append(row)
        # print(pascal_triangle)
        return pascal_triangle[rowIndex]
        """

        # Solution 3 - 12 ms
        res = []
        for i in range(0, rowIndex + 1):
            res.append(int(math.factorial(rowIndex) / (math.factorial(i) * math.factorial(rowIndex - i))))

        return res
        """


# Main Call
solution = Solution()
rowIndex = 3
print(solution.getRow(rowIndex))
