"""
Subarray Product Less Than K
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3475/
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
   Hide Hint #1
For each j, let opt(j) be the smallest i so that nums[i] * nums[i+1] * ... * nums[j] is less than k. opt is an increasing function.
"""
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Solution 1 - 1080 ms
        """
        # Base case
        if not nums:
            return 0
        i = 0
        res = 0
        current = 1
        for j in range(len(nums)):
            current = current * nums[j]
            # j >= i to prevent index out of range cases i.e. nums = [1,2,3], k = 0
            while current >= k and j >= i:
                current = current // nums[i]
                i += 1
            # Add size of the window to final output
            res += j - i + 1
        return res
        """
        # Solution 2 - 1080 ms
        """
        left, right = 0, 0
        ans = 0
        n = len(nums)
        cumProd = 1
        while right < n:
            cumProd *= nums[right]
            right += 1
            while cumProd >= k and left < right:
                cumProd /= nums[left]
                left += 1
            ans += right - left
        return ans
        """
        # Solution 3 - 1052 ms
        # sliding window
        # move left while window product >= k
        # add (right - left + 1) if window < k

        if not nums or k <= 0:
            return 0
        n = len(nums)

        window = 1
        left = 0

        ret = 0
        for right in range(n):
            window *= nums[right]
            while left < right and window >= k:
                window //= nums[left]
                left += 1
            if window < k:
                ret += (right - left + 1)
        return ret


# Main call
solution = Solution()
nums = [10, 5, 2, 6]
k = 100
print(solution.numSubarrayProductLessThanK(nums, k))
