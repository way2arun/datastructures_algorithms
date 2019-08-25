
#O(n^2)
def unique_chars_bft(input_string):
    # 2 loops, to check the characters in the array, 
    # Time Complexity - O(n^2)
    # Space Complexity - O(1)  
    for i in range(len(input_string)):
        for j  in range(i+1, len(input_string)):
            if (input_string[i] == input_string[j]):
                return False
    return True

#Driver Call
print(unique_chars_bft("abcd"))


# Only 1 loop in this case
# Time Complexity - O(n log n)  
# Why log n - as we sorted the array, so the complexity changed to log n time.
# Space Complexity - O(1)
def unique_chars_sorted(input_string):
    #Sort the array, this will help to remove extra loop
    input_string_sorted = sorted (input_string)
    for i in range(len(input_string_sorted) - 1):
        # In this approach we are always checking the elements in adjacent indexes
        # This is how sorted function helps.
        if(input_string_sorted[i] == input_string_sorted[i+1]):
            return False
    return True

#Driver Call
print(unique_chars_sorted("zdabez"))


# Time complexity :- O(n)
# We are using only 1 loop and python string count function 

def unique_char_count(input_string):
    #Initialize the total
    total = 0
    for i in input_string:
        count = input_string.count(i)
        if (count > 1):
            #If count is more increment the total
            total += count
    #Check if any duplicates
    if (total > 0):
        return False
    else:
        return True

#Driver Call
print(unique_char_count("zdabe"))


# More Python based approach
# Time Complexity :- O(1)
# Space Complexity :- O(1)
# Using the set data structure to eliminate the duplicates and check the length is same or not
def unique_char_set(input_string):
    # Use Set data structure and checks the length, if it is same it returns True if not False
    return (len(input_string) == len(set(input_string)))


#Driver Call
print(unique_char_set("zdabe"))

# Using additional data Structure
# Time Complexity :- O(n)
# Space Complexity :- O(n)  - higher as we are using extra data structure to hold
def unique_char_additional_datastructure(input_string): 
    # Initilize the new list with False * 128 for all characters occurrences 
    helper_charcter_list = [False] * 128
    # Now convert the character to ascii value and check if it exists in helper_charcter_list
    # If exists return False, if not return True
    for i in range(0, len(input_string)): 
        #Use ord function to get the unicode/ascii value
        acii_value = ord(input_string[i]) 
        if helper_charcter_list[acii_value]: 
            return False
        #Update the helper_charcter_list to True for each new ascii value in the 128 length array.
        helper_charcter_list[acii_value] = True
    return True
  
# Driver Call 
print(unique_char_additional_datastructure("abcd")) 

#Using bit operator
def unique_char_bit(input_string):
    #Initialize the checker variable
    checker = 0
    #Loop through each characters
    for i in range(len(input_string)):
        #Get the acii or unicode value
        ascii_value  = ord(input_string[i])
        print( 1 << ascii_value)
        #If the & is greater than 0 , the character is repeating, return false.
        if ((checker & 1 << ascii_value ) > 0 ):
            return False
        #update the checker.
        checker = (1 << ascii_value)
    return True

print(unique_char_bit("abcc"))





