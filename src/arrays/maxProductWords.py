"""
Maximum Product of Word Lengths
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.



Example 1:

Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.


Constraints:

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] consists only of lowercase English letters.
"""
import itertools
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # Solution 1 - 168 ms
        """
        words.sort(key=len, reverse=True)
        best, bitsets = 0, {}
        for i in range(len(words)):
            wlen, bitset = len(words[i]), 0
            if wlen * len(words[0]) < best:
                return best
            for c in words[i]:
                bitset |= 1 << ord(c) - 97
            if bitset not in bitsets:
                for k, v in bitsets.items():
                    if not bitset & k:
                        best = max(best, wlen * v)
                bitsets[bitset] = wlen
        return best
        """
        # Solution 2 - 156 ms
        d = {sum(1 << (ord(c) - 97) for c in set(w)): len(w) for w in sorted(words, key=len)}
        return max([d[k] * d[K] for k, K in itertools.combinations(d.keys(), 2) if not K & k] or [0])


# Main Call
words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
solution = Solution()
print(solution.maxProduct(words))