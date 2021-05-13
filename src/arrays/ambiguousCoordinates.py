"""
Ambiguous Coordinates
We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we removed all commas, decimal points, and spaces, and ended up with the string s.  Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits.  Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order.  Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

Example 1:
Input: s = "(123)"
Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
Example 2:
Input: s = "(00011)"
Output:  ["(0.001, 1)", "(0, 0.011)"]
Explanation:
0.0, 00, 0001 or 00.01 are not allowed.
Example 3:
Input: s = "(0123)"
Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
Example 4:
Input: s = "(100)"
Output: [(10, 0)]
Explanation:
1.0 is not allowed.


Note:

4 <= s.length <= 12.
s[0] = "(", s[s.length - 1] = ")", and the other elements in s are digits.

"""
from itertools import product
from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        # Solution 1 - 40 ms
        """
        def generate(s):
            ans = []
            if s == "0" or s[0] != "0": ans.append(s)
            for i in range(1, len(s)):
                if (s[:i] == "0" or s[0] != "0") and s[-1] != "0":
                    ans.append(s[:i] + "." + s[i:])
            return ans

        n, ans = len(s), []
        for i in range(2, n - 1):
            cand_l, cand_r = generate(s[1:i]), generate(s[i:-1])
            for l, r in product(cand_l, cand_r):
                ans.append("(" + l + ", " + r + ")")

        return ans
        """
        # Solution 2 - 28 ms
        s = s[1: -1]
        res = []
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]

            ls = []
            rs = []

            if len(left) == 1:
                ls.append(left)
            else:
                if left[0] != '0':
                    ls.append(left)
                    if left[-1] != '0':
                        for j in range(1, len(left)):
                            ls.append(left[:j] + '.' + left[j:])

                elif left[-1] != '0':
                    ls.append('0.' + left[1:])

            if len(ls) == 0:
                continue

            if len(right) == 1:
                rs.append(right)
            else:
                if right[0] != '0':
                    rs.append(right)
                    if right[-1] != '0':
                        for j in range(1, len(right)):
                            rs.append(right[:j] + '.' + right[j:])

                elif right[-1] != '0':
                    rs.append('0.' + right[1:])

            if len(rs) == 0:
                continue

            for l in ls:
                for r in rs:
                    res.append('(' + l + ', ' + r + ')')

        return res


# Main Call
s = "(123)"
solution = Solution()
print(solution.ambiguousCoordinates(s))