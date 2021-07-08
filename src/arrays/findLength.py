"""
Maximum Length of Repeated Subarray
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.



Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
   Hide Hint #1
Use dynamic programming. dp[i][j] will be the answer for inputs A[i:], B[j:].
"""
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # Solution 1 - 5564 ms
        """
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                ans = max(ans, dp[i][j])
        return ans
        """
        # Solution 2 - 376 ms
        """
        m = len(nums1)
        n = len(nums2)

        def binaryFind(t1, t2, length):
            s = set()
            for i in range(m - length):
                s.add(t1[i:i + length + 1])
            for i in range(n - length):
                if t2[i:i + length + 1] in s:
                    return True
            return False

        t1 = tuple(nums1)
        t2 = tuple(nums2)
        l, r = 0, min(m, n)
        while l <= r:
            mid = l + (r - l) // 2
            if binaryFind(t1, t2, mid):
                l = mid + 1
            else:
                r = mid - 1
        return l
        """
        # Solution 3 - 196 ms
        str1 = ''.join([chr(n) for n in nums1])
        print(len(str1))
        ans = 0
        str2 = ''
        for ch in nums2:
            str2 += chr(ch)
            if str2 in str1:
                ans = len(str2)
            else:
                str2 = str2[1:]
        return ans


# Main Call
nums1 = [1, 2, 3, 2, 1]
nums2 = [3,2,1,4,7]
solution = Solution()
print(solution.findLength(nums1, nums2))