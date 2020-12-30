"""
Game of Life
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.



Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.


Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

"""
from itertools import product
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Solution 1 - 36 ms
        """"
        m, n = len(board), len(board[0])
        for i, j in product(range(m), range(n)):
            cnt = 0
            for di, dj in product(range(-1, 2), repeat=2):
                if di != 0 or dj != 0:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < m and 0 <= jj < n:
                        cnt += board[ii][jj] & 1
            if cnt == 3 or (cnt == 2 and board[i][j] & 1):  # Game-of-Life rule
                board[i][j] |= 2
        # print(board)
        for i, j in product(range(m), range(n)):
            board[i][j] >>= 1
        print(board)
        """
        # Solution 2 - 16 ms
        p = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
        for r in range(len(board)):
            for c in range(len(board[r])):
                p[r + 1][c + 1] = p[r + 1][c] + p[r][c + 1] - p[r][c] + board[r][c]

        for r in range(len(board)):
            for c in range(len(board[r])):
                aa, bb, cc, dd = r + 2, c + 2, r - 1, c - 1
                if aa >= len(p):
                    aa = r + 1
                if bb >= len(p[aa]):
                    bb = c + 1
                if cc < 0:
                    cc = r
                if dd < 0:
                    dd = c

                x = p[aa][bb] - p[aa][dd] - p[cc][bb] + p[cc][dd]

                if board[r][c]:
                    if x < 3 or x > 4:
                        board[r][c] = 0
                else:
                    if x == 3:
                        board[r][c] = 1
        print(board)


# Main Call
board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
solution = Solution()
solution.gameOfLife(board)
