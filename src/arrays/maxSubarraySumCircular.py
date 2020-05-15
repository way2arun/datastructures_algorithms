"""
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)



Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1


Note:

-30000 <= A[i] <= 30000
1 <= A.length <= 30000
   Hide Hint #1
For those of you who are familiar with the Kadane's algorithm, think in terms of that. For the newbies, Kadane's algorithm is used to finding the maximum sum subarray from a given array. This problem is a twist on that idea and it is advisable to read up on that algorithm first before starting this problem. Unless you already have a great algorithm brewing up in your mind in which case, go right ahead!
   Hide Hint #2
What is an alternate way of representing a circular array so that it appears to be a straight array? Essentially, there are two cases of this problem that we need to take care of. Let's look at the figure below to understand those two cases:

   Hide Hint #3
The first case can be handled by the good old Kadane's algorithm. However, is there a smarter way of going about handling the second case as well?
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3330/
"""
from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # Solution 1 - 616 ms
        """
        array_sum = sum(A)
        sum_list = [A[0]]
        print(sum_list)
        for i in range(1, len(A)):
            sum_list.append(max(sum_list[-1] + A[i], A[i]))
        print(sum_list)
        maximum_sub_array = max(sum_list)
        A = [-1 * each for each in A]
        sum_list = [A[0]]
        for i in range(1, len(A)):
            sum_list.append(max(sum_list[-1] + A[i], A[i]))
        array_sum = array_sum + max(sum_list)
        if array_sum > maximum_sub_array and array_sum != 0:
            return array_sum
        else:
            return maximum_sub_array
        """
        # Solution 2 436 ms
        curr_max = 0
        final_max = 0
        for i in A:
            curr_max += i
            if curr_max <= 0:
                curr_max = 0
            if final_max < curr_max:
                final_max = curr_max
        if final_max == 0:
            return max(A)

        curr_min = 0
        final_min = 0
        for i in A:
            curr_min += i
            if curr_min >= 0:
                curr_min = 0
            if final_min > curr_min:
                final_min = curr_min
        return max(final_max, sum(A) - final_min)


# Main Call
solution = Solution()
A = [3, -2, 2, -3]
print(solution.maxSubarraySumCircular(A))
