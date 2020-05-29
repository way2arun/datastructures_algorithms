"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
   Hide Hint #1
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
   Hide Hint #2
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
   Hide Hint #3
Topological sort could also be done via BFS.
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3344/
"""
import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Solution 1 - 96 ms
        """
        graph = dict()
        for i in range(numCourses):
            graph[i] = []

        visited = [False] * numCourses
        temp_stack = [False] * numCourses

        for v1, v2 in prerequisites:
            graph[v1].append(v2)

        def detectCycle(v):
            visited[v] = True
            temp_stack[v] = True
            for adj in graph[v]:
                if not visited[adj]:
                    if detectCycle(adj):
                        return True
                else:
                    if temp_stack[adj]:
                        return True
            temp_stack[v] = False
            return False

        for node in range(numCourses):
            if not visited[node]:
                if detectCycle(node):
                    return False
        return True
        """
        # Solution 2 - 76 ms
        graph = collections.defaultdict(list)
        deg = [0] * numCourses

        for i, j in prerequisites:
            graph[j].append(i)
            deg[i] += 1

        queue = collections.deque([i for i, v in enumerate(deg) if v == 0])

        while queue:
            cur_v = queue.popleft()
            for neighbor in graph[cur_v]:
                deg[neighbor] -= 1
                if deg[neighbor] == 0:
                    queue.append(neighbor)

        return not sum(deg)


# Main Call
solution = Solution()
numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print(solution.canFinish(numCourses, prerequisites))
