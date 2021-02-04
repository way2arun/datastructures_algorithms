"""
Longest Harmonious Subsequence
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Example 2:

Input: nums = [1,2,3,4]
Output: 2
Example 3:

Input: nums = [1,1,1,1]
Output: 0


Constraints:

1 <= nums.length <= 2 * 104
-109 <= nums[i] <= 109
"""
from collections import defaultdict, Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Solution 1 - 312 ms
        """
        my_dict = defaultdict(int)
        # keep in dict the number of times each number appears:
        for num in nums:
            my_dict[num] += 1

        max_ = 0
        # for each number in dict check if it+its following number is more than previous max:
        for num in my_dict.keys():
            if my_dict.get(num + 1):
                max_ = max(max_, my_dict[num] + my_dict.get(num + 1))
        return max_
        """
        # Solution 2 - 272 ms
        d = Counter(nums)
        result = 0

        for k, v in d.items():
            if k + 1 in d:
                length = d[k + 1] + v
                result = max(result, length)

        return result


# Main Call
nums = [1, 3, 2, 2, 5, 2, 3, 7]

solution = Solution()
print(solution.findLHS(nums))
