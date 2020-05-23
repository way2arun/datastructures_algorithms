"""
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)



Example 1:



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.


Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3338/

"""
from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # Solution 1 - 188 ms
        """
        length_A = len(A)
        length_B = len(B)
        i = 0
        j = 0
        answer = []
        while i < length_A and j < length_B:
            low = max(A[i][0], B[j][0])
            high = min(A[i][1], B[j][1])
            if low <= high:
                answer.append([low, high])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return answer
        """
        # Solution 2 - 132 ms
        res = []
        a_i = 0
        b_i = 0

        while a_i < len(A) and b_i < len(B):
            start_a, end_a = A[a_i]
            start_b, end_b = B[b_i]

            if end_a < start_b:
                a_i += 1
            elif end_b < start_a:
                b_i += 1
            else:
                if end_a <= end_b:
                    a_i += 1
                else:
                    b_i += 1
                res.append([max(start_a, start_b), min(end_a, end_b)])
        return res


# Main Call
A = [[0, 2], [5, 10], [13, 23], [24, 25]]
B = [[1, 5], [8, 12], [15, 24], [25, 26]]
solution = Solution()
print(solution.intervalIntersection(A, B))
