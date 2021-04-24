"""
Critical Connections in a Network
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.



Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.


Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
   Hide Hint #1
Use Tarjan's algorithm.

"""
from collections import defaultdict
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Solution 1 - 2476 ms
        """
        used, tin, fup = [0] * n, [-1] * n, [-1] * n
        self.timer, ans = 0, []
        graph = defaultdict(list)

        def dfs(node, par=-1):
            used[node] = 1
            tin[node] = fup[node] = self.timer + 1
            self.timer += 1
            for child in graph[node]:
                if child == par: continue
                if used[child] == 1:
                    fup[node] = min(fup[node], tin[child])
                else:
                    dfs(child, node)
                    fup[node] = min(fup[node], fup[child])
                    if fup[child] > tin[node]: ans.append([node, child])

        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)

        for i in range(n):
            if not used[i]: dfs(i)

        return ans
        """
        # Solution 2 - 1928 ms
        graph = [[] for i in range(n)]
        depth = [-1] * n
        res = []
        for p, q in connections:
            graph[p].append(q)
            graph[q].append(p)

        def dfs(prev, cur, dep):  # from, to, depth
            dep2 = depth[cur] = dep
            for nbr in graph[cur]:
                if nbr == prev: continue
                dep3 = depth[nbr] if depth[nbr] >= 0 else dfs(cur, nbr, dep + 1)
                if dep3 > dep:
                    res.append((cur, nbr))
                elif dep2 > dep3:
                    dep2 = dep3
            depth[cur] = dep2
            return dep2

        dfs(0, 0, 0)
        return res


# Main Call
n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]

solution = Solution()
print(solution.criticalConnections(n, connections))