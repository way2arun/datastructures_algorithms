"""
Max Consecutive Ones
Given a binary array nums, return the maximum number of consecutive 1's in the array.



Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
   Hide Hint #1
You need to think about two things as far as any window is concerned. One is the starting point for the window. How do you detect that a new window of 1s has started? The next part is detecting the ending point for this window. How do you detect the ending point for an existing window? If you figure these two things out, you will be able to detect the windows of consecutive ones. All that remains afterward is to find the longest such window and return the size.

"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Solution 1 - 356 ms
        """
        cur_max, gl_max = 0, 0
        for i in nums:
            if i == 1:
                cur_max += 1
                gl_max = max(gl_max, cur_max)
            else:
                cur_max = 0
        return gl_max
        """
        # Solution 2 - 316 ms
        ones = 0
        local_ones = 0
        for num in nums:
            if num == 1:
                local_ones += 1
            else:
                ones = max(ones, local_ones)
                local_ones = 0

        if local_ones > ones:
            ones = local_ones
        return ones


# Main Call
nums = [1, 1, 0, 1, 1, 1]
solution = Solution()
print(solution.findMaxConsecutiveOnes(nums))