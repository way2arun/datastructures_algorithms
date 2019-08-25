
from itertools import permutations

# Time Complexity - O(n)
# Space Complexity - O(n)
# Using the permucations from itertools - python based.


def palindrome_permutation(input_string1):
    permutation_string = [''.join(permute) for permute in permutations(input_string1)]
    for palindrome_string in set(permutation_string):
        if input_string1[::-1] == palindrome_string:
            print("Got the palindrome String :-{}".format(palindrome_string))


# Driver Call
input_string1 = "Tact Coa"
#input_string1 = "abc"
palindrome_permutation(input_string1)
