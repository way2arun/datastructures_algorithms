"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
   Hide Hint #1
For each stone, check if it is a jewel.
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/

"""


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # Solution 1
        # 8 ms
        result = 0
        for stone in S:
            if stone in J:
                result += 1
        return result

        # 2nd Solution
        print([s in J for s in S])
        #return sum([s in J for s in S])


# Main Call
solution = Solution()
J =  "aA"
S = "aAAbbbb"
print(solution.numJewelsInStones(J, S))
J = "z"
S = "ZZ"
print(solution.numJewelsInStones(J, S))
