"""
Transform to Chessboard
You are given an n x n binary grid board. In each move, you can swap any two rows with each other, or any two columns with each other.

Return the minimum number of moves to transform the board into a chessboard board. If the task is impossible, return -1.

A chessboard board is a board where no 0's and no 1's are 4-directionally adjacent.



Example 1:


Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
Output: 2
Explanation: One potential sequence of moves is shown.
The first move swaps the first and second column.
The second move swaps the second and third row.
Example 2:


Input: board = [[0,1],[1,0]]
Output: 0
Explanation: Also note that the board with 0 in the top left corner, is also a valid chessboard.
Example 3:


Input: board = [[1,0],[1,0]]
Output: -1
Explanation: No matter what sequence of moves you make, you cannot end with a valid chessboard.


Constraints:

n == board.length
n == board[i].length
2 <= n <= 30
board[i][j] is either 0 or 1.
"""
from collections import Counter
from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        # Solution 1 - 72 ms

        n = len(board)
        patt1 = ([0, 1] * (n // 2 + 1))[:n]
        patt2 = ([1, 0] * (n // 2 + 1))[:n]

        board_t = map(list, zip(*board))
        Cnt_r = list(Counter(tuple(row) for row in board).items())
        Cnt_c = list(Counter(tuple(row) for row in board_t).items())
        if len(Cnt_r) != 2 or len(Cnt_c) != 2: return -1
        if abs(Cnt_r[0][1] - Cnt_r[1][1]) > 1: return -1
        if abs(Cnt_c[0][1] - Cnt_c[1][1]) > 1: return -1

        x1 = sum(i != j for i, j in zip(Cnt_r[0][0], patt1))
        y1 = sum(i != j for i, j in zip(Cnt_c[0][0], patt1))

        x2 = sum(i != j for i, j in zip(Cnt_r[0][0], patt2))
        y2 = sum(i != j for i, j in zip(Cnt_c[0][0], patt2))

        cands_x = [x for x in [x1, x2] if x % 2 == 0]
        cands_y = [y for y in [y1, y2] if y % 2 == 0]

        return min(cands_x) // 2 + min(cands_y) // 2


# Main Call
board = [[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]
solution = Solution()
print(solution.movesToChessboard(board))