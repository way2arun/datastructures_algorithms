"""
Keys and Rooms
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room.

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0).

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
Example 2:

Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
Note:

1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.
"""
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Solution 1 - 60 ms
        """
        visited = set([0])

        def dfs(room):
            for neib in rooms[room]:
                if neib not in visited:
                    visited.add(neib)
                    dfs(neib)

        dfs(0)
        return len(visited) == len(rooms)
        """
        # Solution 2 - 48 ms
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]

        # At the beginning, we have a todo list "stack" of keys to use.
        # 'seen' represents at some point we have entered this room.

        while stack:  # While we have keys...
            node = stack.pop()  # get the next key 'node'
            for nei in rooms[node]:  # For every key in room # 'node'...
                if not seen[nei]:  # ... that hasn't been used yet
                    seen[nei] = True  # mark that we've entered the room
                    stack.append(nei)  # add the key to the todo list
        return False not in set(seen)  # Return true if we've visited every room


# Main Call
rooms = [[1],[2],[3],[]]
solution = Solution()
print(solution.canVisitAllRooms(rooms))
