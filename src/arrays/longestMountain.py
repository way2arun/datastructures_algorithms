"""
Longest Mountain in Array
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?
"""
from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        # Solution 1 - 156 ms
        """
        n, max_len = len(A), 0
        state, length = 0, 1
        for i in range(n - 1):
            if state in [0, 1] and A[i + 1] > A[i]:
                state, length = 1, length + 1
            elif state == 2 and A[i + 1] > A[i]:
                state, length = 1, 2
            elif state in [1, 2] and A[i + 1] < A[i]:
                state, length = 2, length + 1
                max_len = max(length, max_len)
            else:
                state, length = 0, 1

        return max_len
        """
        # Solution 2 - 140 ms
        """
        downhill = True
        prev = -1
        cur_len = 0
        maxlen = 0
        for a in A:

            if downhill:
                if prev <= a:
                    maxlen = max(maxlen, cur_len)
                    if prev == -1 or prev == a:
                        cur_len = 1
                    else:
                        cur_len = 2
                    downhill = False
                else:
                    cur_len += 1

            else:
                if prev < a:
                    cur_len += 1
                else:
                    if cur_len > 1 and prev > a:
                        cur_len += 1
                        downhill = True
                    else:
                        cur_len = 1
                        downhill = False

            prev = a

        if downhill:
            maxlen = max(maxlen, cur_len)

        if maxlen < 3:
            return 0
        return maxlen
        """
        # Solution 3 - 136 ms
        up = 0
        down = 0
        ans = 0
        for i in range(0, len(A) - 1):
            if A[i] < A[i + 1]:
                if down == 0:
                    up += 1
                else:
                    up = 1
                    down = 0
            elif A[i] > A[i + 1]:
                if up > 0:
                    down += 1
                    mountain = up + down + 1
                    if ans < mountain:
                        ans = mountain
            else:
                up = 0
                down = 0
        return ans


# Main Call
A = [2, 1, 4, 7, 3, 2, 5]
solution = Solution()
print(solution.longestMountain(A))
