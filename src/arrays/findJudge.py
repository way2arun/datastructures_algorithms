"""
Leet Code Challenge
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.



Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3


Note:

1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N

https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3325/
"""
from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        """
        # Solution 1,
        in_degree = [0] * (N + 1)
        out_degree = [0] * (N + 1)
        for a,b in trust:
            out_degree[a] += 1
            in_degree[b] += 1
        for i in range(1, N + 1):
            if out_degree[i] == 0 and in_degree[i] == N - 1:
                return i
        return -1
        """
        """
        # Solution 2 - 764 ms
        # degree = [0 for _ in range(N + 1)]
        degree = [0] * (N + 1)
        for a, b in trust:
            degree[a] -= 1
            degree[b] += 1
        for i, num in enumerate(degree[1:], 1):
            if num == N - 1:
                return i
        return -1
        """
        # Solution 3 - 734 ms
        trusters = {x[0] for x in trust}
        print(trusters)
        trusted_by = 0
        candidate = -1
        for i in range(1, N + 1):
            if i not in trusters:
                candidate = i

        for a, b in trust:
            if b == candidate:
                trusted_by += 1

        if trusted_by != N - 1:
            candidate = -1

        return candidate


# Main Call
solution = Solution()
N = 2
trust = [[1, 2]]
print(solution.findJudge(N, trust))
N = 3
trust = [[1, 3], [2, 3]]
print(solution.findJudge(N, trust))
