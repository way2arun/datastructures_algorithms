"""
Image Overlap
Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
Notes:

1 <= A.length = A[0].length = B.length = B[0].length <= 30
0 <= A[i][j], B[i][j] <= 1
"""
import collections
from typing import List
import numpy as np


class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        # Solution 1 - 360 ms
        """
        A_points, B_points, d = [], [], collections.defaultdict(int)

        # Filter points having 1 for each matrix respectively.
        for r in range(len(A)):
            for c in range(len(A[0])):
                if A[r][c]:
                    A_points.append((r, c))

                if B[r][c]:
                    B_points.append((r, c))

        # For every point in filtered A, calculate the
        # linear transformation vector with all points of filtered B
        # count the number of the pairs that have the same transformation vector
        for r_a, c_a in A_points:
            for r_b, c_b in B_points:
                d[(r_b - r_a, c_b - c_a)] += 1

        return max(d.values() or [0])
        """
        # Solution 2 - 132 ms
        n = len(A)
        A1 = np.pad(A, [(0, n), (0, n)], mode='constant', constant_values=0)
        B1 = np.pad(B, [(0, n), (0, n)], mode='constant', constant_values=0)
        A2 = np.fft.fft2(A1)
        B2 = np.fft.ifft2(B1)
        print(A1)
        return int(np.round(np.max(np.abs(np.fft.fft2(A2 * B2)))))


# Main Call
solution = Solution()
A = [[1, 1, 0],
     [0, 1, 0],
     [0, 1, 0]]
B = [[0, 0, 0],
     [0, 1, 1],
     [0, 0, 1]]

print(solution.largestOverlap(A, B))
