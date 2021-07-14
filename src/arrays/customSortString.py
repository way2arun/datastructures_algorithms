"""
Custom Sort String
order and str are strings composed of lowercase letters. In order, no letter occurs more than once.

order was sorted in some custom order previously. We want to permute the characters of str so that they match the order that order was sorted. More specifically, if x occurs before y in order, then x should occur before y in the returned string.

Return any permutation of str (as a string) that satisfies this property.

Example:
Input:
order = "cba"
str = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.


Note:

order has length at most 26, and no character is repeated in order.
str has length at most 200.
order and str consist of lowercase letters only.
"""
from collections import Counter
import str as str


class Solution:
    def customSortString(self, order: str, str: str) -> str:
        # Solution 1 - 32 ms
        """
        cnt = Counter(str)
        ans = ""
        for c in order:
            if cnt[c] > 0:
                ans += cnt[c] * c
                del cnt[c]
        for c, v in cnt.items():
            if v > 0:
                ans += v * c
        return ans
        """
        # Solution 2 - 16 ms
        counter = Counter(str)
        res = []
        for i in order:
            if i in counter:
                res.append(i * counter[i])
                counter.pop(i)
        for i, v in counter.items():
            res.append(i * v)
        return ''.join(res)


# Main Call
order = "cba"
str = "abcd"
solution = Solution()
print(solution.customSortString(order, str))