"""
Array Nesting
You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].

You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:

The first element in s[k] starts with the selection of the element nums[k] of index = k.
The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
We stop adding right before a duplicate element occurs in s[k].
Return the longest length of a set s[k].



Example 1:

Input: nums = [5,4,0,3,1,6,2]
Output: 4
Explanation:
nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.
One of the longest sets s[k]:
s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}
Example 2:

Input: nums = [0,1,2]
Output: 1


Constraints:

1 <= nums.length <= 105
0 <= nums[i] < nums.length
All the values of nums are unique.
"""
from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # Solution 1 - 182 ms
        """
        n = len(nums)
        ans = 0
        for x in nums:
            if x == -1: continue
            cnt = 0
            while nums[x] != -1:
                cnt += 1
                nums[x], x = -1, nums[x]
            ans = max(ans, cnt)

        return ans
        """
        # Solution 2 - 96 ms
        ans = cnt = 0
        for i, idx in enumerate(nums):
            if idx < 0: continue  # avoid revisit
            while nums[idx] >= 0:
                cnt, nums[idx], idx = cnt + 1, -1, nums[idx]  # increment length; mark as visited; visit next value
            else:
                ans = max(ans, cnt)
                cnt = 0
        return ans


# Main Call
nums = [5, 4, 0, 3, 1, 6, 2]
solution = Solution()
print(solution.arrayNesting(nums))
