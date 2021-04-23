"""
Count Binary Substrings
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
   Hide Hint #1
How many valid binary substrings exist in "000111", and how many in "11100"? What about "00011100"?
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Solution 1 - 192 ms
        """
        grp = [1]  # declare a list with a base value 1
        for i in range(1, len(s)):  # run the loop till the last element in the string s
            if s[i - 1] != s[i]:  # s[i-1] is not equal to s[i] then append 1 into group.
                grp.append(1)
            else:
                grp[-1] += 1  # increment the value in the last index append 1 into group.
        cnt = 0  # initialize the 0 to a variable.
        # print(grp) # Print the grp just to view the elements in the group
        for i in range(1, len(grp)):  # traverse the whole group list
            cnt += min(grp[i - 1], grp[i])  # take the minimum value by comparing 2 elements and add to the variable
        return cnt
        """
        # Solution 2 - 96 ms
        if len(s) < 2:
            return 0
        prev = 0
        ans = 0
        curd = s[0]
        curnum = 1
        for c in s[1:]:
            if c == curd:
                curnum += 1
                if curnum <= prev:
                    ans += 1
            else:
                curd = c
                prev = curnum
                curnum = 1
                ans += 1
        return ans


# Main Call
s = "00110011"

solution = Solution()
print(solution.countBinarySubstrings(s))