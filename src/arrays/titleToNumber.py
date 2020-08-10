"""
Excel Sheet Column Number
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3419/
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701


Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".
"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        # Solution 1 - 36 ms
        # Create a map of all corresponding alphabet characters and their indexes:
        # { {A:1}, {B:2}, {C:3}.... {Z:26}}
        """
        char_map = {}
        alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for index in range(0, len(alphabets), 1):
            char_map[alphabets[index]] = index + 1

        # Iterate through "s" backwards
        # Find the corresponding value per character
        base_value = 1
        col_num = 0
        for char in s[::-1]:
            col_num += char_map.get(char) * (base_value)
            base_value *= 26
        return col_num
        """
        # Solution 2 - 12 ms

        n = 0
        while len(s):
            n, s = n * 26 + ord(s[0]) - 64, s[1:]
        return n
        """

        # Solution 3 - 16 ms
        power = 1
        res = 0
        for l in reversed(s):
            res += (ord(l) - 64) * power
            power *= 26

        return res
        """


# Main Call
solution = Solution()
s = "A"
print(solution.titleToNumber(s))
s = "ZY"
print(solution.titleToNumber(s))
