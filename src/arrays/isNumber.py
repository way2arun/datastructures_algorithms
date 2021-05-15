"""
Valid Number
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
At least one digit, followed by a dot '.'.
At least one digit, followed by a dot '.', followed by at least one digit.
A dot '.', followed by at least one digit.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
At least one digit.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.



Example 1:

Input: s = "0"
Output: true
Example 2:

Input: s = "e"
Output: false
Example 3:

Input: s = "."
Output: false
Example 4:

Input: s = ".1"
Output: true


Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.

"""


class Solution:
    def isNumber(self, s: str) -> bool:
        # Solution - 52 ms
        """
        num, exp, sign, dec = False, False, False, False
        for c in s:
            if '0' <= c <= '9':
                num = True
            elif c == 'e' or c == 'E':
                if exp or not num:
                    return False
                else:
                    exp, num, sign, dec = True, False, False, False
            elif c == '+' or c == '-':
                if sign or num or dec:
                    return False
                else:
                    sign = True
            elif c == '.':
                if dec or exp:
                    return False
                else:
                    dec = True
            else:
                return False
        return num
        """
        # Solution 2 - 16 ms
        currentState = 0
        state = [
            {'blank': 0, 'sign': 1, 'digit': 2, '.': 3},
            {'digit': 2, '.': 3},
            {'digit': 2, '.': 4, 'e': 5, 'blank': 8},
            {'digit': 4},
            {'digit': 4, 'e': 5, 'blank': 8},
            {'sign': 6, 'digit': 7},
            {'digit': 7},
            {'digit': 7, 'blank': 8},
            {'blank': 8}
        ]

        for c in s:
            if c == 'E':
                c = 'e'
            elif '0' <= c <= '9':
                c = 'digit'
            elif c == ' ':
                c = 'blank'
            elif c in ['+', '-']:
                c = 'sign'
            if c not in state[currentState].keys():
                return False
            currentState = state[currentState][c]
        if currentState not in [2, 4, 7, 8]:
            return False
        return True


# Main Call
s = "0"

solution = Solution()
print(solution.isNumber(s))