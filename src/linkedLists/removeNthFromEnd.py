"""
Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
   Hide Hint #1
Maintain two pointers and update one with a delay of n steps.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def print_nodes(self, node):
        node_list = []
        while node:
            print(node.val)
            node_list.append(node.val)
            node = node.next
        print(node_list)

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Solution 1 - 32 ms
        """
        dummy = ListNode(0)
        dummy.next = head
        P1, P2 = dummy, dummy
        for _ in range(n):
            P2 = P2.next

        while P2.next:
            P1 = P1.next
            P2 = P2.next

        P1.next = P1.next.next

        return dummy.next
        """
        # Solution 2 - 12 ms
        slow = fast = head

        for i in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


# Main Call
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
n = 2
solution = Solution()
node = solution.removeNthFromEnd(head, n)
solution.print_nodes(node)
