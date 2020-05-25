"""
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.



Example 1:


Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2


Note:

1 <= A.length <= 500
1 <= B.length <= 500
1 <= A[i], B[i] <= 2000
   Hide Hint #1
Think dynamic programming. Given an oracle dp(i,j) that tells us how many lines A[i:], B[j:] [the sequence A[i], A[i+1], ... and B[j], B[j+1], ...] are uncrossed, can we write this as a recursion?


https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3340/

"""
from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
       # Solution 1 - 216 ms
       """
        A_length = len(A)
        B_length = len(B)
        temp_array = [[0] * (B_length + 1) for _ in range(A_length + 1)]
        for i in range(A_length):
            for j in range(B_length):
                temp_array[i + 1][j + 1] = max(temp_array[i][j + 1], temp_array[i + 1][j])
                if A[i] == B[j]:
                    temp_array[i + 1][j + 1] = max(temp_array[i + 1][j + 1], 1 + temp_array[i][j])
        return temp_array[-1][-1]
        """
       # Solution 2 68 ms
       s = set(A) & set(B)
       A = [a for a in A if a in s]
       B = [b for b in B if b in s]
       m, n = len(A), len(B)
       if m < n:
           A, B, m, n = B, A, n, m

       dp = [0] * (m + 1)  # dp[i] in loop j: check up to A[i], B[j]
       for j in range(n):  # B[0]..B[j]
           new_dp = dp[:]
           for i in range(m):  # A[0]..A[i]
               if A[i] == B[j]:
                   new_dp[i + 1] = dp[i] + 1  # add a new line
               else:
                   new_dp[i + 1] = max(dp[i + 1], new_dp[i])  # choose the best strategy
           dp = new_dp

       return dp[-1]


# Main Call
A = [2, 5, 1, 2, 5]
B = [10, 5, 2, 1, 5, 2]

solution = Solution()
print(solution.maxUncrossedLines(A, B))
