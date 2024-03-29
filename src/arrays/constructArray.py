"""
Beautiful Arrangement II
Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:
Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
Example 2:
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
Note:
The n and k are in the range 1 <= k < n <= 104.
"""
from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        # Solution - 1 - 48 ms
        """
        dr, diff = 1, k
        result = list(range(1, n - k + 1))
        for i in range(k):
            result.append(result[-1] + dr * diff)
            dr *= -1
            diff -= 1
        return result
        """
        # Solution 2 - 32 ms
        ans = [i for i in range(1, n + 1)]
        for i in range(k + 1):
            ans[i] = i // 2 + 1 if not i % 2 else k + 1 - i // 2
        return ans


# Main Call
n = 3
k = 1

solution = Solution()
print(solution.constructArray(n, k))