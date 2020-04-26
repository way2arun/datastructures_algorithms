"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.



If there is no common subsequence, return 0.



Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
   Hide Hint #1
Try dynamic programming. DP[i][j] represents the longest common subsequence of text1[0 ... i] & text2[0 ... j].
   Hide Hint #2
DP[i][j] = DP[i - 1][j - 1] + 1 , if text1[i] == text2[j] DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) , otherwise
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3311/


"""
import bisect
import collections


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 20 ms
        memo = collections.defaultdict(list)
        for i, a in enumerate(text1):
            memo[a].append(i)
        tmp = []
        for c in text2:
            tmp += memo[c][::-1]

        # print(tmp)
        def lis(arr):
            dp = [-1]
            for n in arr:
                if n > dp[-1]:
                    dp.append(n)
                else:
                    idx = bisect.bisect_left(dp, n)
                    dp[idx] = n
            return len(dp) - 1

        return lis(tmp)
        """
        # 448 ms
        text1_len = len(text1)
        text2_len = len(text2)

        temp = [[None] * (text2_len + 1) for i in range(text1_len + 1)]
        for i in range(text1_len + 1):
            for j in range(text2_len + 1):
                if i == 0 or j == 0:
                    temp[i][j] = 0
                elif text1[i - 1] == text2[j - 1]:
                    temp[i][j] = temp[i - 1][j - 1] + 1
                else:
                    temp[i][j] = max(temp[i - 1][j], temp[i][j - 1])
        return temp[text1_len][text2_len]
        """


# Main Call
solution = Solution()
text1 = "abcde"
text2 = "ace"
result = solution.longestCommonSubsequence(text1, text2)
print(result)
