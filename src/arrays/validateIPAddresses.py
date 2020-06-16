import re

"""
 Validate addresses function, accept input as an array of ip addresses
"""


def validateAddresses(addresses):
    # Regular express for ipv4 includes number
    ipv4_regex = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    # Compile the ipv4 regular expression and make a pattern
    ipv4_pattern = re.compile(r'^(' + ipv4_regex + r'\.){3}' + ipv4_regex + r'$')
    # IPv6 Regular expression
    ipv6_regex = r'([0-9a-fA-F]{1,4})'
    # IPv6 local host
    ipv6_localhost = "::1"
    # Compile the IPv6 Regular Expression pattern.
    ipv6_pattern = re.compile(r'^(' + ipv6_regex + r'\:){7}' + ipv6_regex + r'$')

    # Array to return the status
    ip_return_status = []
    # Traverse through all the addresses
    for ip in addresses:
        # Check for IPv4
        if ipv4_pattern.match(ip):
            ip_return_status.append("IPv4")
        # Check for IPv6
        elif ipv6_pattern.match(ip) or ip == ipv6_localhost:
            ip_return_status.append("IPv6")
        # "Neither"
        else:
            ip_return_status.append("Neither")

    # Return the status array
    return ip_return_status


# Main function to get the inputs from user

def main():
    # Get the number of queries
    try:
        num_queries = int(input("Enter the Number of Queries:\n"))
    except ValueError:
        print("Enter Value in Integer format")
        return False

    # Store it in a set
    ip_address = set()
    # Append the input ip addresses in to set
    for i in range(num_queries):
        ip_address.add(input("Enter the IP Address:="))

    # Call the Validate Address function
    results = validateAddresses(ip_address)
    # Print the results
    for result in results:
        print(result)


# Main Call
if __name__ == '__main__':
    main()
