"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.

"""
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # solution 1
        """
        counter, has = 0, {0: -1}
        max_length = 0

        for i in range(0, len(nums)):
            counter += (1 if nums[i] == 1 else -1)
            if counter not in has:
                has[counter] = i
            elif max_length < i - has[counter]:
                max_length = i - has[counter]
        return max_length
        """
        # solution 2
        has = {0: -1}
        counter = 0
        max_length = 0

        for i, x in enumerate(nums):
            if x == 1:
                counter += 1
            else:
                counter -= 1

            if counter in has:
                l = i - has[counter]
                if l > max_length:
                    max_length = l
            else:
                has[counter] = i

            print(f"\ni={i}, x={x}, net={counter}, mx={max_length}")
            print(has)

        return max_length


# Main Call
solution = Solution()
result = solution.findMaxLength([0, 1, 0])
print(result)
