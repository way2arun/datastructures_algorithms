"""
Shortest Distance to a Character
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the shortest distance from s[i] to the character c in s.



Example 1:

Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
Example 2:

Input: s = "aaab", c = "b"
Output: [3,2,1,0]


Constraints:

1 <= s.length <= 104
s[i] and c are lowercase English letters.
c occurs at least once in s.
"""
import math
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # Solution 1 - 60 ms
        """
        p = []
        for i in range(0, len(s)):
            if s[i] == c:
                p.append(i)
        a = []
        for j in range(0, len(s)):
            m = [abs(x - j) for x in p]
            a.append(min(m))
        return (a)
        """
        # Solution 2- 20 ms
        ans = [None] * len(s)

        prev = -math.inf
        for i, char in enumerate(s):
            if char == c:
                prev = i
                ans[i] = 0
            else:
                ans[i] = i - prev

        prev = math.inf
        for i in reversed(range(len(s))):
            char = s[i]
            if char == c:
                prev = i
                ans[i] = 0
            else:
                ans[i] = min(ans[i], prev - i)

        return ans


# Main Call
s = "loveleetcode"
c = "e"

solution = Solution()
print(solution.shortestToChar(s, c))
