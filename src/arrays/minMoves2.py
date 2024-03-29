"""
Minimum Moves to Equal Array Elements II
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.



Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
Example 2:

Input: nums = [1,10,2,9]
Output: 16


Constraints:

n == nums.length
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # Solution 1 - 72 ms
        """
        n = len(nums)
        mid = sorted(nums)[n // 2]
        res = sum(abs(i - mid) for i in nums)
        return res\
        """
        # Solution 2 - 56 ms
        count = 0
        nums.sort()
        middle_element = nums[len(nums) // 2]
        for num in nums:
            count += abs(middle_element - num)
        return count


# Main Call
nums = [1, 2, 3]
solution = Solution()
print(solution.minMoves2(nums))
