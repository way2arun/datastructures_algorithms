def longest_substring(input_string1):
    substring = ''
    substring_length = 0
    for char in input_string1:
        if char in substring:
            if len(substring) > substring_length:
                substring_length = len(substring)
            substring = substring[substring.index(char) + 1:]
        substring += char
    if len(substring) > substring_length:
        substring_length = len(substring)
    print(substring)
    return substring_length


print(longest_substring("abca"))
print(longest_substring("abcdabcd"))
print(longest_substring("aaaaaaaaa"))
print(longest_substring("hello world"))
print(longest_substring("abcabcbb"))
print(longest_substring("pwwkew"))