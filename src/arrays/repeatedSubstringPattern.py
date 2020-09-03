"""
Repeated Substring Pattern
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3447/
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.



Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Solution 1 - 128 ms
        """
        for i in range(1, len(s) // 2 + 1):
            if s[:i] * (len(s) // i) == s:
                return True
        return False
        """
        # Solution 2 - 16 ms
        ss = (s + s)[1:-1]
        print(ss)
        print(s)
        return ss.find(s) != -1


# Main Solution
s = "abab"
solution = Solution()
print(solution.repeatedSubstringPattern(s))
