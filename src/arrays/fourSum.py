"""
4Sum
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

"""
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Solution 1 - 1068 ms
        """
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n):
            for j in range(i + 1, n):
                l, r = j + 1, n - 1
                remain = target - nums[i] - nums[j]
                while l < r:
                    if nums[l] + nums[r] == remain:
                        ans.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] > remain:
                        r -= 1
                    else:
                        l += 1
        return ans
        """
        # Solution 2 - 36 ms
        res, nums, n = set(), sorted(nums), len(nums)
        numDict = {num: i for i, num in enumerate(nums)}
        i = bisect_left(nums, target - nums[n - 1] * 3, 0, n)
        right1 = bisect_right(nums, target / 4, i, n)
        while i < right1:
            end2 = bisect_right(nums, target - nums[i] * 3, i + 1, n)
            target2 = target - nums[i]
            j = bisect_left(nums, target2 - nums[end2 - 1] * 2, i + 1, end2)
            right2 = bisect_right(nums, target2 / 3, j, end2)
            while j < right2:
                end3 = bisect_right(nums, target2 - nums[j] * 2, j + 1, n)
                target3 = target2 - nums[j]
                k = bisect_left(nums, target3 - nums[end3 - 1], j + 1, end3)
                right3 = bisect_right(nums, target3 / 2, k, end3)
                while k < right3:
                    target4 = target3 - nums[k]
                    if (target4 in numDict) and (numDict[target4] > k):
                        res.add((nums[i], nums[j], nums[k], target4))
                    k = numDict[nums[k]] + 1
                j = numDict[nums[j]] + 1
            i = numDict[nums[i]] + 1
        return res


# Main Call
nums = [1, 0, -1, 0, -2, 2]
target = 0
solution = Solution()
print(solution.fourSum(nums, target))