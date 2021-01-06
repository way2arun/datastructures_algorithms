"""
Kth Missing Positive Number
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.



Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.


Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
   Hide Hint #1
Keep track of how many positive numbers are missing as you scan the array.
"""
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Solution 1 - 48 ms
        """
        beg, end = 0, len(arr)
        while beg < end:
            mid = (beg + end) // 2
            if arr[mid] - mid - 1 < k:
                beg = mid + 1
            else:
                end = mid
        return end + k
        """
        # Solution 2 - 32 ms
        i, m, len_a = 0, 0, len(arr)
        while k > 0:
            m += 1
            if i < len(arr) and arr[i] == m:
                i += 1
            else:
                k -= 1
        return m


# Main Call
arr = [2, 3, 4, 7, 11]
k = 5
solution = Solution()
print(solution.findKthPositive(arr, k))