"""
Find the Smallest Divisor Given a Threshold
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor and divide all the array by it and sum the result of the division. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.



Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1.
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2).
Example 2:

Input: nums = [2,3,5,7,11], threshold = 11
Output: 3
Example 3:

Input: nums = [19], threshold = 5
Output: 4


Constraints:

1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^6
nums.length <= threshold <= 10^6
   Hide Hint #1
Examine every possible number for solution. Choose the largest of them.
   Hide Hint #2
Use binary search to reduce the time complexity.
"""
from math import ceil
from typing import List
from numpy import array, ceil, sum

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # Solution 1 - 384 ms
        """
        beg, end = 0, max(nums) + 1
        while beg + 1 < end:
            mid = (beg + end) // 2
            if sum(ceil(num / mid) for num in nums) <= threshold:
                end = mid
            else:
                beg = mid
        return end
        """
        # Solution 2 - 224 ms
        """
        nums = array(nums)
        left = 0
        right = max(nums)
        while (left < right):
            mid = left + ((right - left) // 2)
            if sum(ceil(nums / mid)) > threshold:
                left = mid + 1
            else:
                right = mid
        return left
        """
        # Solution 2 - 212 ms
        nums = array(nums)
        left, right = 1, max(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            sum_ = sum(ceil(nums / mid))
            if sum_ > threshold:
                left = mid
            else:
                right = mid
        sum_ = sum(ceil(nums / left))

        return left if sum_ <= threshold else right



# Main Call
nums = [2, 3, 5, 7, 11]
threshold = 11

solution = Solution()
print(solution.smallestDivisor(nums, threshold))
