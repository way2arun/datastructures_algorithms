"""
Partition Equal Subset Sum
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.



Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Solution 1 - 1228 ms
        """
        t = sum(nums) / 2
        P = set([nums[0]])
        for x in nums[1:]:
            for y in list(P):
                P.add(x + y)
        return t in P
        """
        # Solution 2 - 64 ms
        if len(nums) < 2 or sum(nums) % 2 != 0:
            return False
        subset_sum = sum(nums) // 2
        cache = {}

        def backtrace(start, target):
            if target in cache:
                return cache[target]
            if target == 0:
                return True
            cache[target] = False
            for i in range(start, len(nums)):
                if target - nums[i] >= 0 and backtrace(i + 1, target - nums[i]):
                    cache[target] = True
                    break
            return cache[target]

        return backtrace(0, subset_sum)


# Main Call
nums = [1, 5, 11, 5]
solution = Solution()
print(solution.canPartition(nums))
