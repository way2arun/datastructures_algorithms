"""
Palindrome Pairs
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.



Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]


Constraints:

1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lower-case English letters.
"""
from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # Solution 1 - 468 ms
        """
        wmap, ans = {}, []
        for i in range(len(words)):
            wmap[words[i]] = i
        for i in range(len(words)):
            if words[i] == "":
                for j in range(len(words)):
                    w = words[j]
                    if self.isPal(w, 0, len(w) - 1) and j != i:
                        ans.append([i, j])
                        ans.append([j, i])
                continue
            bw = words[i][::-1]
            if bw in wmap:
                res = wmap[bw]
                if res != i: ans.append([i, res])
            for j in range(1, len(bw)):
                if self.isPal(bw, 0, j - 1) and bw[j:] in wmap:
                    ans.append([i, wmap[bw[j:]]])
                if self.isPal(bw, j, len(bw) - 1) and bw[:j] in wmap:
                    ans.append([wmap[bw[:j]], i])
        return ans

    def isPal(self, word: str, i: int, j: int) -> bool:
        while i < j:
            if word[i] != word[j]: return False
            i += 1
            j -= 1
        return True
    """
        # Solution 2 - 328 ms
        # 0 means the word is not reversed, 1 means the word is reversed
        words, length, result = sorted([(w, 0, i, len(w)) for i, w in enumerate(words)] +
                                       [(w[::-1], 1, i, len(w)) for i, w in enumerate(words)]), len(words) * 2, []
        for i, (word1, rev1, ind1, len1) in enumerate(words):
            for j in range(i + 1, length):
                word2, rev2, ind2, _ = words[j]
                if word2.startswith(word1):
                    if ind1 != ind2 and rev1 ^ rev2:
                        rest = word2[len1:]
                        if rest == rest[::-1]: result += ([ind1, ind2],) if rev2 else ([ind2, ind1],)
                else:
                    break
        return result



# Main Call
words = ["abcd", "dcba", "lls", "s", "sssll"]
solution = Solution()
print(solution.palindromePairs(words))