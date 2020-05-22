"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3337/
"""
import collections
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        # Solution 1 - 64 ms
        """
        temp = {}
        new_array = []
        for char in s:
            if char not in temp:
                temp[char] = 1
            else:
                temp[char] += 1
        for char in (sorted(temp, key=temp.get, reverse=True)):
            for j in range(temp[char]):
                new_array.append(char)
        return "".join(new_array)
        """

        # Solution 2 - 20 ms
        counterMap = collections.Counter(s)
        res = ''
        hq = []
        for char, freq in counterMap.items():
            heapq.heappush(hq, (-freq, char))

        while hq:
            freq, char = heapq.heappop(hq)
            res += -freq * char

        return res


# Main Call
s = "cccaaa"
solution = Solution()
print(solution.frequencySort(s))
