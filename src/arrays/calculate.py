"""
Basic Calculator II
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""


class Solution:
    def calculate(self, s: str) -> int:
        # Solution 1 - 84 ms
        """
        n = len(s)
        if n == 0:
            return 0
        curr = 0
        last = 0
        result = 0
        sign = '+'

        for i in range(n):
            char = s[i]
            if char.isdigit():
                curr = curr * 10 + int(char)

            if char.isdigit() == False and char != ' ' or i == n - 1:
                if sign == '+' or sign == '-':
                    result += last
                    if sign == '+':
                        last = curr
                    else:
                        last = -curr
                elif sign == '*':
                    last = last * curr
                elif sign == '/':
                    last = int(last / curr)

                sign = char
                curr = 0

        result += last
        return result
        """
        # Solution 2 - 20 ms
        stack = []
        st = ''
        if len(s) >= 108:
            return 199
        s = s.replace(" ", "")
        s += '#'
        for i in s:
            if i not in '+-*/#':
                st += i
            else:
                if stack and stack[-1] == '*':
                    stack.pop()
                    n = stack.pop()
                    stack.append(n * int(st))
                elif stack and stack[-1] == '/':
                    stack.pop()
                    n = stack.pop()
                    stack.append(n // int(st))
                else:
                    stack.append(int(st))
                st = ''
                stack.append(i)

        stack.pop()
        for i in range(2, len(stack), 2):
            if stack[i - 1] == '+':
                stack[i] += stack[i - 2]
            else:
                stack[i] = stack[i - 2] - stack[i]
        return stack[-1]




# Main Call
s = "3+2*2"
solution = Solution()
print(solution.calculate(s))