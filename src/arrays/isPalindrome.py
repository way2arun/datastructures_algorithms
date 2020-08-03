"""
Valid Palindrome
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3411/
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false


Constraints:

s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Solution 1 - 32 ms
        """
        if s is None:
            return True

        # filter
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()

        # init
        i = 0
        j = len(s) - 1

        # main loop
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        # is pal
        return True
        """
        # Solution 2 - 16 ms
        if not s:
            return True

        check = '!@#$%^&*-;,.<>"?/:\|~()[]{}`~'
        list_1 = ["'", '"', " "]

        for x in check:
            if x in s:
                s = s.replace(x, '')

        for x in list_1:
            if x in s:
                s = s.replace(x, '')

        if s.lower() == s[:: -1].lower():
            return True
        return False

        # Solution 3 - 20 ms
        """
        new_s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return new_s == new_s[::-1]
        """


# Main Call
solution = Solution()
s = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s))
s = "race a car"
print(solution.isPalindrome(s))
