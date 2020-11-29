"""
Jump Game III
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.



Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation:
All possible ways to reach at index 3 with value 0 are:
index 5 -> index 4 -> index 1 -> index 3
index 5 -> index 6 -> index 4 -> index 1 -> index 3
Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true
Explanation:
One possible way to reach at index 3 with value 0 is:
index 0 -> index 4 -> index 1 -> index 3
Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.


Constraints:

1 <= arr.length <= 5 * 10^4
0 <= arr[i] < arr.length
0 <= start < arr.length
   Hide Hint #1
Think of BFS to solve the problem.
   Hide Hint #2
When you reach a position with a value = 0 then return true.

"""

from collections import defaultdict
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # Solution 1 - 216 ms
        """
        visit = defaultdict(bool)
        this_level = [start]
        while this_level:
            next_level = []
            while this_level:
                x = this_level.pop()
                if arr[x] == 0: return True
                visit[x] = 1
                for y in (x - arr[x], x + arr[x]):
                    if 0 <= y <= len(arr) - 1 and not visit[y]:
                        next_level.append(y)
            this_level = next_level
        return False
        """
        # Solution 2 - 192 ms
        def solve(arr, start, n):
            nonlocal flag
            if arr[start] == 0:
                flag = True
                return
            if start in visited:
                return
            if start - arr[start] >= 0:
                visited[start] = True
                solve(arr, start - arr[start], n)
            if start + arr[start] < n:
                visited[start] = True
                solve(arr, start + arr[start], n)

        visited = {}
        flag = False
        solve(arr, start, len(arr))
        return flag


# Main Call
solution = Solution()
arr = [3,0,2,1,2]
start = 2
print(solution.canReach(arr, start))

