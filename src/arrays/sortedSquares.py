"""
Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Solution 1 - 264 ms
        """
        stk, q = [], []
        res = []
        for num in nums:
            if num < 0:
                stk.append(num ** 2)
            else:
                q.append(num ** 2)
        while stk and q:
            if stk[-1] < q[0]:
                res.append(stk.pop())
            elif stk[-1] > q[0]:
                res.append(q.pop(0))
            else:
                res.append(q.pop(0))
                res.append(stk.pop())
        while stk:
            res.append(stk.pop())
        while q:
            res.append(q.pop(0))
        return res
        """
        # Solution 2 - 184 ms
        """
        for i, n in enumerate(nums):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums
        """

        # Solution 3 - 176 ms
        return sorted(x * x for x in nums)


# Main Call
nums = [-4, -1, 0, 3, 10]
solution  = Solution()
print(solution.sortedSquares(nums))