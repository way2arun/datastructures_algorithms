"""
Minimum Operations to Reduce X to Zero
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.



Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
   Hide Hint #1
Think in reverse; instead of finding the minimum prefix + suffix, find the maximum subarray.
   Hide Hint #2
Finding the maximum subarray is standard and can be done greedily.

"""
from typing import List

from itertools import accumulate


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # Solution 1 - 1308 ms
        """
        cumsum = [0] + list(accumulate(nums))
        dic = {c: i for i, c in enumerate(cumsum)}
        goal = cumsum[-1] - x
        ans = -float("inf")

        if goal < 0:
            return -1

        for num in dic:
            if num + goal in dic:
                ans = max(ans, dic[num + goal] - dic[num])

        return len(nums) - ans if ans != -float("inf") else -1
        """
        # Solution 2 - 1056 ms
        # This problem is equivalent to finding the longest subarray whose sum is == totalSum - x

        sub_sum = sum(nums) - x
        if sub_sum < 0:
            return -1
        if sub_sum == 0:
            return len(nums)

        start = 0
        cur = 0
        sub_len = -1

        # starting from the first element in nums, look for the longest subarray tha has sum == x

        for end in range(len(nums)):
            if cur < sub_sum:
                cur += nums[end]

            while cur >= sub_sum:
                if cur == sub_sum:
                    sub_len = max(sub_len, end - start + 1)
                cur -= nums[start]
                start += 1

        return -1 if (sub_len == -1) else (len(nums) - sub_len)


# Main call
nums = [5, 6, 7, 8, 9]
x = 4
solution = Solution()
print(solution.minOperations(nums, x))