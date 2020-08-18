"""
Numbers With Same Consecutive Differences
Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.



Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


Note:

1 <= N <= 9
0 <= K <= 9
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3428/
"""

from typing import List
from collections import deque

class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        # Solution - 28 ms
        """
        # Initialize queue with numbers from 1-10 as Tuple of (num, length)
        que = [(i, 1) for i in range(1, 10)]
        visited = set(que)
        ans = []

        while que:
            popped, length = que.pop(0)
            # If the length is N, we can add the number to the result array
            if length == N:
                ans.append(popped)
                continue

            # Get the last digit
            last_digit = popped % 10

            # Would adding K to the number keep the number within bounds?
            if last_digit + K <= 9:
                new_num = (popped * 10) + (last_digit + K)
                # If so and it is not visited (generated) before, then add it to the result array
                if new_num not in visited:
                    visited.add(new_num)
                    que.append((new_num, length + 1))

                # Would subtracting K to the number keep the number within bounds?
            if last_digit - K >= 0:
                new_num = (popped * 10) + (last_digit - K)
                # If so and it is not visited (generated) before, then add it to the result array
                if new_num not in visited:
                    visited.add(new_num)
                    que.append((new_num, length + 1))

            # Since our q is initialized with numbers [1,2,3,4,5,6,7,8,9] at beginning
            # For N == 1, 0 is a valid answer too
        if N == 1:
            ans += [0]
        return ans
        """
        # Solution 2 - 24 ms
        deltas = [-K, K] if K > 0 else [K]
        results = deque(range(10))
        threshold = 10 ** (N - 1) if N > 1 else 0
        while results[0] < threshold:
            n = results.popleft()
            if n == 0:
                continue
            digit = n % 10
            for delta in deltas:
                if 0 <= digit + delta <= 9:
                    results.append(n * 10 + digit + delta)
        return results


# Main Call
solution = Solution()
N = 3
K = 7
print(solution.numsSameConsecDiff(N, K))
