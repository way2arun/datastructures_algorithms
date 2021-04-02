"""
Ones and Zeroes
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.



Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.


Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
"""
import collections
from typing import List


class Solution:
    def helper(self, strs, m, n, si):
        if si == len(strs):
            return 0
        # exclude the current string
        if (si + 1, m, n) in self.dp:
            exclude = self.dp[(si + 1, m, n)]
        else:
            exclude = self.helper(strs, m, n, si + 1)
            self.dp[(si + 1, m, n)] = exclude
        count0, count1 = 0, 0
        for char in strs[si]:
            if char == '0':
                count0 += 1
            else:
                count1 += 1
        if count0 <= m and count1 <= n:
            # include the current string
            if (si + 1, m - count0, n - count1) in self.dp:
                smallAns = self.dp[(si + 1, m - count0, n - count1)]
            else:
                smallAns = self.helper(strs, m - count0, n - count1, si + 1)
                self.dp[(si + 1, m - count0, n - count1)] = smallAns
            # +1 so as to include the current string
            include = 1 + smallAns
        else:
            include = -1
        self.dp[(si, m, n)] = max(include, exclude)
        return self.dp[(si, m, n)]

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Solution 1 - 3464 ms
        """
        self.dp = {}
        return self.helper(strs, m, n, 0)
        """
        # Solution 2 - 1120 ms
        dp = collections.defaultdict(int)
        dp[0, 0] = 0
        for s in strs:
            a = s.count('0')
            b = s.count('1')
            dp2 = dp.copy()
            for (i, j), count in dp.items():
                ni = i + a
                nj = j + b
                if ni <= m and nj <= n:
                    dp2[ni, nj] = max(dp2[ni, nj], dp[i, j] + 1)
            dp = dp2
        return max(dp.values())


# Main Call
solution = Solution()
strs = ["10","0001","111001","1","0"]
m = 5
n = 3
print(solution.findMaxForm(strs, m, n))