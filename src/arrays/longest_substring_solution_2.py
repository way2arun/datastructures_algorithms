def longest_substring(input_string1):
    substring = []
    start = 0
    while start < len(input_string1) and input_string1[start] not in substring:
        substring.append(input_string1[start])
        start += 1
    return ''.join(substring)


print(longest_substring("abca"))
print(longest_substring("abcdabcd"))
print(longest_substring("aaaaaaaaa"))
print(longest_substring("hello world"))
