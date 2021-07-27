"""
3Sum Closest
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Solution 1 - 140 ms
        """
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if abs(ans - target) > abs(sum3 - target):
                    ans = sum3
                if sum3 == target: return target
                if sum3 > target:
                    r -= 1  # Sum3 is greater than the target, to minimize the difference, we have to decrease our sum3
                else:
                    l += 1  # Sum3 is lesser than the target, to minimize the difference, we have to increase our sum3
        return ans
        """
        # Solution 2 - 32 ms
        nums.sort()
        print(nums, target)
        ans = float('inf')
        for i in range(len(nums) - 2):
            print("iterate: ", i, ans)
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            minsum = nums[i] + nums[i + 1] + nums[i + 2]
            maxsum = nums[i] + nums[-1] + nums[-2]
            # print(f'ini minsum: {minsum} maxsum {maxsum} , nnn {nums[i], nums[-1], nums[-2]}')
            if minsum >= target:
                if abs(minsum - target) >= abs(ans - target):
                    # print(f"minsum - target {abs(minsum-target)} ans {abs(ans-target):}")
                    return ans
            if maxsum < target:
                if abs(maxsum - target) < abs(ans - target):
                    # print(f"maxsum - target: {abs(maxsum-target)} ans: {abs(ans-target):}")
                    ans = maxsum
                # print("ans", ans)
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                # print(f'left: {left}  right: {right} -> {ans}')
                thsum = nums[i] + nums[left] + nums[right]
                # print("smua ", nums[i] ,nums[left] ,nums[right])
                # print(f'thsum: {thsum}')
                if abs(thsum - target) < abs(ans - target):
                    ans = thsum
                if thsum == target:
                    return thsum
                elif thsum < target:
                    left += 1
                    while left < len(nums) - 1 and nums[left - 1] == nums[left]:
                        left += 1

                else:
                    right -= 1
                    while right > i and nums[right + 1] == nums[right]:
                        right -= 1
        return ans


# Main Call
solution = Solution()
nums = [-1,2,1,-4]
target = 1
print(solution.threeSumClosest(nums, target))