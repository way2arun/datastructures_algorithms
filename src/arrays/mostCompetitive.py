"""
Find the Most Competitive Subsequence
Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.



Example 1:

Input: nums = [3,5,2,6], k = 2
Output: [2,6]
Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
Example 2:

Input: nums = [2,4,3,3,5,4,9,6], k = 4
Output: [2,3,3,4]


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
1 <= k <= nums.length
   Hide Hint #1
In lexicographical order, the elements to the left have higher priority than those that come after. Can you think of a strategy that incrementally builds the answer from left to right?

"""
from collections import deque
from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # Solution 1 - 1280  ms
        """
        stack = []
        needDeleteCount = len(nums) - k
        for e in nums:
            while stack and e < stack[-1] and needDeleteCount > 0:
                needDeleteCount -= 1
                stack.pop()
            stack.append(e)
        return stack[:k]
        """
        # Solution 2 - 1096 ms
        if len(nums) < k:
            return []

        stack = deque([])
        for i in range(len(nums) - k - 1, -1, -1):
            if not stack or nums[i] <= stack[-1]:
                stack.append(nums[i])

        ans = []
        for i in range(k, 0, -1):
            if stack[-1] > nums[len(nums) - i]:
                ans += nums[len(nums) - i:]
                return ans
            else:
                ans.append(stack[-1])
                stack.pop()
                if stack and stack[0] <= nums[len(nums) - i]:
                    stack.appendleft(nums[len(nums) - i])
                    continue
                tmp = deque([])
                while stack and stack[-1] <= nums[len(nums) - i]:
                    el = stack[-1]
                    stack.pop()
                    tmp.append(el)
                stack = deque([nums[len(nums) - i]])
                while tmp:
                    stack.append(tmp[-1])
                    tmp.pop()

        return ans



    # Main Call
nums = [3, 5, 2, 6]
k = 2
solution = Solution()
print(solution.mostCompetitive(nums, k))