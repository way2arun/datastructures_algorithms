"""
Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def printList(self, node):
        temp = node
        while (temp):
            print(temp.val)
            temp = temp.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Solution 1 - 72 ms
        """
        carry = 0
        head = curr = ListNode(0)

        while l1 or l2 or carry:
            d1, d2 = 0, 0
            if l1:
                d1 = l1.val
                l1 = l1.next
            if l2:
                d2 = l2.val
                l2 = l2.next
            carry, digit = divmod(d1 + d2 + carry, 10)
            curr.next = ListNode(digit)
            curr = curr.next

        return head.next
        """
        # Solution 2 - 44 ms
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next




l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

solution = Solution()
sum_node = solution.addTwoNumbers(l1, l2)
solution.printList(sum_node)