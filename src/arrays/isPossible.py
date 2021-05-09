"""
Construct Target Array With Multiple Sums
Given an array of integers target. From a starting array, A consisting of all 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
You may repeat this procedure as many times as needed.
Return True if it is possible to construct the target array from A otherwise return False.



Example 1:

Input: target = [9,3,5]
Output: true
Explanation: Start with [1, 1, 1]
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done
Example 2:

Input: target = [1,1,1,2]
Output: false
Explanation: Impossible to create target array from [1,1,1,1].
Example 3:

Input: target = [8,5]
Output: true


Constraints:

N == target.length
1 <= target.length <= 5 * 10^4
1 <= target[i] <= 10^9
   Hide Hint #1
Given that the sum is strictly increasing, the largest element in the target must be formed in the last step by adding the total sum in the previous step. Thus, we can simulate the process in a reversed way.
   Hide Hint #2
Subtract the largest with the rest of the array, and put the new element into the array. Repeat until all elements become one
"""

from heapq import heapify, heappush, heappop, heapreplace
from typing import List


class Solution:
    def helper(self, arr):
        m = float('-inf')
        i = -1
        for j, v in enumerate(arr):
            if v > m:
                m = v
                i = j
        return i, m

    def isPossible(self, target: List[int]) -> bool:
        # Solution 1 - 256 ms
        """
        heap = [-num for num in target]
        total = sum(target)
        heapify(heap)
        while heap[0] != -1:
            num = -heappop(heap)
            total -= num
            if num <= total or total < 1: return False
            num %= total
            total += num
            heappush(heap, -num)
        return True
        """
        # Solution 2 - 236 ms
        if len(target) == 1:
            if target == [1]:
                return True
            else:
                return False

        q = [-x for x in target]
        heapify(q)
        sm = sum(target)
        while True:
            high, rest = -q[0], sm + q[0]
            if high == 1 or rest == 1: return True
            original = high % rest
            if rest >= high or not original: return False
            sm -= high - original
            heapreplace(q, -original)


# Main Call
target = [9, 3, 5]
solution = Solution()
print(solution.isPossible(target))
