"""
Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Solution 1 - using Hash Set -
        """
        N = 9
        rowSet = [set() for _ in range(N)]
        colSet = [set() for _ in range(N)]
        squareSet = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                if board[r][c] == ".": continue
                sr, sc = r // 3, c // 3
                sPos = sr * 3 + sc
                if board[r][c] in rowSet[r] or board[r][c] in colSet[c] or board[r][c] in squareSet[sPos]:
                    return False
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                squareSet[sPos].add(board[r][c])

        return True
        """
        # Solution 2 - Bit Masking - 100 ms
        """
        def getBit(x, k):
            return (x >> k) & 1

        N = 9
        rows, cols, squares = [0] * N, [0] * N, [0] * N
        for r in range(N):
            for c in range(N):
                if board[r][c] == ".": continue
                val = int(board[r][c])
                sr, sc = r // 3, c // 3
                sPos = sr * 3 + sc
                if getBit(rows[r], val) or getBit(cols[c], val) or getBit(squares[sPos], val):
                    return False
                rows[r] |= 1 << val
                cols[c] |= 1 << val
                squares[sPos] |= 1 << val
        return True
        """
        # Solution 3 - 72 ms
        rowSets = [set() for _ in range(9)]
        columnSets = [set() for _ in range(9)]
        boxSets = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in columnSets[i]:
                        return False
                    else:
                        columnSets[i].add(board[i][j])

                    if board[i][j] in rowSets[j]:
                        return False
                    else:
                        rowSets[j].add(board[i][j])

                    if board[i][j] in boxSets[i // 3][j // 3]:
                        return False
                    else:
                        boxSets[i // 3][j // 3].add(board[i][j])
        return True


# Main Call
solution = Solution()
board =[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(solution.isValidSudoku(board))