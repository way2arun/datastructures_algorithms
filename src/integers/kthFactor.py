"""
The kth Factor of n
Given two positive integers n and k.

A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.



Example 1:

Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
Example 2:

Input: n = 7, k = 2
Output: 7
Explanation: Factors list is [1, 7], the 2nd factor is 7.
Example 3:

Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.
Example 4:

Input: n = 1, k = 1
Output: 1
Explanation: Factors list is [1], the 1st factor is 1.
Example 5:

Input: n = 1000, k = 3
Output: 4
Explanation: Factors list is [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000].


Constraints:

1 <= k <= n <= 1000
   Hide Hint #1
The factors of n will be always in the range [1, n].
   Hide Hint #2
Keep a list of all factors sorted. Loop i from 1 to n and add i if n % i == 0. Return the kth factor if it exist in this list
"""


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        """
               Given integers n and k, this program determines the kth
               smallest factor.

               :param n: integer to be factored
               :type n: int
               :param k: integer identifying which factor is returned
               :type k: int
               :return: kth smallest factor or -1 if it does not exist
               :rtype: int
               """
        # Solution - 1 - 36 ms
        """
        factors = 0
        for m in range(1, n + 1):
            if n % m == 0:
                factors += 1
                if factors == k:
                    return m
        return -1
        """
        # Solution 2 - 12 ms
        cur_factor_count = 0

        for i in range(1, 1 + (n // 2)):
            if n % i == 0:
                cur_factor_count += 1
            if cur_factor_count == k:
                return i
        if cur_factor_count + 1 == k:
            return n
        return -1


# Main Call
solution = Solution()
n = 1
k = 1
print(solution.kthFactor(n, k))
