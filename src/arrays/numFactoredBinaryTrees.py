"""
Binary Trees With Factors
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.



Example 1:

Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:

Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].


Constraints:

1 <= arr.length <= 1000
2 <= arr[i] <= 109
"""
from functools import lru_cache
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # Solution 1 - 108 ms
        """
        c = 0
        arr.sort()
        d = {}
        for i in arr:
            no = 1
            limit = i ** .5
            for j in arr:
                if j > limit:
                    break
                if i % j == 0 and (f2 := i // j) in d:
                    no += 2 * d[j] * d[f2] if j != f2 else d[j] * d[f2]
            d[i] = no
            c += no
        return c % (10 ** 9 + 7)
        """
        # Solution 2 - 104 ms
        arr.sort()

        ss = set(arr)

        @lru_cache(None)
        def process(val):
            ans = 1

            for x in arr:
                if x * x <= val:
                    if val % x == 0 and (val // x) in ss:
                        cnt = process(x) * process(val // x)
                        if x != val // x:
                            cnt += cnt
                        ans += cnt
                else:
                    break

            return ans

        ans = 0
        for x in arr:
            v = process(x)
            # print(x, v)
            ans += v

        return ans % (10 ** 9 + 7)


# Main Call
arr = [2, 4]

solution = Solution()
print(solution.numFactoredBinaryTrees(arr))
