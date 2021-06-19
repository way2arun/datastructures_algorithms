"""
K Inverse Pairs Array
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.



Example 1:

Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
Example 2:

Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.


Constraints:

1 <= n <= 1000
0 <= k <= 1000
"""


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # Solution 1 - 548 ms
        """
        dp = [[1] * (k + 1) for _ in range(n + 1)]
        sp = [[1] * (k + 1) for _ in range(n + 1)]
        N = 10 ** 9 + 7

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = sp[i - 1][j] if j < i else (sp[i - 1][j] - sp[i - 1][j - i]) % N
                sp[i][j] = (sp[i][j - 1] + dp[i][j]) % N

        return dp[-1][-1]
        """
        # Solution 2 - 296 ms
        b = 10 ** 9 + 7
        d = [1, 0]
        for i in range(2, n + 1):
            d2 = []
            summ = 0
            w = min(i, len(d))
            print(i, len(d), w)
            for j in range(min(k + 1, w)):
                summ += d[j]
                d2.append(summ)
            for j in range(j + 1, min(k + 1, len(d))):
                summ += d[j] - d[j - w]
                d2.append(summ)
            for j in range(j + 1, min(k + 1, j + 1 + w)):
                if summ == 0:
                    break
                summ -= d[j - w]
                d2.append(summ)
            d = d2
            # print(d)
        if k < len(d):
            return d[k] % b
        else:
            return 0


# Main Call
n = 3
k = 0
solution = Solution()
print(solution.kInversePairs(n, k))
