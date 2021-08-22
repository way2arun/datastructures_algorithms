"""
Rectangle Area II
We are given a list of (axis-aligned) rectangles. Each rectangle[i] = [xi1, yi1, xi2, yi2] , where (xi1, yi1) are the coordinates of the bottom-left corner, and (xi2, yi2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane. Since the answer may be too large, return it modulo 109 + 7.



Example 1:


Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
Example 2:

Input: rectangles = [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 1018 modulo (109 + 7), which is (109)2 = (-7)2 = 49.


Constraints:

1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= rectangles[i][j] <= 109
The total area covered by all rectangles will never exceed 263 - 1 and thus will fit in a 64-bit signed integer.
"""
from typing import List, Tuple


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # Solution 1 - 72 ms
        """
        ys = sorted(set([y for x1, y1, x2, y2 in rectangles for y in [y1, y2]]))
        y_i = {v: i for i, v in enumerate(ys)}
        count = [0] * len(y_i)

        sides_lft = [(x1, -1, y1, y2) for x1, y1, x2, y2 in rectangles]
        sides_rgh = [(x2, 1, y1, y2) for x1, y1, x2, y2 in rectangles]
        sides = sorted(sides_lft + sides_rgh)

        cur_x = cur_y_sum = area = 0
        for x, op_cl, y1, y2 in sides:
            area += (x - cur_x) * cur_y_sum
            cur_x = x
            for i in range(y_i[y1], y_i[y2]):
                count[i] += op_cl
            cur_y_sum = sum(y2 - y1 if c else 0 for y1, y2, c in zip(ys, ys[1:], count))
        return area % (10 ** 9 + 7)
        """
        # Solution 2 - 36 ms
        events = []

        for x1, y1, x2, y2 in rectangles:
            events.append((x1, y1, y2, 's'))
            events.append((x2, y1, y2, 'e'))

        events.sort(key=lambda x: (x[0], -x[1]))

        ans = 0
        prevX = 0
        yPairs = []

        def getHeight(yPairs: List[Tuple[int, int]]) -> int:
            height = 0
            prevBottom = 0

            for y1, y2 in yPairs:
                bottom = max(y1, prevBottom)
                if y2 > bottom:
                    height += y2 - bottom
                    prevBottom = y2

            return height

        for currX, y1, y2, type in events:
            if currX > prevX:
                width = currX - prevX
                ans += width * getHeight(yPairs)
            if type == 's':
                yPairs.append((y1, y2))
                yPairs.sort()
            else:  # type == 'e'
                yPairs.remove((y1, y2))
            prevX = currX

        return ans % (10 ** 9 + 7)

# Main Call
solution = Solution()
rectangles = [[0,0,1000000000,1000000000]]
print(solution.rectangleArea(rectangles))