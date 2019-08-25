# Brute Force method
# 2 loops - first loop on input_string_1 and second loop on input_string_2
# Time Complexity - O(n^2)
# Space Complexity - O(n)


def check_permutations_bfm(input_string_1, input_string_2):
    # Check if the lengths are equal or not
    if len(input_string_1) != len(input_string_2):
        print("Strings are not equal")
        return False

    # Initialize the character count
    char_count = 0
    # Loop 1 - Input String 1
    for i in range(len(input_string_1)):
        # Loop 2 Input String 2
        for j in range(len(input_string_2)):
            # Check the characters
            if input_string_1[i] == input_string_2[j]:
                # Increase the count
                char_count += 1
    # Check if the character count is equal to the length of the input_string_1 or 2
    if char_count == len(input_string_1):
        return True
    else:
        return False


# Driver Call
print("BFM {}".format(check_permutations_bfm("abc", "cba")))
