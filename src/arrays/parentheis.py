
#parenthesis validation
#Time Complexity = O(n) (depends upon the length of the String)
#Space Complexity O(n) (Still keeping the information in the input_string)
def validate_parenthesis(input_string):
    #Counter values for forward and reverse parenthesis
    forward_parenthesis = 0
    reverse_parenthesis = 0
    start_pos = False
    #Traverse through each characters in the input_string
    for char in input_string:
        #Check if the character is '(' - then increment the forward counter
        if (char == '(') :
            forward_parenthesis +=1 
        #Check if the character is ')' - then increment the reverse counter
        elif (char == ')' ):
            if (input_string[0] == ')'):
                start_pos = True
            reverse_parenthesis +=1 
    if (forward_parenthesis == 0 or reverse_parenthesis == 0):
        return "Not a Proper Parenthesis"
    
    #If equal return the input string
    if (forward_parenthesis == reverse_parenthesis):
        return (input_string)
    # if forward_parenthesis > reverse_parenthesis remove the additionals
    elif (forward_parenthesis > reverse_parenthesis):
        return (input_string[forward_parenthesis - reverse_parenthesis:])
    # if reverse_parenthesis > forward_parenthesis remove the additionals
    else:
        if(start_pos):
            return (input_string[reverse_parenthesis - forward_parenthesis:])
        return (input_string[: (-1 * (reverse_parenthesis - forward_parenthesis))])
   
#Driver Call
#print(validate_parenthesis('((((())()(((('))
# Python3 code to Check for  
# balanced parentheses in an expression 
open_list = ["[","{","("] 
close_list = ["]","}",")"] 
  
# Function to check parentheses 
def check(myStr): 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "Unbalanced"
    if len(stack) == 0: 
        return "Balanced"
  
# Driver code 
string = "{[]{()}}"
print(string,"-", check(string)) 
  
string = "[{}{})(]"
print(string,"-", check(string)) 