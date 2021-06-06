"""
 Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Solution 1 - 2808 ms
        """
        set_nums, ans = set(nums), 0
        for num in nums:
            if num - 1 in set_nums: continue

            nxt = num
            while nxt + 1 in set_nums:
                nxt += 1
            ans = max(ans, nxt - num + 1)

        return ans
        """
        # Solution 2 - 52 ms
        if not nums:
            return 0
        nums.sort()

        max_streak = 1
        streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    streak += 1
                else:
                    max_streak = max(max_streak, streak)
                    streak = 1
        return max(max_streak, streak)


# Main Call
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
solution = Solution()
print(solution.longestConsecutive(nums))
