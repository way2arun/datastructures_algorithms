"""
Remove All Adjacent Duplicates in String II
Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.



Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"


Constraints:

1 <= s.length <= 10^5
2 <= k <= 10^4
s only contains lower case English letters.
   Hide Hint #1
Use a stack to store the characters, when there are k same characters, delete them.
   Hide Hint #2
To make it more efficient, use a pair to store the value and the count of each character.
"""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Solution 1 - 68 ms
        """
        stack = [["!", 1]]
        for elem in s:
            if elem == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([elem, 1])

            while stack[-1][1] >= k:
                stack[-1][1] -= k
                if stack[-1][1] == 0: stack.pop()

        return "".join(i * j for i, j in stack[1:])
        """
        # Solution 2 - 24 ms
        remove = []
        ## Generating possible duplicates
        for ch in set(s):
            remove.append(ch * k)

        old, new = s, s
        while True:
            for candidate in remove:
                new = new.replace(candidate, "")
            if len(old) == len(new):
                break
            old = new
        return old


# Main Call
s = "abcd"
k = 2

solution = Solution()
print(solution.removeDuplicates(s, k))