"""
 Verifying an Alien Dictionary
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""
from itertools import zip_longest
from typing import List, Dict


class Solution:
    def ordered(self, first: str, second: str, alphabet: Dict[str, int]) -> bool:
        i = 0
        while True:
            if i >= len(first):
                return True
            if i >= len(second):
                return False
            fl = first[i]
            sl = second[i]
            if fl == sl:
                i += 1
                continue
            if alphabet[fl] > alphabet[sl]:
                return False
            return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Solution 1 - 36 ms
        """
        order = {key: idx for idx, key in enumerate(order)}
        order['_'] = -1

        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip_longest(w1, w2, fillvalue='_'):
                cmp = order[c1] - order[c2]
                if cmp > 0: return False
                if cmp < 0: break

        return True
        """
        # Solution 2 - 16 ms
        alphabet = {letter: ix for ix, letter in enumerate(order)}

        result = True
        i = 0
        while i < (len(words) - 1) and result:
            result &= self.ordered(words[i], words[i + 1], alphabet)
            i += 1
        return result


# Main Call
words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

solution = Solution()
print(solution.isAlienSorted(words, order))
