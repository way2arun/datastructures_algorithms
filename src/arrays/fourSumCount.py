"""
4Sum II
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""
from collections import defaultdict
from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # Solution 1 - 360 ms
        """
        AB = defaultdict(int)
        for a in A:
            for b in B:
                AB[a + b] += 1

        CD = defaultdict(int)
        for c in C:
            for d in D:
                CD[c + d] += 1

        ans = 0
        for key in AB.keys():
            ans += AB[key] * CD[-key]
        return ans
        """
        # Solution 2 - 140 ms
        if len(A) == 0:
            return 0

        m1 = {}
        for a in A:
            if a in m1:
                m1[a] += 1
            else:
                m1[a] = 1
        m2 = {}
        for a, v in m1.items():
            for b in B:
                ab = a + b
                if ab in m2:
                    m2[ab] += v
                else:
                    m2[ab] = v

        m3 = {}
        for c in C:
            if c in m3:
                m3[c] += 1
            else:
                m3[c] = 1

        res = 0
        for c, v in m3.items():
            for d in D:
                cd = - c - d
                if cd in m2:
                    res += m2[cd] * v

        return res




# Main Call
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
solution = Solution()
print(solution.fourSumCount(A, B, C, D))
