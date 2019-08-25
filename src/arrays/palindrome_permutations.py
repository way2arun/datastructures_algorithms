# Palindrome Permutation
# Time Complexity  :- O(n)


def palindrome_permutations(input_string: object, i: object, length: object):
    if i == length:
        palindrome_string: str = ''.join(input_string)
        print(palindrome_string)
        if palindrome_string == palindrome_string[::-1]:
            print("True permutations {}".format(palindrome_string))
    else:
        for j in range(i, length):
            # swap each characters
            input_string[i], input_string[j] = input_string[j], input_string[i]
            # Call recursively
            palindrome_permutations(input_string, i + 1, length)
            input_string[i], input_string[j] = input_string[j], input_string[i]


# string = "tacocat"
string = "Tact Coa"
n = len(string)
input_string = list(string)
palindrome_permutations(input_string, 0, n)
