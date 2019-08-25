def find_length_word(input_string):
    word_list = input_string.split('\n')
    word_sum = 0
    for word in word_list:
        if len(word) >= word_sum:
            word_sum = len(word)
    return word_sum


print(find_length_word("Some te\nxt about stuff\nshort"))


def word_split(input_string):
    # Find the new line in the string
    newline_split_index = input_string.find('\n')
    # Check if the index is -1, then return the splited string
    if newline_split_index == -1:
        return input_string,
    else:
        # recursively add the words.
        return (input_string[:newline_split_index],) + word_split(input_string[newline_split_index + 1:])


words = (word_split("Some te\nxt about stuff\nshort"))

word_sum = 0
for word in words:
    if len(word) >= word_sum:
        word_sum = len(word)
print(word_sum)
