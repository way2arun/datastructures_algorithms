"""
N-Queens
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.



Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]


Constraints:

1 <= n <= 9
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Solution 1 - 68 ms
        """
        def dfs(board, i, c1, c2, c3):
            if i == n:
                ans.append(["." * j + "Q" + "." * (n - j - 1) for j in board])

            for j in range(n):
                if c1 & (1 << j) == 0 and c2 & (1 << (i - j + n)) == 0 and c3 & (1 << (i + j)) == 0:
                    dfs(board + [j], i + 1, c1 ^ (1 << j), c2 ^ (1 << (i - j + n)), c3 ^ (1 << (i + j)))

        ans = []
        dfs([], 0, 0, 0, 0)
        return ans
        """
        # Solution 2 - 36 ms
        #         Approach 1 - leetcode solution: time = O(N!) ; space = O(N)
        #def could_place(row, col):
        #   return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])

        #         def place_queen(row, col):
        #             queens.add((row, col))
        #             cols[col] = 1
        #             hill_diagonals[row - col] = 1
        #             dale_diagonals[row + col] = 1

        #         def remove_queen(row, col):
        #             queens.remove((row, col))
        #             cols[col] = 0
        #             hill_diagonals[row - col] = 0
        #             dale_diagonals[row + col] = 0

        #         def add_solution():
        #             solution = []
        #             for _, col in sorted(queens):
        #                 solution.append('.' * col + 'Q' + '.' * (n - col - 1))
        #             output.append(solution)

        #         def backtrack(row = 0):
        #             for col in range(n):
        #                 if could_place(row, col):
        #                     place_queen(row, col)
        #                     if row + 1 == n:
        #                         add_solution()
        #                     else:
        #                         backtrack(row + 1)
        #                     remove_queen(row, col)

        #         cols = [0] * n
        #         hill_diagonals = [0] * (2 * n - 1)
        #         dale_diagonals = [0] * (2 * n - 1)
        #         queens = set()
        #         output = []
        #         backtrack()
        #         return output

        # approach 2, refer - https://leetcode.com/problems/n-queens/discuss/19971/Python-recursive-dfs-solution-with-comments.
        d1 = [False] * (2 * n - 1)
        d2 = [False] * (2 * n - 1)
        c = [False] * n
        res = []
        def solve(i, tmp):
            if i == n:
                res.append(list(tmp))
                return
            st = ''
            for j in range(n):
                if not c[j] and not d1[i + j] and not d2[i - j]:
                    c[j] = d1[i + j] = d2[i - j] = True
                    st = '.' * j + 'Q' + '.' * (n - j - 1)
                    tmp.append(st)
                    solve(i + 1, tmp)
                    c[j] = d1[i + j] = d2[i - j] = False
                    tmp.pop()
        solve(0, [])
        return res


# Main Call
n = 4
solution = Solution()
print(solution.solveNQueens(n))