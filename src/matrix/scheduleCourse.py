"""
Course Schedule III
There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.



Example 1:

Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3
Explanation:
There are totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day.
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
Example 2:

Input: courses = [[1,2]]
Output: 1
Example 3:

Input: courses = [[3,2],[4,3]]
Output: 0


Constraints:

1 <= courses.length <= 104
1 <= durationi, lastDayi <= 104
   Hide Hint #1
During iteration, say I want to add the current course, currentTotalTime being total time of all courses taken till now, but adding the current course might exceed my deadline or it doesn’t.

1. If it doesn’t, then I have added one new course. Increment the currentTotalTime with duration of current course.
   Hide Hint #2
2. If it exceeds deadline, I can swap current course with current courses that has biggest duration.
* No harm done and I might have just reduced the currentTotalTime, right?
* What preprocessing do I need to do on my course processing order so that this swap is always legal?

"""
import heapq
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Solution 1 - 708 ms
        """
        heap, time = [], 0
        for t, end in sorted(courses, key=lambda x: x[1]):
            time += t
            heapq.heappush(heap, -t)
            if time > end:
                nt = heapq.heappop(heap)
                time += nt
        return len(heap)
        """
        # Solution 2 - 636 ms
        """
        O(nlog(n)) time, O(n) space. Refer to last approach in solution tab.
        """
        sorted_courses = sorted(courses, key=lambda course: course[1])
        pq = []  # Max-heap so push negatives
        time = 0
        for course in sorted_courses:
            # If course can finish before its last possible day, add to pq
            if time + course[0] <= course[1]:
                heapq.heappush(pq, -course[0])
                time += course[0]
            # If course cannot finish before last possible day but its duration is less than
            # duration of longest course in heap, remove longest course on heap and add new course since
            # new course end time definitely sufficient (smaller duration and courses were sorted by end time)
            elif pq and -pq[0] > course[0]:
                # recalculate time (remove duration of heap top a and add duration of new course)
                time += course[0] - -heapq.heappop(pq)
                heapq.heappush(pq, -course[0])

        return len(pq)


# Main Call
courses = [[1, 2]]
solution = Solution()
print(solution.scheduleCourse(courses))