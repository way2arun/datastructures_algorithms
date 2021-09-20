"""
Find Winner on a Tic Tac Toe Game
Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places "O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.



Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"
Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: "B" wins.
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO "
"   "    "   "    "   "    "   "    "   "    "O  "
Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
"XXO"
"OOX"
"XOX"
Example 4:

Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
"X  "
" O "
"   "


Constraints:

1 <= moves.length <= 9
moves[i].length == 2
0 <= moves[i][j] <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.
   Hide Hint #1
It's straightforward to check if A or B won or not, check for each row/column/diag if all the three are the same.
   Hide Hint #2
Then if no one wins, the game is a draw iff the board is full, i.e. moves.length = 9 otherwise is pending.
"""
from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # Solution - 1 - 46 ms
        """
        rows, cols, diag, anti = [0] * 3, [0] * 3, 0, 0

        for turn, (x, y) in enumerate(moves):
            player = (turn % 2) * 2 - 1
            rows[x] += player
            cols[y] += player
            if x == y: diag += player
            if x + y == 2: anti += player

            if any(abs(cand) == 3 for cand in [rows[x], cols[y], diag, anti]):
                return "B" if player == 1 else "A"

        return "Draw" if len(moves) == 9 else "Pending"
        """
        # Solution 2 - 20 ms
        board = [[' ' for b in range(3)] for a in range(3)]

        player = 0

        for move in moves:
            board[move[0]][move[1]] = player
            player = (player + 1) % 2

        for row in range(3):
            lastPlayer = board[row][0]
            if lastPlayer == ' ':
                continue
            same = True
            for col in range(1, 3):
                if board[row][col] != lastPlayer:
                    same = False
                    break
            if same:
                return chr(ord('A') + lastPlayer)

        for row in range(3):
            lastPlayer = board[0][row]
            if lastPlayer == ' ':
                continue
            same = True
            for col in range(1, 3):
                if board[col][row] != lastPlayer:
                    same = False
                    break
            if same:
                return chr(ord('A') + lastPlayer)

        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return chr(ord('A') + board[1][1])

        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return chr(ord('A') + board[1][1])

        if len(moves) < 9:
            return 'Pending'

        return 'Draw'


# Main Call
moves = [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
solution = Solution()
print(solution.tictactoe(moves))