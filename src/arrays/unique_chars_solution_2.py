# Only 1 loop in this case
# Time Complexity - O(n log n)
# Why log n - as we sorted the array, so the complexity changed to log n time.
# Space Complexity - O(1)


def unique_chars_sorted(input_string):
    # Sort the array, this will help to remove extra loop
    input_string_sorted = sorted(input_string)
    for i in range(len(input_string_sorted) - 1):
        # In this approach we are always checking the elements in adjacent indexes
        # This is how sorted function helps.
        if input_string_sorted[i] == input_string_sorted[i + 1]:
            return False
    return True


# Driver Call
print(unique_chars_sorted("zdabez"))
