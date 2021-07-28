"""
Beautiful Array
For some fixed n, an array nums is beautiful if it is a permutation of the integers 1, 2, ..., n, such that:

For every i < j, there is no k with i < k < j such that nums[k] * 2 = nums[i] + nums[j].

Given n, return any beautiful array nums.  (It is guaranteed that one exists.)



Example 1:

Input: n = 4
Output: [2,1,4,3]
Example 2:

Input: n = 5
Output: [3,1,2,5,4]


Note:

1 <= n <= 1000
"""
from functools import lru_cache
from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        # Solution 1 - 40 ms
        """
        @lru_cache(None)
        def dfs(n):
            if n == 1: return (1,)
            t1 = dfs((n + 1) // 2)
            t2 = dfs(n // 2)
            return tuple(i * 2 - 1 for i in t1) + tuple(i * 2 for i in t2)

        return dfs(n)
        """
        # Solution 2- 20 ms
        L = list(range(1, n + 1))

        def helper(L):
            if len(L) < 3:
                return L
            even = L[::2]
            odd = L[1::2]
            return helper(even) + helper(odd)

        return helper(L)


# Main Call
n = 4
solution = Solution()
print(solution.beautifulArray(n))