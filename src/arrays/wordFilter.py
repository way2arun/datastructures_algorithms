"""
Prefix and Suffix Search
Design a special dictionary which has some words and allows you to search the words in it by a prefix and a suffix.

Implement the WordFilter class:

WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string prefix, string suffix) Returns the index of the word in the dictionary which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.


Example 1:

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]

Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".


Constraints:

1 <= words.length <= 15000
1 <= words[i].length <= 10
1 <= prefix.length, suffix.length <= 10
words[i], prefix and suffix consist of lower-case English letters only.
At most 15000 calls will be made to the function f.
   Hide Hint #1
For a word like "test", consider "#test", "t#test", "st#test", "est#test", "test#test". Then if we have a query like prefix = "te", suffix = "t", we can find it by searching for something we've inserted starting with "t#te".

"""
import collections

from itertools import product
from typing import List


class WordFilter:
    # Solution 1 - 836 ms
    """
    def __init__(self, words: List[str]):
        self.d = {}
        for i, word in enumerate(words):
            for p, s in product(range(len(word) + 1), repeat=2):
                self.d[word[:p], word[s:]] = i

    def f(self, prefix: str, suffix: str) -> int:
        print(self.d.get((prefix, suffix), -1))
        return self.d.get((prefix, suffix), -1)
    """
    # Solution 2 - 560 ms
    def __init__(self, words: List[str]):
        self.pref = collections.defaultdict(set)
        self.suff = collections.defaultdict(set)
        seen = set()
        for i in range(len(words) - 1, -1, -1):
            w = words[i]
            if w in seen:
                continue
            seen.add(w)
            for j in range(len(w) + 1):
                self.pref[w[:j]].add(i)
                self.suff[w[j:]].add(i)

    def f(self, prefix: str, suffix: str) -> int:
        a = self.pref[prefix]
        b = self.suff[suffix]
        x = a & b
        if x:
            print(max(x))
        else:
            print(-1)
        return max(x) if x else -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

wordFilter = WordFilter(["apple"])
wordFilter.f("a", "e")
