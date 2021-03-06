"""
Insert Interval
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3458/
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Solution 1 - 84 ms
        """
        inter = intervals
        newInter = newInterval
        r_newInter = newInter[0]
        col_newInter = newInter[1]
        answer = []

        for row, col in inter:
            f = 0
            if r_newInter <= row and col <= col_newInter:
                f = 1
            if row <= r_newInter <= col:
                r_newInter, f = row, 1
            if row <= col_newInter <= col:
                col_newInter, f = col, 1
            if f == 1:
                continue
            answer += [[row, col]]
        answer += [[r_newInter, col_newInter]]
        answer.sort()
        return answer
        """
        # Solution 2 - 60 ms

        found = False
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                intervals = intervals[:i] + [newInterval] + intervals[i:]
                found = True
                break

        if not found:
            intervals.append(newInterval)

        merged = []
        for interval in intervals:
            if len(merged) != 0 and merged[-1][1] >= interval[0]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)

        return merged

        # Solution 3 - 64 ms
        """
        start, end = newInterval[0], newInterval[-1]
        left, right = [], []

        for interval in intervals:
            if interval[-1] < start:
                left += interval,
            elif interval[0] > end:
                right += interval,
            else:
                start = min(start, interval[0])
                end = max(end, interval[-1])

        print(type([left]))
        print(right)
        rtn = []
        rtn.extend(left)
        rtn.append([start, end])
        rtn.extend(right)
        return rtn
        """


# Main Call
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
solution = Solution()
print(solution.insert(intervals, newInterval))
