"""
Word Search
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3397/
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""
from collections import Counter
from itertools import chain
from typing import List


class Solution:
    # Solution 1 - 360 ms
    def dfs(self, board, word, row, col, len_of_word):
        if len_of_word == len(word):
            return True

        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or word[len_of_word] != board[row][col]:
            return False

        tmp = board[row][col]
        board[row][col] = "#"

        ans = self.dfs(board, word, row + 1, col, len_of_word + 1) or \
              self.dfs(board, word, row, col + 1, len_of_word + 1) or \
              self.dfs(board, word, row - 1, col, len_of_word + 1) or \
              self.dfs(board, word, row, col - 1, len_of_word + 1)

        board[row][col] = tmp

        return ans

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        self.ans = 0
        self.rows = len(board)
        self.cols = len(board[0])
        vis = [[False] * self.cols for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                if self.dfs(board, word, row, col, 0):
                    return True
        return False
        """
        # Solution 2 - 144 ms
        b = board
        w = word
        if not b or not b[0]: return False
        bc = Counter(chain(*b))
        wc = Counter(w)
        if any(c > bc[s] for s, c in wc.items()): return False
        m, n, wl = len(b), len(b[0]), len(w) - 1

        def dfs(d: int, x: int, y: int) -> bool:
            if w[d] != b[y][x]: return False
            if d == wl: return True
            c, b[y][x] = b[y][x], ''
            if x > 0 and dfs(d + 1, x - 1, y):
                return True
            if x < n - 1 and dfs(d + 1, x + 1, y):
                return True
            if y > 0 and dfs(d + 1, x, y - 1):
                return True
            if y < m - 1 and dfs(d + 1, x, y + 1):
                return True
            b[y][x] = c
            return False

        return any(dfs(0, j, i) for i in range(m) for j in range(n) if w[0] == b[i][j])


# Main Call
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
word = "ABCCED"
solution = Solution()
print(solution.exist(board, word))
