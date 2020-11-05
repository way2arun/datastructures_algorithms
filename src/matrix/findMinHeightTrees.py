"""
Minimum Height Trees
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.



Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
Example 3:

Input: n = 1, edges = []
Output: [0]
Example 4:

Input: n = 2, edges = [[0,1]]
Output: [0,1]


Constraints:

1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.
   Hide Hint #1
How many MHTs can a graph have at most?
"""
from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Solution 1 - 236 ms
        """
        total_node_count = n

        if total_node_count == 1:
            # Quick response for one node tree
            return [0]

        # build adjacency matrix
        adj_matrix = defaultdict(set)

        for src_node, dst_node in edges:
            adj_matrix[src_node].add(dst_node)
            adj_matrix[dst_node].add(src_node)

        # get leaves node whoose degree is 1
        leave_nodes = [node for node in adj_matrix if len(adj_matrix[node]) == 1]

        # keep doing leave nodes removal until total node count is smaller or equal to 2
        while total_node_count > 2:

            total_node_count -= len(leave_nodes)

            leave_nodes_next_round = []

            # leave nodes removal
            for leaf in leave_nodes:

                neighbor = adj_matrix[leaf].pop()
                adj_matrix[neighbor].remove(leaf)

                if len(adj_matrix[neighbor]) == 1:
                    leave_nodes_next_round.append(neighbor)

            leave_nodes = leave_nodes_next_round

        # final leave nodes are root node of minimum height trees
        return leave_nodes
        """
        # Solution 2 - 204 ms
        graph = {i: [] for i in range(n)}

        if n == 1:
            return [0]

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        leaves = []
        for node in graph:
            if len(graph[node]) == 1:
                leaves.append(node)

        while n > 2:
            l = len(leaves)
            n -= l
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf][0]
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves


# Main Call
solution = Solution()
n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
print(solution.findMinHeightTrees(n, edges))
