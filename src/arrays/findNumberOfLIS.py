"""
Number of Longest Increasing Subsequence
Given an integer array nums, return the number of longest increasing subsequences.



Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.



Constraints:

0 <= nums.length <= 2000
-106 <= nums[i] <= 106
"""
import bisect
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # Solution 1 - 80 ms
        """
        if not nums: return 0
        n = len(nums) + 1

        decks, ends_decks, paths = [[] for _ in range(n)], [float("inf")] * n, [[0] for _ in range(n)]
        for num in nums:
            idx = bisect.bisect_left(ends_decks, num)
            n_paths = 1
            if idx > 0:
                l = bisect.bisect(decks[idx - 1], -num)
                n_paths = paths[idx - 1][-1] - paths[idx - 1][l]

            decks[idx].append(-num)
            ends_decks[idx] = num
            paths[idx].append(n_paths + paths[idx][-1])

        return paths[paths.index([0]) - 1][-1]
        """
        # Solution 2 - 64 ms
        if not nums: return 0

        decks, ends_decks, paths = [], [], []
        for num in nums:
            deck_idx = bisect.bisect_left(ends_decks, num)
            n_paths = 1
            if deck_idx > 0:
                l = bisect.bisect(decks[deck_idx - 1], -num)
                n_paths = paths[deck_idx - 1][-1] - paths[deck_idx - 1][l]

            if deck_idx == len(decks):
                decks.append([-num])
                ends_decks.append(num)
                paths.append([0, n_paths])
            else:
                decks[deck_idx].append(-num)
                ends_decks[deck_idx] = num
                paths[deck_idx].append(n_paths + paths[deck_idx][-1])

            # print(decks)
            # print(paths)
            # print("@@@@@")

        return paths[-1][-1]



# Main Call
nums = [2, 2, 2, 2, 2]
solution = Solution()
print(solution.findNumberOfLIS(nums))
