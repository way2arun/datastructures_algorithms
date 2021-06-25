"""
Redundant Connection
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.



Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]


Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Solution 1 - 56 ms
        """
        par = [i for i in range(len(edges) + 1)]

        def find(x: int) -> int:
            if x != par[x]: par[x] = find(par[x])
            return par[x]

        def union(x: int, y: int) -> None:
            par[find(y)] = find(x)

        for a, b in edges:
            if find(a) == find(b):
                return [a, b]
            else:
                union(a, b)
        """
        # Solution 2 - 36 ms
        # union find
        parents, ranks = {}, {}

        def findParent(n, parents):
            while parents[n] != n:
                parents[n] = parents[parents[n]]
                n = parents[n]
            return n

        for edge in edges:
            u = edge[0]
            v = edge[1]

            if u not in parents:
                parents[u] = u
                ranks[u] = 1
            if v not in parents:
                parents[v] = v
                ranks[v] = 1

            pu = findParent(u, parents)
            pv = findParent(v, parents)

            if pu == pv:
                return edge

            if ranks[pu] < ranks[pv]:
                parents[pu] = pv
                ranks[pv] += ranks[pu]
            else:
                parents[pv] = pu
                ranks[pu] += ranks[pv]


# Main Call
edges = [[1, 2], [1, 3], [2, 3]]
solution = Solution()
print(solution.findRedundantConnection(edges))