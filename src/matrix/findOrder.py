"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3394/
Course Schedule II
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
   Hide Hint #1
This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
   Hide Hint #2
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
   Hide Hint #3
Topological sort could also be done via BFS.

"""
import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Solution 1 - 164 ms
        """
        # if there is no prerequisits, return all courses
        if not prerequisites:
            return [i for i in range(numCourses)]
        inDegree = {i: 0 for i in range(numCourses)}
        outDegree = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            outDegree[pre].append(course)
            inDegree[course] += 1

        # BFS
        q = collections.deque([])
        # initializing the q, if num_pre is == 0 than there is no prerequisite to take current course
        for course, num_pre in inDegree.items():
            if num_pre == 0:
                q.append(course)
        ans = []
        while q:
            course = q.popleft()
            ans.append(course)
            numCourses -= 1

            for next_course in outDegree[course]:
                inDegree[next_course] -= 1
                if not inDegree[next_course]:
                    q.append(next_course)

        return ans if numCourses == 0 else []
        """
        # Solution 2 - 80 ms
        """
        e = collections.defaultdict(list)
        d = collections.defaultdict(int)

        for b, a in prerequisites:
            e[a].append(b)
            d[b] += 1

        result = []
        for num in range(numCourses):
            if not d[num]:
                result.append(num)

        for ele in result:
            for end in e[ele]:
                d[end] -= 1
                if not d[end]:
                    result.append(end)

        return result if len(result) == numCourses else []
        """
        # Solution 3 - 88 ms
        how_many_pre_req = [0] * numCourses
        other_course = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            other_course[pre].append(course)
            how_many_pre_req[course] += 1
        dfs = [i for i in range(numCourses) if how_many_pre_req[i] == 0]
        for course in dfs:
            for i in other_course[course]:
                how_many_pre_req[i] -= 1
                if how_many_pre_req[i] == 0:
                    dfs.append(i)
        if len(dfs) == numCourses:
            return dfs
        return []


# Main Call
solution = Solution()
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(solution.findOrder(numCourses, prerequisites))
