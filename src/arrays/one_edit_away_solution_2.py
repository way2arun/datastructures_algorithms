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

    # Indexes for each strings to travers.
    index_1 = 0
    index_2 = 0
    one_edit_away_change = False

    # Traverse through each strings.
    while index_1 < string1_len and index_2 < string2_len:

        # Check if the characters are equal, if so , increment the indexes
        if input_string1[index_1] == input_string2[index_2]:
            index_1 += 1
            index_2 += 1
        else:
            # Checking if a change has already detected.
            if one_edit_away_change:
                return False

            # update the boolean
            one_edit_away_change = True

            # Check if the first string is greater than second string, extra character added on first string
            if string1_len > string2_len:
                index_1 += 1
            # Extra character added on second String
            elif string1_len < string2_len:
                index_2 += 1
            # increment the indexes there could be an edit happened on the string.
            else:
                index_1 += 1
                index_2 += 1

    # No edits more than 1, return true
    return True


# Driver Call
print(one_edit_away("pale", "ple"))
print(one_edit_away("pale", "le"))
print(one_edit_away("pales", "pale"))
print(one_edit_away("pale", "bale"))
print(one_edit_away("pale", "bake"))
