"""
All Paths From Source to Target
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3400/
Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []]
Output: [[0,1,3],[0,2,3]]
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Note:

The number of nodes in the graph will be in the range [2, 15].
You can print different paths in any order, but you should keep the order of nodes inside one path.
"""
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Solution 1 - 112 ms
        """
        self.graph = graph
        self.answer = []
        self.dfs(graph[0], [0])
        return self.answer
        """
        # Solution 2 - 88 ms
        q = [[0]]
        res = []
        while len(q) > 0:
            current = q.pop(0)
            if current[-1] == len(graph) - 1:
                res.append(current)
                continue
            for neighbor in graph[current[-1]]:
                q.append(current + [neighbor])

        return res

    def dfs(self, nodes, prev_nodes):
        for node_index in range(len(nodes)):
            node = nodes[node_index]
            if node == len(self.graph) - 1:
                self.answer.append(prev_nodes + [node])
            self.dfs(self.graph[node], prev_nodes + [node])


# Main Call
solution = Solution()
graph = [[1, 2], [3], [3], []]
print(solution.allPathsSourceTarget(graph))
