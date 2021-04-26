"""
Furthest Building You Can Reach
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.



Example 1:


Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
Example 2:

Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7
Example 3:

Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3


Constraints:

1 <= heights.length <= 105
1 <= heights[i] <= 106
0 <= bricks <= 109
0 <= ladders <= heights.length
   Hide Hint #1
Assume the problem is to check whether you can reach the last building or not.
   Hide Hint #2
You'll have to do a set of jumps, and choose for each one whether to do it using a rope or bricks. It's always optimal to use ropes in the largest jumps.
   Hide Hint #3
Iterate on the buildings, maintaining the largest r jumps and the sum of the remaining ones so far, and stop whenever this sum exceeds b.
"""
from typing import List
from heapq import heappush, heappop


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # Solution 1 - 540 ms
        """
        # Following a simplistic approach from the official leetcode solution
        # Observations:
        # Let's call a positive difference in consequetive heights a "climb"
        # Ladders can be used to replace infinite bricks
        # So let's try and start allocating ladders to every climb that we see first
        # For any consequent climbs, we have two options (note that we have used all ladders at this point)-
        # if the climb's height is greater than a previous climb that we used a ladder for, reclaim the ladder for this climb and try to use bricks for the previous climb
        # if the climb's height is less than the previous climb that we used a ladder for or we do not have any ladders to start with - we have to use bricks 🧱!
        # At any point we might have a negative number of bricks, which implies we cannot make the next climb.

        # Code
        # Keep track of climbs we use ladders for
        ladder_climbs = []

        # Iterate over heights
        for i in range(len(heights) - 1):

            # Extract the current and next heights
            current = heights[i]
            next = heights[i + 1]
            climb_height = next - current

            if climb_height <= 0:  # No need for ladders or bricks, continue
                continue

            # Try to use a ladder if available
            if ladders > 0:
                # Add the climb height to a minheap
                heappush(ladder_climbs, climb_height)
                # Reduce ladders by 1
                ladders -= 1
            else:
                # no ladders available
                # we have 2 options now:
                # see if the climb_height is greater than the minimum height we used a ladder for
                # if that's the case, reclaim the previous ladder and try to use bricks for the previous climb
                if ladder_climbs and ladder_climbs[0] < climb_height:
                    # Use bricks for the previous climb
                    bricks -= heappop(ladder_climbs)
                    # Use the reclaimed ladder for current climb
                    heappush(ladder_climbs, climb_height)
                else:  # No option but to use bricks
                    bricks -= climb_height
                # If the number of bricks is negative, return
                if bricks < 0:
                    return i
        # We were able to successfully jump over all buildings!
        return len(heights) - 1
        """
        # Solution 2 - 532 ms
        bricks_heap = []
        position = 0

        for cur_height, next_height in zip(heights, heights[1:]):
            if next_height > cur_height:
                bricks_required = next_height - cur_height
                if bricks >= bricks_required:
                    bricks -= bricks_required
                    heappush(bricks_heap, -1 * bricks_required)
                elif ladders > 0 and bricks_heap and bricks_heap[0] * -1 > bricks_required:
                    bricks += heappop(bricks_heap) * -1 - bricks_required
                    heappush(bricks_heap, bricks_required * -1)
                    ladders -= 1
                elif ladders > 0:
                    ladders -= 1
                else:
                    break
            position += 1

        return position


# Main Call
heights = [4, 2, 7, 6, 9, 14, 12]
bricks = 5
ladders = 1

solution = Solution()
print(solution.furthestBuilding(heights, bricks, ladders))