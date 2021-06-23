"""
Reverse Linked List II
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n


Follow up: Could you do it in one pass?
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
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # Solution 1 - 28 ms
        """
        if left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(left - 1):
            pre = pre.next

        curr = pre.next
        nxt = curr.next

        for i in range(right - left):
            tmp = nxt.next
            nxt.next = curr
            curr = nxt
            nxt = tmp

        pre.next.next = nxt
        pre.next = curr
        return dummy.next
        """
        # Solution 2 - 12 ms
        m, n = left, right
        l = ListNode()
        l.next = head
        while m > 1:
            l = l.next
            m -= 1
        r = head
        while n > 0:
            r = r.next
            n -= 1

        prev, curr = l, l.next
        while curr != r:
            curr.next, prev, curr = prev, curr, curr.next
        l.next.next = curr
        if l.next == head:
            head = prev
        l.next = prev
        return head


# Main Call
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
left = 2
right = 4

solution = Solution()
node = solution.reverseBetween(head, left, right)
solution.print_nodes(node)

