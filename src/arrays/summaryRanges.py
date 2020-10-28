"""
Summary Ranges
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
Example 3:

Input: nums = []
Output: []
Example 4:

Input: nums = [-1]
Output: ["-1"]
Example 5:

Input: nums = [0]
Output: ["0"]


Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
"""
from typing import List


def makeRange(ci, cj):
    if ci == cj:
        return str(ci)
    else:
        return f"{ci}->{cj}"


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Solution 1 - 32 ms
        """
        i, result, N = 0, [], len(nums)

        while i < N:
            beg = end = i
            while end < N - 1 and nums[end] + 1 == nums[end + 1]: end += 1
            result.append(str(nums[beg]) + ("->" + str(nums[end])) * (beg != end))
            i = end + 1

        return result
        """
        """
        # Solution 2 - 12 ms
        if not nums: return []
        res = []
        i = 0
        while i < len(nums):
            j = i
            while j < len(nums) - 1 and nums[j] == nums[j + 1] - 1:
                j += 1
            if j == i:
                res.append(str(nums[i]))
            else:
                res.append('%s->%s' % (str(nums[i]), str(nums[j])))
            i = j + 1
        return res
        """
        # Solution 3 - 8 ms

        if not nums:
            return []
        idx, ci, cj = nums[0] - 1, nums[0], nums[0]
        res = []
        for n in nums:
            if n != (idx + 1):
                res.append(makeRange(ci, cj))
                ci = idx = n
            else:
                idx += 1
            cj = n
        res.append(makeRange(ci, cj))
        return res



# Main Call
nums = [0, 2, 3, 4, 6, 8, 9]
solution = Solution()
print(solution.summaryRanges(nums))
