"""
Find and Replace Pattern
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.



Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
Example 2:

Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]


Constraints:

1 <= pattern.length <= 20
1 <= words.length <= 50
words[i].length == pattern.length
pattern and words[i] are lowercase English letters.
"""
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # Solution 1 - 36 ms
        """
        def normalize(s):
            seen = dict()
            next = 'a'
            ans = ""
            for c in s:
                if c not in seen:
                    seen[c] = next
                    next = chr(ord(next) + 1)
                ans += seen[c]
            return ans

        p = normalize(pattern)
        ans = []
        for word in words:
            if p == normalize(word):
                ans.append(word)
        return ans
        """
        # Solution 2 - 12 ms
        pattern = list(pattern)
        subP = ""
        pattNo = []
        for char in pattern:
            if char in subP:
                pattNo.append(subP.index(char))
            else:
                subP += char
                pattNo.append(subP.index(char))

        # print(subP)
        # print(pattNo)
        ans = []
        for word in words:
            tempNo = []
            tempP = ""
            for char in word:
                if char in tempP:
                    tempNo.append(tempP.index(char))
                else:
                    tempP += char
                    tempNo.append(tempP.index(char))
            # print(tempNo)
            # print(tempP)
            if tempNo == pattNo:
                ans.append(word)
        return (ans)


# Main Call
words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"
solution = Solution()
print(solution.findAndReplacePattern(words, pattern))
