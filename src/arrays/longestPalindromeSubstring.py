"""
Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
   Hide Hint #1
How can we reuse a previously computed palindrome to compute a larger palindrome?
   Hide Hint #2
If “aba” is a palindrome, is “xabax” and palindrome? Similarly is “xabay” a palindrome?
   Hide Hint #3
Complexity based hint:
If we use brute-force and check whether for every start and end position a substring is a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks. Can we reduce the time for palindromic checks to O(1) by reusing some previous computation.

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Solution 1 - 736 ms
        """
        result = s[0]
        for i in range(len(s)):
            p1, p2 = i - 1, i + 1
            while p2 < len(s) and s[p2] == s[i]:
                p2 += 1
            while (p1 > -1 and p2 < len(s)) and s[p1] == s[p2]:
                p1 -= 1
                p2 += 1
            result = s[p1 + 1:p2] if (p2 - p1 - 1) > len(result) else result
        return result
        """
        # Solution 2 - 72 ms
        if len(s) <= 1 or s == s[::-1]:
            return s

        start = 0
        length = 1

        for i in range(len(s)):
            odd = s[i - length - 1: i + 1]
            even = s[i - length: i + 1]

            if 0 <= i - length - 1 and odd == odd[::-1]:
                start = i - length - 1
                length += 2
            elif 0 <= i - length and even == even[::-1]:
                start = i - length
                length += 1

        return s[start: start + length]


# Main Call
solution = Solution()
s = "babad"
print(solution.longestPalindrome(s))
