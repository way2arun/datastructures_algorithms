"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 20 ms
        left_side, right_side = 0, len(nums) - 1
        while left_side <= right_side:
            middle = (left_side + right_side) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] >= nums[left_side]:
                if nums[left_side] <= target < nums[middle]:
                    right_side = middle - 1
                else:
                    left_side = middle + 1
            else:
                if nums[middle] < target <= nums[right_side]:
                    left_side = middle + 1
                else:
                    right_side = middle - 1
        return -1

        """
        # 36 ms
        left_side = 0
        right_side = len(nums) - 1
        return self.binary_search(left_side, right_side, target, nums)

    def binary_search(self, left_side, right_side, target, nums):
        if right_side >= left_side:
            # Take the middle
            middle = left_side + (right_side - left_side) // 2
            # check the target in the middle
            if nums[middle] == target:
                return middle
            elif nums[left_side] <= target < nums[middle] or (
                    nums[middle] <= nums[right_side] and not nums[middle] < target <= nums[right_side]):
                return self.binary_search(left_side, middle - 1, target, nums)
            else:
                return self.binary_search(middle + 1, right_side, target, nums)
        else:
            return -1
        """


# Main Call
solution = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
result = solution.search(nums, 3)
print(result)

result = solution.search(nums, 0)
print(result)
