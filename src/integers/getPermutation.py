"""
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3366/
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        numbers = [1]
        i = 1
        while i < n:
            numbers.append(i + 1)
            a = factorial.pop(len(factorial) - 1)
            factorial.append(a)
            factorial.append(a * i)
            i += 1
        i = 1
        str_n = 0
        k -= 1
        while i <= n:
            index = int(k / factorial[n - i])
            str_n = 10 * str_n + numbers[index]
            numbers.remove(numbers[index])
            k %= factorial[n - i]
            i += 1
        return str(str_n)


# Main Call
solution = Solution()
n = 3
k = 3
print(solution.getPermutation(n, k))
n = 4
k = 9
print(solution.getPermutation(n, k))
