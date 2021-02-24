"""
Score of Parentheses
Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6


Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50
"""


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        # Solution 1 - 28 ms
        """"
        ans, bal = 0, 0
        for i, s in enumerate(S):
            bal = bal + 1 if s == "(" else bal - 1
            if i > 0 and S[i - 1:i + 1] == "()":
                ans += 1 << bal
        return ans
        """
        # Solution 2 - 16 ms
        arr = list(S)
        stack = []
        for char in arr:
            if char == "(":
                stack.append(char)
                continue
            inter = 0
            while stack[-1] != "(":
                inter += stack.pop()
            stack.pop()
            stack.append(max(2 * inter, 1))
        return sum(stack)


# Main Call
S = "(()(()))"
solution = Solution()
print(solution.scoreOfParentheses(S))