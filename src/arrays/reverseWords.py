"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3391/
Given an input string, reverse the string word by word.



Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.


Follow up:

For C programmers, try to solve it in-place in O(1) extra space.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        # Solution 1 - 52 ms
        """
        s = s.lstrip(" ")
        s = s.rstrip(" ")
        s = s.split(" ")

        index = 0
        word_length = 0
        string_length = len(s) - 1
        ans = []

        while index < len(s):
            if s[index] == "":
                del s[index]
                string_length -= 1
            else:
                index += 1
        while word_length < string_length:
            s[word_length], s[string_length] = s[string_length], s[word_length]
            word_length += 1
            string_length -= 1
        return " ".join(s)
        """
        # Solution 2 - 8 ms
        words = s.split(" ")
        words = [x for x in words if x != ""]
        rev = list(reversed(words))

        out = ""

        for i, string in enumerate(rev):
            if i == len(rev) - 1:
                out += string
            else:
                out += string + " "

        return out


# Main Call
solution = Solution()
s = "the sky is blue"
print(solution.reverseWords(s))