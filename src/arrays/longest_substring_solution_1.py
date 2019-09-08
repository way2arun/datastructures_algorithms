def longest_substring(input_string1):
    substring_length = 0
    substring = ''
    for char in input_string1:
        if char not in substring:
            substring += char
            substring_length = max(substring_length, len(substring))
        else:
            remove_char = substring.index(char)
            substring = substring[remove_char + 1:] + char
    print(substring)
    return substring_length


# Driver Code
print(longest_substring("abca"))
print(longest_substring("abcdabcd"))
print(longest_substring("aaaaaaaaa"))
print(longest_substring("hello world"))
print(longest_substring("abcabcbb"))
print(longest_substring("pwwkew"))
