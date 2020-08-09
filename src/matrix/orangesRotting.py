"""
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3418/
Rotting Oranges
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.



Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Solution 1 - 48 ms
        """
        data = []
        fresh_count = 0
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    data.append([0, [i, j]])
                elif grid[i][j] == 1:
                    fresh_count += 1
        # print(data)

        ans = 0
        while data:
            # print(data)
            curr = data.pop(0)
            loc = curr[1]

            # left check
            if loc[1] > 0:
                if grid[loc[0]][loc[1] - 1] == 1:
                    data.append([curr[0] + 1, [loc[0], loc[1] - 1]])
                    ans = curr[0] + 1
                    grid[loc[0]][loc[1] - 1] = 2
                    fresh_count -= 1

            # right check
            if loc[1] < (c - 1):
                if grid[loc[0]][loc[1] + 1] == 1:
                    data.append([curr[0] + 1, [loc[0], loc[1] + 1]])
                    ans = curr[0] + 1
                    grid[loc[0]][loc[1] + 1] = 2
                    fresh_count -= 1

            # up check
            if loc[0] > 0:
                if grid[loc[0] - 1][loc[1]] == 1:
                    data.append([curr[0] + 1, [loc[0] - 1, loc[1]]])
                    ans = curr[0] + 1
                    grid[loc[0] - 1][loc[1]] = 2
                    fresh_count -= 1

            # down check
            if loc[0] < (r - 1):
                if grid[loc[0] + 1][loc[1]] == 1:
                    data.append([curr[0] + 1, [loc[0] + 1, loc[1]]])
                    ans = curr[0] + 1
                    grid[loc[0] + 1][loc[1]] = 2
                    fresh_count -= 1

        if fresh_count > 0:
            return -1
        else:
            return ans
        """
        # Solution 2 - 28 ms
        minutes = 0
        toVisit = []
        nextMinuteVisit = []
        freshOranges = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 2):
                    toVisit.append((i, j))
                elif (grid[i][j] == 1):
                    freshOranges += 1

        # BFS from every rotten orange
        # If at the end there exists a fresh orange we return.
        while len(toVisit) > 0:
            currentPoint = toVisit.pop(0)

            x = currentPoint[0]
            y = currentPoint[1]

            if x + 1 < len(grid) and grid[x + 1][y] == 1:
                nextMinuteVisit.append((x + 1, y))
                grid[x + 1][y] = 2
                freshOranges -= 1
            if x - 1 >= 0 and grid[x - 1][y] == 1:
                nextMinuteVisit.append((x - 1, y))
                grid[x - 1][y] = 2
                freshOranges -= 1
            if y + 1 < len(grid[0]) and grid[x][y + 1] == 1:
                nextMinuteVisit.append((x, y + 1))
                grid[x][y + 1] = 2
                freshOranges -= 1
            if y - 1 >= 0 and grid[x][y - 1] == 1:
                nextMinuteVisit.append((x, y - 1))
                grid[x][y - 1] = 2
                freshOranges -= 1

            if len(toVisit) == 0 and len(nextMinuteVisit) > 0:
                toVisit = nextMinuteVisit
                nextMinuteVisit = []
                minutes += 1

        # Check if any oranges are still fresh
        if freshOranges > 0:
            return -1

        return minutes

# Main Call
grid =  [[2,1,1],[1,1,0],[0,1,1]]
solution = Solution()
print(solution.orangesRotting(grid))
