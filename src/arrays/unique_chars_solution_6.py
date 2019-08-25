# Using bit operator


def unique_char_bit(input_string):
    # Initialize the checker variable
    checker = 0
    # Loop through each characters
    for i in range(len(input_string)):
        # Get the acii or unicode value
        ascii_value = ord(input_string[i])
        print(1 << ascii_value)
        # If the & is greater than 0 , the character is repeating, return false.
        if (checker & 1 << ascii_value) > 0:
            return False
        # update the checker.
        checker = (1 << ascii_value)
    return True

# Driver Call
print(unique_char_bit("abcc"))
