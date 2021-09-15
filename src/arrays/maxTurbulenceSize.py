"""
Longest Turbulent Subarray
Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.


Example 1:

Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
Example 2:

Input: arr = [4,8,12,16]
Output: 2
Example 3:

Input: arr = [100]
Output: 1


Constraints:

1 <= arr.length <= 4 * 104
0 <= arr[i] <= 10^9

"""
from functools import lru_cache
from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # Solution 1 - 720 ms
        """
        @lru_cache(None)
        def dp(i, dr):
            if i == 0 or (arr[i] - arr[i - 1]) * dr >= 0: return 1
            return dp(i - 1, -dr) + 1

        return max(dp(i, dr) for i in range(len(arr)) for dr in [-1, 1])
        """
        # Solution 2 - 416 ms
        l = len(arr)
        if l == 1:
            return 1
        prevdiff = arr[1] - arr[0]
        if l == 2:
            if prevdiff == 0:
                return 1
            else:
                return 2
        e = 0
        while e < l:
            if arr[e] == arr[0]:
                e += 1
            else:
                break
        if e == l:
            return 1
        starti = e - 1
        result = 2  # e-1,e
        prevdiff = arr[e] - arr[e - 1]
        for i in range(e + 1, l):
            diff = arr[i] - arr[i - 1]
            if diff * prevdiff < 0:
                pass
            else:
                # can't add i
                result = max(result, i - starti)
                if diff == 0:
                    starti = i
                else:
                    starti = i - 1
            prevdiff = diff
        result = max(result, l - starti)
        return result


# Main Call
arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
solution = Solution()
print(solution.maxTurbulenceSize(arr))
