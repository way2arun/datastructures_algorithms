"""
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift).
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.



Example 1:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation:
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"
Example 2:

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"


Constraints:

1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
0 <= shift[i][0] <= 1
0 <= shift[i][1] <= 100

Hint 1
Intuitively performing all shift operations is acceptable due to the constraints.

Hint 2
You may notice that left shift cancels the right shift, so count the total left shift times (may be negative if the final result is right shift), and perform it once.

"""
import collections
from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        # solution 1 - 32 ms
        """
        string_len, left_shift, right_shift = len(s), 0, 0
        for direction, amount in shift:
            if direction == 0:
                left_shift += amount
            else:
                right_shift += amount
        left_shift = left_shift % string_len
        right_shift = right_shift % string_len
        if left_shift == right_shift:
            return s
        if left_shift > right_shift:
            left_shift = left_shift - right_shift
            return s[left_shift:] + s[:left_shift]
        else:
            right_shift = right_shift - left_shift
            return s[-right_shift:] + s[:-right_shift]
        """
        # solution 2
        """
        chars = collections.deque(s)
        for d, amount in shift:
            if d == 0:
                for _ in range(amount):
                    num = chars.popleft()
                    chars.append(num)
            else:
                for _ in range(amount):
                    num = chars.pop()
                    chars.appendleft(num)
        return ''.join(chars)
        """
        # solution 3
        left = 0
        for d, a in shift:
            if d:
                left -= a
            else:
                left += a
        left %= len(s)
        return s[left:] + s[:left]


# Main Call
solution = Solution()
result = solution.stringShift("abc", [[0, 1], [1, 2]])
print(result)
