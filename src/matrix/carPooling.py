"""
Car Pooling
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3467/
You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips.



Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
Example 3:

Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
Example 4:

Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true



Constraints:

trips.length <= 1000
trips[i].length == 3
1 <= trips[i][0] <= 100
0 <= trips[i][1] < trips[i][2] <= 1000
1 <= capacity <= 100000
   Hide Hint #1
Sort the pickup and dropoff events by location, then process them in order.
"""
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Solution 1 - 68 ms
        """
        dic = dict()
        for i in trips:
            if i[1] not in dic:
                dic[i[1]] = i[0]
            else:
                dic[i[1]] += i[0]
            if i[2] not in dic:
                dic[i[2]] = -i[0]
            else:
                dic[i[2]] -= i[0]

        cap = 0
        l = []
        for i in dic.keys():
            l.append(i)
        l.sort()
        for i in l:
            cap += dic[i]
            if cap > capacity:
                return False
        return True
        """
        # Solution 2 - 48 ms
        pois = []
        for num, start, end in trips:
            pois.extend([(start, num), (end, -num)])
        num_used = 0
        for _, num in sorted(pois):
            num_used += num
            if num_used > capacity:
                return False
        return True


# Main Call
solution = Solution()

trips = [[2, 1, 5], [3, 3, 7]]
capacity = 4
print(solution.carPooling(trips, capacity))

trips = [[2,1,5],[3,3,7]]
capacity = 5
print(solution.carPooling(trips, capacity))
