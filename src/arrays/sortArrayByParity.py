"""
Sort Array By Parity
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3431/
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.



Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000

"""
from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # Solution 1 - 132 ms
        """
        start, end = 0, len(A) - 1
        while start <= end:
            if A[start] % 2 == 0:
                start += 1
            else:
                A[start], A[end] = A[end], A[start]
                end -= 1
        return A
        """
        # Solution 2 - 60 ms
        i = 0
        j = len(A) - 1

        while i < j:
            if A[i] % 2 != 0:
                A[i], A[j] = A[j], A[i]
                i -= 1
                j -= 1
            i += 1
        return A

        # Solution 3 - 64 ms
        """
        even = []
        odd = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])
        result = even + odd
        return result
        """


# Main Call
solution = Solution()
A = [3, 1, 2, 4]
print(solution.sortArrayByParity(A))
