"""
Beautiful Arrangement
Suppose you have n integers from 1 to n. We define a beautiful arrangement as an array that is constructed by these n numbers successfully if one of the following is true for the ith position (1 <= i <= n) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
Given an integer n, return the number of the beautiful arrangements that you can construct.



Example 1:

Input: n = 2
Output: 2
Explanation:
The first beautiful arrangement is [1, 2]:
Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
The second beautiful arrangement is [2, 1]:
Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 15
"""


class Solution:
    dp = {}

    def countArrangement(self, n: int) -> int:
        # Solution 1 - 184 ms
        """
        self.ans = 0
        nums = [x for x in range(1, n + 1)]

        def dfs(curr, nums, j):
            if len(curr) == n:
                self.ans += 1
            else:
                for i in range(len(nums)):
                    if nums[i] % j == 0 or j % nums[i] == 0:
                        dfs(curr + [nums[i]], nums[:i] + nums[i + 1:], j - 1)

        dfs([], nums, n)
        return self.ans
        """
        # Solution 2 - 32 ms
        arr = tuple(range(1, n + 1))

        def dfs(arr):
            i = len(arr)
            if i == 1:
                return 1
            if arr in self.dp:
                return self.dp[arr]
            ans = 0
            for j, val in enumerate(arr):
                if val % i == 0 or i % val == 0:
                    ans += dfs(arr[:j] + arr[j + 1:])
            self.dp[arr] = ans
            return ans

        return dfs(arr)


# Main Call
n = 2
solution = Solution()
print(solution.countArrangement(n))
