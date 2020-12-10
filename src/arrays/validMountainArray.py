"""
Valid Mountain Array
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < A[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]



Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true


Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
   Hide Hint #1
It's very easy to keep track of a monotonically increasing or decreasing ordering of elements. You just need to be able to determine the start of the valley in the mountain and from that point onwards, it should be a valley i.e. no mini-hills after that. Use this information in regards to the values in the array and you will be able to come up with a straightforward solution.

"""
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # Solution 1 - 204 ms
        """
        start, run, l = 0, 0, len(arr)
        # Going up hill
        while run + 1 < l and arr[run] < arr[run + 1]: run += 1
        # Check if run pointer has moved compared to last Start position
        if run == start: return False
        # Going down hill
        start = run
        while run + 1 < l and arr[run] > arr[run + 1]: run += 1
        # Check if run pointer has moved compared to last Start position
        if run == start: return False
        # Final Check if run is pointing to the last element
        return run == l - 1
        """
        # Solution 2 - 168 ms
        n = len(arr)
        if n < 3: return False
        inc = arr[0] < arr[1]
        k = 0
        for i in range(1, n):
            if inc and arr[i - 1] >= arr[i]:
                k += 1
                inc = False
            if not inc and arr[i - 1] <= arr[i]:
                return False
        return k == 1


# Main Call
arr = [3, 5, 5]
solution = Solution()
print(solution.validMountainArray(arr))
