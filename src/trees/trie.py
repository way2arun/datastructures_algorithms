"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3329/
"""


class Trie:
    # Solution 2 104 ms
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        root = self.trie
        for c in word:
            if c not in root:
                root[c] = {}
            root = root[c]
        root['#'] = '#'

    def search(self, word: str) -> bool:
        # start = self.trie
        # for c in word:
        #     if c not in start:
        #         return False
        #     start = start[c]
        # if '#' in start:
        #     return True
        # return False
        return self.startsWith(word + '#')

    def startsWith(self, prefix: str) -> bool:
        start = self.trie
        for c in prefix:
            if c not in start:
                return False
            start = start[c]
        return True

    """
    # Solution 1032 ms
    def __init__(self):
        self.trie = set()

    def insert(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        return word in self.trie


    def startsWith(self, prefix: str) -> bool:
        for word in self.trie:
            if word.startswith(prefix):
                return True
        return False
    """

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
obj.insert("app")
print(obj.search("app"))
