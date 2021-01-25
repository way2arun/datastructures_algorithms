"""
Check If All 1's Are at Least Length K Places Away
Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.



Example 1:



Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
Example 2:



Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.
Example 3:

Input: nums = [1,1,1,1,1], k = 0
Output: true
Example 4:

Input: nums = [0,1,0,1], k = 1
Output: true


Constraints:

1 <= nums.length <= 105
0 <= k <= nums.length
nums[i] is 0 or 1
   Hide Hint #1
Each time you find a number 1, check whether or not it is K or more places away from the next one. If it's not, return false.
"""
from cmath import inf
from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # Solution 1 - 576 ms
        """
        left = 0
        flag = 0
        res = float(inf)
        for idx, num in enumerate(nums):
            if num == 1:
                if flag == 0:  # first time we meet 1
                    flag = 1
                    left = idx
                else:
                    dist = idx - left - 1
                    left = idx
                    res = min(res, dist)
                    if res < k:
                        return False
        return True
        """
        # Solution 2 - 520 ms
        if not nums or len(nums) <= 0 or k <= 0:
            return True

        prev_i = -1
        for i, n in enumerate(nums):
            if n == 0:
                continue

            if prev_i == -1:
                prev_i = i
                continue

            if i - prev_i - 1 < k:
                return False

            prev_i = i
        return True


# Main Call
nums = [1, 0, 0, 0, 1, 0, 0, 1]
k = 2

solution = Solution()
print(solution.kLengthApart(nums, k))