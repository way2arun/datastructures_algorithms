"""
Length of Last Word
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3461/
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5

"""
import re


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Solution 1 - 32 ms without using split
        """
        We can just split our string, remove all extra spaces and return length of the last word, however we need to spend O(n) time for this, where n is length of our string. There is a simple optimization: let us traverse string from the end and:

        find the last element of last word: traverse from the end and find first non-space symbol.
        continue traverse and find first space symbol (or beginning of string)
        return end - beg.
        Complexity: is O(m), where m is length of part from first symbol of last word to the end. Space complexity is O(1).
        """
        """
        end = len(s) - 1
        while end > 0 and s[end] == " ":
            end -= 1
        beg = end
        while beg >= 0 and s[beg] != " ":
            beg -= 1
        return end - beg
        """
        # Solution 2 - 12 ms using split
        """
        if not s or len(s) == 0:
            return 0
        return len(re.split('\s+', s.strip())[-1])
        """
        # Solution 3 - 16 ms without using split
        l = 0
        if len(s) == 1 and ' ' not in s:
            return 1
        for i in range(len(s) - 1, 0, -1):
            if s[i] == ' ':
                l = l + 1
            else:
                break
        l1 = 0
        for i in range(len(s) - l - 1, -1, -1):
            if s[i] != ' ':
                l1 = l1 + 1
            else:
                break
        return l1


# Main Call
s = "Hello World"
solution = Solution()
print(solution.lengthOfLastWord(s))
