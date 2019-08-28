
def string_compression(string):
    compressed_string = []
    char_count = 0
    for i in range(len(string)):
        if i != 0 and string[i] != string[i - 1]:
            compressed_string.append(string[i - 1] + str(char_count))
            char_count = 0
        char_count += 1
    # add last repeated character
    compressed_string.append(string[-1] + str(char_count))

    # returns original string if compressed string isn't smaller
    if len(''.join(compressed_string)) > len(string):
        return string
    else:
        return ''.join(compressed_string)
    # return min(string, ''.join(compressed), key=len)


# Driver Call
print(string_compression("aabbccddaadd"))
