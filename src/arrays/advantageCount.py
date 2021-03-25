"""
Advantage Shuffle
Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.



Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]


Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9
"""
import bisect
from typing import List


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        # Solution 1 - 356 ms
        """"
        res = []
        A.sort()
        for num in B:
            i = bisect.bisect_right(A, num)  # should put to the right if it has duplicate elements
            if i <= len(A) - 1:
                res.append(A.pop(i))  # valid
            else:
                res.append(-1)  # placeholder
        return [num if num != -1 else A.pop() for num in res]
        """
        # Solution 2 - 312 ms
        idx = list(range(len(B)))
        idx.sort(key=lambda i: B[i])
        A.sort()
        res = [-1] * len(A)
        start, end = 0, len(B) - 1
        # iterate through sorted A and B
        # if a can cover b, then correspond b with a
        # if a cannot, correspond a with largest of b
        for a in A:
            if a > B[idx[start]]:
                res[idx[start]] = a
                start += 1
            else:
                res[idx[end]] = a
                end -= 1
        return res


# Main Call
A = [2, 7, 11, 15]
B = [1, 10, 4, 11]

solution = Solution()
print(solution.advantageCount(A, B))