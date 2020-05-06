"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/

"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # solution 1
        """
        cache = {}
        for num in nums:
            if num not in cache:
                cache[num] = 1
            if cache[num] > len(nums) // 2:
                return num
            else:
                cache[num] += 1
        """
        # solution 2
        # 40 ms and 164 ms
        nums.sort()
        return nums[len(nums) // 2]


# Main Call
solution = Solution()
input = [3, 2, 3]
print(solution.majorityElement(input))
input = [2, 2, 1, 1, 1, 2, 2]
print(solution.majorityElement(input))
