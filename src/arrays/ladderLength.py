"""
Word Ladder
Given two words beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Return 0 if there is no such transformation sequence.



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.


Constraints:

1 <= beginWord.length <= 100
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the strings in wordList are unique.
"""
from collections import defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Solution 1 - 236 ms
        """
        masks = defaultdict(list)
        for word in wordList:
            for i, ch in enumerate(word):
                masks[word[:i] + '*' + word[i + 1:]].append(word)

        steps = 1
        queue = [beginWord]

        while queue:
            next_queue = []
            while queue:
                cur_word = queue.pop()
                if cur_word == endWord:
                    return steps
                for i, ch in enumerate(cur_word):
                    mask = cur_word[:i] + '*' + cur_word[i + 1:]
                    next_queue.extend(masks[mask])
                    del masks[mask]
            steps += 1
            queue = next_queue

        return 0
        """
        # Solution 2 - 68 ms
        if endWord not in wordList:
            return 0
        wL = set(wordList)  # word list
        start = set([beginWord])
        end = set([endWord])
        step = 2
        alpha = "qwertyuiopasdfghjklzxcvbnm"

        while start and end:
            if len(start) > len(end):
                start, end = end, start
            wL -= start

            newStart = []

            for i in start:
                for j in range(len(i)):
                    new1 = i[:j]
                    new2 = i[j + 1:]
                    for a in alpha:
                        newWord = new1 + a + new2
                        if newWord in wL:
                            newStart.append(newWord)
                        if newWord in end:
                            return step
            step += 1
            start = set(newStart)
        return 0


# Main Call
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

solution = Solution()
print(solution.ladderLength(beginWord, endWord, wordList))