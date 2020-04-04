"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Run Time O(n) = 32ms
"""


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for count in range(len(nums)):
            if (nums[count]) != 0:
                nums[index] = nums[count]
                index += 1

        while index < len(nums):
            nums[index] = 0
            index += 1
        print("{}".format(nums))

        # 2nd Solution
        if len(nums) <= 1:
            return nums
        first, second = 0, 1
        while first < second < len(nums):
            if nums[first] == 0 and nums[second] != 0:
                nums[first], nums[second] = nums[second], nums[first]
            if nums[first] == 0 and nums[second] == 0:
                second += 1
                continue
            first += 1
            second += 1
        print("{}".format(nums))


# Main Call
solution = Solution()
solution.moveZeroes([1, 2, 0, 0, 0, 3, 4, 0, 5, 0])
solution.moveZeroes([0, 1, 0, 3, 12])
solution.moveZeroes([0, 0, 1])
