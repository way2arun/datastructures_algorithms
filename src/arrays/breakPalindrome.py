"""
Break a Palindrome
Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.



Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.
Example 2:

Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.
Example 3:

Input: palindrome = "aa"
Output: "ab"
Example 4:

Input: palindrome = "aba"
Output: "abb"


Constraints:

1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.
   Hide Hint #1
How to detect if there is impossible to perform the replacement? Only when the length = 1.
   Hide Hint #2
Change the first non 'a' character to 'a'.
   Hide Hint #3
What if the string has only 'a'?
   Hide Hint #4
Change the last character to 'b'.


"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # Solution 1 - 28 ms
        """
        n = len(palindrome)
        for i in range(n // 2):
            if palindrome[i] != "a": return palindrome[:i] + "a" + palindrome[i + 1:]
        return palindrome[:-1] + "b" if n > 1 else ""
        """
        # Solution 2 - 12 ms
        N = len(palindrome)
        mid = int(N / 2)
        res = ""

        if N == 1:
            return res

        for i, char in enumerate(palindrome[0:mid]):

            if char != 'a':
                res += 'a' + palindrome[i + 1:N]
                return res
            else:
                res += char

        return palindrome[:-1] + 'b'

# Main Call
palindrome = "aba"
solution = Solution()
print(solution.breakPalindrome(palindrome))