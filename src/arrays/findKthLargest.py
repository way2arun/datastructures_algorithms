"""
Kth Largest Element in an Array
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Solution 1 - 68 ms
        """
        ma = max(0, max(nums))
        mi = abs(min(0, min(nums)))

        arr = [0] * mi + [0] + [0] * ma

        for n in nums:
            arr[mi + n] += 1

        i = len(arr) - 1

        while k > 0:

            if k - arr[i] > 0:
                k -= arr[i]

            else:
                return i - mi

            i -= 1
            """
        # Solution 2 - 48 ms
        nums.sort(reverse=True)
        return nums[k - 1]


# Main Call
nums = [3,2,1,5,6,4]
k = 2
solution = Solution()
print(solution.findKthLargest(nums, k))