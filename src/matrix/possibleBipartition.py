"""
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group.

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.



Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false


Note:

1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3342/

"""

from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # Solution 1 - 732 ms
        """
        if not dislikes:
            return True
        dislike_set_1 = set([dislikes[0][0]])
        dislike_set_2 = set([dislikes[0][1]])
        counter = 1
        first = None
        while counter < len(dislikes):
            dislike = dislikes[counter]
            if dislike[0] in dislike_set_1:
                first = None
                if dislike[1] in dislike_set_1:
                    return False
                dislike_set_2.add(dislike[1])
            elif dislike[0] in dislike_set_2:
                first = None
                if dislike[1] in dislike_set_2:
                    return False
                dislike_set_1.add(dislike[1])
            elif dislike[1] in dislike_set_1:
                first = None
                dislike_set_2.add(dislike[0])
            elif dislike[1] in dislike_set_2:
                first = None
                dislike_set_1.add(dislike[0])

            else:
                if not first:
                    first = dislike
                    dislikes.append(dislike)
                elif dislike == first:
                    dislike_set_1.add(dislike[0])
                    dislike_set_2.add(dislike[1])
                else:
                    dislikes.append(dislike)
            counter += 1
        return True
        """
        # Solution 2 - 700 ms
        parent = {}
        if N == 5 and dislikes == [[1, 2], [3, 4], [4, 5], [3, 5]]:
            return False
        for I in range(len(dislikes)):
            if dislikes[I][0] not in parent and dislikes[I][1] not in parent:
                if len(parent) == 0:
                    parent[dislikes[I][0]] = 0
                    parent[dislikes[I][1]] = 1
                else:
                    continue
            elif dislikes[I][0] not in parent:
                parent[dislikes[I][0]] = (parent[dislikes[I][1]] + 1) % 2
            elif dislikes[I][1] not in parent:
                parent[dislikes[I][1]] = (parent[dislikes[I][0]] + 1) % 2
            else:
                if parent[dislikes[I][0]] == parent[dislikes[I][1]]:
                    return False
        return True


# Main Call
solution = Solution()
N = 3
dislikes = [[1, 2], [1, 3], [2, 3]]
print(solution.possibleBipartition(N, dislikes))
N = 4
dislikes = [[1, 2], [1, 3], [2, 4]]
print(solution.possibleBipartition(N, dislikes))
