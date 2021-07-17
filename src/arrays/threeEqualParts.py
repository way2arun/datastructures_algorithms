"""
Three Equal Parts
You are given an array arr which consists of only zeros and ones, divide the array into three non-empty parts such that all of these parts represent the same binary value.

If it is possible, return any [i, j] with i + 1 < j, such that:

arr[0], arr[1], ..., arr[i] is the first part,
arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
All three parts have equal binary values.
If it is not possible, return [-1, -1].

Note that the entire part is used when considering what binary value it represents. For example, [1,1,0] represents 6 in decimal, not 3. Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.



Example 1:

Input: arr = [1,0,1,0,1]
Output: [0,3]
Example 2:

Input: arr = [1,1,0,1,1]
Output: [-1,-1]
Example 3:

Input: arr = [1,1,0,0,1]
Output: [0,2]


Constraints:

3 <= arr.length <= 3 * 104
arr[i] is 0 or 1
"""
from typing import List


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        # Solution 1 - 428 ms
        """
        one_count = sum(arr)

        if one_count % 3 != 0: return [-1, -1]
        if one_count == 0: return [0, len(arr) - 1]

        session_one_count = one_count // 3
        session_trailing_zero = 0  # padding for each session
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 0:
                session_trailing_zero += 1
            else:
                break

        last_accu = -1
        curr_count = 0
        curr_accu = 0
        session_id = []

        i = 0
        while i < len(arr):
            curr_count += arr[i]
            curr_accu = curr_accu * 2 + arr[i]
            i += 1
            if curr_count == session_one_count:
                curr_trailing = 0
                while i < len(arr) and curr_trailing < session_trailing_zero:
                    # find trailing zeros
                    curr = arr[i]
                    if curr == 0:
                        curr_trailing += 1
                        i += 1
                    else:
                        return [-1, -1]  # not enough trailing zeros

                if (last_accu != -1) and (curr_accu != last_accu):
                    return [-1, -1]

                # reset
                last_accu = curr_accu
                session_id.append(i)
                curr_count = 0
                curr_accu = 0

        return [session_id[0] - 1, session_id[1]]
        """
        # Solution 2 - 344 ms
        n, s = len(arr), sum(arr)
        if s == 0: return [0, 2]
        if s % 3: return [-1, -1]
        t = s // 3
        idx = {x: 0 for x in {1, t, t + 1, 2 * t, 2 * t + 1, s}}
        k = 0
        for i, a in enumerate(arr):
            if not a: continue
            k += 1
            if k in idx: idx[k] = i
        z0 = n - idx[s]

        if idx[t] + z0 > idx[t + 1] or idx[2 * t] + z0 > idx[2 * t + 1]:
            return [-1, -1]
        i1, i2, i3 = idx[1], idx[t + 1], idx[2 * t + 1]
        for _ in range(idx[t] - idx[1] + 1):
            if not arr[i1] == arr[i2] == arr[i3]:
                return [-1, -1]
            i1, i2, i3 = i1 + 1, i2 + 1, i3 + 1
        return [idx[t] + z0 - 1, idx[2 * t] + z0]


# Main Call
solution = Solution()
arr = [1,0,1,0,1]
print(solution.threeEqualParts(arr))