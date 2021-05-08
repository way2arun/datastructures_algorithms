"""
Super Palindromes
Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.

Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right].



Example 1:

Input: left = "4", right = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
Example 2:

Input: left = "1", right = "2"
Output: 1


Constraints:

1 <= left.length, right.length <= 18
left and right consist of only digits.
left and right cannot have leading zeros.
left and right represent integers in the range [1, 1018].
left is less than or equal to right.
"""


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        # Solution 1 - 744 ms
        """
        left, right = int(left), int(right)
        # Just to travese the loop declare a variable and set the limit
        limit = 100000
        # to count super Palindromes
        cnt = 0
        # count odd number length palindromes
        for i in range(1, limit):
            # to add the the numbers it easily I have converted it to string
            s = str(i)
            # add s with s in the reverse order by leaving the 1st element so that we will get odd number length string
            p = s + s[::-1][1:]  # or U can use negative indexing s[-2::-1]
            # square the number we got
            p2 = int(p) ** 2
            # if the squares number of p is greater than right value break the loop
            if p2 > right:
                break
            # if squared value of p is greater than or equal to left and and the reversal of that squares value is also a palindrome then increase the count
            if p2 >= left and str(p2) == str(p2)[::-1]:
                # print(p,p2)
                cnt += 1
            # to count even number length palindromes
        for i in range(limit):
            # to add the the numbers it easily I have converted it to string
            s = str(i)
            # add s with s in the reverse order so that we will get even number length string
            p = s + s[::-1]
            # square the number we got
            p2 = int(p) ** 2
            # if the squares number of p is greater than right value break the loop
            if p2 > right:
                break
            # if squared value of p is greater than or equal to left and and the reversal of that squares value is also a palindrome then increase the count
            if p2 >= left and str(p2) == str(p2)[::-1]:
                # print(p,p2)
                cnt += 1
        return cnt
        """
        # Solution 2 - 180 ms
        sqrt_sp = ['11', '22']
        for i in sqrt_sp:
            for j in ('0', '1', '2'):
                sqrt_sp.append(str(i[:len(i) // 2]) + j + str(i[len(i) // 2:]))
            if int(i) ** 2 > int(right):
                break
        sqrt_sp.append(1)
        sqrt_sp.append(2)
        sqrt_sp.append(3)

        ans = 0

        for i in sqrt_sp:
            s = int(i) ** 2
            if int(left) <= s <= int(right) and str(s) == str(s)[::-1]:
                ans += 1
        return ans


# Main Call
left = "4"
right = "1000"

solution = Solution()
print(solution.superpalindromesInRange(left, right))
