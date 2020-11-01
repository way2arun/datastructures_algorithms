"""
Convert Binary Number in a Linked List to Integer
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.



Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
Example 3:

Input: head = [1]
Output: 1
Example 4:

Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880
Example 5:

Input: head = [0,0]
Output: 0


Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
   Hide Hint #1
Traverse the linked list and store all values in a string or array. convert the values obtained to decimal value.
   Hide Hint #2
You can solve the problem in O(1) memory using bits operation. use shift left operation ( << ) and or operation ( | ) to get the decimal value in one operation.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # Solution 1 - 32 ms
        """
        int_value = 0
        while head:
            int_value = 2 * int_value + head.val
            head = head.next
        return int_value
        """
        # Solution - 2 16 ms
        """
        ans = ''
        while head:
            ans += str(head.val)
            head = head.next
        return int(ans, 2)
        """

        # Solution 2 - 12 ms
        number = 0
        length = 0
        copy_head = head
        while head.next is not None:
            length += 1
            head = head.next
        check_number = []
        while length > 0:
            check_number.append([copy_head.val, 2 ** length])
            number += copy_head.val * (2 ** length)
            length -= 1
            copy_head = copy_head.next
        number += copy_head.val * (2 ** length)

        return number


# Main Call
node = ListNode(1)
node.next = ListNode(0)
node.next.next = ListNode(1)

solution = Solution()
print(solution.getDecimalValue(node))
