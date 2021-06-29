"""
Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.



Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
   Hide Hint #1
One thing's for sure, we will only flip a zero if it extends an existing window of 1s. Otherwise, there's no point in doing it, right? Think Sliding Window!
   Hide Hint #2
Since we know this problem can be solved using the sliding window construct, we might as well focus in that direction for hints. Basically, in a given window, we can never have > K zeros, right?
   Hide Hint #3
We don't have a fixed size window in this case. The window size can grow and shrink depending upon the number of zeros we have (we don't actually have to flip the zeros here!).
   Hide Hint #4
The way to shrink or expand a window would be based on the number of zeros that can still be flipped and so on.
"""
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Solution 1 - 708 ms
        """
        beg, end, zeroes, ans = 0, 0, 0, 0
        while end < len(nums):
            if zeroes + (nums[end] == 0) <= k:
                zeroes += nums[end] == 0
                end += 1
                ans = max(ans, end - beg)
            else:
                zeroes -= nums[beg] == 0
                beg += 1
        return ans
        """
        # Solution 2 - 520 ms
        j = 0
        # always move right to expand sliding window, move left when k < 0
        for i in range(len(nums)):
            if nums[i] == 0: k -= 1
            if k < 0:
                if nums[j] == 0: k += 1
                j += 1
        return i - j + 1


# Main Call
solution = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(solution.longestOnes(nums, k))