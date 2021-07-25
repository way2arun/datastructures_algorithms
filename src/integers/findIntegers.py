"""
Non-negative Integers without Consecutive Ones
Given a positive integer n, return the number of the integers in the range [0, n] whose binary representations do not contain consecutive ones.



Example 1:

Input: n = 5
Output: 5
Explanation:
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.
Example 2:

Input: n = 1
Output: 2
Example 3:

Input: n = 2
Output: 3


Constraints:

1 <= n <= 109
"""


class Solution:
    def findIntegers(self, n: int) -> int:
        # Solution 1 - 32 ms
        """
        # f stores the fibonacci numbers
        f = [1, 2]
        for i in range(2, 30):
            f.append(f[-1] + f[-2])

        # last_seen tells us if there was a one right before.
        # If that is the case, we are done then and there!
        # ans is the answer
        ans, last_seen = 0, 0
        for i in reversed(range(30)):
            if (1 << i) & n:  # is the ith bit set?
                ans += f[i]
                if last_seen:
                    ans -= 1
                    break
                last_seen = 1
            else:
                last_seen = 0
        return ans + 1
        """
        # Solution 2 - 20 ms
        FIB = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
               28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465]
        Y = "01010101010101010101010101010101"

        B = f"{n:b}"
        LOG = len(B)

        for i in range(1, LOG):
            if B[i] == "1" and B[i - 1] == "1":
                B = B[:i] + Y[:LOG - i]
                break

        c = 0
        for i in range(LOG):
            if B[i] == "1":
                c += FIB[LOG - i]
        # c+=1
        return c + 1


# Main Call
n = 5
solution = Solution()
print(solution.findIntegers(n))