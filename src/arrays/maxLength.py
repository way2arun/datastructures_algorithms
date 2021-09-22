"""
Maximum Length of a Concatenated String with Unique Characters
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.



Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26


Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
   Hide Hint #1
You can try all combinations and keep mask of characters you have.
   Hide Hint #2
You can use DP.

"""
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Solution 1 - 1912 ms
        """
        n = len(arr)
        ans = 0
        for mask in range(1 << n):
            seen = set()
            isValid = True
            strSize = 0
            for i in range(n):
                if (mask >> i) & 1 == 0: continue
                for c in arr[i]:
                    if c in seen:  # If c is already existed then it's invalid subsequence.
                        isValid = False
                        break
                    seen.add(c)
                    strSize += 1
                if not isValid: break
            if isValid and strSize > ans:
                ans = strSize
        return ans
        """
        # Solution 2 - 40 ms
        visited = set()
        visited.add('')
        maximum = 0
        t = ''

        for let in arr:
            t += let
        n = len(set(t))

        for word in arr:
            times = {word: 1 for word in arr}
            times[word] -= 1
            stack = [word]
            visited.add(word)
            path = word
            if len(word) == len(set(word)):
                maximum = max(maximum, len(word))
            arr = arr[1:]

            while stack:
                state = False
                for tm in times:
                    temp = path + tm
                    if times[tm] > 0 and len(temp) == len(set(temp)) and temp not in visited:
                        path += tm
                        stack.append(tm)
                        visited.add(path)
                        maximum = max(maximum, len(path))
                        if maximum >= n:
                            return maximum
                        times[tm] -= 1
                        state = True
                        break
                if not state:
                    top = stack.pop()
                    times[top] += 1
                    path = path[:-len(top)]
        return maximum


# Main Call
arr = ["cha", "r", "act", "ers"]
solution = Solution()
print(solution.maxLength(arr))
