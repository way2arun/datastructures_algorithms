"""
Arithmetic Slices
A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of the array A is called arithmetic if the sequence:
A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
"""
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # Solution 1 - 36 ms
        """
        if len(A) < 3: return 0

        res, counter = 0, 2
        last_dif = A[1] - A[0]

        for index, num in enumerate(A[2:], 1):

            if last_dif == num - A[index]:
                counter += 1
            else:
                if counter >= 3:
                    res += (counter - 1) * (counter - 2) // 2
                counter = 2
                last_dif = num - A[index]

        if counter >= 3:
            res += (counter - 1) * (counter - 2) // 2
        return res
        """
        # Solution 2 - 20 ms
        # sliding window?
        diff = [0] * (len(A) - 1)
        res = 0
        for i in range(1, len(A)):
            diff[i - 1] = A[i] - A[i - 1]  # diff[0] = A[1] - A[0]

        # number of same diffs.
        # [2, 2, 2, 2] = 3 + 2 + 1 = 3*4/2 = n*(n-1)/2

        consec = 1  # need next number to verify consec is 1

        # this diff is not really necessary, i think
        for i in range(1, len(diff)):
            # print(diff)
            if diff[i - 1] == diff[i]:
                consec += 1
            else:
                res += consec * (consec - 1) / 2
                consec = 1

        res += consec * (consec - 1) / 2

        return int(res)


# Main Call
A = [1, 2, 3, 4]
solution = Solution()
print(solution.numberOfArithmeticSlices(A))
