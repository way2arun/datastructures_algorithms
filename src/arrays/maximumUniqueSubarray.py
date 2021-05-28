"""
Maximum Erasure Value
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).



Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
   Hide Hint #1
The main point here is for the subarray to contain unique elements for each index. Only the first subarrays starting from that index have unique elements.
   Hide Hint #2
This can be solved using the two pointers technique
"""
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # Solution 1 - 1312 ms
        """
        beg, end, S, n, sm = 0, 0, set(), len(nums), 0
        ans = 0
        while end < n:
            if nums[end] not in S:
                sm += nums[end]
                S.add(nums[end])
                end += 1
                ans = max(ans, sm)
            else:
                sm -= nums[beg]
                S.remove(nums[beg])
                beg += 1

        return ans
        """
        # Solution 2 - 1096 ms
        last = replySum = currSum = 0
        cache = set()
        for i in range(len(nums)):
            if nums[i] in cache:
                replySum = max(replySum, currSum)
                while nums[last] != nums[i]:
                    currSum -= nums[last]
                    cache.remove(nums[last])
                    last += 1
                last += 1
            else:
                cache.add(nums[i])
                currSum += nums[i]
        return max(replySum, currSum)


# Main Call
nums = [4, 2, 4, 5, 6]
solution = Solution()
print(solution.maximumUniqueSubarray(nums))
