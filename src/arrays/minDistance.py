"""
Delete Operation for Two Strings
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.



Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4


Constraints:

1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
"""
from collections import defaultdict
from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Solution 1 - 772 ms
        """
        @lru_cache()
        def min_dist(i, j):
            if i == len(word1) or j == len(word2):
                return len(word2) + len(word1) - i - j
            else:
                if word1[i] == word2[j]:
                    return min_dist(i + 1, j + 1)
                else:
                    return min(min_dist(i + 1, j), min_dist(i, j + 1)) + 1

        return min_dist(0, 0)
        """

        # Solution 2 - 76 ms
        """
        @lru_cache(None)
        def helper(i: int, j: int) -> int:

            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                return helper(i + 1, j + 1)

            return min(helper(i + 1, j) + 1, helper(i, j + 1) + 1)

        return helper(0, 0)

        """
        # Solution 3 - 76 ms
        return len(word1) + len(word2) - 2 * self.lcs(word1, word2)

    def lcs(self, text1: str, text2: str) -> int:
        positionCount = defaultdict(list)
        letterSet = set(text1)
        dp = []
        for index in range(len(text2) - 1, -1, -1):
            letter2 = text2[index]
            if letter2 in letterSet:
                positionCount[letter2].append(index)
        for letter1 in text1:
            positionList = positionCount[letter1]
            if len(positionList) == 0:
                continue
            if len(dp) == 0:
                dp.append(positionList[-1])
            else:
                for index in positionList:
                    if index > dp[-1]:
                        dp.append(index)
                    else:
                        bisectIndex = bisect_left(dp, index)
                        print(index, bisectIndex)
                        if bisectIndex < len(dp):
                            dp[bisect_left(dp, index)] = index
        return len(dp)


# Main Call
word1 = "sea"
word2 = "eat"

solution = Solution()
print(solution.minDistance(word1, word2))