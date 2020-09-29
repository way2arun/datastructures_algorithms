"""
Word Break
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/558/week-5-september-29th-september-30th/3477/
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Solution 1 - 40 ms
        """
        dp = [True] + [False] * len(s)
        for indx in range(1, len(s) + 1):
            for word in wordDict:
                if dp[indx - len(word)] and s[:indx].endswith(word):
                    dp[indx] = True
        return dp[-1]
        """
        # Solution 2 - 16 ms
        """
        lookup = {}
        return self.word_break(lookup, s, wordDict)
        """

        # Solution 3 - 12 ms
        @lru_cache
        def helper(idx):
            if idx == len(s):
                return True
            if idx > len(s):
                return False
            for word in wordDict:
                if s.find(word, idx) == idx and helper(idx + len(word)) == True:
                    # Matched following words
                    return True
            return False

        return helper(0)

    def word_break(self, lookup, s, wordDict):
        if len(s) == 0:
            return True
        if s in lookup:
            return lookup[s]
        for word in wordDict:
            if s.startswith(word):
                print(s, "starts with", word)
                # Remove word and continue
                if self.word_break(lookup, s[len(word):], wordDict):
                    lookup[s] = True
                    return True
        lookup[s] = False
        return False


# Main Call
s = "applepenapple"
wordDict = ["apple", "pen"]
solution = Solution()
print(solution.wordBreak(s, wordDict))
