"""
Add Two Numbers II
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Solution 1 - 68 ms
        """
        st1, st2 = [], []
        while l1:
            st1.append(l1.val)
            l1 = l1.next

        while l2:
            st2.append(l2.val)
            l2 = l2.next

        carry, head = 0, None

        while st1 or st2 or carry:
            d1, d2 = 0, 0
            d1 = st1.pop() if st1 else 0
            d2 = st2.pop() if st2 else 0
            carry, digit = divmod(d1 + d2 + carry, 10)
            head_new = ListNode(digit)
            head_new.next = head
            head = head_new

        return head
        """
        # Solution 2 - 48 ms
        a = 0
        b = 0
        head1, head2 = l1, l2
        while head1:
            a = a * 10 + head1.val
            head1 = head1.next
        while head2:
            b = b * 10 + head2.val
            head2 = head2.next
        res = a + b
        new_head = None
        if res == 0:
            node = ListNode(0)
            node.next = new_head
            new_head = node
            return new_head
        while res:
            val = res % 10
            res = res // 10
            node = ListNode(val)
            node.next = new_head
            new_head = node
        return new_head

    def printList(self, node):
        temp = node
        while (temp):
            print(temp.val)
            temp = temp.next


# Main Call
node = ListNode(7)
node.next = ListNode(2)
node.next.next = ListNode(4)
node.next.next.next = ListNode(3)

node_2 = ListNode(5)
node_2.next = ListNode(6)
node_2.next.next = ListNode(4)

solution = Solution()
sum_node = solution.addTwoNumbers(node, node_2)
solution.printList(sum_node)
