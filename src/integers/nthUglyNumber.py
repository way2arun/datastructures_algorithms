"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3380/
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.
   Hide Hint #1
The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
   Hide Hint #2
An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
   Hide Hint #3
The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
   Hide Hint #4
Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).
"""
from heapq import heappush, heappop


class Ugly:
    def __init__(self):
        seen = {1, }
        self.nums = nums = []
        heap = []
        heappush(heap, 1)

        for _ in range(1690):
            curr_ugly = heappop(heap)
            nums.append(curr_ugly)
            for i in [2, 3, 5]:
                new_ugly = curr_ugly * i
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heappush(heap, new_ugly)


class Solution:
    # Solution 2 - 20 ms
    u = Ugly()

    def nthUglyNumber(self, n: int) -> int:
        # Solution 1 - 164 ms
        """
        if n == 1:
            return 1
        temp_2 = 0
        temp_3 = 0
        temp_5 = 0
        ugly = [0] * n
        ugly[0] = 1

        for i in range(1, n):
            ugly[i] = min(ugly[temp_2] * 2, ugly[temp_3] * 3, ugly[temp_5] * 5)
            if ugly[i] == ugly[temp_2] * 2:
                temp_2 += 1
            if ugly[i] == ugly[temp_3] * 3:
                temp_3 += 1
            if ugly[i] == ugly[temp_5] * 5:
                temp_5 += 1

        return ugly[n - 1]
        """
        # Solution 2 - 20 ms
        return self.u.nums[n - 1]


# Main Call
solution = Solution()
n = 10
print(solution.nthUglyNumber(n))
