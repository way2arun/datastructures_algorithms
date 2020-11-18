"""
Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Solution 1 - 80 ms
        """
        ans = []
        for begin, end in sorted(intervals):
            if not ans or ans[-1][1] < begin:
                ans += [[begin, end]]
            else:
                ans[-1][1] = max(ans[-1][1], end)

        return ans
        """
        # Solution 2 - 60 ms
        # sort by the start of each interval
        # then for loop the intervals, and merge if needed
        '''
        1: put the first interval in to the output
        2: compare the second of invervals to the last item in the output:
        if last.end < cur_interfval.starte: simply add the current into the output and continue
        if cur_interval.start  <= last.end <= cur_interval.end; update the last item.end = current_interva;.end
        else: cur_interval.start and cur_interval.end <= last.end, skip

        '''
        """
        if not intervals: return []
        n = len(intervals)

        intervals.sort()

        res = [intervals[0]]

        for i in range(1, n):
            last = res[-1]
            last_start, last_end = last[0], last[1]

            cur_start, cur_end = intervals[i][0], intervals[i][1]
            if last_end < cur_start:
                res.append(intervals[i])
            elif cur_start <= last_end <= cur_end:
                res[-1][1] = cur_end
            elif cur_start <= last_end and cur_end <= last_end:
                continue

        return res
        """
        # Solution 3 - 56 ms
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        answer = []
        start, end = intervals[0][0], intervals[0][1]
        for i in intervals[1:]:
            if i[0] <= end:
                end = max(end, i[1])
            else:
                answer.append([start, end])
                start, end = i[0], i[1]
        answer.append([start, end])
        return answer


# Main Call
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

solution = Solution()
print(solution.merge(intervals))
