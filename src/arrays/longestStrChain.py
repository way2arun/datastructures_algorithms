"""
Longest String Chain
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2. For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.



Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chain is "a","ba","bda","bdca".
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5


Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
   Hide Hint #1
Instead of adding a character, try deleting a character to form a chain in reverse.
   Hide Hint #2
For each word in order of length, for each word2 which is word with one character removed, length[word2] = max(length[word2], length[word] + 1).
"""
import collections
from collections import defaultdict
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Solution 1 - 100 ms
        """
        W = [set() for _ in range(17)]
        for word in words:
            W[len(word)].add(word)
        dp, best = defaultdict(lambda: 1), 1
        for i in range(16, 0, -1):
            if len(W[i - 1]) == 0: continue
            for word in W[i]:
                wVal = dp[word]
                for j in range(len(word)):
                    pred = word[0:j] + word[j + 1:]
                    if pred in W[i - 1] and wVal >= (dp.get(pred) or 1):
                        dp[pred] = wVal + 1
                        best = max(best, wVal + 1)
        return best
        """
        # Solution 2 - 64 ms
        def get_predecessors(node):
            res = []
            n = len(node)
            for i in range(n):
                word = node[:i] + node[i + 1:]
                if word in length_hashmap[n - 1]:
                    res.append(word)
            return res

        def dfs(node):
            visited.add(node)
            count = 0
            for predecessor in get_predecessors(node):
                # we don't need to check visited set here, based on the problem definition
                # we will not revisit a node if we trace the words chain backward.
                if predecessor not in visited:
                    count = max(count, dfs(predecessor))
            return count + 1

        # build length_hashmap to save neighbor lookup time
        length_hashmap = collections.defaultdict(set)
        for word in words:
            length_hashmap[len(word)].add(word)

        visited = set()
        longest = 0
        min_length = min(length_hashmap)
        # start from the longest words
        for length in sorted(length_hashmap, reverse=True):
            for word in length_hashmap[length]:
                # skipping checking captured/visited nodes
                if word in visited:
                    continue
                longest = max(longest, dfs(word))
                # no enough words to break the record
                if length - min_length < longest:
                    return longest
        return longest


# Main Call
words = ["a", "b", "ba", "bca", "bda", "bdca"]
solution = Solution()
print(solution.longestStrChain(words))