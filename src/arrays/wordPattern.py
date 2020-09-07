"""
Word Pattern
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
"""
import str as str


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        # Solution 1 -  28 ms
        """
        my_dict = {}
        words = str.split()

        # pattern is not the same length as list of words:
        if len(words) != len(pattern):
            return False

        # keep in dictionary each letter in pattern with corresponding word:
        for i, p in enumerate(pattern):
            if my_dict.get(p):
                # found a word that doesn't match previous letter in pattern:
                if my_dict.get(p) != words[i]:
                    return False
            else:
                # same letter in pattern for two different words:
                if words[i] in my_dict.values():
                    return False
                my_dict[p] = words[i]

        return True
        """
        # Solution 2 - 12 ms
        words = str.lstrip().split(" ")

        if len(words) != len(pattern):
            return False

        letter_to_word = {}
        word_to_letter = {}

        for letter, word in zip(pattern, words):
            if not letter in letter_to_word:
                letter_to_word[letter] = word
            elif letter_to_word[letter] != word:
                return False

            if not word in word_to_letter:
                word_to_letter[word] = letter
            elif word_to_letter[word] != letter:
                return False

        return True


# Main Solution
solution = Solution()
pattern = "abba"
str = "dog cat cat dog"
print(solution.wordPattern(pattern, str))
