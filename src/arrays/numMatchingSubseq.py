"""
Number of Matching Subsequences
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".


Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2


Constraints:

1 <= s.length <= 5 * 104
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.
"""
import bisect
from collections import defaultdict, Counter
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Solution 1 - 608 ms
        """
        ans, mappings = 0, defaultdict(list)
        for index, char in enumerate(s):
            mappings[char].append(index)
        for word in words:
            prev, found = -1, True
            for c in word:
                tmp = bisect.bisect(mappings[c], prev)
                if tmp == len(mappings[c]):
                    found = False
                    break
                else:
                    prev = mappings[c][tmp]
            ans += found == True
        return ans
        """
        # Solution 2 - 248 ms
        res = 0
        for w, c in Counter(words).items():
            i, match = 0, True
            for x in w:
                i = s.find(x, i) + 1
                if not i:
                    match = False
                    break
            if match:
                res += c
        return res


# Main Call
solution = Solution()
s = "abcde"
words = ["a","bb","acd","ace"]
print(solution.numMatchingSubseq(s, words))