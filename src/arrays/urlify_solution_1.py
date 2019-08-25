
#Time Complexity :- O(1)
#space complexity :- O(1)


def urlify(input_string, input_string_length):
    urlify_output = input_string.replace(' ', '%20')
    print(urlify_output)


#Driver Call
urlify("Mr John Smith", 13)
