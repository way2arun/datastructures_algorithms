def longest_substring(input_string1):
    string_len = len(input_string1)
    substring = [input_string1[0]]
    for i in range(1, string_len):
        if input_string1[i] != input_string1[i - 1] and input_string1[i] not in substring:
            substring.append(input_string1[i])
        else:
            return ''.join(substring)

    return ''.join(substring)


print(longest_substring("abca"))
print(longest_substring("abcdabcd"))
print(longest_substring("aaaaaaaaa"))
print(longest_substring("hello world"))
