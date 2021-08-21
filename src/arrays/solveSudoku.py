"""
Sudoku Solver
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.



Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:




Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Solution 1 - 190 ms
        """
        def getBit(x, k):
            return (x >> k) & 1

        def setBit(x, k):
            return (1 << k) | x

        def clearBit(x, k):
            return ~(1 << k) & x

        rows, cols, boxes = [0] * 9, [0] * 9, [0] * 9
        emptyCells = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    emptyCells.append([r, c])
                else:
                    val = int(board[r][c])
                    boxPos = (r // 3) * 3 + (c // 3)
                    rows[r] = setBit(rows[r], val)
                    cols[c] = setBit(cols[c], val)
                    boxes[boxPos] = setBit(boxes[boxPos], val)

        def backtracking(i):
            if i == len(emptyCells): return True  # Check if we filled all empty cells?

            r, c = emptyCells[i]
            boxPos = (r // 3) * 3 + c // 3
            for val in range(1, 10):
                if getBit(rows[r], val) or getBit(cols[c], val) or getBit(boxes[boxPos],
                                                                          val): continue  # skip if that value is existed!
                board[r][c] = str(val)
                rows[r] = setBit(rows[r], val)
                cols[c] = setBit(cols[c], val)
                boxes[boxPos] = setBit(boxes[boxPos], val)
                if backtracking(i + 1): return True
                rows[r] = clearBit(rows[r], val)
                cols[c] = clearBit(cols[c], val)
                boxes[boxPos] = clearBit(boxes[boxPos], val)

            return False

        backtracking(0)
        print(board)
        """
        # Solution 2 - 28 ms
        def returnMinItem(possible_values):
            return min(possible_values.items(), key=lambda x: len(x[1]))[0]
            i, j = next(iter(possible_values))
            min_value_len = len(possible_values[i, j])
            for k, v in possible_values.items():
                if len(v) == 1:
                    return k
                if len(v) < min_value_len:
                    (i, j), min_value_len = k, len(v)
            return i, j

        def placeNextDigit(board, possible_values):
            i, j = returnMinItem(possible_values)
            numbers = possible_values.pop((i, j))

            for n in numbers:
                board[i][j] = n
                if not possible_values:
                    return

                discarded = []

                for (i2, j2), v in possible_values.items():
                    if (i == i2 or j == j2 or (i // 3, j // 3) == (i2 // 3, j2 // 3)) and n in v:
                        if len(v) == 1:
                            for v in discarded:
                                v.add(n)
                            possible_values[i, j] = numbers
                            return
                        v.discard(n)
                        discarded.append(v)

                placeNextDigit(board, possible_values)

                if not possible_values:
                    return

                for v in discarded:
                    v.add(n)

            possible_values[i, j] = numbers

        possible_values = {(i, j): {"1", "2", "3", "4", "5", "6", "7", "8", "9"} \
                                   - {board[i][k] for k in range(9)} \
                                   - {board[k][j] for k in range(9)} \
                                   - {board[3 * (i // 3) + di][3 * (j // 3) + dj]
                                      for di in range(3) for dj in range(3)}
                           for i in range(9) for j in range(9)
                           if board[i][j] == '.'}

        i, j = returnMinItem(possible_values)
        while possible_values and len(possible_values[i, j]) == 1:
            for n in possible_values.pop((i, j)):
                board[i][j] = n
                for (i2, j2), v in possible_values.items():
                    if (i == i2 or j == j2 or (i // 3, j // 3) == (i2 // 3, j2 // 3)) and n in v:
                        v.discard(n)
            if possible_values:
                i, j = returnMinItem(possible_values)
        if possible_values:
            placeNextDigit(board, possible_values)
        print(board)


# Main Call
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
solution = Solution()
solution.solveSudoku(board)
