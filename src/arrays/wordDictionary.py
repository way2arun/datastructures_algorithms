"""
Add and Search Word - Data structure design
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3413/
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.

   Hide Hint #1
You should be familiar with how a Trie works. If not, please work on this problem: Implement Trie (Prefix Tree) first.

"""
from collections import defaultdict


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Solution 1 - 200 ms
        # self.words = defaultdict(set)

        # Solution 2 - 112 ms
        self.word_dict = defaultdict(list)
        self.wordSet = set()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        # Solution 1 - 200 ms
        # self.words[len(word)].add(word)

        # Solution 2 - 112 ms
        if word:
            self.word_dict[len(word)].append(word)
            self.wordSet.add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        # Solution 1 - 200 ms
        """
        if word in self.words[len(word)]:
            return True
        if "." in word:
            new_set = self.words[len(word)]
            index = [i for i in range(len(word)) if word[i] != '.']
            new_word = [word[i] for i in index]  # new word to search

            for s in new_set:
                new_s = [s[i] for i in
                         index]  # new word in dict to be compared, faster if use explicity for loop, but more ugly
                if new_s == new_word:
                    return True
            return False
        return False
        """
        # Solution 2 - 112 ms
        if word in self.wordSet:
            return True
        else:
            for v in self.word_dict[len(word)]:
                # match xx.xx.x with yyyyyyy
                for i, ch in enumerate(word):
                    if ch != v[i] and ch != '.':
                        break
                else:
                    return True
            return False


# Your WordDictionary object will be instantiated and called as such:
solution = WordDictionary()
solution.addWord("bad")
solution.addWord("dad")
solution.addWord("mad")
print(solution.search("pad"))
print(solution.search("bad"))
print(solution.search(".ad"))
print(solution.search("b.."))
