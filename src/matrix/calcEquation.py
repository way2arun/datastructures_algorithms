"""
Evaluate Division
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3474/
You are given equations in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating-point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.



Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]


Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= equations[i][0], equations[i][1] <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= queries[i][0], queries[i][1] <= 5
equations[i][0], equations[i][1], queries[i][0], queries[i][1] consist of lower case English letters and digits.
   Hide Hint #1
Do you recognize this as a graph problem?
"""

from collections import defaultdict, deque
from itertools import chain
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Solution 1 - 32 ms
        """
        varbs = set(chain(*equations))
        result, it = [], 0
        self.edges = defaultdict(list)
        for it, [i, j] in enumerate(equations):
            self.edges[i].append([j, values[it]])
            self.edges[j].append([i, 1 / values[it]])

        self.w = defaultdict(list)
        for var in varbs: self.w[var] = [-1, -1]

        for key in varbs:
            if self.w[key][0] == -1:
                self.dfs(key, it, 1)
                it += 1

        for a, b in queries:
            if a not in varbs or b not in varbs or self.w[a][0] != self.w[b][0]:
                result.append(-1.0)
            else:
                result.append(self.w[a][1] / self.w[b][1])

        return result
        """
        # Solution 2 - 8 ms
        result = [-1.0] * len(queries)
        # construct the graph
        graph = defaultdict(dict)
        for ind, (i, j) in enumerate(equations):
            graph[i][j] = values[ind]
            graph[j][i] = 1 / values[ind]

        def helper(x, y):
            # find path from x to y, given a graph
            queue = [(x, 1)]
            visited = set()
            while queue:
                node, val = queue.pop()
                if node in visited:
                    continue
                visited.add(node)
                neighbors = graph[node]  # a dict {node:value}
                if y in neighbors:
                    return val * neighbors[y]
                else:
                    for n in neighbors:
                        queue.append((n, val * neighbors[n]))
                # queue = next_queue
            return -1.0

        for ind, (x, y) in enumerate(queries):
            if x not in graph or y not in graph:
                continue
            elif x == y and x in graph[x]:
                result[ind] = 1.0
            elif y in graph[x]:
                result[ind] = graph[x][y]
            else:
                # find the transition path there maybe multiple paths, but since the assumption is there is no
                # contradiction, it is safe to pick random one depth first search, search neighbors and neighbors'
                # neighbors until get the target

                result[ind] = helper(x, y)
        return result

    def dfs(self, start, comp, w):
        self.w[start] = [comp, w]
        for j, weight in self.edges[start]:
            if self.w[j][0] == -1:
                self.dfs(j, comp, w / weight)

        # Solution 3 - 12 ms
        """
        if len(equations) == 0:
            return [-1.0 for i in range(len(queries))]
        if len(queries) == 0:
            return []

        self.dict1 = defaultdict(dict)

        for i, equation in enumerate(equations):
            self.dict1[equation[0]][equation[1]] = values[i]
            self.dict1[equation[1]][equation[0]] = 1 / values[i]
        self.result = []
        for query in queries:
            self.visited = set()
            temp = self.bfs(query[0], query[1], 1)
            self.result.append(temp)

        return self.result
        """

    def bfs(self, start, end, val):
        q = deque()
        q.append((start, val))
        self.visited.add(start)
        if end not in self.dict1:
            return -1.0
        while q:
            s, val = q.popleft()
            if s not in self.dict1:
                return -1.0
            if s == end:
                return val
            for news in self.dict1[s]:
                if news not in self.visited:
                    self.visited.add(news)
                    q.append((news, val * self.dict1[s][news]))
        return -1.0


# Main Call
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

solution = Solution()
print(solution.calcEquation(equations, values, queries))
