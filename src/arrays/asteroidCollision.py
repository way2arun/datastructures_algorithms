"""
Asteroid Collision
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.



Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
Example 4:

Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right. Asteroids moving the same direction never meet, so no asteroids will meet each other.


Constraints:

1 <= asteroids <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
   Hide Hint #1
Say a row of asteroids is stable. What happens when a new asteroid is added on the right?
"""
from collections import deque
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Solution 1 - 104 ms
        """
        stack = []
        for ast in asteroids:
            stack.append(ast)
            while len(stack) > 1 and stack[-1] < 0 and stack[-2] > 0:
                if stack[-1] + stack[-2] < 0:
                    stack.pop(-2)
                elif stack[-1] + stack[-2] > 0:
                    stack.pop()
                else:
                    stack.pop();
                    stack.pop()
                    break

        return stack
        """
        # Solution 2 - 76 ms
        stackleft = deque()
        stackright = deque()

        for asteroid in asteroids:
            if asteroid > 0:
                stackright.append(asteroid)
            else:
                while stackright and stackright[-1] <= abs(asteroid):
                    temp = stackright[-1]
                    stackright.pop()
                    if temp == abs(asteroid): break

        for asteroid in reversed(asteroids):
            if asteroid < 0:
                stackleft.appendleft(asteroid)
            else:
                while stackleft and abs(stackleft[0]) <= asteroid:
                    temp = stackleft[0]
                    stackleft.popleft()
                    if abs(temp) == asteroid: break
        return stackleft + stackright



# Main Call
asteroids = [-2, -1, 1, 2]
solution = Solution()
print(solution.asteroidCollision(asteroids))