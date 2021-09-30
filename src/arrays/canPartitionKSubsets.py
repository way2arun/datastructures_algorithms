"""
Partition to K Equal Sum Subsets
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.



Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false


Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].
   Hide Hint #1
We can figure out what target each subset must sum to. Then, let's recursively search, where at each call to our function, we choose which of k subsets the next value will join.
"""
import collections
from functools import lru_cache
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Solution 1 - 1368 ms
        """
        subsetSum, remain = divmod(sum(nums), k)
        if max(nums) > subsetSum or remain > 0:
            return False  # Prune since we can't divide `nums` into subsets where each sums is equal to `subsetSum`
        n = len(nums)

        @lru_cache(None)
        def dp(mask):
            if mask == 0: return 0
            for i in range(n):
                if (mask >> i) & 1:
                    newMask = mask ^ (1 << i)
                    remain = dp(newMask)
                    if remain == -1: continue  # Skip case can't divide by using `newMask`
                    if remain + nums[i] <= subsetSum:
                        return (remain + nums[i]) % subsetSum
            return -1

        return dp((1 << n) - 1) == 0
        """
        # Solution 2 - 28 ms
        # how to use element in the back
        # how to track how many elements are used
        # 1 1 1 2 2 3 4
        def dfs(c, g, t, x):
            # will this use all the elements?
            # yes, as your target is n//k
            if g == k:
                return True
            if t > x:
                return False

            if t == x:
                # how to define n
                return dfs(0, g + 1, 0, x)

            last = -1
            for i in range(c, len(nums)):
                if visited[i]: continue

                if nums[i] == last: continue
                last = nums[i]
                visited[i] = True
                if dfs(i, g, t + nums[i], x):
                    return True
                visited[i] = False

            return False

        total = sum(nums)
        if total % k != 0: return False
        nums.sort(reverse=True)
        visited = collections.defaultdict(lambda: False)
        return dfs(0, 0, 0, total // k)


# Main Call
nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
solution = Solution()
print(solution.canPartitionKSubsets(nums, k))