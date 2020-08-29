"""
Pancake Sorting
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/553/week-5-august-29th-august-31st/3441/
Given an array of integers A, We need to sort the array performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 0 <= k < A.length.
Reverse the sub-array A[0...k].
For example, if A = [3,2,1,4] and we performed a pancake flip choosing k = 2, we reverse the sub-array [3,2,1], so A = [1,2,3,4] after the pancake flip at k = 2.

Return an array of the k-values of the pancake flips that should be performed in order to sort A. Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.



Example 1:

Input: A = [3,2,4,1]
Output: [4,2,4,3]
Explanation:
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k = 4): A = [1, 4, 2, 3]
After 2nd flip (k = 2): A = [4, 1, 2, 3]
After 3rd flip (k = 4): A = [3, 2, 1, 4]
After 4th flip (k = 3): A = [1, 2, 3, 4], which is sorted.
Notice that we return an array of the chosen k values of the pancake flips.
Example 2:

Input: A = [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.


Constraints:

1 <= A.length <= 100
1 <= A[i] <= A.length
All integers in A are unique (i.e. A is a permutation of the integers from 1 to A.length).
"""
from typing import List


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        # Solution 1 - 40 ms
        """
        i = 0
        length = len(A)
        res = list()
        while i < len(A) and length > 1:
            max_val = max(A[0:length])
            max_val_index = ((A[0:length].index(max_val)) + 1)

            if max_val_index > 1:
                A = A[0:max_val_index][::-1] + A[max_val_index:]
                res.append(max_val_index)

            A = A[0:length][::-1] + A[length:]
            res.append(length)
            length -= 1
            i += 1
        return res
        """
        # Solution 2 - 24 ms

        res = []
        for x in range(len(A), 1, -1):
            i = A.index(x)
            res.extend([i + 1, x])
            A = A[:i:-1] + A[:i]
        return res

        # Solution 3 - 28 ms
        """
        swaps = []
        for n in range(len(A), 1, -1):
            m = max(A[:n])
            if m == A[n - 1]:
                continue
            if A[0] != m:
                i = A.index(m, 0, n)
                swaps.append(i + 1)
                A[:i + 1] = A[i::-1]
            swaps.append(n)
            A[:n] = A[n - 1::-1]
        return swaps
        """


# Main Call
solution = Solution()
A = [3, 2, 4, 1]
print(solution.pancakeSort(A))
