"""String Compression: Implement a method to perform basic string compression using the counts of repeated
characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become
smaller than the original string, your method should return the original string. You can assume the string has only
uppercase and lowercase letters (a - z). """


# Time Complexity - O(n)
# Space Complexity - O(1)

def string_compression(input_string1):
    print(input_string1)
    # Get the length of the input string
    string_len = len(input_string1)
    # Initialize the character count to 1
    char_count = 1
    # response compressed string
    response_string = ""
    # Traverse through the characters.
    for i in range(string_len - 1):  # Length - 1 is required as we are always checking a character of the next index.
        # Compare the first index with the second index character,
        if input_string1[i] == input_string1[i + 1]:
            char_count += 1
        else:
            # If the characters are not same, create the compressed response string.
            response_string += input_string1[i]
            response_string += str(char_count)
            # Re-initialize the counter
            char_count = 1
    # To add the last characters
    response_string += input_string1[i]
    response_string += str(char_count)

    if len(response_string) >= string_len:
        return input_string1
    else:
        return response_string


# Driver Call
print(string_compression("aabcccccaaa"))
print(string_compression("aabbbbbbcccccaaaddd"))
