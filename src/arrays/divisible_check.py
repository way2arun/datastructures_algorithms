"""
find the divisible numbers between 1 to 100, if it is divisible by 4 print "Linked"
if it is divisible by 6 print "In"
if it is divisible by 4 and 6 print "LinkedIn"

"""

# Time Complexity - O(n)
# Space Complexity - O(1)


def divisible_check():
    for i in range(1, 100):
        # print(i)
        if i % 4 == 0 and i % 6 == 0:
            print(i)
            print("LinkedIn")
        elif i % 6 == 0:
            print(i)
            print("In")
        elif i % 4 == 0:
            print(i)
            print("Linked")


# Driver Call
divisible_check()
