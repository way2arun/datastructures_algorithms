"""
Is Graph Bipartite?
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split its set of nodes into two independent subsets A and B, such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists. Each node is an integer between 0 and graph.length - 1. There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.



Example 1:


Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can divide the vertices into two groups: {0, 2} and {1, 3}.

Example 2:


Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: We cannot find a way to divide the set of nodes into two independent subsets.


Constraints:

1 <= graph.length <= 100
0 <= graph[i].length < 100
0 <= graph[i][j] <= graph.length - 1
graph[i][j] != i
All the values of graph[i] are unique.
The graph is guaranteed to be undirected.
"""
from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Solution 1 - 168 ms
        """
        def dfs(start):
            if self.loop: return  # early stop if we found odd cycle

            for neib in graph[start]:
                if dist[neib] >= 0 and dist[neib] == dist[start]:
                    self.loop = True
                elif dist[neib] < 0:
                    dist[neib] = dist[start] ^ 1
                    dfs(neib)

        n = len(graph)
        self.loop, dist = False, [-1] * n

        for i in range(n):
            if self.loop: return False  # early stop if we found odd cycle
            if dist[i] == -1:
                dist[i] = 0
                dfs(i)

        return True
        """
        # Solution 2 - 148 ms
        coloring = {}
        for i in range(len(graph)):
            q = deque([])
            if i not in coloring:
                coloring[i] = 1
                q.append(i)
                while q:
                    curr = q.popleft()
                    for neighbor in graph[curr]:
                        if neighbor not in coloring:
                            coloring[neighbor] = -1 * coloring[curr]
                            q.append(neighbor)
                        elif coloring[neighbor] == coloring[curr]:
                            return False

        return True


# Main Call
graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
solution  = Solution()
print(solution.isBipartite(graph))
