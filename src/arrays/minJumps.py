"""
Jump Game IV
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.



Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You don't need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
Example 4:

Input: arr = [6,1,9]
Output: 2
Example 5:

Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
Output: 3


Constraints:

1 <= arr.length <= 5 * 10^4
-10^8 <= arr[i] <= 10^8
   Hide Hint #1
Build a graph of n nodes where nodes are the indices of the array and edges for node i are nodes i+1, i-1, j where arr[i] == arr[j].
   Hide Hint #2
Start bfs from node 0 and keep distance, answer is the distance when you reach onode n-1.

"""
from collections import defaultdict
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # Solution 1 - 1128 ms
        """
        n = len(arr)
        map = defaultdict(list)
        visited = [False] * n
        jump = 0
        if len(arr) == 1:
            return jump
        for i in range(n):
            map[arr[i]].append(i)
        queue = [0]

        while queue:
            l = len(queue)

            for i in range(l):
                index = queue.pop(0)
                if index == n - 1:
                    return jump
                if 0 <= index - 1 < n and not visited[index - 1]:
                    visited[index - 1] = True
                    queue.append(index - 1)
                if 0 <= index + 1 < n and not visited[index + 1]:
                    visited[index + 1] = True
                    queue.append(index + 1)
                if 0 <= index < n:
                    for j in map[arr[index]]:
                        if not visited[j]:
                            visited[j] = True
                            queue.append(j)
                    del map[arr[index]]
            jump += 1

        return jump
        """
        # Solution 2 - 384 ms
        """
            https://leetcode.com/problems/jump-game-iv/discuss/853365/No-DP-Faster-Bidirectional-BFS-with-explanation
        """
        length = len(arr)
        if len(set(arr)) == length:
            return length - 1
        if arr[0] == arr[-1]:
            return 1
        _map = defaultdict(list)  # connection map
        for i, val in enumerate(arr):
            _map[val].append(i)
        step, curs, other = 0, {0}, {length - 1}
        while curs:
            # choose smaller side
            if len(curs) > len(other):
                curs, other = other, curs
            step, thisLevel = step + 1, set()
            for i in curs:
                # add backward and forward moves into current jumping space
                # make the same operation accomplished in only one loop
                for j in (i + 1, i - 1):
                    if 0 < j < length:
                        _map[arr[i]].append(j)
                for j in _map[arr[i]]:
                    if j in other:
                        return step
                    else:
                        thisLevel.add(j)
                del _map[arr[i]]
            # update current side for next round
            curs = thisLevel


# Main Call
arr = [6, 1, 9]
solution = Solution()
print(solution.minJumps(arr))
