# Reduced to single loop
# Time complexity - O(n)
# Space complexity - O(n)


def check_permutations(input_string_1, input_string_2):
    # Check if the lengths are equal or not
    if len(input_string_1) != len(input_string_2):
        print("Strings are not equal")
        return False
    # Initialize the character count
    char_count = 0
    # Loop through one of the input string
    for i in range(len(input_string_1)):
        # Check if the character exits in the input string 2
        if input_string_1[i] in input_string_2:
            # Increment the character count
            char_count += 1
    # Check if the character count is equal to the length of the input_string_1 or 2
    if char_count == len(input_string_1):
        return True
    else:
        return False


# Driver Call
print(check_permutations("abc", "cba"))
