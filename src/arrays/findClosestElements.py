"""
Find K Closest Elements
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b


Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]


Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
"""
from bisect import bisect_left
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Solution 1 - 292 ms
        """
        n = len(arr)
        ind = bisect_left(arr, x)
        if ind == n or ind > 0 and arr[ind] + arr[ind - 1] >= 2 * x:
            ind -= 1

        beg, end = ind, ind
        for i in range(k - 1):
            if beg == 0:
                end += 1
            elif end == n - 1:
                beg -= 1
            else:
                if arr[end + 1] + arr[beg - 1] >= 2 * x:
                    beg -= 1
                else:
                    end += 1

        return arr[beg:end + 1]
        """
        # Solution 2 - 248 ms
        lo = 0
        hi = len(arr) - k - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            st = arr[mid]
            end = arr[mid + k]
            if x < st:
                hi = mid - 1
            elif x >= end:
                lo = mid + 1
            else:
                if abs(x - st) <= abs(x - end):
                    hi = mid - 1
                else:
                    lo = mid + 1
        return arr[lo: lo + k]


# Main Call
arr = [1, 2, 3, 4, 5]
k = 4
x = 3

solution = Solution()
print(solution.findClosestElements(arr, k, x))