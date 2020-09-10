"""
Bulls and Cows
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows.

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
"""
from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # Solution 1 - 28 ms
        """
        secret = list(secret)
        guess = list(guess)
        number_of_b = 0
        for i in range(len(secret)):
            if secret[i - number_of_b] == guess[i - number_of_b]:
                secret.pop(i - number_of_b)
                guess.pop(i - number_of_b)
                number_of_b += 1
        top = Counter(secret)
        bottom = Counter(guess)
        intersections = set(top).intersection(bottom)
        total = 0
        for i in intersections:
            total += min(top[i], bottom[i])
        return "{}A{}B".format(number_of_b, total)
        """
        # Solution 2 - 20 ms
        bull = 0
        for i in range(len(secret)):
            bull += int(secret[i] == guess[i])

        # This loop will take care of "cow" cases
        cows = 0
        for c in set(secret):
            cows += min(secret.count(c), guess.count(c))

        return f"{bull}A{cows - bull}B"


# Main Call
secret = "1807"
guess = "7810"
solution = Solution()
print(solution.getHint(secret, guess))
