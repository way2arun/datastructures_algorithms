"""
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3374/
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""
import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Solution 1 - 80 ms
        """
        self.graph = collections.defaultdict(list)
        for x, y in tickets:
            self.graph[x].append(y)
            self.graph[x].sort()
        self.res = []
        self.dfs("JFK")
        return self.res
        """
        # Solution 2 60 ms
        #### By Euler path using DFS
        self.graph = collections.defaultdict(list)
        for frm, to in tickets:
            self.graph[frm].append(to)

        for k, v in self.graph.items():
            v.sort()

        self.ans = []
        self.DFS("JFK")
        return self.ans[::-1]

    def DFS(self, src):
        dest = self.graph[src]
        while dest:
            nextD = dest.pop(0)
            self.DFS(nextD)
        self.ans.append(src)


    def dfs(self, city):
        while len(self.graph[city]) > 0:
            self.dfs(self.graph[city].pop(0))
        self.res.insert(0, city)  # last airport


# Main Call
solution = Solution()
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(solution.findItinerary(tickets))
tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
print(solution.findItinerary(tickets))
