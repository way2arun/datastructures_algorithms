"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False


Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
   Hide Hint #1
Obviously, brute force will result in TLE. Think of something else.
   Hide Hint #2
How will you check whether one string is a permutation of another string?
   Hide Hint #3
One way is to sort the string and then compare. But, Is there a better way?
   Hide Hint #4
If one string is a permutation of another string then they must one common metric. What is that?
   Hide Hint #5
Both strings must have same character frequencies, if one is permutation of another. Which data structure should be used to store frequencies?
   Hide Hint #6
What about hash table? An array of size 26?

https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3333/

"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Solution 1
        """
        temp_storage = {}
        for char in s1:
            if char not in temp_storage:
                temp_storage[char] = 1
            else:
                temp_storage[char] += 1
        s1_length = len(s1)
        for char in range(len(s2)):
            if s2[char] in temp_storage:
                if temp_storage[s2[char]] > 0:
                    s1_length -= 1
                temp_storage[s2[char]] -= 1
            if char + 1 >= len(s1):  # sliding window
                if s1_length == 0:
                    print("Found at : ", char + 1 - len(s1))
                    return True
                if s2[char + 1 - len(s1)] in temp_storage:
                    temp_storage[s2[char + 1 - len(s1)]] += 1
                    if temp_storage[s2[char + 1 - len(s1)]] > 0:
                        s1_length += 1
        return False
        """
        # Solution 2
        n = len(s1)
        m = len(s2)
        counter1 = [0] * 26
        counter2 = [0] * 26
        for i in range(n):
            counter1[ord(s1[i]) - ord('a')] += 1

        for j in range(m):
            if j >= n:
                counter2[ord(s2[j - n]) - ord('a')] -= 1
            counter2[ord(s2[j]) - ord('a')] += 1
            if counter1 == counter2:
                return True
        return False


# Main Call
solution = Solution()
s1= "ab"
s2 = "eidboaoo"
print(solution.checkInclusion(s1, s2))
s1 = "ab"
s2 = "eidbaooo"
print(solution.checkInclusion(s1, s2))
