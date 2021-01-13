"""
Boats to Save People
The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)



Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
Note:

1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000
"""
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Solution 1 - 452 ms
        """
        people.sort()
        beg, end, ans = 0, len(people) - 1, 0
        while beg <= end:
            if people[beg] + people[end] <= limit:
                beg += 1
            ans += 1
            end -= 1

        return ans
        """
        # Solution 2 - 416 ms
        '''
                any item >= limit require that much items
                for remaining, start from left and right
                '''

        people.sort()
        # remove all those whose weight >= limit
        left = 0
        right = len(people) - 1
        boats = 0
        while people[right] >= limit:
            right -= 1
            boats += 1
        while left < right:
            current_weight = people[left] + people[right]
            if current_weight <= limit:
                boats += 1
                left += 1
                right -= 1
            else:
                boats += 1
                right -= 1
        if left == right:  # single entry remaining
            boats += 1

        return boats



# Main Call
people = [1, 2]
limit = 3

solution = Solution()
print(solution.numRescueBoats(people, limit))