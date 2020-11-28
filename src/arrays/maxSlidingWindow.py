"""
Sliding Window Maximum
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]
Example 4:

Input: nums = [9,11], k = 2
Output: [11]
Example 5:

Input: nums = [4,-2], k = 2
Output: [4]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
   Hide Hint #1
How about using a data structure such as deque (double-ended queue)?
   Hide Hint #2
The queue size need not be the same as the window’s size.
   Hide Hint #3
Remove redundant elements and the queue should store only elements that need to be considered.

"""
import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Solution 1 - 2280 ms
        """
        ret = []
        maximum_indices = collections.deque([0])

        for i in range(1, k):
            while len(maximum_indices) > 0 and nums[i] >= nums[maximum_indices[0]]:
                maximum_indices.popleft()

            maximum_indices.appendleft(i)

        ret.append(nums[maximum_indices[-1]])

        for i in range(k, len(nums)):
            if maximum_indices[-1] == i - k:
                maximum_indices.pop()

            while len(maximum_indices) > 0 and (nums[i] >= nums[maximum_indices[0]]):
                maximum_indices.popleft()

            maximum_indices.appendleft(i)
            ret.append(nums[maximum_indices[-1]])

        return ret
        """
        # Solution 2 - 1180 ms
        m = max(nums[:k])
        res = [m]
        left = 0
        for n in range(k, len(nums)):
            cur = nums[n]
            left += 1
            if left > 0 and nums[left - 1] == m:
                if nums[left] == m - 1:
                    m = nums[left]
                else:
                    m = max(nums[left: n + 1])
            if cur > m:
                m = cur
            res.append(m)
        return res


# Main Call
solution = Solution()
nums = [9, 11]
k = 2

print(solution.maxSlidingWindow(nums, k))
