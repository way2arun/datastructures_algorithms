"""
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3352/
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


   Hide Hint #1
What can you say about the position of the shortest person?
If the position of the shortest person is i, how many people would be in front of the shortest person?
   Hide Hint #2
Once you fix the position of the shortest person, what can you say about the position of the second shortest person?
"""
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda person: (person[0], -person[1]))
        people.reverse()
        queue = []
        for person in people:
            queue.insert(person[1], person)
        return queue


# Main Call
people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
solution = Solution()
print(solution.reconstructQueue(people))
