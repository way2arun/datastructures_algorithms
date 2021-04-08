"""
Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.





Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]


Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
from typing import List


class Solution:
    def __init__(self):
        self.combinations = []
    def letterCombinations(self, digits: str) -> List[str]:
        # Solution 1 - 28 ms
        """
        if not digits: return []
        mappings = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = []

        def construct(idx=0, partial=[]):
            if idx >= len(digits):
                result.append(''.join(partial))
                return
            for ch in mappings[digits[idx]]:
                partial.append(ch)
                construct(idx + 1, partial)
                partial.pop()

        construct()
        return result
        """
        # Solution 2 - 8 ms
        digit_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if len(digits) == 0:
            return []

        if len(digits) == 1:
            return [digit_letters[char] for char in digits][0]

        self.combinations = digit_letters[digits[0]]

        for digit in digits[1:]:

            new_combinations = []
            print(new_combinations)

            for combination in self.combinations:

                for char in digit_letters[digit]:
                    new_combinations.append(combination + char)
            self.combinations = new_combinations

        return self.combinations


# Main Call
digits = "23"
solution = Solution()
print(solution.letterCombinations(digits))