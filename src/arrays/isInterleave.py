"""
Interleaving String
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.



Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true


Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.


Follow up: Could you solve it using only O(s2.length) additional memory space?
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Solution 1 -  36 ms
        """
        if len(s1) + len(s2) != len(s3):
            return False
        i = 0
        j = 0
        k = 0

        while i >= 0 and j < len(s2):

            if i < len(s1) and s3[k] == s1[i]:
                i += 1
                k += 1

            elif s3[k] == s2[j]:
                j += 1
                k += 1
            else:
                i -= 1
                j += 1

        return s1[i:] + s2[j:] == s3[k:]
        """
        # Solution 2 - 16 ms
        dp = {}

        if len(s1) + len(s2) != len(s3):
            return False

        def tlehelper(i, j, k):
            if i < len(s1) and j < len(s2):
                if (s1[i:], s2[j:]) in dp:
                    return dp[(s1[i:], s2[j:])]

                if s1[i] == s3[k] and s2[j] == s3[k]:
                    dp[(s1[i:], s2[j:])] = tlehelper(i + 1, j, k + 1) or tlehelper(i, j + 1, k + 1)
                    return dp[(s1[i:], s2[j:])]
                elif s1[i] == s3[k]:
                    dp[(s1[i:], s2[j:])] = tlehelper(i + 1, j, k + 1)
                    return dp[(s1[i:], s2[j:])]
                elif s2[j] == s3[k]:
                    dp[(s1[i:], s2[j:])] = tlehelper(i, j + 1, k + 1)
                    return dp[(s1[i:], s2[j:])]
                else:
                    return False
            elif i < len(s1):
                return s1[i:] == s3[k:]
            else:
                return s2[j:] == s3[k:]

        return tlehelper(0, 0, 0)


    # Main Call
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

solution = Solution()
print(solution.isInterleave(s1, s2, s3))
