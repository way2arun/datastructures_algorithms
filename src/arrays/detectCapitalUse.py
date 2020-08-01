"""
Detect Capital
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.


Example 1:

Input: "USA"
Output: True


Example 2:

Input: "FlaG"
Output: False


Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3409/
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Solution 1 - 36 ms
        """
        total_capital_chars = 0
        word_length = len(word)
        for letter in word:
            total_capital_chars += letter.isupper()
        if total_capital_chars == 0 or total_capital_chars == word_length or total_capital_chars == 1 and word[
            0].isupper():
            return True
        return False
        """
        # Solution 2 - 12 ms
        if word.lower() == word:
            return True
        if word.upper() == word:
            return True
        if word[0].upper() == word[0] and word[1:].lower() == word[1:]:
            return True
        return False

        """
        # Solution 3 - 16 ms

        if len(word) <= 1:
            return True
        cap1 = word[1]
        for c in word[2:]:
            if c.islower() != cap1.islower():
                return False
        if word[0].islower() and cap1.isupper():
            return False
        return True
        """


# Main Call
solution = Solution()
word = "USA"
print(solution.detectCapitalUse(word))
word = "FlaG"
print(solution.detectCapitalUse(word))
