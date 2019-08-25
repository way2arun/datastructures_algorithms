# Use sorted method and compare 2 strings, if equals prints true, if not, false
# Time Complexity - O(1)
# Space Complexity - O(1)
# using just python functions


def check_permutations_sorted(input_string_1, input_string_2):
    # Sort the first input string
    input_string_1 = sorted(input_string_1)
    # Sort the second input string
    input_string_2 = sorted(input_string_2)
    print(input_string_1)
    print(input_string_2)

    # Compare the strings.
    print(input_string_2 == input_string_1)


# Driver Call
check_permutations_sorted("abc", "cba")
