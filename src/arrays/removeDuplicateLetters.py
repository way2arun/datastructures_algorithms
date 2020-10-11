"""
Remove Duplicate Letters
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/



Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
   Hide Hint #1
Greedily try to add one missing character. How to check if adding some character will not cause problems ? Use bit-masks to check whether you will be able to complete the sub-sequence if you add the character at some index i.

"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Solution 1 - 36 ms
        """
        last_occurance = {c: i for i, c in enumerate(s)}
        stack = ["!"]
        Visited = set()

        for i, symbol in enumerate(s):
            if symbol in Visited:
                continue

            while symbol < stack[-1] and last_occurance[stack[-1]] > i:
                Visited.remove(stack.pop())

            stack.append(symbol)
            Visited.add(symbol)
        return "".join(stack)[1:]
        """
        # Solution 2 - 16 ms

        d = {c: i for i, c in enumerate(s)}
        res = ""
        for i, x in enumerate(s):
            if x not in res:
                while res and x < res[-1] and i < d[res[-1]]:
                    res = res[:-1]
                res += x
        return res

        # Solution 3 - 20 ms
        """
                cdadabcc

                01234567
                43131244

                1: 2, 4
                2: 5
                3: 1, 3
                4: 0, 6, 7

                stack = []
                c d 
                a d b c 

        """
        """
        last_index = {}
        for i, char in enumerate(s):
            last_index[char] = i

        stack = []
        used = set()

        i = 0
        while i < len(s):
            curr_char = s[i]
            if curr_char not in used:
                while stack and stack[-1] > curr_char and i < last_index[stack[-1]]:
                    used.discard(stack.pop())
                used.add(curr_char)
                stack.append(curr_char)
            i += 1

        return ''.join(stack)
        """


# Main Call
s = "cbacdcbc"
solution = Solution()
print(solution.removeDuplicateLetters(s))
