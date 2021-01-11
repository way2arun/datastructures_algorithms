"""
Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]


Constraints:

0 <= n, m <= 200
1 <= n + m <= 200
nums1.length == m + n
nums2.length == n
-109 <= nums1[i], nums2[i] <= 109
   Hide Hint #1
You can easily solve this problem if you simply think about two elements at a time rather than two arrays. We know that each of the individual arrays is sorted. What we don't know is how they will intertwine. Can we take a local decision and arrive at an optimal solution?
   Hide Hint #2
If you simply consider one element each at a time from the two arrays and make a decision and proceed accordingly, you will arrive at the optimal solution.

"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Solution 1 - 32 ms
        """
        p1, p2 = m - 1, n - 1
        for i in range(m + n - 1, -1, -1):
            if p1 < 0 or p2 < 0:
                break
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1

        while p2 >= 0:
            nums1[i] = nums2[p2]
            i -= 1
            p2 -= 1

        print(nums1)
        """
        # Solution 2 - 16 ms
        temp = [0] * (m + n)

        i, j = 0, 0
        cursor = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                temp[cursor] = nums1[i]
                i += 1
                cursor += 1
            else:
                temp[cursor] = nums2[j]
                j += 1
                cursor += 1

        while i < m:
            temp[cursor] = nums1[i]
            i += 1
            cursor += 1

        while j < n:
            temp[cursor] = nums2[j]
            j += 1
            cursor += 1

        for i in range(m + n):
            nums1[i] = temp[i]

        print(nums1)


# Main Call
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

solution = Solution()
solution.merge(nums1, m, nums2, n)
