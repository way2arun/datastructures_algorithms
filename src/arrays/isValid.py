"""
Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
   Hide Hint #1
An interesting property about a valid parenthesis expression is that a sub-expression of a valid expression should also be a valid expression. (Not every sub-expression) e.g.
{ { } [ ] [ [ [ ] ] ] } is VALID expression
          [ [ [ ] ] ]    is VALID sub-expression
  { } [ ]                is VALID sub-expression
Can we exploit this recursive structure somehow?
   Hide Hint #2
What if whenever we encounter a matching pair of parenthesis in the expression, we simply remove it from the expression? This would keep on shortening the expression. e.g.
{ { ( { } ) } }
      |_|

{ { (      ) } }
    |______|

{ {          } }
  |__________|

{                }
|________________|

VALID EXPRESSION!
   Hide Hint #3
The stack data structure can come in handy here in representing this recursive structure of the problem. We can't really process this from the inside out because we don't have an idea about the overall structure. But, the stack can help us process this recursively i.e. from outside to inwards.

"""


class Solution:
    def isValid(self, s: str) -> bool:
        # Solution 1 - 24 ms
        """
        dct = {"[": "]", "(": ")", "{": "}"}
        stack = []
        for char in s:
            if char in dct:
                stack.append(char)
            else:
                if not stack or char != dct[stack.pop()]:
                    return False
        return not stack
        """
        # Solution 2 - 12 ms
        """
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in d:  # 1
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:  # 2
                return False
        return len(stack) == 0  # 3

        # 1. if it's the left bracket then we append it to the stack
        # 2. else if it's the right bracket and the stack is empty(meaning no matching left bracket), or the left bracket doesn't match
        # 3. finally check if the stack still contains unmatched left bracket
        """

        # Solution 3 - 8 ms
        ob = []
        brackets = {'(': ')', '{': '}', '[': ']'}
        for bracket in s:
            if bracket in brackets:
                ob.append(bracket)
                continue
            if not ob:
                return False
            b = ob.pop()
            if bracket != brackets[b]:
                return False
        return not ob


# Main Call
s = "{[]}"
solution = Solution()
print(solution.isValid(s))