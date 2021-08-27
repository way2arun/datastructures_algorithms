"""
Longest Uncommon Subsequence II
Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.

An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.

A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).


Example 1:

Input: strs = ["aba","cdc","eae"]
Output: 3
Example 2:

Input: strs = ["aaa","aaa","aa"]
Output: -1


Constraints:

1 <= strs.length <= 50
1 <= strs[i].length <= 10
strs[i] consists of lowercase English letters.
"""
from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # Solution 1 - 77 ms
        """
        def isSubsequence(s, t):
            t = iter(t)
            return all(c in t for c in s)

        strs.sort(key=lambda x: -len(x))
        for i, word in enumerate(strs):
            if all(not isSubsequence(word, strs[j]) for j in range(len(strs)) if j != i):
                return len(word)

        return -1
        """
        # Solution 2 - 20 ms
        def isSubsequence(s, t):
            t = iter(t)
            return all(c in t for c in s)

        strs.sort(key=len, reverse=True)
        for i, s in enumerate(strs):
            found = False
            for j, ss in enumerate(strs):
                if i == j:
                    continue
                if isSubsequence(s, ss):
                    found = True
                    break
            if not found:
                return len(s)
        return -1


# Main Call
strs = ["aba", "cdc", "eae"]
solution = Solution()
print(solution.findLUSlength(strs))
