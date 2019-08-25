# O(n^2)
def unique_chars_bft(input_string):
    # 2 loops, to check the characters in the array, 
    # Time Complexity - O(n^2)
    # Space Complexity - O(1)  
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string)):
            if input_string[i] == input_string[j]:
                return False
    return True


# Driver Call
print(unique_chars_bft("abcd"))
