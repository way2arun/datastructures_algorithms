"""
 One Away:  There are three types of edits that can be performed on strings: insert a character, remove a character, or
 replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false

"""


# Time Complexity :- O(n^2)
# Space Complexity :- O(1)


def one_edit_away(input_string1, input_string2):
    # Get the length of 2 strings.
    string1_len = len(input_string1)
    string2_len = len(input_string2)

    # If the difference itself is more than 1 then there are more than 1 edits happened.
    if abs(string1_len - string2_len) > 1:
        return False

    # Counter for character edit
    char_edit_count = 0
    # Indexes for each strings to travers.
    index_1 = 0
    index_2 = 0

    # Traverse through each strings.
    while index_1 < string1_len and index_2 < string2_len:
        # Check If the characters are not equal
        if input_string1[index_1] != input_string2[index_2]:
            if char_edit_count == 1:
                return False
            # If length of 1 string is greater than the other,
            if string1_len > string2_len:
                index_1 += 1
            elif string1_len < string2_len:
                index_2 += 1
            # assuming both string lengths are equal
            else:
                index_1 += 1
                index_2 += 2
            # Increment the counter
            char_edit_count += 1
        else:
            index_1 += 1
            index_2 += 1

    # If any characters are extra in either strings.
    if index_1 < string1_len or index_2 < string2_len:
        char_edit_count += 1

    # return boolean if 1 true, else false
    return char_edit_count == 1


# Driver Call
print(one_edit_away("pale", "ple"))
print(one_edit_away("pale", "le"))
print(one_edit_away("pales", "pale"))
print(one_edit_away("pale", "bale"))
print(one_edit_away("pale", "bake"))
