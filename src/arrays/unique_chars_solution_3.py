# Time complexity :- O(n)
# We are using only 1 loop and python string count function


def unique_char_count(input_string):
    # Initialize the total
    total = 0
    for i in input_string:
        count = input_string.count(i)
        if count > 1:
            # If count is more increment the total
            total += count
    # Check if any duplicates
    if total > 0:
        return False
    else:
        return True


# Driver Call
print(unique_char_count("zdabe"))
