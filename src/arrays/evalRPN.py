"""
Evaluate Reverse Polish Notation
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.



Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Solution 1 - 64 ms
        """
        def eval(b, a, op):
            if op == "+":
                return a + b
            elif op == "-":
                return a - b
            elif op == "*":
                return a * b
            else:
                return int(a / b)

        st = []
        for token in tokens:
            if token in "+-*/":
                st.append(eval(st.pop(), st.pop(), token))
            else:
                st.append(int(token))

        return st.pop();
        """
        # Solution 2 - 44 ms
        s = []
        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                r = s.pop()
                l = s.pop()
                if t == "+":
                    s.append(l + r)
                elif t == "-":
                    s.append(l - r)
                elif t == "*":
                    s.append(l * r)
                elif t == "/":
                    s.append(int(l / r))
            else:
                s.append(int(t))
        return s.pop()


# Main Call
tokens = ["2", "1", "+", "3", "*"]

solution = Solution()
print(solution.evalRPN(tokens))
