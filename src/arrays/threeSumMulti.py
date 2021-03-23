"""
  3Sum With Multiplicity
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.



Example 1:

Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation:
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
Example 2:

Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation:
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.


Constraints:

3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300
"""
import collections
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        # Solution 1 - 4992 ms
        """
        ans = 0
        n = len(arr)
        level2 = collections.defaultdict(int)
        for i in range(2, n):
            for j in range(i - 1):
                level2[arr[j] + arr[i - 1]] += 1
            ans = ans + level2[target - arr[i]]
            ans = ans % (10 ** 9 + 7)
        return ans
        """
        # Solution 2 - 60 ms
        c = collections.Counter(arr)

        res = 0
        if target % 3 == 0:
            n = c.get(target // 3, 0)
            res += n * (n - 1) * (n - 2) // 6

        keys = sorted(c.keys())
        for k in keys:
            n = c[k]
            if n > 1 and target > k != target - 2 * k:
                res += c.get(target - 2 * k, 0) * n * (n - 1) // 2

        for i in range(len(keys)):
            if keys[i] >= target // 3: break
            for j in range(i + 1, len(keys)):
                new = target - (keys[i] + keys[j])
                if new <= keys[j]: break
                if new in c:
                    res += c[keys[i]] * c[keys[j]] * c[new]

        return res % (10 ** 9 + 7)


# Main Call
arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
target = 8

solution = Solution()
print(solution.threeSumMulti(arr, target))