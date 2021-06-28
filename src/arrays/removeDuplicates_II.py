"""
Remove All Adjacent Duplicates In String
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.



Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
   Hide Hint #1
Use a stack to process everything greedily.
"""
from string import ascii_lowercase

class Solution:
    def removeDuplicates(self, s: str) -> str:
        # Solution 1 - 68 ms
        """
        stack = []
        for symb in s:
            if stack and stack[-1] == symb:
                stack.pop()
            else:
                stack.append(symb)
        return "".join(stack)
        """
        # Solution 2 - 40 ms
        duplicates = [2 * ch for ch in ascii_lowercase]
        prev_length = -1
        while prev_length != len(s):
            prev_length = len(s)
            for d in duplicates:
                s = s.replace(d, '')
        return s


# Main Call
solution = Solution()
s = "abbaca"
print(solution.removeDuplicates(s))
