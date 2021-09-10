"""
Arithmetic Slices II - Subsequence
Given an integer array nums, return the number of all the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
The test cases are generated so that the answer fits in 32-bit integer.



Example 1:

Input: nums = [2,4,6,8,10]
Output: 7
Explanation: All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
Example 2:

Input: nums = [7,7,7,7,7]
Output: 16
Explanation: Any subsequence of this array is arithmetic.


Constraints:

1  <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
"""
from collections import Counter, defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # Solution 1 - 1196 ms
        """
        total, n = 0, len(nums)
        dp = [Counter() for item in nums]
        for i in range(n):
            for j in range(i):
                dp[i][nums[i] - nums[j]] += (dp[j][nums[i] - nums[j]] + 1)
            total += sum(dp[i].values())

        return total - (n - 1) * n // 2
        """
        # Solution 2 - 128 ms
        positions = defaultdict(list)
        n = len(nums) - 1
        for i, a in enumerate(reversed(nums)):
            positions[a].append(n - i)
        previous = defaultdict(int)
        subseqs = [defaultdict(int) for _ in range(len(nums))]
        for i, a in enumerate(nums):
            del positions[a][-1]
            if not positions[a]:
                del positions[a]
            if len(positions) > len(previous):
                for b in previous:
                    c = (a << 1) - b
                    if c in positions:
                        n = previous[b] + subseqs[i][b]
                        for j in positions[c]:
                            if j <= i:
                                break
                            subseqs[j][a] += n
            else:
                for c in positions:
                    b = (a << 1) - c
                    if b in previous:
                        n = previous[b] + subseqs[i][b]
                        for j in positions[c]:
                            subseqs[j][a] += n
            previous[a] += 1
        return sum(sum(p.values()) for p in subseqs)


# Main Call
nums = [2, 4, 6, 8, 10]
solution = Solution()
print(solution.numberOfArithmeticSlices(nums))
