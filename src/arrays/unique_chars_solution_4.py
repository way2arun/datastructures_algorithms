
# More Python based approach
# Time Complexity :- O(1)
# Space Complexity :- O(1)
# Using the set data structure to eliminate the duplicates and check the length is same or not


def unique_char_set(input_string):
    # Use Set data structure and checks the length, if it is same it returns True if not False
    return len(input_string) == len(set(input_string))


# Driver Call
print(unique_char_set("zdabe"))
