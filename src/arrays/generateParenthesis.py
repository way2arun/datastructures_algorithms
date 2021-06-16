"""
Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Solution 1 - 32 ms
        """
        ans, m = [], 2 * n

        def dfs(pos: int, opn: int, seq: int) -> None:
            if pos == m:
                res = [0] * m
                for i in range(m):
                    res[i] = "(" if seq & 1 << i else ")"
                ans.append("".join(res))
                return
            if opn: dfs(pos + 1, opn - 1, seq)
            if m - pos > opn: dfs(pos + 1, opn + 1, seq | 1 << pos)

        dfs(0, 0, 0)
        return ans
        """
        # Solution 2 - 16 ms
        def generate(n: int) -> List[str]:
            if n == 0: return ['']
            if n == 1: return ['()']

            result = []
            for x in range(n):
                for l in generate(x):
                    for r in generate(n - 1 - x):
                        result.append("(" + l + ")" + r)

            return result

        return generate(n)


# Main Call
n = 3
solution = Solution()
print(solution.generateParenthesis(n))