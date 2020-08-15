"""
Non-overlapping Intervals
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3425/
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.



Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Solution 1 - 132 ms
        """
        # if intervals is empty then return 0
        if not intervals:
            return 0

        # sort intervals
        intervals.sort()

        # getting initial value to compare every interval with
        last_interval_finish = intervals[0][0]

        # count of non overlapping interval, inc only when
        # current interval is not overlapping
        non_overlap_interval = 0

        # for each interval decide whether it overlap or not
        for interval in intervals:
            # if last interval have finish greater than start of current interval
            if last_interval_finish > interval[0]:
                # choose optimal finish as latest finish
                last_interval_finish = min(last_interval_finish, interval[1])
            else:
                # if current interval do not overlap inc count by 1
                non_overlap_interval += 1
                # update latest finish to current interval finish
                last_interval_finish = interval[1]

        # return number of overlapping intervals
        return len(intervals) - non_overlap_interval
        """
        # Solution 2 - 52 ms
        end_sort = sorted(intervals, key=lambda x: x[1])
        last = None
        ans = 0
        for it in end_sort:
            if not last:
                last = it
            else:
                if it[0] >= last[1]:
                    last = it
                else:
                    ans += 1
        return ans
        """

        # Solution 3 - 56 ms
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][0]
        rmCount = 0
        for s, e in intervals:
            if s >= end:
                end = e
            else:
                rmCount += 1
        return rmCount
        """


# Main Call
solution = Solution()
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(solution.eraseOverlapIntervals(intervals))
