"""
Intersection of Two Arrays II
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000


Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Solution 1 - 55 ms
        """
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)

        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans
        """
        # Solution 2 - 28 ms
        # 4 5 9
        # 4 4 8 9 9
        if not nums1 or not nums2:
            return []

        if len(nums1) < len(nums2):
            shorter = sorted(nums1)
            longer = sorted(nums2)
        else:
            shorter = sorted(nums2)
            longer = sorted(nums1)

        i = j = 0
        out = []

        while i < len(shorter) and j < len(longer):
            if shorter[i] == longer[j]:
                out.append(shorter[i])
                i += 1
                j += 1
            elif shorter[i] < longer[j]:
                i += 1
            else:
                j += 1
        return out


# Main Call
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

solution = Solution()
print(solution.intersect(nums1, nums2))
