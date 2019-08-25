# Using additional data Structure
# Time Complexity :- O(n)
# Space Complexity :- O(n)  - higher as we are using extra data structure to hold


def unique_char_additional_datastructure(input_string):
    # Initialize the new list with False * 128 for all characters occurrences
    helper_character_list = [False] * 128
    # Now convert the character to ascii value and check if it exists in helper_charcter_list
    # If exists return False, if not return True
    for i in range(0, len(input_string)):
        # Use ord function to get the unicode/ascii value
        acii_value = ord(input_string[i])
        if helper_character_list[acii_value]:
            return False
        # Update the helper_character_list to True for each new ascii value in the 128 length array.
        helper_character_list[acii_value] = True
    return True


# Driver Call
print(unique_char_additional_datastructure("abcd"))
