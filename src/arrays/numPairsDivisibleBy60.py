"""
Pairs of Songs With Total Durations Divisible by 60
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.



Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.


Constraints:

1 <= time.length <= 6 * 104
1 <= time[i] <= 500
   Hide Hint #1
We only need to consider each song length modulo 60.
   Hide Hint #2
We can count the number of songs with (length % 60) equal to r, and store that in an array of size 60.

"""
from typing import List
from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # Solution 1 - 544ms
        """
        ans = 0
        ht = defaultdict(int)
        for x in time:
            for i in range(17):
                ans += ht[60 * i - x]
            ht[x] += 1
        return ans
        """
        # Solution 2 - 188 ms
        arr = [0 for _ in range(60)]
        count = 0
        for elem in time:
            arr[elem % 60] += 1

        for i in range(0, 31):
            if arr[i] == 0:
                continue
            elif i == 0 or i == 30:

                count += int(arr[i] * (arr[i] - 1) / 2)
            else:
                count += arr[i] * arr[60 - i]
        return count



# Main Call
solution = Solution()
time = [30,20,150,100,40]
print(solution.numPairsDivisibleBy60(time))