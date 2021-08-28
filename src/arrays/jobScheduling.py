"""
Maximum Profit in Job Scheduling
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.



Example 1:



Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job.
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
Example 2:



Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job.
Profit obtained 150 = 20 + 70 + 60.
Example 3:



Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6


Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 104
1 <= startTime[i] < endTime[i] <= 109
1 <= profit[i] <= 104
   Hide Hint #1
Think on DP.
   Hide Hint #2
Sort the elements by starting time, then define the dp[i] as the maximum profit taking elements from the suffix starting at i.
   Hide Hint #3
Use binarySearch (lower_bound/upper_bound on C++) to get the next index for the DP transition.
"""
import bisect
import heapq
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Solution 1 - 548 ms
        """
        jobs = sorted([(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))], key=lambda x: x[0])
        heap = []
        currentProfit = 0
        maxProfit = 0
        for start, end, profit in jobs:
            # Calculate the total profit of all the jobs that would have end by this time(start: startTime of current job)
            while heap and heap[0][0] <= start:
                _, tempProfit = heapq.heappop(heap)
                currentProfit = max(currentProfit, tempProfit)

            # Push the job into heap to use it further. It's profit would be definitely currentProfit + profit(of current job)
            heapq.heappush(heap, (end, currentProfit + profit))
            maxProfit = max(maxProfit, currentProfit + profit)

        return maxProfit
        """
        # Solution 2 - 460 ms
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        profits = [0]
        endTimes = [0]

        for s, e, p in jobs:
            i = bisect.bisect(endTimes, s) - 1
            if profits[i] + p > profits[-1]:
                profits.append(profits[i] + p)
                endTimes.append(e)
        return profits[-1]


# Main Call
startTime = [1, 2, 3, 4, 6]
endTime = [3, 5, 10, 6, 9]
profit = [20, 20, 100, 70, 60]
solution = Solution()
print(solution.jobScheduling(startTime, endTime, profit))
