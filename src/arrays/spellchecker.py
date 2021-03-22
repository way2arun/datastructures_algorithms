"""
Vowel Spellchecker
Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
When the query matches a word up to capitlization, you should return the first such match in the wordlist.
When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
If the query has no matches in the wordlist, you should return the empty string.
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].



Example 1:

Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]


Note:

1 <= wordlist.length <= 5000
1 <= queries.length <= 5000
1 <= wordlist[i].length <= 7
1 <= queries[i].length <= 7
All strings in wordlist and queries consist only of english letters.
"""
import collections
from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # Solution 1 - 200 ms
        """
        # Convert words and vowels to sets for O(1) lookup times
        words = set(wordlist)
        vowels = set('aeiouAEIOU')

        # Create two maps.
        # One for case insensitive word to all words that match "key" -> ["Key", "kEy", "KEY"]
        # The other for vowel insensitive words "k*t*" -> ["Kite", "kato", "KUTA"]
        case_insensitive = collections.defaultdict(list)
        vowel_insensitive = collections.defaultdict(list)
        for word in wordlist:
            case_insensitive[word.lower()].append(word)
            key = ''.join(char.lower() if char not in vowels else '*' for char in word)
            vowel_insensitive[key].append(word)

        res = []
        for word in queries:

            # Case 1: When query exactly matches a word
            if word in words:
                res.append(word)
                continue

            # Case 2: When query matches a word up to capitalization
            low = word.lower()
            if low in case_insensitive:
                res.append(case_insensitive[low][0])
                continue

            # Case 3: When query matches a word up to vowel errors
            key = ''.join(char.lower() if char not in vowels else '*' for char in word)
            if key in vowel_insensitive:
                res.append(vowel_insensitive[key][0])
                continue

            res.append('')

        return res
        """
        # Solution 2 - 144 ms
        set_wordlist = set(wordlist)

        lc_wordlist = dict()
        for w in wordlist:
            lower = w.lower()
            if lower in lc_wordlist:
                continue
            lc_wordlist[lower] = w

        vo_dict = dict()
        for w, w_orig in lc_wordlist.items():
            vowelless_w = w.lower().replace('a', '_').replace('e', '_').replace('i', '_').replace('o', '_').replace('u',
                                                                                                                    '_')
            if vowelless_w in vo_dict:
                continue

            vo_dict[vowelless_w] = w_orig

        ans = list()
        for query in queries:
            if query in set_wordlist:
                ans.append(query)
            elif query.lower() in lc_wordlist:
                ans.append(lc_wordlist[query.lower()])
            else:
                # Check for vowel errors
                vo_w = query.lower().replace('a', '_').replace('e', '_').replace('i', '_').replace('o', '_').replace(
                    'u', '_')
                if vo_w in vo_dict:
                    ans.append(vo_dict[vo_w])
                else:
                    # Nothing? return ""
                    ans.append("")

        return ans


# Main Call
wordlist = ["KiTe", "kite", "hare", "Hare"]
queries = ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti","keet", "keto"]

solution = Solution()
print(solution.spellchecker(wordlist, queries))