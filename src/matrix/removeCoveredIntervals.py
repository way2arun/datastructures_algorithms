"""
Remove Covered Intervals
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3483/
Given a list of intervals, remove all intervals that are covered by another interval in the list.

Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.



Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1
Example 3:

Input: intervals = [[0,10],[5,12]]
Output: 2
Example 4:

Input: intervals = [[3,10],[4,10],[5,11]]
Output: 2
Example 5:

Input: intervals = [[1,2],[1,4],[3,4]]
Output: 1


Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= intervals[i][0] < intervals[i][1] <= 10^5
All the intervals are unique.
   Hide Hint #1
How to check if an interval is covered by another?
   Hide Hint #2
Compare each interval to all others and check if it is covered by any interval.

"""
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Solution 1 - 96 ms
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        right, rem, n = -1, 0, len(intervals)
        for _, end in intervals:
            if end <= right:
                rem += 1
            else:
                right = end
        return n - rem
        """
        # Solution 2 - 76 ms
        n = len(intervals)
        if not n:
            return 0

        inter = sorted(intervals, key=lambda x: x[0] * 10 ** 6 - x[1])
        ans = n
        l, r = inter[0]
        for stard, end in inter[1:]:
            if end > r:
                r = end
            elif end <= r:
                ans -= 1
            else:
                l, r = stard, end

        return ans


# Main Call
solution = Solution()
intervals = [[3,10],[4,10],[5,11]]
print(solution.removeCoveredIntervals(intervals))