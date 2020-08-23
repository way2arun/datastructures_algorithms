"""
Stream of Characters
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3434/
Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.


Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist


Note:

1 <= words.length <= 2000
1 <= words[i].length <= 2000
Words will only consist of lowercase English letters.
Queries will only consist of lowercase English letters.
The number of queries is at most 40000.
   Hide Hint #1
Put the words into a trie, and manage a set of pointers within that trie.
"""
from functools import reduce
from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.dict = defaultdict(TrieNode)
        self.is_word = False


class StreamChecker:
    # Solution 1 - 744 ms
    """
    def __init__(self, words: List[str]):
        '''
        Build a trie for each word in reversed order
        '''

        # for user query record, init as empty string
        self.prefix = ''

        # for root node of trie, init as empty Trie
        self.trie = TrieNode()

        for word in words:

            cur_node = self.trie

            # make word in reverse order
            word = word[::-1]

            for char in word:
                cur_node = cur_node.dict[char]

            # mark this trie path as a valid word
            cur_node.is_word = True

    def query(self, letter: str) -> bool:
        '''
        Search user input in trie with reversed order
        '''

        self.prefix += letter

        cur_node = self.trie
        for char in reversed(self.prefix):

            if char not in cur_node.dict:
                # current char not in Trie, impossible to match words
                break

            cur_node = cur_node.dict[char]

            if cur_node.is_word:
                # user input match a word in Trie
                return True

        # No match
        return False
    """
    # Solution 2 - 584 ms
    def __init__(self, words: List[str]):
        # build the trie of reverse words
        T = lambda: defaultdict(T)
        self.trie = T()
        for w in words:
            reduce(dict.__getitem__, w[::-1], self.trie)['#'] = True
        self.s = ''
        self.L = max(map(len, words))

    def query(self, letter: str) -> bool:
        # query directly
        self.s = (letter + self.s)[:self.L]
        node = self.trie
        for x in self.s:
            if x in node:
                node = node[x]
                if '#' in node:
                    return True
            else:
                break
        return False


# Main Call
words = ["cd", "f", "kl"]
streamChecker = StreamChecker(words)
print(streamChecker.query('a'))
print(streamChecker.query('b'))
print(streamChecker.query('c'))
print(streamChecker.query('d'))
print(streamChecker.query('e'))
print(streamChecker.query('f'))
print(streamChecker.query('g'))
print(streamChecker.query('h'))
print(streamChecker.query('i'))
print(streamChecker.query('j'))
print(streamChecker.query('k'))
print(streamChecker.query('l'))
