"""
Erect the Fence
You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.

You are asked to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed.

Return the coordinates of trees that are exactly located on the fence perimeter.



Example 1:


Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]
Example 2:


Input: points = [[1,2],[2,2],[4,2]]
Output: [[4,2],[2,2],[1,2]]


Constraints:

1 <= points.length <= 3000
points[i].length == 2
0 <= xi, yi <= 100
All the given points are unique.
"""
from functools import cmp_to_key
from typing import List


class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        # Solution 1 - 380 ms
        """
        def quater(p):
            x, y = p
            if x >= 0 and y >= 0: return 2
            if x < 0 and y >= 0: return 1
            if x < 0 and y < 0: return 4
            if x >= 0 and y < 0: return 3

        def compare(p1, p2):
            if quater(p1) == quater(p2):
                t1 = p1[1] * p2[0] - p2[1] * p1[0]
                return 1 - 2 * int((-p1[1], p1[0]) < (-p2[1], p2[0])) if t1 == 0 else 1 if t1 > 0 else -1
            else:
                return 1 if quater(p1) < quater(p2) else -1

        def cross(p1, p2, p3):
            return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

        start = min(points)
        points.pop(points.index(start))
        points = [[x - start[0], y - start[1]] for x, y in points]
        points.sort(key=cmp_to_key(compare))

        ans = [[0, 0]]
        for p in points:
            ans.append(p)
            while len(ans) > 2 and cross(*ans[-3:]) < 0:
                ans.pop(-2)

        return [[x + start[0], y + start[1]] for x, y in ans]
        """
        # Solution 2 - 196 ms
        t0x, t0y = points[0]
        t = t0y
        ts = []
        b = t0y
        bs = []
        l = t0x
        ls = []
        r = t0x
        rs = []
        for x, y in points:
            if y > t:
                t = y
                ts = [(x, y)]
            elif y == t:
                ts.append((x, y))
            if y < b:
                b = y
                bs = [(x, y)]
            elif y == b:
                bs.append((x, y))
            if x < l:
                l = x
                ls = [(x, y)]
            elif x == l:
                ls.append((x, y))
            if x > r:
                r = x
                rs = [(x, y)]
            elif x == r:
                rs.append((x, y))
        ls.sort()
        ts.sort()
        rs.sort(reverse=True)
        bs.sort(reverse=True)
        # print(ls, ts, rs, bs)
        _lt = {}
        _tr = {}
        _rb = {}
        _bl = {}
        for x, y in points:
            if ls[len(ls) - 1][0] < x < ts[0][0] and ls[len(ls) - 1][1] < y < ts[0][1]:
                _lt[x] = max(_lt.get(x, ls[len(ls) - 1][1]), y)
            elif ts[len(ts) - 1][0] < x < rs[0][0] and ts[len(ts) - 1][1] > y > rs[0][1]:
                _tr[y] = max(_tr.get(y, ts[len(ts) - 1][0]), x)
            elif rs[len(rs) - 1][0] > x > bs[0][0] and rs[len(rs) - 1][1] > y > bs[0][1]:
                _rb[x] = min(_rb.get(x, rs[len(rs) - 1][1]), y)
            elif bs[len(bs) - 1][0] > x > ls[0][0] and bs[len(bs) - 1][1] < y < ls[0][1]:
                _bl[y] = min(_bl.get(y, bs[len(bs) - 1][0]), x)
        lt = [(x, _lt[x]) for x in list(_lt.keys())]
        tr = [(_tr[y], y) for y in list(_tr.keys())]
        rb = [(x, _rb[x]) for x in list(_rb.keys())]
        bl = [(_bl[y], y) for y in list(_bl.keys())]
        # print(lt, tr, rb, bl)
        border = set()
        border |= set(ls)
        if len(lt) > 0:
            i, j = ls[len(ls) - 1]
            lt.append(ts[0])
            while len(lt) > 0:
                # print("lt", lt, i, j)
                p = ts[0]
                m = (p[1] - j) / (p[0] - i)
                for x, y in lt:
                    _m = (y - j) / (x - i)
                    if _m > m or (_m == m and x < p[0]):
                        m = _m
                        p = (x, y)
                border.add(p)
                i, j = p
                _lt = []
                for x, y in lt:
                    if x > i and y > j:
                        _lt.append((x, y))
                lt = _lt
        border |= set(ts)
        if len(tr) > 0:
            i, j = ts[len(ts) - 1]
            tr.append(rs[0])
            while len(tr) > 0:
                # print("tr", tr, i, j)
                p = rs[0]
                m = (p[1] - j) / (p[0] - i)
                for x, y in tr:
                    _m = (y - j) / (x - i)
                    if _m > m or (_m == m and y > p[1]):
                        m = _m
                        p = (x, y)
                border.add(p)
                i, j = p
                _tr = []
                for x, y in tr:
                    if x > i and y < j:
                        _tr.append((x, y))
                tr = _tr
        border |= set(rs)
        if len(rb) > 0:
            i, j = rs[len(rs) - 1]
            rb.append(bs[0])
            while len(rb) > 0:
                # print("rb", rb, i, j)
                p = bs[0]
                m = (p[1] - j) / (p[0] - i)
                for x, y in rb:
                    _m = (y - j) / (x - i)
                    if _m > m or (_m == m and x > p[0]):
                        m = _m
                        p = (x, y)
                border.add(p)
                i, j = p
                _rb = []
                for x, y in rb:
                    if x < i and y < j:
                        _rb.append((x, y))
                rb = _rb
        border |= set(bs)
        if len(bl) > 0:
            i, j = bs[len(bs) - 1]
            bl.append(ls[0])
            while len(bl) > 0:
                # print("bl", bl, i, j)
                p = ls[0]
                m = (p[1] - j) / (p[0] - i)
                for x, y in bl:
                    _m = (y - j) / (x - i)
                    if _m > m or (_m == m and y < p[1]):
                        m = _m
                        p = (x, y)
                border.add(p)
                i, j = p
                _bl = []
                for x, y in bl:
                    if x < i and y > j:
                        _bl.append((x, y))
                bl = _bl
        return [[x, y] for x, y in border]


# Main Call
solution = Solution()
points = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
print(solution.outerTrees(points))
