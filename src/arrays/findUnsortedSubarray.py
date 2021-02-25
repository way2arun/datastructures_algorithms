"""
Shortest Unsorted Continuous Subarray
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.



Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0


Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105


Follow up: Can you solve it in O(n) time complexity?
"""
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Solution 1 - 228 ms
        """
        left = idx_l = 0
        right = idx_r = len(nums) - 1
        l_max = -float('inf')
        r_min = float('inf')

        while left <= right:
            l_max = max(l_max, nums[left])
            if nums[left] < l_max:
                idx_l = left
            left += 1

        while right >= 0:
            r_min = min(r_min, nums[right])
            if nums[right] > r_min:
                idx_r = right
            right -= 1

        return idx_l - idx_r + 1 if idx_r - idx_l != len(nums) - 1 else 0
        """
        # Solution 2 - 164 ms
        # 2 6 | 4 8 | 7, 9, 15
        # 2, 6, | 4, 9, 15
        # 2 4 6 9 15

        a, b = 0, len(nums) - 1
        while a < b and nums[a + 1] >= nums[a]: a += 1
        while a < b and nums[b - 1] <= nums[b]: b -= 1
        if a == b: return 0

        # print(a, b)
        if a < b:
            minv = min(nums[a + 1:b + 1])
            maxv = max(nums[a:b])
        while b < len(nums) and nums[b] < maxv: b += 1
        while a > -1 and nums[a] > minv: a -= 1
        # print(a, b)
        return b - 1 - a


# Main Call
nums = [2, 6, 4, 8, 10, 9, 15]
solution = Solution()
print(solution.findUnsortedSubarray(nums))