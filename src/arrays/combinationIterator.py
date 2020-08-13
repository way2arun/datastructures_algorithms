"""
Iterator for Combination
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3422/
Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.


Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false


Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.
   Hide Hint #1
Generate all combinations as a preprocessing.
   Hide Hint #2
Use bit masking to generate all the combinations.

"""
import itertools


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        # Solution 1 - 64 ms
        """
        self.characters = characters
        self.char_length = len(characters)
        self.combinations = self.generate_combinations(self.char_length, combinationLength)
        self.char_index = len(self.combinations) - 1
        """
        # Solution 2 - 32 ms
        self.combs = list(map(''.join, itertools.combinations(characters, combinationLength)))[::-1]

    def next(self) -> str:
        # Solution 1 - 64 ms
        """
        s = ""
        for i in range(self.char_length):
            if self.combinations[self.char_index][i] != "0":
                s += self.characters[i]
        self.char_index -= 1
        return s
        """
        # Solution 2 - 32 ms
        return self.combs.pop(-1)

    def hasNext(self) -> bool:
        # Solution 1 - 64 ms
        """
        return self.char_index > -1
        """
        # Solution 2 - 32 ms
        return bool(self.combs)

    def generate_combinations(self, l, n):
        end = int("1" * l, 2)
        ans = []
        for i in range(end + 1):
            b = bin(i)[2:]
            if b.count('1') == n:
                ans.append(b.zfill(l))
        return ans


# Main Call
iterator = CombinationIterator("abc", 2)
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
