"""
Minimum Remove to Make Valid Parentheses
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"


Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
   Hide Hint #1
Each prefix of a balanced parentheses has a number of open parentheses greater or equal than closed parentheses, similar idea with each suffix.
   Hide Hint #2
Check the array from left to right, remove characters that do not meet the property mentioned above, same idea in backward way.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Solution 1 - 140 ms
        """
        def clean(s, op, cl):
            balance, ans = 0, ""
            for i in s:
                if i == op:
                    balance += 1
                    ans += i
                elif i == cl and balance > 0:
                    balance -= 1
                    ans += i
                elif i not in "()":
                    ans += i
            return ans

        return clean(clean(s, "(", ")")[::-1], ")", "(")[::-1]
        """
        # Solution 2 - 64 ms
        closing_tags, opening_tags = 0, 0
        for c in s:
            if c == '(':
                opening_tags += 1
            elif c == ')':
                if opening_tags:
                    opening_tags -= 1
                else:
                    closing_tags += 1

        print(opening_tags, closing_tags)
        res, j = [], 0
        while j < len(s) and closing_tags:
            if s[j] == ')':
                closing_tags -= 1
            else:
                res.append(s[j])
            j += 1

        res_end, j_end = [], len(s) - 1
        while 0 <= j_end and opening_tags:
            if s[j_end] == '(':
                opening_tags -= 1
            else:
                res_end.append(s[j_end])
            j_end -= 1
        # print(res, s[j:j_end+1], res_end[::-1], j, j_end)
        return ''.join(res) + s[j:j_end + 1] + ''.join(res_end[::-1])


# Main Call
s = "lee(t(c)o)de)"

solution = Solution()
print(solution.minRemoveToMakeValid(s))