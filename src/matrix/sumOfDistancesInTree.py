"""
 Sum of Distances in Tree
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.



Example 1:


Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.
Example 2:


Input: n = 1, edges = []
Output: [0]
Example 3:


Input: n = 2, edges = [[1,0]]
Output: [1,1]


Constraints:

1 <= n <= 3 * 104
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
The given input represents a valid tree.
"""
from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Solution 1 - 1008 ms
        """
        # build a adjacency list representation
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # init distance array, and count of nodes in the subtree
        dist = [0 for _ in range(n)]
        count = [float('inf') for _ in range(n)]

        # next first pass of the dfs, should start from a node
        # it gets the answer of distances from that.
        # also, the same dfs should calculate the size of the subtree in itself.
        def first_dfs():
            visited = set()
            # choose start
            s = 0

            def dfs(v, distance_from_source=0):
                # add to visited
                visited.add(v)
                dist[s] += distance_from_source
                # check the neighbours
                # initialize a count
                counter = 1  # since a node contains itself by default
                for n in g[v]:
                    if n not in visited:
                        # increment count
                        counter += dfs(n, distance_from_source + 1)
                # set the counter for the current node
                count[v] = counter
                return counter

            # invoke dfs from starting vertex (randomly chosen)
            dfs(s)

        first_dfs()

        # now lemme worry sbout second dfs
        def second_dfs():
            s = 0
            visited = set()

            def dfs(v, parent=None):
                visited.add(v)
                if parent is not None:
                    # if parent exists, then take that answer
                    dist[v] = dist[parent] - count[v] + (n - count[v])

                # else continue normal dfs
                for neigh in g[v]:
                    if neigh not in visited:
                        dfs(neigh, v)

            dfs(s)

        second_dfs()
        return dist  #build a adjacency list representation
        g = [[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        #init distance array, and count of nodes in the subtree
        dist = [0 for _ in range(n)]
        count = [float('inf') for _ in range(N)]

        #next first pass of the dfs, should start from a node
        #it gets the answer of distances from that.
        #also, the same dfs should calculate the size of the subtree in itself.
        def first_dfs():
            visited = set()
            #choose start
            s = 0
            def dfs(v,distance_from_source = 0):
                #add to visited
                visited.add(v)
                dist[s]+=distance_from_source
                #check the neighbours
                #initialize a count
                counter = 1 #since a node contains itself by default
                for n in g[v]:
                    if n not in visited:
                        #increment count
                        counter+=dfs(n,distance_from_source+1)
                #set the counter for the current node
                count[v]= counter
                return counter
            #invoke dfs from starting vertex (randomly chosen)
            dfs(s)
        first_dfs()

        #now lemme worry sbout second dfs
        def second_dfs():
            s = 0
            visited = set()
            def dfs(v,parent = None):
                visited.add(v)
                if parent is not None:
                    #if parent exists, then take that answer
                    dist[v] = dist[parent]-count[v] + (N-count[v])

                #else continue normal dfs
                for neigh in g[v]:
                    if neigh not in visited:
                        dfs(neigh,v)
            dfs(s)
        second_dfs()
        return dist
        """
        # Solution 2 - 300 ms
        graph = [[] for i in range(n)]
        for edge in edges:
            start, end = edge
            graph[start].append(end)
            graph[end].append(start)

        count = [1 for i in range(n)]
        distance = [0 for i in range(n)]
        self.dfs(graph, 0, None, count, distance)
        self.fillUpRest(graph, 0, None, count, distance)
        return distance

    def dfs(self, graph, current, parent, count, distance):
        for child in graph[current]:
            if child == parent:
                continue
            self.dfs(graph, child, current, count, distance)
            count[current] += count[child]
            distance[current] += distance[child] + count[child]
        return

    def fillUpRest(self, graph, current, parent, count, distance):
        for child in graph[current]:
            if child == parent:
                continue
            distance[child] = distance[current] - count[child] + len(graph) - count[child]
            self.fillUpRest(graph, child, current, count, distance)
        return


# Main Call
n = 6
edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
solution = Solution()
print(solution.sumOfDistancesInTree(n, edges))