def palindrome_permutation(actual_string, input_string1, index=0):
    # check the index is equal to the length of the input string
    if index == len(input_string1):
        palindrome_string = ''.join(input_string1)
        if actual_string[::-1] == palindrome_string:
            print("Found the Palindrome String {}".format(palindrome_string))

    # Swap each characters
    for i in range(index, len(input_string1)):
        # copy to a temp variable
        swap_copy = [character for character in input_string1]

        # Swap the characters on index.
        swap_copy[index], swap_copy[i] = swap_copy[i], swap_copy[index]

        # Increase the index and recursively call to swap the rest of the characters.
        palindrome_permutation(actual_string, swap_copy, index + 1)


# Driver Call
actual_string = input_string1 = "Tact Coa"
palindrome_permutation(actual_string, input_string1, 0)
