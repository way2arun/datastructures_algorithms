# Time Complexity - O(n)
# Space Complexity - O(1)


def urlify2(input_string, input_string_length):
    urlify_output = ''
    for char in input_string:
        if char == ' ':
            urlify_output += '%20'
        else:
            urlify_output += char
    print(urlify_output)


# Driver Call
urlify2("Mr John Smith", 13)
