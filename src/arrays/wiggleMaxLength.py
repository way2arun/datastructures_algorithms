"""
 Wiggle Subsequence
Given an integer array nums, return the length of the longest wiggle sequence.

A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) are alternately positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.
A subsequence is obtained by deleting some elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.



Example 1:

Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
Example 2:

Input: nums = [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
Example 3:

Input: nums = [1,2,3,4,5,6,7,8,9]
Output: 2


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000


Follow up: Could you solve this in O(n) time?

"""
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # Solution 1 - 28 ms
        """
        res = 1
        last, asc = nums[0], None
        for i in range(1, len(nums)):
            n = nums[i]
            if n == last: continue
            if asc is None:  # fill first 2 valid elements
                res += 1
                asc = n > last
            elif asc and n < last or not asc and n > last:
                res += 1
                asc = n > last
            last = n
        return res
        """
        # Solution 2 - 16 ms
        size = len(nums)
        if size == 0:
            return 0
        count = 1
        direction = 0
        prev = nums[0]
        for i in range(1, size):
            if direction == 0:
                if nums[i] != prev:
                    count += 1
                    direction = 1 if nums[i] > prev else -1
            elif direction == 1:
                if nums[i] < prev:
                    count += 1
                    direction = -1
            else:
                if nums[i] > prev:
                    count += 1
                    direction = 1
            prev = nums[i]
        return count



# Main Call
nums = [1, 7, 4, 9, 2, 5]

solution = Solution()
print(solution.wiggleMaxLength(nums))