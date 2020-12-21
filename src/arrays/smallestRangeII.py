"""
Smallest Range II
Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.



Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]
Example 3:

Input: A = [1,3,6], K = 3
Output: 3
Explanation: B = [4,6,3]


Note:

1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000
"""
from typing import List


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        # Solution 1 - 164 ms
        """
        A.sort()
        res = A[-1] - A[0]  # possible result
        for i in range(len(A) - 1):
            a, b = A[i], A[i + 1]
            hi = max(A[-1] - K, a + K)  # possible max num
            lo = min(A[0] + K, b - K)  # possible min num
            res = min(res, hi - lo)
        return res
        """
        # Solution 2 - 132 ms
        A = sorted(set(A))
        gap = A[-1] - A[0]
        if gap <= K: return gap
        if gap >= 4 * K: return gap - K * 2

        for i in range(len(A) - 1):
            a, b = A[i], A[i + 1]
            gap = min(gap, max(A[-1] - K, a + K) - min(A[0] + K, b - K))
        return gap


# Main Call
A = [0, 10]
K = 2

solution = Solution()
print(solution.smallestRangeII(A, K))
