"""
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3363/
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> List:
        """
        Do not return anything, modify board in-place instead.
        """

        if len(board) < 2 or len(board[0]) < 2:
            return

        # making DFS calls only from borders.
        for row in range(len(board)):
            if board[row][0] == 'O':
                self.dfs(board, row, 0)
            if board[row][len(board[0]) - 1] == 'O':
                self.dfs(board, row, len(board[0]) - 1)

        for col in range(1, len(board[0])):
            if board[0][col] == 'O':
                self.dfs(board, 0, col)
            if board[len(board) - 1][col] == 'O':
                self.dfs(board, len(board) - 1, col)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':  # after DFS, its still "O", so it cannot escape, so merge with X
                    board[row][col] = 'X'
                if board[row][col] == 'E':
                    board[row][col] = 'O'
        return board

    def dfs(self, board, row, col):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != 'O':
            return
        board[row][col] = 'E'  # can be escaped from border
        self.dfs(board, row + 1, col)
        self.dfs(board, row - 1, col)
        self.dfs(board, row, col + 1)
        self.dfs(board, row, col - 1)


from typing import Dict, List, Set


def extend_safety(grid: List[List[str]], row: int, col: int, safe: Set, seen: Set) -> None:
    '''
    Given a point next to a safe 0-point, check if it is also 0, in which
    case mark it safe and extend safety to its non-x neighbors.
    Explore RLTB (Right, Left, Top, Bottom).
    TODO: ? micro-optimize ?
    '''
    if (row, col) in seen:
        return
    seen.add((row, col))
    if grid[row][col] != 'X':
        safe.add((row, col))  # mark as safe first, then explore more
        if col + 1 < len(grid[row]):
            extend_safety(grid, row, col + 1, safe, seen)
        if col > 0:
            extend_safety(grid, row, col - 1, safe, seen)
        if row + 1 < len(grid):
            extend_safety(grid, row + 1, col, safe, seen)
        if row > 0:
            extend_safety(grid, row - 1, col, safe, seen)


def board_capture(board: List[List[str]]) -> List:
    '''
    Runtime: 144 ms, faster than 78.18% of Python3 online submissions for Surrounded Regions.
    Memory Usage: 15.4 MB, less than 49.64% of Python3 online submissions for Surrounded Regions.
    '''
    rows = len(board)
    if not rows:
        return
    cols = len(board[0])
    if not cols:
        return
    safe = set()
    seen = set()
    for row in [0, rows - 1]:
        for col in range(cols):
            extend_safety(board, row, col, safe, seen)
    for col in [0, cols - 1]:
        for row in range(1, rows - 1):
            extend_safety(board, row, col, safe, seen)
    # print("SAFE:", safe)
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if (row, col) not in safe:
                board[row][col] = 'X'
    return board


class Solution2:
    def solve(self, board: List[List[str]]) -> List:
        """
        Do not return anything, modify board in-place instead.
        """
        board = board_capture(board)
        return board


# Main Call
solution = Solution()
board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
board = solution.solve(board)
print(board)

# 124 ms
solution = Solution2()
board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
board = solution.solve(board)
print(board)
