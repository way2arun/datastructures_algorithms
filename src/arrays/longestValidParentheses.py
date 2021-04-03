"""
Longest Valid Parentheses
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.



Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Solution 1 - 44ms
        """
        # stack, used to record index of parenthesis
        # initialized to -1 as dummy head for valid parentheses length computation
        stack = [-1]

        max_length = 0

        # linear scan each index and character in input string s
        for cur_idx, char in enumerate(s):

            if char == '(':

                # push when current char is (
                stack.append(cur_idx)

            else:

                # pop when current char is )
                stack.pop()

                if not stack:

                    # stack is empty, push current index into stack
                    stack.append(cur_idx)
                else:
                    # stack is non-empty, update maximal valid parentheses length
                    max_length = max(max_length, cur_idx - stack[-1])

        return max_length
        """
        # Solution 2 - 24 ms
        if len(s) < 2:
            return 0
        max_val = 0
        stack = [-1]

        # Saving the last invalid paranthesis index in stack When a ( comes, store index in stack When a ) come,
        # pop from stack, then check if stack if empty If stack is empty, push index in stack because that's invalid
        # If stack is not empty, check i - top of stack, this will be length of valid substring because top of stack
        # will be index of last invalid paranthesis

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_val = max(max_val, i - stack[-1])
        return max_val


# Main Call
s = "(()"
solution = Solution()
print(solution.longestValidParentheses(s))