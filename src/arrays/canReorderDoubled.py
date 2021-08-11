"""
Array of Doubled Pairs
Given an array of integers arr of even length, return true if and only if it is possible to reorder it such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2.



Example 1:

Input: arr = [3,1,3,6]
Output: false
Example 2:

Input: arr = [2,1,2,6]
Output: false
Example 3:

Input: arr = [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
Example 4:

Input: arr = [1,2,4,16,8,4]
Output: false


Constraints:

0 <= arr.length <= 3 * 104
arr.length is even.
-105 <= arr[i] <= 105
"""
from collections import Counter
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # Solution 1 - 708 ms
        """
        cnt = Counter(arr)
        arr.sort()
        for x in arr:
            if cnt[x] == 0: continue
            if x < 0 and x % 2 != 0: return False  # For example: arr=[-5, -2, 1, 2], x = -5, there is no x/2 pair to match
            y = x * 2 if x > 0 else x // 2
            if cnt[y] == 0: return False  # Don't have the corresponding `y` to match with `x` -> Return IMPOSSIBLE!
            cnt[x] -= 1
            cnt[y] -= 1
        return True
        """
        # Solution 2 - 540 ms
        count = Counter(arr)
        for key in sorted(count, key=abs):
            if count[key] > count[2 * key]:
                return False
            count[2 * key] -= count[key]
        return True


# Main Call
solution = Solution()
arr = [4, -2, 2, -4]
print(solution.canReorderDoubled(arr))
