"""
Distribute Candies to People
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3427/
We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.



Example 1:

Input: candies = 7, num_people = 4
Output: [1,2,3,1]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0,0].
On the third turn, ans[2] += 3, and the array is [1,2,3,0].
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].
Example 2:

Input: candies = 10, num_people = 3
Output: [5,2,3]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0].
On the third turn, ans[2] += 3, and the array is [1,2,3].
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].


Constraints:

1 <= candies <= 10^9
1 <= num_people <= 1000
   Hide Hint #1
Give candy to everyone each "turn" first [until you can't], then give candy to one person per turn.
"""
from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # Solution 1 - 40 ms
        """
        # candies distribution for each person
        answer = [0] * num_people
        candy = 0
        while candies > 0:
            # candies may be not enough on last round, therefore compute min(candies, c+1)
            answer[candy % num_people] += min(candies, candy + 1)
            # add one more candies for next person
            candy += 1
            # update total number of candies
            candies -= candy
        return answer
        """
        # Solution 2 - 20 ms
        """
        We distribute some number of candies, to a row of 
        n = num_people people in the following way:

        We first give 1 candy to the first person, 2 candies to the 
        second person, and so on until we give n candies to the last
        person.

        Then, we go back to the start of the row, giving n + 1 candies
        to the first person, n + 2 candies to the second person, and so
        on until we give 2 * n candies to the last person.

        This process repeats (with us giving one more candy each time,
        and moving to the start of the row after we reach the end) 
        until we run out of candies. The last person will receive all
        of our remaining candies (not necessarily one more than
        the previous gift).

        Return an array (of length num_people and sum candies) that
        represents the final distribution of candies.

        Example 1:

        Input: candies = 7, num_people = 4
        Output: [1,2,3,1]
        Explanation:
        On the first turn, ans[0] += 1, and the array is [1,0,0,0].
        On the second turn, ans[1] += 2, and the array is [1,2,0,0].
        On the third turn, ans[2] += 3, and the array is [1,2,3,0].
        On the fourth turn, ans[3] += 1 
            (because there is only one candy left), and the final array
            is [1,2,3,1].

        Example 2:

        Input: candies = 10, num_people = 3
        Output: [5,2,3]
        Explanation: 
        On the first turn, ans[0] += 1, and the array is [1,0,0].
        On the second turn, ans[1] += 2, and the array is [1,2,0].
        On the third turn, ans[2] += 3, and the array is [1,2,3].
        On the fourth turn, ans[0] += 4, and the final array is [5,2,3].

        Constraints:

        1 <= candies <= 10^9
        1 <= num_people <= 1000

        Idea: Round number k (starting from 1)
              -> give away
              (k-1)*n+1 + (k-1)*n+2 + ... + (k-1)*n + n = 
              (k-1)*n^2 + n*(n+1)/2 candies
              
        Assume we have completed K full rounds, then K is the largest integer >= 0 with
        
        K*n*(n+1)/2 + K * (K-1)/2 * n^2 <= candies 
        
        Find K by binary search and then simulate the last round.
        
        The person at index i gets
    
        0*n+i+1 + ... + (K-1)*n+i+1 = K*(i+1) + n*K*(K-1)/2 
        
        candies from rounds 1 to K, plus everything they get on their
        last round.
        
        Important: Allow for the fact that we may not complete a single round.
        """
        low, high = 0, candies
        middle = 0
        while low <= high:
            k = (low + high) // 2
            if k * (num_people * (num_people + 1)) // 2 + (k * (k - 1)) // 2 * num_people ** 2 <= candies:
                middle = k
                low = k + 1
            else:
                high = k - 1
        result = [(i + 1) * middle + num_people * (middle * (middle - 1)) // 2 for i in range(num_people)]
        candies -= sum(result)
        for i in range(num_people):
            add = min(candies, middle * num_people + i + 1)
            result[i] += add
            candies -= add
            if candies == 0:
                break
        return result


# Main Call
candies = 7
num_people = 4
solution = Solution()
print(solution.distributeCandies(candies, num_people))
