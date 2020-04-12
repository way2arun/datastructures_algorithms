"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)



Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.


Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000

Simulate the process. We can do it with a heap, or by sorting some list of stones every time we take a turn.

"""
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Solution 1 12 ms
        stones.sort(reverse=True)
        while len(stones) > 1:
            arr = stones[2:]
            y = stones[0]
            x = stones[1]
            if x != y:
                arr.append(y - x)
            stones = sorted(arr, reverse=True)
        if stones:
            return stones[0]
        return 0

        """
        # Solution 2 #48 ms
        while len(stones) > 1:
            stone1, stone2 = stones[-1], stones[-2]
            if stone1 == stone2:
                stones.pop(-1)
                stones.pop(-1)
            else:
                stone1 = abs(stone1 - stone2)
                stones.pop(-1)
                stones[-1] = stone1
        if len(stones):
            return stones[-1]
        return 0
        """

# Main Call
solution = Solution()
result = solution.lastStoneWeight([2, 7, 4, 1, 8, 1])
print(result)
