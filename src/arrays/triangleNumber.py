"""
Valid Triangle Number
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.



Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:

Input: nums = [4,2,3,4]
Output: 4


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Solution 1 - 1116ms
        """
        nums.sort()
        n = len(nums)
        ans = 0
        for k in range(2, n):
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    ans += j - i
                    j -= 1
                else:
                    i += 1
        return ans
        """
        # Solution 2 - 1000 ms
        ln = len(nums)
        if ln < 3:
            return 0
        res = 0
        nums.sort()

        # target(nums[i]) is till index 2, because start and end should be different
        # for i == 2, start 0 and end = 1
        for i in range(ln - 1, 1, -1):
            start, end = 0, i - 1
            target = nums[i]
            while start < end:
                if nums[start] + nums[end] > target:
                    # assuming I fix the end and take all the elements from star to end-1 one by one
                    # because, if nums[start] + nums[end] > target then nums[start+k] + nums[end],
                    # where k < end is also greater than target
                    # so now move on and try with end-1
                    res += (end - start)
                    end -= 1
                else:
                    # I need to increase the nums[start] + nums[end], so move forward
                    start += 1

        return res


# Main Call
nums = [2, 2, 3, 4]
solution = Solution()
print(solution.triangleNumber(nums))