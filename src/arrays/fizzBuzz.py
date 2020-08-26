"""
Fizz Buzz
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3437/
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # Solution 1 - 44 ms
        """
        result = []
        for num in range(1, n + 1):
            string = ""
            if num % 3 == 0:
                string += "Fizz"
            if num % 5 == 0:
                string += "Buzz"
            if string:
                result.append(string)
            else:
                result.append(str(num))
        return result
        """
        # Solution 2 - 24 ms

        arr = []
        for i in range(0, n):
            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                arr.append("FizzBuzz")
            elif (i + 1) % 3 == 0:
                arr.append("Fizz")
            elif (i + 1) % 5 == 0:
                arr.append("Buzz")
            else:
                arr.append(str(i + 1))
        return arr

        # Solution 3 - 28 ms
        """
        result = []
        for i in range(1, n + 1):
            word = ""
            if i % 3 == 0:
                word += "Fizz"
            if i % 5 == 0:
                word += "Buzz"
            if not word:
                word = str(i)

            result.append(word)

        return result
        """


# Main Solution
solution = Solution()
n = 15
print(solution.fizzBuzz(n))
