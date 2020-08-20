"""
Reorder List
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3430/
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

# Definition for singly-linked list.
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Solution 1 - 100 ms
        """
        if not head:
            return

        q = deque()
        node = head
        while True:
            node = node.next
            if not node:
                break
            q.append(node)

        while q:
            if head:
                temp = q.pop()
                head.next = temp
                head = head.next

            if head and q:
                temp = q.popleft()
                head.next = temp
                head = head.next

        head.next = None
        temp = head

        while temp:
            print(temp.val)
            temp = temp.next
        """
        # Solution 2 - 76ms
        if not head:
            return

        prev = None
        slow = fast = l1 = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        l2 = self.reverse_ll(slow)

        while l2.next:
            tmp = l1.next
            l1.next = l2
            l1 = tmp

            tmp = l2.next
            l2.next = l1
            l2 = tmp


    def reverse_ll(self, head: ListNode) -> ListNode:
        prev = nex = None
        curr = head
        while curr:
            nex = curr.next  # store the next term
            curr.next = prev  # then switch next pointer to the previous term
            prev = curr  # increment previous term to the current term
            curr = nex  # increment current term to the stored old_next_term
        return prev  # prev is at the new head


# Main Call
# Load the linked list
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.nex = node5

solution = Solution()
solution.reorderList(head)
"""
temp = node

while temp:
    print(temp.val)
    temp = temp.next
"""
