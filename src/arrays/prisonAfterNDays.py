"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3379/
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)



Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation:
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]


Note:

cells.length == 8
cells[i] is in {0, 1}
1 <= N <= 10^9
"""
from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        # Solution 1 - 60 ms
        """
        if len(cells) < 3:
            return cells

        if N % 14 == 0:
            n = 14
        else:
            n = N % 14
        # n = 14 if N % 14 == 0 else N % 14
        for i in range(n):
            next_state = [0 for _ in range(8)]
            for j in range(8):
                if j - 1 < 0 or j + 1 > 7 or cells[j - 1] != cells[j + 1]:
                    next_state[j] = 0
                else:
                    next_state[j] = 1
            cells = next_state
        return cells
        """
        # Solution 2 - 24 ms

        if not N:
            return cells

        while N:
            state = cells.copy()
            for i in range(len(cells)):
                if i == 0 or i == len(state) - 1:
                    cells[i] = 0
                else:
                    if state[i - 1] == state[i + 1]:
                        cells[i] = 1
                    else:
                        cells[i] = 0
            N = (N - 1) % 14
        return cells
        """
        # Solution 3 :
        first = True
        while (N):
            tempList = [0] * 8
            if first:
                tempList[7] = 0
                tempList[0] = 0
                first = False
            for i in range(1, 7):
                if (cells[i - 1] and cells[i + 1]) or (not (cells[i - 1] or cells[i + 1])):
                    tempList[i] = 1

            cells = tempList
            N -= 1

        return cells
         """


# Main Call
solution = Solution()
cells = [0, 1, 0, 1, 1, 0, 0, 1]
N = 7
print(solution.prisonAfterNDays(cells, N))
