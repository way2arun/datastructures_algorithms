"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

Can you solve it in O(N) time and O(1) space?

"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # Solution 1
        temp = ""
        for char in S:
            if char == "#":
                temp = temp[:-1]
            else:
                temp += char
        temp2 = ""
        for char2 in T:
            if char2 == "#":
                temp2 = temp2[:-1]
            else:
                temp2 += char2

        return temp == temp2

        # Solution 2
        #return self.getString(S) == self.getString(T)

    def getString(self, st):
        s = ""
        for c in st:
            if c == "#":
                s = s[:-1]
            else:
                s += c
        return s


# Main Call
solution = Solution()
result = solution.backspaceCompare("ab#c", "ad#c")
print(result)
result = solution.backspaceCompare("ab##", "c#d#")
print(result)
result = solution.backspaceCompare("a##c", "#a#c")
print(result)
result = solution.backspaceCompare("a#c", "b")
print(result)
