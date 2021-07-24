"""
Word Ladder II
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


Constraints:

1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 1000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""
from collections import defaultdict
from string import ascii_lowercase
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # Solution 1 - 74 ms
        """
        wordSet = set(wordList)  # to check if a word is existed in O(1)

        def neighbors(word):
            for i in range(len(word)):  # change every possible single letters and check if it's in wordSet
                for c in ascii_lowercase:
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in wordSet:
                        yield newWord

        layer = {}
        layer[beginWord] = [
            [beginWord]]  # layer[word] is all possible sequence paths which start from beginWord and end at `word`.
        while layer.keys():
            nextLayer = defaultdict(list)
            for word in layer.keys():
                if word == endWord:
                    return layer[word]  # return all shortest sequence paths
                for nei in neighbors(word):
                    for path in layer[word]:
                        nextLayer[nei].append(path + [nei])  # add new word to all sequences and form new layer element
            wordSet -= set(nextLayer.keys())  # remove visited words to prevent loops
            layer = nextLayer  # move to new layer

        return []
        """
        # Solution 2 - 20 ms
        if not endWord in wordList:
            return []
        hash = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                hash[word[:i] + "*" + word[i + 1:]].append(word)

        def edges(word):
            for i in range(len(word)):
                for newWord in hash[word[:i] + '*' + word[i + 1:]]:
                    if not newWord in marked:
                        yield newWord

        def findPath(end):
            res = []
            for curr in end:
                for parent in path[curr[0]]:
                    res.append([parent] + curr)
            return res

        marked = set()
        path =  defaultdict(set)
        begin = set([beginWord])
        end = set([endWord])
        forward = True
        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin
                forward = not forward
            temp = set()
            for word in begin:
                marked.add(word)
            for word in begin:
                for w in edges(word):
                    temp.add(w)
                    if forward:
                        path[w].add(word)
                    else:
                        path[word].add(w)
            begin = temp
            if begin & end:
                res = [[endWord]]
                while res[0][0] != beginWord:
                    res = findPath(res)
                return res
        return []


# Main Call
solution = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(solution.findLadders(beginWord, endWord, wordList))